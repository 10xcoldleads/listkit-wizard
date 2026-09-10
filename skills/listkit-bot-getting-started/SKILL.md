---
name: ListKit bot getting started
description: >-
  Use on first run: ListKit + Zapier login, paste Grok Bot webhook URL/Bearer,
  wire bridge, audit ListKit, and skillize every recurring process.
---
# Getting started — ListKit cold email bot

Keep first-run tight. One question at a time. When they hand you real work, drop the questionnaire and help.

## Operating principle
All recurring processes are skills. Run them. After any miss, fix the live thing and skillize the same turn ([ListKit process skillization](sand-workflow:listkit-process-skillization), [Skillize after every miss](sand-workflow:skillize-after-every-miss)). Prospect-facing copy: [humanizer](sand-workflow:humanizer) then [Outbound QC gate](sand-workflow:outbound-qc-gate).

## First three steps
1. **Log into ListKit** — `next.listkit.io`
2. **Log into Zapier** — `zapier.com`
3. **Paste webhook URL + Bearer from Grok Bot** — create the reply-catcher routine, they paste URL + Bearer from that routine panel

Then you wire Zapier and the ListKit in-app webhook ([ListKit Zapier webhook bridge](sand-workflow:listkit-zapier-webhook-bridge)).

## Then scan their ListKit
If the account has activity, run [ListKit account audit](sand-workflow:listkit-account-audit): campaigns, messaging/copy, Master Inbox replies, lists, reply path. Summarize what you will own. Empty account: website/docs/brain-dump → first campaign (names required on every lead).

## Docs
Scan https://docs.listkit.io/en/ when stale. Weekly Monday refresh stays silent unless material change.

## Standing rules
- Master Inbox as sender (no Gmail Reply Forwarding for prospects)
- Full thread before replies
- Fix wrong categories; validate before import
- first_name + last_name on every lead
- Never invent metrics; silence on empty/OOO
- No em/en dashes in communications (fleet writing)

## Routines after config
- Webhook catcher → reply handler (+ hot-lead forward)
- Weekday now-positive follow-up
- Optional Master Inbox sweep
- Weekly week-in-review
- Weekly ListKit docs refresh
