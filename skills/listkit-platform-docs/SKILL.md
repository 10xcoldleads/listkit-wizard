---
name: ListKit platform docs
description: >-
  Use at startup and whenever ListKit product behavior is unclear — scan
  official docs.listkit.io and keep platform knowledge current.
---
# ListKit platform docs

Keep intimate, current knowledge of ListKit from the official Help Center at https://docs.listkit.io/en/

## At startup / new user
Before deep ops advice, ensure you have recently refreshed docs (or run a refresh now if memory shows last refresh older than ~7 days, or never):
1. Open https://docs.listkit.io/en/
2. Re-read Getting Started, Domains/Inboxes/Warmup, Finding and Exporting Leads, Running Campaigns, Integrations, and any articles tied to the user's ask
3. Update agent memory (log) with durable product facts and the refresh date
4. Update this skill's cheatsheet section below if product behavior changed
5. Store a local snapshot under `/workspace/listkit-docs/` when useful (`platform-knowledge.md`, `sources.json`)

Do not invent product features. Prefer official docs over tribal memory when they conflict; then update memory.

## Weekly refresh (routine)
A standing weekly routine re-scans docs.listkit.io, diffs against prior notes, updates memory + this skill cheatsheet, and tells the operator only if something material changed (new integration, webhook behavior, limits, UI paths). Stay silent if nothing meaningful changed.

## Known product facts (refresh these — do not treat as forever)
- App: `next.listkit.io`. Docs: `docs.listkit.io/en/`.
- No public general-purpose REST API for arbitrary automation; integrations are first-class (Zapier API key, Google Drive/Sheets, Smartlead) plus webhooks.
- Integrations live under left-nav **Integrations**. Zapier uses a ListKit API key from Connect → Zapier.
- CRM/reply webhooks: often Zapier Catch Hook URL; some setups still go through ListKit configuring the sending-tool webhook (support@listkit.io) for positive replies — also check in-app Integrations / Email Engine for newer self-serve Zapier event triggers (Positive Replies, Replies, OOO, Unsubscribes, etc.).
- Lead finding: B2B database, AI Search, filters, intent data, export/credits, CSV export, push Order History → campaign.
- Email Engine: sequences, campaigns, Master Inbox / replies, analytics, contacts, domains/inboxes/warmup/ramp-up/sending limits/signatures.
- Prefer in-product Master Inbox replies over Gmail Reply Forwarding for bot-operated accounts unless the operator insists otherwise.

## Cheatsheet links (verify weekly)
- Home: https://docs.listkit.io/en/
- Integrations collection: https://docs.listkit.io/en/collections/19693770-integrations
- What integrations: https://docs.listkit.io/en/articles/13263818-what-integrations-does-listkit-support
- CRM webhook: https://docs.listkit.io/en/articles/13263810-how-do-i-connect-listkit-to-my-crm-using-a-webhook
- Zapier: https://docs.listkit.io/en/articles/16127844-how-do-i-use-zapier-with-listkit

Expand the cheatsheet after each full crawl.
