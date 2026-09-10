---
name: Outbound QC gate
description: >-
  Use before any prospect, client, guest, or public-facing upload/send: requires
  humanizer first; blocks AI stamp phrases, leaks, template mail-merge, spam,
  and missing Unbroken invite framework beats.
---
# Prospect / client / guest facing QC gate

Use before any prospect, client, guest, or public-facing upload/send.

For podcast invites also run [Podcast guest Instantly invites](sand-workflow:podcast-guest-instantly-invites).
**Always run [humanizer](sand-workflow:humanizer) before this gate on outbound prose.**

## Hard rule
Do not upload or send until QC passes. Pause live sends on a miss. Never upload and fix later.

## Fail if present
- Strategy scaffolding / research dumps / placeholders / markdown artifacts
- Wrong signoff; missing first_name+last_name; invented emails or revenue
- Em/en dashes or `--` as dashes; smashed HTML signoff
- Reading level avg FK above ~6 for guest cold email
- Spam/hype words (free, act now, guarantee, click here, urgent, exclusive, amazing, world class, god send, unlock, crush, make money, flexing 7/8/9-figure at them)
- Template mail-merge / swappable bodies / generic subjects / crumb openers
- Subject containing Unbroken / Marketers / podcast / show name (must be interview-framed)
- **AI stamp phrases** (humanizer miss): stands out, stuck with me, hard chapter most people skip, change lives, tough chapters teach you, mess into a message is the point, logistics stay easy, worth putting on tape, not another tip list, builders in a rough week, you know what it costs to start again, you know what rebuild pressure, deeply, delve, landscape, testament, underscore, pivotal, in today's world, it's not just, more than just, at its core, the real question, not X but Y staging, one-line dramatic closers

## Unbroken invite FAIL if missing
1. Specific true hook about them
2. Plain reason their chapter helps people (no cliche)
3. Host adversity bridge (foster youth; drug addiction + grace of God; AI authority/speaker) without I-stack monologue
4. Why the show exists (mess into message / hard seasons), varied wording
5. Proof: Anik Singal, Tanner Chidester, Adam Robinson (Rb2b), Julia McCoy, legends like them
6. Soft Riverside ask + easy out + house signoff

VIP cream: hand-read end to end. If it sounds like ChatGPT, fail.

## Process
Draft → humanizer → automated leak/dash/spam/grade/template/AI-tell/legend-frame scan → VIP reads + mid-tier spot checks → upload → post-scan → activate only on Ty go.

## After a miss
Fix live artifact; update this skill + surface skill same turn; CoS if fleet-wide.
