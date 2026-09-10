"""
Cold Email Personalization Tool (config-file edition)
-----------------------------------------------------
Reads your email template + extraction rules from a JSON config file so
multi-paragraph templates work reliably, and feeds extra CSV columns
(e.g. Industry, City, State) to Claude for better personalization.

Usage:
    python3 personalize.py leads.csv --config config.json
    python3 personalize.py leads.csv --config config.json --limit 10
    python3 personalize.py leads.csv --config config.json --output enriched.csv

config.json format:
    {
      "template": "Noticed you're {{company_descriptor}}.\\n\\n...",
      "instructions": {
        "company_descriptor": "what Claude should look for...",
        "ideal_customers": "what Claude should look for..."
      },
      "fallbacks": {
        "company_descriptor": "a growing business",
        "ideal_customers": "new customers"
      },
      "context_cols": ["Industry", "City", "State"],
      "description_col": "Keywords"
    }

Requirements:
    pip install anthropic requests beautifulsoup4
"""

from typing import Optional
import argparse
import csv
import json
import os
import re
import sys
import time

import anthropic
import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
MODEL = "claude-haiku-4-5"
MAX_TOKENS = 256
SCRAPE_TIMEOUT = 10
MAX_PAGE_CHARS = 8_000
MAX_CONTEXT_CHARS = 1_500

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


# ---------------------------------------------------------------------------
# Scraping
# ---------------------------------------------------------------------------
def fetch_page_text(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    resp = requests.get(url, headers=HEADERS, timeout=SCRAPE_TIMEOUT)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "meta"]):
        tag.decompose()
    text = soup.get_text(separator=" ", strip=True)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:MAX_PAGE_CHARS]


# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------
def load_config(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        cfg = json.load(f)

    template = cfg.get("template", "")
    placeholders = re.findall(r"\{\{(\w+)\}\}", template)

    cfg.setdefault("instructions", {})
    cfg.setdefault("fallbacks", {})

    # Standalone variables: any key declared in "instructions" becomes an
    # extracted column even if it never appears in the email template.
    for key in cfg["instructions"]:
        if key not in placeholders:
            placeholders.append(key)

    if not placeholders:
        sys.exit("Error: no {{placeholders}} in the template and no variables declared.")

    cfg["placeholders"] = placeholders
    cfg.setdefault("context_cols", [])
    cfg.setdefault("description_col", "")
    for p in placeholders:
        if p == "company_name":
            continue
        cfg["fallbacks"].setdefault(p, p)
    return cfg


def build_context(row: dict, config: dict) -> str:
    """Assemble known facts about the company from the CSV row."""
    parts = []
    for col in config["context_cols"]:
        val = (row.get(col) or "").strip()
        if val:
            parts.append(f"{col}: {val}")
    desc_col = config.get("description_col")
    if desc_col:
        desc = (row.get(desc_col) or "").strip()
        if desc:
            parts.append(f"About the company: {desc[:MAX_CONTEXT_CHARS]}")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Claude
# ---------------------------------------------------------------------------
def generate_values(
    client: anthropic.Anthropic,
    page_text: str,
    company_name: str,
    context: str,
    config: dict,
) -> dict:
    placeholder_instructions = ""
    for p in config["placeholders"]:
        if p == "company_name":
            continue
        placeholder_instructions += f"\n- **{p}**: {config['instructions'].get(p, '')}"

    source_block = ""
    if context:
        source_block += f"\nKnown facts (from a data provider):\n{context}\n"
    if page_text:
        source_block += f"\nWebsite content:\n{page_text}\n"
    if not source_block:
        source_block = "\n(No website or data available.)\n"

    output_format = "\n".join(
        f"{p}: [value]" for p in config["placeholders"] if p != "company_name"
    )

    prompt = f"""You are helping personalize a cold outreach email to {company_name}.
{source_block}
Task: Determine the following, being specific and concrete:{placeholder_instructions}

Rules:
- Base every value on the facts above — do not invent details.
- Each value is a short phrase (2-8 words) that will be dropped directly into a sentence.
- Do not include the company name, quotation marks, or trailing punctuation.
- If you truly cannot tell, use a sensible generic phrase rather than saying you don't know.
- Return ONLY the values, one per line, in exactly this format:
{output_format}"""

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )
    if not response.content:
        raise ValueError("Empty response from Claude")

    text = response.content[0].text.strip()
    values = {}
    for p in config["placeholders"]:
        if p == "company_name":
            values[p] = company_name
            continue
        match = re.search(rf"{p}:\s*(.+)", text, re.IGNORECASE)
        if match:
            val = match.group(1).strip().strip('"').strip("'").rstrip(".")
            if len(val) > config.get("max_value_len", 220) or "cannot" in val.lower() or val.lower() in ("n/a", "none"):
                val = config["fallbacks"][p]
            values[p] = val
        else:
            values[p] = config["fallbacks"][p]
    return values


