---
name: ListKit email validation
description: >-
  Use this before any ListKit import or outreach when emails were found online —
  primary verify, re-check risky/catchall, never assume deliverable.
---
# ListKit email validation

Validate every email found online (site scrape, LinkedIn, enrichment) before treating it as good. Never assume deliverability.

## Pipeline
1. Find candidate emails for named people at known domains.
2. Verify with the primary validator (e.g. TryKitt). Only `validity=valid` counts as email_ok on the first pass.
3. For valid-risky / catchall / unknown: always re-check with a secondary verifier (e.g. BounceBan) before using.
4. Drop invalids and junk/generic mailboxes (`info@`, `account@`, etc.) unless the operator says otherwise.
5. Record verification status on the lead row.

## Rules
- Never import unverified emails into ListKit.
- Never invent an email.
- If verification is blocked (missing API key), stop and ask the operator — do not guess.
