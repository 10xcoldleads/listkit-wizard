---
name: ListKit campaign launch
description: >-
  Use when creating or extending a ListKit campaign: first-import custom-field
  mapping, QC, subjects/threading, and launch checklist.
---
# ListKit campaign launch

Launch or extend a ListKit cold-email campaign from a QC'd lead file.

## Preconditions
- Every lead has verified email ([ListKit email validation](sand-workflow:listkit-email-validation)).
- Every lead has **first_name and last_name** (never email-only).
- Personalized bodies attached as custom fields **before first import** when the campaign uses per-lead copy.
- QC the merged sheet before upload. Run [Outbound QC gate](sand-workflow:outbound-qc-gate) (and [humanizer](sand-workflow:humanizer)) on any prospect-facing copy before load.

## Custom fields (critical)
- Map `email_1_body` / `email_2_body` / `email_3_body` (or equivalent) to the campaign Custom Fields on the **first** import.
- Re-importing contacts that already exist often reports 0 imported and **does not update** custom bodies. Preview then shows literal `{{email_1_body}}`.
- If bodies were missing on first import: bulk-remove those contacts from the campaign (or delete the known email set), then re-import with fields mapped. Do not assume an "update existing" toggle will fill blank custom fields.
- After import, spot-check preview: bodies must resolve, not show raw merge tags.

## Subject and threading defaults
- At least 5 subject variants per step when possible.
- Strong pattern: short punchy subject + name merge.
- Later emails usually thread under email 1 unless the operator wants otherwise.

## Launch checklist
1. Prepare CSV with required + custom body fields.
2. Create/open campaign; map fields; select sender inboxes.
3. Set send window and daily limits within account caps.
4. Preview several leads (bodies + subjects resolve).
5. Operator approval for new campaigns; still QC when adding to Active.
6. Keep replies in Master Inbox.
7. Report: contacts imported, skipped dups, status, inbox count, send window.

## Import tips
- CSV upload works even when Upload looks disabled (hidden file input).
- Exclude junk/generic accounts and leads already in campaign when you cannot safely update them.
- Collapse multi-entity shared emails to one row when appropriate.

## After a miss
Fix the live campaign, then update this skill the same turn ([ListKit process skillization](sand-workflow:listkit-process-skillization)).
