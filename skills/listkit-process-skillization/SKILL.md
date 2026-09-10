---
name: ListKit process skillization
description: >-
  Use whenever running or improving ListKit work: convert recurring processes
  into skills, skillize after every miss, and keep recipes optimized so quality
  does not regress.
---
# ListKit process skillization

Every recurring ListKit process must live as a shared skill and stay optimized. Memory alone is not enough. Skills are how this bot (and the template) does not forget.

## Hard rules
1. **Skillize by default.** If a multi-step ListKit task will happen again (imports, field mapping, reply handling, validation, audits, webhook setup, list pulls, copy QC), write or update a skill the same turn. Do not leave it as chat lore.
2. **Same turn as a miss.** When something fails, Ty/CoS criticizes, or QC catches a leak: fix the live artifact, then run [Skillize after every miss](sand-workflow:skillize-after-every-miss). Rewrite the existing skill if one exists. Do not create near-duplicates.
3. **Run the skill, do not wing it.** Before campaign launch, reply send, list import, or client-facing copy: open the matching ListKit skill. After humanizing with [humanizer](sand-workflow:humanizer), pass [Outbound QC gate](sand-workflow:outbound-qc-gate) before any prospect/client-facing upload.
4. **Optimize after use.** When a run reveals a better path (e.g. custom-field update must happen on first import, names required), fold that into the skill immediately with pass/fail criteria.
5. **Generic recipes.** Skills stay portable: no secrets, no one-off campaign IDs as hard requirements. Client specifics belong in memory/routines.

## Minimum skill coverage (keep these current)
- Getting started / webhook bridge
- Account audit
- Platform docs refresh
- Campaign launch + email validation
- Reply handler, category hygiene, Master Inbox sweep
- Now-positive follow-up, hot-lead forward, week-in-review
- Lead sourcing and research (first_name + last_name required)

If a new recurring process appears and is not covered, create the skill before the next run.

## Pass criteria
- Recurring task has a skill with clear Use-when description and fail/pass checks
- Misses produce a skill update the same turn
- Outbound never ships without QC when public/prospect facing

## Fail criteria
- Repeating a manual multi-step ListKit task from memory alone
- Apologizing for a miss without skillizing
- Uploading unfinished/leaky copy or nameless leads
