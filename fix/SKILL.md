---
name: fix
description: Something is broken — diagnose the most recent error or failure and propose a minimal fix.
argument-hint: [optional: describe what's broken or paste the error]
allowed-tools: Read Grep Glob Edit Bash(git status:*) Bash(git diff:*) Bash(git log:*) Bash(npm test:*) Bash(npm run:*) Bash(pytest:*) Bash(python:*) Bash(node:*)
---

Something is broken. Find it. Fix it. Don't expand scope.

## How to find the problem

1. **Read the most recent signal.**
   - The latest terminal output in this conversation.
   - Any failing test output.
   - Any error message in $ARGUMENTS.
   - Recent edits — `git status` and `git diff` to see what just changed.

2. **If the error isn't obvious**, ask one specific question:
   - Which file? Which command? What did you see vs. expect?
   - Don't guess — confirm before changing code.

3. **Read the relevant code in full.**
   - Open the file the error points at.
   - Read the function or component, not just the line.
   - Check imports and call sites if the error involves a name that's not defined.

## How to fix it

1. **Identify the smallest change** that resolves the failure.
   - One file edit if possible. Two if it has to be.
   - No "while I'm in here" refactoring.

2. **Make the fix.** Show the diff before applying if it's more than a few lines.

3. **Re-run whatever was failing.**
   - The test that broke. The build command. The script. The dev server.
   - Confirm green before reporting "fixed".

4. **If the fix has side effects on other files**, list them — don't silently propagate.

## What not to do

- **Don't add error handling, logging, or fallbacks** for hypothetical future failures. Fix the actual failure.
- **Don't add comments** explaining what the code now does.
- **Don't bundle unrelated cleanups** into this fix.
- **Don't bypass safety** — no `--no-verify`, no `--force`, no skipping tests, no commenting out the assertion.
- **Don't catch-and-swallow** the error to make the symptom go away.

## Output format

```
**Problem:** <one-sentence diagnosis>

**Root cause:** <why it broke — be specific>

**Fix:** <what changed and where>

**Verified by:** <command you ran + result>
```

## Rules

- If you're not sure what's broken, ask. Don't fix a guess.
- If the same error has come up multiple times, suggest a regression test before closing.
- If the fix exposes a deeper structural issue, flag it — but don't fix it. That's a separate task.

$ARGUMENTS
