---
name: ListKit cold email personalization
description: >-
  Use when enriching a ListKit/CSV lead list with website-researched
  personalization lines via the bundled personalize.py tool (Anthropic + scrape),
  then QC before campaign import.
---

# ListKit cold email personalization

Fill per-lead personalization from company websites using the bundled script, then import into ListKit with first_name + last_name + custom body fields.

## Bundled tool
- Script: `scripts/personalize/personalize.py`
- Operator guide: `scripts/personalize/HOW_TO_RUN.md`
- Example config: `scripts/personalize/lead_types_config.example.json`

## When to use
- Building or refreshing ListKit campaigns that need researched `{{personalization}}` / custom email bodies
- Batch-enriching a CSV before [ListKit campaign launch](sand-workflow:listkit-campaign-launch)

## Hard rules
- Every row needs **first_name** and **last_name** (never email-only)
- Company research required. CRM fields alone are not enough for a unique hook
- Operator uses **their own** `ANTHROPIC_API_KEY` (never store keys in skills, git, or chat)
- Test with `--limit 10` before full runs
- After enrichment: run [Cold email write](sand-workflow:cold-email-write) critique on samples, then [humanizer](sand-workflow:humanizer) + [Outbound QC gate](sand-workflow:outbound-qc-gate) before ListKit import
- Map personalized bodies on **first** ListKit import

## Steps
1. Prepare leads CSV (Company Name, Company URL, First Name, Last Name, Business Email, optional Industry/Job Title).
2. Copy `lead_types_config.example.json` → campaign-specific `lead_types_config.json`. Edit `template`, `instructions`, `fallbacks`.
3. Install deps once: `pip install anthropic requests beautifulsoup4`
4. Dry run:
   ```bash
   ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" python3 scripts/personalize/personalize.py leads.csv --config lead_types_config.json --limit 10 --output test10.csv
   ```
5. Spot-check `lead_types` / `personalized_email` columns. Fail and rewrite config if mail-merge / vanity / wrong-company hooks.
6. Full run to `enriched.csv` (script saves per row; safe to resume).
7. Merge into ListKit upload fields (`email_1_body` etc.) with names present.
8. Launch via campaign launch skill; preview must not show literal merge tags.

## Pass / fail
- Pass: each kept row has names, a company-specific personalization beat, and passes sample QC
- Fail: email-only rows, CRM-only hooks, literal `{{...}}` in ListKit preview, shipping without humanizer/QC

## After a miss
Fix the live list/campaign, then update this skill or the config example the same turn ([ListKit process skillization](sand-workflow:listkit-process-skillization)).
