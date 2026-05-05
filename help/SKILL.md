---
name: help
description: Stuck or want to see your options — list available course skills and recommend the right one.
argument-hint: [optional: describe what you're trying to do]
allowed-tools: Read Glob Bash(ls:*)
---

The user wants help. Either they're stuck on something specific, or they want to see what tools they have. Be direct, list what's relevant, recommend one next step.

## Steps

1. **Read the situation.**
   - If $ARGUMENTS describes a problem ("my tests are failing", "I need to ship this", "I don't know how to start"), skip to step 3.
   - If $ARGUMENTS is empty, ask the user one question: "What are you trying to do right now?"

2. **List the 7 course skills** with one-line descriptions:

   ```
   /kickoff   — Starting any new feature or project
   /review    — Before any git commit
   /scaffold  — Starting a new project from scratch
   /help      — You're stuck or want to see your options (you're here)
   /fix       — Something is broken
   /commit    — Ready to commit — runs a secret check first
   /deploy    — Ready to go live
   ```

3. **Recommend one skill** based on what the user said. Map their words to the right command:

   | If the user says... | Recommend |
   |---|---|
   | "I'm starting [a new thing]" | `/kickoff` |
   | "I want to build [a brand new project from scratch]" | `/scaffold` |
   | "I'm about to commit / I'm done" | `/review` then `/commit` |
   | "Something broke / it's not working" | `/fix` |
   | "I'm ready to push / go live" | `/deploy` |
   | "I don't know where to start" | `/kickoff` |

4. **If they're stuck on something the skills don't cover**, just answer the question directly. Don't force a skill recommendation that doesn't fit.

5. **Keep it short.** This is help, not a tutorial. Three to five lines is usually enough.

## Output format

```
**You're trying to:** <one-sentence restatement of what they said>

**Best skill for this:** /<skill-name>

**Why:** <one sentence>

**Run it like this:** /<skill-name> [optional argument]
```

## Rules

- Don't over-explain. The skills have their own help.
- Don't recommend chained commands (`/kickoff` then `/commit`) unless the user is asking about a full workflow.
- If the user is venting frustration, acknowledge it in one sentence before recommending a skill.

$ARGUMENTS
