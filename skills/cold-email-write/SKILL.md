---
name: Cold email write
description: >-
  HARD RULE: ColdIQ/Braun/Voss + company research for personalization; mandatory
  humanizer then outbound-qc-gate before any Instantly/outbound send; always use
  blank-line Instantly formatting; critique bans
  mail-merge/pitchy/CRM-only/AI-tell/bunched openers.
---
# Cold email write (ColdIQ + Braun + Voss)

## HARD RULE (no exceptions unless the operator explicitly overrides)

Always follow proven frameworks. Frameworks beat speed.

1. **ColdIQ / Michel Lieben** — Trigger → Pain → Value → CTA; Short-Trigger; unique E1/E2/E3; shell under ~75–100 words; colleague subjects; no links in E1.
2. **Josh Braun** — Line 1 after greeting = **Think / poke QUESTION** with why-them-why-now. Conversational peer tone. Not pitchy.
3. **Chris Voss** — "If more sales calls isn't a bad outcome for you, I can show you the exact roadmap sometime next week?"
4. **Company research required** — ListKit/CRM fields alone are NOT enough. Research site/news/LinkedIn/interviews/rankings for a specific hook before writing `{{personalization}}`.
5. **Segment proof** — Josh/Plumber SEO only on confirmed 7FA.
6. **Mandatory send stack** — Before any guest/prospect/public Instantly or outbound send: run [humanizer](sand-workflow:humanizer), then [Outbound QC gate](sand-workflow:outbound-qc-gate), then send (plus [Instantly no double-send](sand-workflow:instantly-no-double-send) on replies). Humanizer is not optional. AI tells like "stands out" are fails.
7. **Line spacing (ALL cold emails, always)** — Never ship bunched text. Every paragraph / sentence beat gets its own block with a blank line between. Instantly HTML uses `<div>line</div><div><br /></div><div>next</div>` (never smash into one div or one newline-less string). Plain text uses real blank lines (`\\n\\n`). Signature lines can stack without a blank between name and company, but there MUST be a blank line before the signature block. Fail QC if the body looks like a single wall of text.

## Critique checklist (run on every E1 before ship)

Fail and rewrite if any:
1. **Mail-merge line 1** — swapping company+industry still works (no unique researched hook).
2. **Bio/statement opener** — "Company is the world's largest..." or about-page paste.
3. **CRM-only hook** — only used Industry/Keywords/employees with no public company research.
4. **Stale contact** — research shows person left / wrong title; remove or replace lead.
5. **Pitchy early** — "We built..." / feature dump before soft value + CTA.
6. **Framework narration** — "That gap shows up a lot for X agencies..." as scaffolding.
7. **Not conversational** — sounds like sequence software, not a peer note.
8. **Redundant lines** — line 2 only restates line 1.
9. **Vanity** — world's largest, cutting edge, first-to-market as the hook.
10. **Empty personalization**.
11. **AI stamp phrases** — stands out, stuck with me, delve, landscape, testament, pivotal, in today's world, it's not just, more than just, at its core, etc. (full list in outbound-qc-gate).
12. **Bunched formatting** — missing blank lines / smashed Instantly divs.

## Opener rule

Line 1 after `Hey {{firstName}},` MUST:
- End with `?`
- Include a **specific researched hook** (news, hire, launch, ranking, quote, handoff) inside the question
- Name the company or a fact only true for them
- Sound like something you'd send one peer, not 313

## Conversational E1 shape (ListKit / non-7FA)

Hey {{firstName}},

{{personalization}}  ← researched poke question ONLY

One short peer implication (optional, not category lecture).

Soft value without "we built" (what it does for their calendar, plain).

Voss CTA (sometime next week).

Sig: use the operator-configured sender signature for this campaign.

## Instantly format
- Prefer HTML div paragraphs with `<div><br /></div>` between beats even when `text_only` is true (Instantly often stores HTML under the hood).
- Subject exact as specified; no accidental HTML in subject.
- Never paste a single multi-sentence paragraph without breaks when the beats are meant to breathe.

## E2 / E3
E2 = new angle before/after (never bump).
E3 = delegation / breakup.

## Research process before personalization
1. Open company site + recent news/LinkedIn.
2. Confirm contact still valid.
3. Pick one hook; kill vanity.
4. Write poke question; run critique checklist.
5. Humanizer → outbound-qc-gate → only then patch Instantly.

## Living rules
Update this skill same turn when the operator criticizes copy. On any quality miss: fix live artifact, then skillize via [Skillize after every miss](sand-workflow:skillize-after-every-miss).
