---
name: deploy
description: Deploy to production — runs pre-deploy checks, confirms target, then ships.
argument-hint: [optional: prod | staging | preview]
allowed-tools: Read Grep Glob Bash(git status:*) Bash(git log:*) Bash(git push:*) Bash(npm test:*) Bash(npm run build:*) Bash(npm run lint:*) Bash(pytest:*) Bash(vercel:*)
---

The user is ready to go live. Your job: **run pre-deploy checks**, confirm the target, then deploy.

## Step 1 — Pre-deploy checks (all must pass)

1. **Working tree is clean.**
   - `git status` — no uncommitted changes. If there are, ask the user to `/commit` first or to stash.

2. **Tests pass.**
   - Detect the test runner (`package.json` `scripts.test`, `pytest`, etc.).
   - Run the test suite and wait for green.
   - If tests fail, **stop**. Show the failures. Don't deploy red.

3. **Build succeeds.**
   - Detect the build command (`npm run build`, etc.).
   - Run it. If it errors, stop and show the error.

4. **Lint clean** (if a linter is configured).
   - Run the lint command. Warn on warnings, stop on errors.

5. **Branch sanity.**
   - On the right branch for the target? (`main` for prod, a preview branch for previews).
   - Up to date with origin? (`git status` reports "Your branch is up to date").

6. **No debug code left.**
   - Quick grep for `console.log`, `debugger`, `print(`, `TODO: remove before deploy`.
   - Surface anything found and ask the user before continuing.

## Step 2 — Confirm the target

Identify the deploy target from $ARGUMENTS or the project's deploy config.

- `prod` / `production` → deploys to live users.
- `staging` → deploys to a pre-prod environment.
- `preview` → deploys an isolated preview URL.
- Default: ask the user. Don't assume prod.

**Ask explicitly before a production deploy:**
```
🚀 About to deploy to PRODUCTION.

Target: <env name + URL if known>
Branch: <current branch>
Last commit: <hash + summary>
Tests: ✅ passed
Build: ✅ passed

Proceed? (yes / cancel)
```

## Step 3 — Deploy

Run the deploy command:
- **Vercel:** `vercel --prod` (production) or `vercel` (preview).
- **Netlify, Fly, Cloudflare, etc.:** the project's documented command.
- **Custom:** if the project has a `npm run deploy` script, use it.
- **Git-driven (Vercel, Netlify auto-deploy from `main`):** `git push origin <branch>` and let CI take it.

If you're not sure what the deploy command is, **ask** — don't guess. Wrong deploy command on the wrong project can take a service offline.

## Step 4 — Verify post-deploy

1. Show the deploy URL.
2. Suggest a smoke check the user can run (open the URL, hit a healthcheck endpoint, watch logs for 30 seconds).
3. If the deploy reports an error, stop and surface it. Don't claim success when the platform reported failure.

## Step 5 — Report

```
✅ Deployed to <env>

URL: <url>
Commit: <hash> — <message>
Build time: <duration>
Smoke check: <pass / pending — go check>

Rollback: <one-line how to roll back if something's wrong>
```

## Rules

- **Never deploy with failing tests.** No exceptions.
- **Never deploy with uncommitted changes.** Commit first.
- **Never `git push --force`** to a deploy branch. If you think you need to, stop and ask the user.
- **Confirm before prod.** Even if the user typed `/deploy prod`, show the plan and wait for one explicit "yes."
- **Don't skip checks "just this once."** The checks exist because of past pain.

$ARGUMENTS
