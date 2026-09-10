# ListKit Wizard

Cursor / Grok Bot plugin packing the **ListKit Wizard** cold email ops skill set for marketplace distribution.

## What it does

Gives an agent end-to-end ListKit operating recipes:

1. Onboard: log into ListKit + Zapier, paste Grok Bot webhook URL/Bearer, bot wires ListKit Integrations → Zapier Catch Hook → Bearer POST
2. Audit existing campaigns, copy/messaging, and Master Inbox replies
3. Launch campaigns (first-import custom fields, validation, QC)
4. Handle replies with full-thread context and no double-send
5. Website-researched CSV personalization (`scripts/personalize/personalize.py`) + cold email write stack
6. Now-positive follow-ups, hot-lead forwards, week-in-reviews, Master Inbox sweeps
7. Keep every recurring process skillized so quality does not regress

## Install

### Local (this machine)

Copy or symlink this folder to:

```text
~/.cursor/plugins/local/listkit-wizard
```

On Windows:

```text
%USERPROFILE%\.cursor\plugins\local\listkit-wizard
```

Restart Cursor / Grok Bot so skills are picked up.

### Marketplace

Submit this plugin directory (with `.cursor-plugin/plugin.json`) through the Cursor plugin marketplace flow. No MCP connector is required for core ListKit UI + Zapier browser setup.

## Components

- **Skills** under `skills/*/SKILL.md` (ListKit ops recipes)
- **Agent** under `agents/listkit-wizard.md` (persona / operating brief)
- **Rules** under `rules/` (standing hard rules)

## Core onboarding (operators)

1. Log into `next.listkit.io`
2. Log into `zapier.com`
3. Paste webhook URL + Bearer from the Grok Bot reply-catcher routine panel
4. Bot creates Zapier Catch Hook, pastes it into ListKit Settings Integrations webhook, then adds Zapier Bearer POST to Grok Bot
5. Bot audits their ListKit account

No Gmail or Composio plugin required for core setup.

## License

MIT
