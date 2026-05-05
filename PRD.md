# PRD: Client Progress Dashboard

## Problem
Coaching clients have no independent visibility into their own progress. Between
sessions, they rely entirely on their coach to hold the record of what was
committed to, what was accomplished, and how far they've come. Without a personal
log, motivation fades, accountability weakens, and clients underestimate their own
growth. The coach becomes a bottleneck for a client's self-awareness.

## Goals
1. Clients can complete a weekly check-in in under 5 minutes.
2. Clients can view a visual timeline of progress across their tracked metrics
   without needing to ask their coach.
3. 70% of onboarded clients log at least one check-in per week for their first
   4 weeks.
4. Coaches receive a structured summary of client check-ins without manual
   follow-up or chasing.

## Target Users
**Primary:** Coaching clients actively working toward goals with a professional coach.
- Roles: individuals in life, fitness, business, or wellness coaching programs.
- Context: motivated but busy; they have goals and a coach but no system of record
  for their own progress.
- Pain points: forgetting what they committed to last session, losing sight of
  progress, feeling unaccountable between sessions, no visual record of wins.

**Secondary:** The client's coach — receives a digest of check-ins (read-only in v1).

## Scope

### In scope
- Client auth: email/magic link login (no passwords to manage)
- Weekly check-in form: structured fields (reflection, accomplishments, next-week
  commitment) + optional freeform notes
- Custom metric entries: log a value against a coach-defined metric (e.g. weight,
  revenue, sleep hours)
- Progress timeline: chart or list view of metric values over time
- Check-in history: searchable log of all past check-ins
- Coach digest: read-only summary view of a client's recent check-ins (v1: no
  coach-side editing or commenting)

### Out of scope
- Coach admin portal (separate product — see Coach Client Progress Tracker PRD)
- Direct messaging or chat between client and coach
- Coach-defined check-in questions (v1 uses fixed structure; customization deferred)
- Group or cohort progress comparisons
- Payment or subscription management
- Native mobile app (responsive web only in v1)

## Success Criteria
- Check-in completion time < 5 minutes (validated by user test with 5 clients).
- 70% of clients log ≥ 1 check-in/week during weeks 1–4 post-onboarding.
- Clients can locate any past check-in within 10 seconds.
- Zero cross-client data leaks: a client can only ever see their own data.

## Risks
1. **Engagement drop-off:** Clients are motivated at signup but stop logging within
   2–3 weeks. Without reminders or intrinsic value, the product becomes shelfware.
   Need a notification strategy and a progress view compelling enough to revisit.
2. **Sequencing dependency with the coach tool:** Custom metrics are defined by the
   coach. If the coach hasn't set them up, the client has nothing meaningful to
   track. The two products need a handoff mechanism or sensible defaults for clients
   whose coaches aren't on the platform yet.
3. **Privacy expectations:** Clients log health, financial, and personal data. Any
   breach or accidental cross-client data exposure is a trust-ending event. Auth
   and data scoping must be airtight from day one.

## Open Questions
- Does the coach define the weekly check-in questions, or are they fixed for all
  clients in v1?
- How does a client get invited — pushed by their coach, or can they self-sign-up
  and link to a coach later?
- Should there be automated reminders for weekly check-ins? If so, email or push
  notification?
- Can the coach comment on or respond to a check-in in v1, or is the digest
  strictly read-only?
- What is the relationship between this product and the Coach Client Progress
  Tracker — same codebase, separate apps, or a monorepo?
