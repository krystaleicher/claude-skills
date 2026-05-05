---
name: kickoff
description: Kick off a new feature or project — gather context, set the goal, plan the approach before writing code.
argument-hint: [optional: brief description of what you're starting]
allowed-tools: Read Grep Glob Bash(git status:*) Bash(git log:*) Bash(git branch:*) Bash(ls:*)
---

You're starting a new feature or project. The job here is **not to write code yet** — it's to load the right context, lock the goal, and plan the approach so the actual build goes fast and clean.

## Steps

1. **Read the project context.**
   - Check for `CLAUDE.md` at the repo root and read it if it exists.
   - Run `git status` and `git log --oneline -10` to see where the project is right now.
   - Run `git branch --show-current` and note whether we should branch.
   - Skim the top-level folder structure with `ls` to understand the shape of the codebase.

2. **Lock the goal in one sentence.**
   - If $ARGUMENTS is non-empty, treat it as the user's stated goal and confirm it back in your own words.
   - If empty, ask the user one specific question: "What are we starting today, in one sentence?"
   - Write the goal at the top of your response so we both have it.

3. **Plan the approach.**
   - **Files to touch / create.** List them with one-line descriptions.
   - **Dependencies.** Anything new to install? Any existing module to refactor?
   - **Risks.** Where could this go wrong? What's load-bearing in the current code?
   - **Definition of done.** What does success look like? How will we know it works?

4. **Surface clarifying questions.**
   - List any unknowns the user needs to answer before code happens.
   - Don't guess your way past ambiguity — ask.

5. **Recommend a branch name** if the work warrants a new one.

## Output format

```
## Goal
<one sentence>

## Plan
- File: <path> — <what changes>
- File: <path> — <what changes>
- New dependency: <name + reason> (if any)
- Risk: <one risk + how we'll handle it>

## Questions before we start
- <question 1>
- <question 2>

## Suggested branch
<branch-name>
```

## Rules

- **Don't write code in this skill.** This is the planning step. Code happens after.
- Keep the plan small enough to execute in one focused session. If it's bigger, recommend splitting.
- Prefer modifying existing patterns over inventing new ones.
- If `CLAUDE.md` says something specific about how the project works, follow it.

$ARGUMENTS
