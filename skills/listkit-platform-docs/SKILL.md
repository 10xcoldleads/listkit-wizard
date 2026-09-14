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
Last full crawl: **2026-09-14** (snapshot: `/workspace/listkit-docs/platform-knowledge.md`).

- App: `next.listkit.io` (docs flows). Help Center header also links Login at `app.listkit.io/login`. Docs: `docs.listkit.io/en/`.
- No public general-purpose REST API documented. Automation via Integrations (Zapier API key, Google Drive/Sheets, Smartlead AI), in-app webhooks, Workflows, CSV, Order History → campaign.
- Integrations live under left-nav **Integrations** (collection under Account, Billing and Support). Zapier: API key from Integrations → Connect Zapier (lead export automation). Dedicated Zapier how-to article is gone; see What integrations.
- **Webhooks (current documented path):** Integrations → Manage webhooks → Add webhook → paste Zapier Catch Hook URL → Event Type **Lead category updated** → signing secret → Send test. Self-serve. Do not rely on emailing Catch Hook to support@listkit.io for sending-tool config.
- **Positive-reply notifications:** Email Engine → Settings → Positive-reply notifications (on by default; Interested / Meeting Booked; optional forward address). Full reply text still requires Master Inbox.
- Lead finding: B2B Search, AI Search, filters, intent data, credits, CSV from Order History, Order History → campaign. Workflows for scheduled exports.
- Email Engine: sequences, campaigns, Master Inbox, analytics/contacts, domains/inboxes/warmup/ramp-up/signatures (max 350 chars).
- **Sending limits (docs):** default **25 emails/inbox/day**; ramp starts at 1 then +4/day to 25 over ~7 days; base example ~40 inboxes ≈ 1,000/day.
- Prefer in-product Master Inbox replies over Gmail Reply Forwarding for bot-operated accounts unless the operator insists otherwise.
- Also documented: AI Script Writer (100 credits/gen), Warm-Up Reputation Score (warmup-network only; campaign reply rate >1% is the health signal).

## Cheatsheet links (verify weekly)
- Home: https://docs.listkit.io/en/
- Getting Started: https://docs.listkit.io/en/collections/19693756-getting-started
- Domains/Inboxes/Warmup: https://docs.listkit.io/en/collections/19712347-domains-inboxes-and-warmup
- Finding and Exporting Leads: https://docs.listkit.io/en/collections/19712348-finding-and-exporting-leads
- Running Campaigns: https://docs.listkit.io/en/collections/19712352-running-campaigns
- Cold Email Playbook: https://docs.listkit.io/en/collections/19693777-cold-email-playbook
- Account/Billing/Support: https://docs.listkit.io/en/collections/19693776-account-billing-and-support
- Integrations collection: https://docs.listkit.io/en/collections/19712355-integrations
- What integrations: https://docs.listkit.io/en/articles/13263818-what-integrations-does-listkit-support
- Webhooks (positive replies → CRM): https://docs.listkit.io/en/articles/16774358-how-do-i-use-webhooks-to-send-positive-replies-to-my-crm
- Workflows (scheduled exports): https://docs.listkit.io/en/articles/13263801-how-do-i-use-workflows-in-listkit
- Sending limits: https://docs.listkit.io/en/articles/16146357-what-are-sending-limits-and-how-are-they-set-in-my-inboxes

Dead URLs (do not use): `collections/19693770-integrations`, `articles/16127844-how-do-i-use-zapier-with-listkit`, `articles/13263810-how-do-i-connect-listkit-to-my-crm-using-a-webhook`.

Expand the cheatsheet after each full crawl.