def fill_template(template: str, values: dict) -> str:
    out = template
    for p, v in values.items():
        out = out.replace("{{" + p + "}}", v)
    return out


# ---------------------------------------------------------------------------
# CSV processing
# ---------------------------------------------------------------------------
def process_csv(
    input_path: str,
    output_path: str,
    website_col: str,
    company_col: str,
    config: dict,
    delay: float = 1.0,
    limit: Optional[int] = None,
) -> None:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            sys.exit("Error: CSV appears to be empty.")

        fieldnames = list(reader.fieldnames)
        if website_col not in fieldnames:
            sys.exit(f"Error: column '{website_col}' not found. Available: {fieldnames}")

        for col in config["placeholders"] + ["personalized_email"]:
            if col not in fieldnames and col != "company_name":
                fieldnames.append(col)

        rows = list(reader)

    if limit:
        rows = rows[:limit]

    total = len(rows)
    print(f"\nProcessing {total} leads -> {output_path}\n")

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i, row in enumerate(rows, start=1):
            website = (row.get(website_col) or "").strip()
            company = (row.get(company_col) or "").strip() or website
            context = build_context(row, config)

            print(f"[{i}/{total}] {company} — {website or '(no url)'}")

            fallback_values = {
                p: config["fallbacks"].get(p, p) for p in config["placeholders"]
            }
            fallback_values["company_name"] = company

            page_text = ""
            if website:
                try:
                    page_text = fetch_page_text(website)
                except requests.RequestException as e:
                    print(f"         (scrape failed, using CSV data: {e})")

            try:
                # As long as we have the website OR CSV context, ask Claude.
                if page_text or context:
                    values = generate_values(client, page_text, company, context, config)
                else:
                    values = fallback_values
                email = fill_template(config["template"], values)
                for p in config["placeholders"]:
                    if p != "company_name" and p in fieldnames:
                        row[p] = values[p]
                row["personalized_email"] = email
                print(f"         -> {email.splitlines()[0][:100]}")
            except (anthropic.APIError, ValueError, KeyError) as e:
                for p in config["placeholders"]:
                    if p != "company_name" and p in fieldnames:
                        row[p] = fallback_values[p]
                row["personalized_email"] = fill_template(config["template"], fallback_values)
                print(f"         x failed, using fallback: {e}")

            writer.writerow(row)
            f.flush()

            if i < total:
                time.sleep(delay)

    print(f"\nDone. Results saved to: {output_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="Personalize cold emails from a leads CSV.")
    parser.add_argument("input", help="Path to input CSV file")
    parser.add_argument("--config", "-c", required=True, help="Path to config.json")
    parser.add_argument("--output", "-o", help="Path to output CSV (default: input_enriched.csv)")
    parser.add_argument("--website-col", default="Company URL", help="Column for website URLs")
    parser.add_argument("--company-col", default="Company Name", help="Column for company name")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between rows (default: 1.0)")
    parser.add_argument("--limit", type=int, default=None, help="Only process first N rows")
    parser.add_argument("--api-key", help="Anthropic API key (or set ANTHROPIC_API_KEY env var)")
    args = parser.parse_args()

    if args.api_key:
        os.environ["ANTHROPIC_API_KEY"] = args.api_key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Error: no API key. Pass --api-key or set ANTHROPIC_API_KEY.")
    if not os.path.isfile(args.input):
        sys.exit(f"Error: file not found: {args.input}")

    config = load_config(args.config)

    output = args.output or args.input.replace(".csv", "_enriched.csv")
    if output == args.input:
        output = args.input.replace(".csv", "_enriched.csv")

    process_csv(
        args.input, output, args.website_col, args.company_col,
        config, args.delay, args.limit,
    )


if __name__ == "__main__":
    main()
