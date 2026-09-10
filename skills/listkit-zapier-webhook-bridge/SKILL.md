---
name: ListKit Zapier webhook bridge
description: >-
  Use when wiring ListKit replies: ListKit login, Zapier login, paste Grok Bot
  webhook URL/Bearer; bot sets up Zapier and ListKit in-app webhook.
---
# ListKit Zapier webhook bridge

ListKit cannot POST with our Authorization Bearer header directly. Bridge: ListKit in-app webhook → Zapier Catch Hook → this bot's webhook routine (header auth).

## Operator does only this
1. Log into **ListKit** (`next.listkit.io`) on this computer
2. Log into **Zapier** (`zapier.com`) on this computer
3. After you create the reply-catcher webhook routine, paste from that Grok Bot routine panel:
   - **webhook URL**
   - **Bearer / sender key**

Script:
> Log me into ListKit and Zapier. I'll create the reply catcher — paste the webhook URL and Bearer from that routine in Grok Bot. I'll set up Zapier and the ListKit in-app webhook myself.

## You do everything else
1. Create the webhook reply-catcher routine
2. Take their pasted URL + Bearer (secrets — use for Zapier only; never store in skills/template memory)
3. In **Zapier**: Catch Hook trigger → POST to bot URL with `Authorization: Bearer <key>`; pass through JSON
4. In **ListKit in-app**: webhook for Lead category updated (or equivalent covering interested / not interested / unsub / meeting booked) → Zapier Catch Hook URL
5. Publish, test, confirm this routine wakes, delete duplicates

## Notes
- Payload usually has no reply body — always open Master Inbox
- Prefer in-app ListKit webhook over Gmail-notification fallbacks
- Do not hand them a long Zap click-path
- Do not require a Gmail marketplace plugin for this bridge
