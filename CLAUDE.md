# CLAUDE.md

## Project Overview
Client Progress Dashboard is a client-facing web app where coaching clients log
structured weekly check-ins, track custom progress metrics defined by their coach,
and view a personal timeline of their growth over time. It is the client-side
companion to the Coach Client Progress Tracker. Coaches receive a read-only digest
of client check-ins in v1; all coaching-side management lives in the separate coach
tool. The product prioritizes simplicity and speed — a check-in should take under
5 minutes.

## Tech Stack
- Language: TBD — recommend TypeScript throughout
- Framework: TBD — recommend Next.js (pairs naturally with the coach tool if
  sharing a monorepo)
- Database: TBD — recommend PostgreSQL via Supabase (magic link auth included)
- Hosting / Infra: TBD

> **Fill this section in before writing any code.**

## Commands
> Fill in once stack is confirmed.
- Dev server: TBD
- Build: TBD
- Test: TBD
- Lint: TBD

## Environment Variables
> Fill in once stack is confirmed.
- Auth provider credentials (e.g. SUPABASE_URL, SUPABASE_ANON_KEY)
- Database connection string
- Email provider key (for magic link / reminders)

## Testing
> Fill in once stack is confirmed. All data-layer code must have integration tests
> against a real database — do not mock the DB in tests.

## Coding Style
Follow idiomatic conventions for the chosen language. Until the stack is confirmed,
no framework-specific patterns should be added here.

## Key Rules
- All data is strictly scoped to the authenticated client — never return or expose
  another client's check-ins, metrics, or profile under any circumstances.
- The coach digest view is read-only in v1 — no coach-side editing, commenting,
  or mutation of client data.
- Check-in question structure is fixed in v1 — do not build a dynamic form
  configuration system until that feature is explicitly scoped.
- Treat all client entries as sensitive personal data (health, finances, personal
  struggles) — no PII in logs or error trackers without scrubbing.

## What Claude Should Never Do
- Write code not covered by the v1 scope in the PRD (no messaging, coach editing,
  group/cohort features, native mobile).
- Change the tech stack without explicit user approval.
- Build dynamic check-in question configuration — questions are fixed in v1.
- Skip asking when the relationship between this product and the Coach Client
  Progress Tracker is ambiguous (shared DB? monorepo? separate deploy?).
