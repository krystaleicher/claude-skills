---
name: review
description: Pre-commit code review of your staged and unstaged changes — bugs, security, regressions, missing tests.
argument-hint: [optional: file or area to focus on]
allowed-tools: Read Grep Glob Bash(git diff:*) Bash(git status:*) Bash(git log:*) Bash(git branch:*)
---

Review what's about to be committed. This runs **before** `/commit` — it catches problems while they're still cheap to fix.

## Steps

1. **See what changed.**
   - `git status` — list staged and unstaged files.
   - `git diff` — unstaged changes.
   - `git diff --staged` — staged changes.
   - If $ARGUMENTS names a file or folder, narrow the review to that path.

2. **Read the changed files in full.**
   - Don't review just the diff — context lives in the surrounding code.
   - Open each modified file and read the function or component being changed.

3. **Flag issues in this order of severity.**

   **Blocking** — fix before commit:
   - Bugs (off-by-one, null paths, race conditions, wrong return types).
   - Secrets in code (API keys, passwords, tokens, `.env` contents pasted in).
   - Auth/security holes (missing auth checks, unsafe deserialisation, injection).
   - Regressions (behaviour changes the diff didn't intend).
   - Broken builds (typos, missing imports, syntax errors).

   **Should fix** — fix soon:
   - Missing tests for new branches.
   - Dead code or unused imports.
   - Performance traps (N+1 queries, blocking I/O on hot paths).
   - Public API breakage with no migration plan.

   **Nit** — author's choice:
   - Style drift from the rest of the file.
   - Naming improvements.
   - Stale comments.

4. **Don't write the fix.**
   - Note one line of intent per issue. Let the author decide.
   - Exception: if you spot a leaked secret, scream loudly and stop the user from committing.

## Output format

```
## Review of <branch> (<N> files changed)

### Blocking
- `path/to/file.ts:42` — <one-sentence issue> · suggested fix: <one line>

### Should fix
- `path/to/file.ts:88` — <issue>

### Nits
- `path/to/file.ts:120` — <issue>

### What looks good
<one or two sentences on what's solid — only if true>
```

## Rules

- **Honest reporting.** No "looks good overall" if it doesn't. No invented issues to look thorough.
- If the diff is clean, say so plainly: "Nothing blocking. Ready to commit."
- Don't stack performative compliments. The author can read the diff themselves.

$ARGUMENTS
