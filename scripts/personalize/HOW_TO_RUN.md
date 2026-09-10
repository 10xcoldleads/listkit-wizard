# Cold Email Personalization — How to Run

This tool reads a CSV of leads, visits each company's website, and uses Claude to
fill in a personalized line for every row. You get back the same CSV plus a
`lead_types` column and a ready-to-send `personalized_email` column.

**You have 2 files:**
- `personalize.py` — the script (don't edit)
- `lead_types_config.json` — the campaign (edit this to change the message)

---

## 1. One-time setup

**Install Python 3** if you don't have it: https://www.python.org/downloads/ (Mac usually has it already — check with `python3 --version`).

**Install the required packages** — open Terminal (Mac: Cmd+Space → "Terminal") and run:
```bash
pip install anthropic requests beautifulsoup4
```

**Get an Anthropic API key:**
1. Go to https://console.anthropic.com → **API keys** → **Create Key**.
2. Copy the key (starts with `sk-ant-`). Keep it private — never share it or paste it into chat/email.
3. Go to **Plans & Billing** and add credits (a few dollars covers thousands of rows).

---

## 2. Run it

Put `personalize.py`, `lead_types_config.json`, and your leads CSV in the **same folder**.
In Terminal, `cd` into that folder, then:

**Test on the first 10 rows first** (always do this):
```bash
ANTHROPIC_API_KEY="sk-ant-YOUR-KEY" python3 personalize.py leads.csv --config lead_types_config.json --limit 10 --output test10.csv
```
Open `test10.csv` and check the `lead_types` / `personalized_email` columns.

**Run the whole list:**
```bash
ANTHROPIC_API_KEY="sk-ant-YOUR-KEY" python3 personalize.py leads.csv --config lead_types_config.json --output enriched.csv
```

Replace `leads.csv` with your file's name (drag the file into Terminal to paste its full path).

---

## 3. Options

| Flag | What it does |
|---|---|
| `--config` | path to the JSON campaign file (required) |
| `--output` / `-o` | output filename (default: `<input>_enriched.csv`) |
| `--limit N` | only process the first N rows (use for testing) |
| `--website-col` | name of the website column if not "Company URL" |
| `--company-col` | name of the company column if not "Company Name" |
| `--delay` | seconds between rows (default 1.0) |

It **saves after every row**, so if it stops you can just re-run on the rest.
Sites that block scraping fall back to the config's fallback value, so every row stays usable.

---

## 4. Change the message

Open `lead_types_config.json` in any text editor:
- **`template`** — the email line. Put `{{lead_types}}` where the personalized part goes.
- **`instructions.lead_types`** — tells Claude what to write for each company. Be specific; give an example.
- **`fallbacks.lead_types`** — used when a site can't be read.
- **`context_cols`** — extra CSV columns to feed Claude (e.g. `["Industry"]`).

You can rename `lead_types` to anything (e.g. `pain_point`) — just keep the name identical in `template`, `instructions`, and `fallbacks`. Add more placeholders by adding more entries to each section.

---

## Notes
- Everyone uses their **own** API key.
- For very large lists (10k+), run it in Terminal (no timeout) and let it finish; use `--limit` to test first.
