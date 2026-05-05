---
name: commit
description: Commit your work — scans for secrets first, then drafts a clean commit message for approval.
argument-hint: [optional: hint about what this commit is about]
allowed-tools: Read Grep Bash(git status:*) Bash(git diff:*) Bash(git log:*) Bash(git add:*) Bash(git commit:*)
---

The user is ready to commit. Your job: **scan for secrets first**, then draft a clean message and ship it after approval.

## Step 1 — Secret scan (non-negotiable)

1. Run `git diff --staged` and `git diff` to see everything that's about to land.
2. Scan for any of the following patterns. **If even one matches, STOP.**
   - API key shapes: `sk_live_*`, `sk_test_*`, `AIza*`, `AKIA*`, `ya29.*`, `ghp_*`, `xoxb-*`, `xoxp-*`.
   - Generic key/token strings of 32+ chars assigned to variables named `key`, `secret`, `token`, `password`, `auth`, `api_key`, `apikey`.
   - Lines from a `.env` file: `KEY=value` patterns where value is non-trivial.
   - Private key headers: `-----BEGIN PRIVATE KEY-----`, `-----BEGIN RSA PRIVATE KEY-----`, `-----BEGIN OPENSSH PRIVATE KEY-----`.
   - Anything that looks like a secret an attacker could use, even if you can't name the format.

3. **If a match is found:**
   ```
   ❌ SECRET DETECTED — commit blocked.

   Found in: <file>:<line>
   Pattern: <what matched>

   Before committing:
   1. Move the value to a `.env` file (gitignored).
   2. Reference it in code via `process.env.NAME` (or your language's env-read).
   3. Run /commit again.

   If you've ALREADY pushed this somewhere, treat the secret as compromised and rotate it immediately.
   ```
   Do not commit. Do not pass go.

4. **If clean**, continue.

## Step 2 — Quick sanity check

Skim `git diff` for:
- Debug code left in (`console.log`, `print(`, `debugger`, `pdb.set_trace`).
- Commented-out blocks the user probably meant to delete.
- Unintended changes (config files modified by accident, lockfiles updated when no deps changed).

If you spot any, surface them — let the user decide whether to keep, fix, or carry on.

## Step 3 — Draft the commit message

Read the diff. Write a message in the project's existing style (look at `git log -10 --oneline` for tone — short imperative? conventional commits? prose?).

**Default format if no style is obvious:**
```
<type>: <one-line summary in present tense, under 70 chars>

<optional body — 1–3 short paragraphs explaining the WHY, not the WHAT>
```

Common types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`.

## Step 4 — Show + approve

Print the proposed commit message and ask: "Commit with this message? (yes / edit / cancel)"

- **yes** → run `git commit -m "<message>"` (or with `-F` for multi-line).
- **edit** → ask for changes, redraft, show again.
- **cancel** → don't commit.

## Step 5 — Confirm

After committing, show the new commit hash and the one-line summary so the user knows it landed.

## Rules

- **Never use `--no-verify`.** Hooks exist for a reason. If a hook fails, fix the underlying issue.
- **Never amend a published commit** unless the user explicitly asks.
- **Never `git add -A` or `git add .`** — only stage files the user has already staged or named explicitly. Bulk-add picks up `.env` and other surprises.
- **Don't push.** Pushing is a separate step. This skill ends at the local commit.

$ARGUMENTS
