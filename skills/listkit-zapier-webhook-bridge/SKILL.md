---
name: ListKit Zapier webhook bridge
description: >-
  Use when wiring ListKit replies. Mandatory order: Zapier Catch Hook (step 1),
  paste that URL into ListKit Settings Integrations webhook, then Zapier step 2
  Bearer POST to Grok Bot. Never skip the ListKit Integrations wire.
---
# ListKit Zapier webhook bridge

ListKit cannot POST with our Authorization Bearer header directly. Bridge:

**ListKit Settings Integrations webhook → Zapier Catch Hook (Zap step 1) → Zapier Webhooks POST with Bearer (Zap step 2) → this bot's webhook routine.**

## Hard rule (do not skip)
Agents often jump straight to Zapier Bearer POST and forget ListKit. **Both ends are required:**

1. **ListKit** must POST category updates into the **Zapier Catch Hook** URL (Zap step 1).
2. **Zapier** must then POST that JSON to the Grok Bot webhook with `Authorization: Bearer <key>` (Zap step 2).

If ListKit Integrations is empty or still points elsewhere, the bridge is incomplete even when Zapier looks fine.

## Operator does only this
1. Log into **ListKit** (`next.listkit.io`) on this computer
2. Log into **Zapier** (`zapier.com`) on this computer
3. After you create the reply-catcher webhook routine, paste from that Grok Bot routine panel:
   - **webhook URL**
   - **Bearer / sender key**

Script:
> Log me into ListKit and Zapier. I'll create the reply catcher. Paste the webhook URL and Bearer from that routine in Grok Bot. I'll set up Zapier and the ListKit Integrations webhook myself.

## You do everything else (strict order)

### A. Grok Bot catcher
1. Create the webhook reply-catcher routine
2. Take their pasted URL + Bearer (secrets: use for Zapier only; never store in skills/template memory)

### B. Zapier Zap step 1 (Catch Hook) FIRST
3. In **Zapier**, create a Zap with trigger **Webhooks by Zapier → Catch Hook**
4. Copy the Catch Hook URL Zapier gives you (this is step 1 only; do not add Bearer auth here)

### C. ListKit Settings Integrations → Catch Hook (MANDATORY)
5. In **ListKit**: open **Settings → Integrations** (or left-nav Integrations)
6. Paste the **Zapier Catch Hook URL** into the ListKit webhook input for **Lead category updated** (or equivalent covering interested / not interested / unsub / meeting booked / positive replies)
7. Save. Confirm the field shows the Catch Hook URL, not the Grok Bot Bearer URL
8. Do **not** put the Grok Bot Bearer webhook URL into ListKit. ListKit has no Bearer header support.

### D. Zapier Zap step 2 (Bearer POST) AFTER ListKit is wired
9. Add Zapier action **Webhooks by Zapier → POST** (or Custom Request)
10. URL = Grok Bot webhook URL from the routine panel
11. Header `Authorization: Bearer <key>` from the same panel
12. Pass through the Catch Hook JSON body
13. Publish the Zap

### E. Prove both hops
14. Trigger a test category change in ListKit (or Zapier test with a real ListKit payload)
15. Confirm Catch Hook receives it, then this bot's routine wakes
16. Delete duplicate Zaps / webhooks

## Failure modes
- Zapier Bearer step configured but ListKit Integrations blank → **no wakes** (most common miss)
- ListKit webhook set to Grok Bot URL directly → ListKit cannot send Bearer; use Catch Hook only
- Catch Hook URL changed after ListKit save → re-paste into ListKit Integrations

## Notes
- Payload usually has no reply body. Always open Master Inbox.
- Prefer in-app ListKit Integrations webhook over Gmail-notification fallbacks.
- Do not hand them a long Zap click-path; do the wiring yourself once logged in.
- Do not require a Gmail marketplace plugin for this bridge.
