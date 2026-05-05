---
name: standup
description: Write a daily standup from recent git commits. Pass 'yesterday' or 'week' to scope by timeframe.
argument-hint: [optional: yesterday | week]
allowed-tools: Bash(git log:*) Bash(git status:*)
---

Generate a daily standup from git history. Argument: **$ARGUMENTS**

## Step 1 — Gather data

Choose the git log command based on the argument:

- **"yesterday"** → `git log --oneline --since="yesterday" --format="%s"`
- **"week"** → `git log --oneline --since="1 week ago" --format="%s"`
- **anything else (default)** → `git log --oneline -10 --format="%s"`

Then always run: `git status --short`

## Step 2 — Write the standup

Output exactly this structure, nothing else:

**Yesterday**
- (1–3 bullets of what got done, based on the git log)

**Today**
- (1–2 bullets of what logically comes next, inferred from the work done)

**Blockers**
- None (or one bullet if git status shows something stuck or conflicted)

## Rules — follow without exception

- Plain English only — no commit SHAs, no branch names, no jargon
- One short sentence per bullet (under 15 words)
- Infer "Today" from the direction of recent commits — don't make things up
- If git log returns nothing: write "No commits found in this timeframe" under Yesterday
- If merge conflicts or a pile of untracked files appear in git status, flag it under Blockers
