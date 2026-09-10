---
name: ListKit Master Inbox sweep
description: >-
  Use this for weekday or ad-hoc Master Inbox sweeps to catch
  unreplied/mislabeled threads the webhook missed.
---
# ListKit Master Inbox sweep

Sweep ListKit Master Inbox for unreplied or mislabeled threads when the webhook may have missed negatives or the catcher was down.

## Steps
1. Open Master Inbox for the client's campaigns.
2. For each unreplied human inbound: run [ListKit reply handler](sand-workflow:listkit-reply-handler).
3. Fix category mismatches with [ListKit category hygiene](sand-workflow:listkit-category-hygiene).
4. Forward any new hot/trust leads via [ListKit hot-lead forward](sand-workflow:listkit-hot-lead-forward).
5. Skip OOO/auto/bounce and ListKit product mail (export-ready notices, affiliate pitches).
6. Report only what you actually handled; stay silent if the inbox was clean.

## Guardrails
- Full thread context before every reply.
- In-product replies only as the campaign sender.
- Do not use public catchers, ListKit internal APIs, or Gmail Reply Forwarding unless the operator explicitly directs it.
