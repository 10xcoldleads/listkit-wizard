---
name: ListKit now-positive follow-up
description: >-
  Use when weekday ListKit follow-ups on true now-positive leads need a
  3-then-4-day NEPQ cadence with full-thread context before every send.
---
# ListKit now-positive follow-up

Work NOW-positive leads in ListKit Master Inbox until they book or tell you to stop. Never use Gmail or Reply Forwarding.

## Hard gate: full context before every send
Before drafting or sending ANY follow-up:
1. Open the FULL Master Inbox thread. Read every outbound and inbound message, not just the latest.
2. Read the lead record (name, org, inventory named, last sender assets already sent).
3. Ask: did they already take a next step (list promised, call booked, bid process, handed to someone else, waiting on a date they named)? If yes, write to THAT state. Do not send a generic cadence nudge.
4. Ask: is silence actually due, or was our last sender message so recent / so action-forcing that another touch is premature? If premature, skip and note why in the tracker.
5. The FU must reference their specific inventory, timeline, or open loop. If you cannot name it from the thread, do not send.

Fail = generic chase, wrong timing, or ignoring steps already taken.
Pass = one short, situation-specific question that only makes sense for this thread.

Also run [humanizer](sand-workflow:humanizer) and [Outbound QC gate](sand-workflow:outbound-qc-gate) before send. No em dashes.

## Qualify every run (full thread first)
**IN:** named surplus sitting now, device/counts/models, "yes we have X", asked for a quote on inventory they control, or asked to talk about current inventory that is NOT locked behind a formal bid.
**OUT:** nothing now, we'll let you know, maybe later this year, keep-in-mind / warm future, OOO, unsub/nah, wrong person with no surplus owner.
**BID/RFP:** hand off once to the client owner and STOP cadence (see [ListKit hot-lead forward](sand-workflow:listkit-hot-lead-forward)). Do not NEPQ bid threads.
Trust/domain questions are a separate track, not this surplus cadence unless they also have quoteable now-inventory.
Recategorize if the ListKit label disagrees with the thread ([ListKit category hygiene](sand-workflow:listkit-category-hygiene)).

**STOP and remove when:** they booked (confirmed in-thread or by the operator, never invent), they tell you to stop / unsub / not interested, bid handoff, or they convert to later-not-now. New now-inventory resets follow-up count to 0.

## Cadence (client timezone, weekdays only)
After last inbound OR your last sender reply, whichever is later:
- FU1 at 3 days of silence
- FU2 at 3 more days (day 6)
- FU3 at 3 more days (day 9)
- Then every 4 days until stop
If due Sat/Sun, send next weekday. Never send twice the same day. Stay silent if nobody is due.
Cadence is a calendar hint only. Context can override: skip or delay if the thread says wait, or if steps are already in motion.

## Tracker
Keep a JSON tracker of active now-positives, fu_count, last_touch, and excluded_not_now with reasons. Scan Master Inbox Interested for new now-positives not yet on the list. Log skip reasons when cadence was due but context blocked the send.

## NEPQ / pattern-interrupt copy
High status, curious, short. You are not chasing.
**Banned phrases:** just following up, following up, circling back, checking in, touching base, bumping this, any news, per my last email, wanted to reconnect, looping back, hope this finds you, we'd love to work with you, just wanted to see.
**Do:** lead with one question about THEIR situation (the inventory or timeline they named). One idea per email. 1–4 short lines. Vary copy every time.
- FU1: situation question tied to exact inventory. Light next step without dumping every asset if the last sales reply already had them.
- FU2: problem / consequence if it sits or the window moves.
- FU3: status drop, not needy. Tried a couple times… Where should we go from here?
- FU4+: rotate a new interrupt; keep shortening.

Re-offer booking or list-for-quote only when it is the natural answer. Match the campaign signature.

## Report
Tell the operator only when you sent a follow-up, skipped a due FU for context reasons, forwarded a hot/trust/bid lead, moved someone off cadence, or added a new now-positive. One line per lead. Stay silent if nobody was due.
