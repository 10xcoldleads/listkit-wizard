---
name: ListKit account audit
description: >-
  Use this when a new ListKit user already has an account — analyze campaigns,
  copy, leads, inbox, and reply path before taking over.
---
# ListKit account audit

Run this when a new operator already has (or just gave you) ListKit access. Goal: understand what they're doing before you change anything.

## Steps
1. Confirm signed in at `next.listkit.io` on the correct workspace.
2. Inventory **campaigns**: names, status (Active/Paused/Draft), contact counts, send windows, inbox sets, sequence length.
3. Read **copy**: subjects (all variants), email bodies / custom fields, signatures, merge tags. Note voice, CTA, and personalization depth.
4. Sample **leads/lists**: ICP, titles, geos, custom fields, obvious junk, verification state.
5. Check **Master Inbox**: recent reply mix, unreplied threads, category hygiene issues.
6. Check **integrations / notifications**: existing webhooks, email alerts, Zapier, Reply Forwarding (flag if on — prefer in-product replies).
7. Note account limits (credits, daily send caps) if visible.

## Deliverable
Write a short operator-facing brief:
- Who they sell to and what they sell (from their materials, not guesses)
- Current machine: campaigns, volume, reply path
- What's strong vs broken (copy, lists, hygiene, speed-to-reply)
- Recommended takeover plan (what you'll own first: catcher, FU cadence, list build, relaunch)

Do not invent metrics. If a number isn't in the UI, omit it.
Ask only for the gaps the audit cannot answer (assets, hot-lead recipient, preferences).
