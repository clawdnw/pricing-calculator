---
name: root-cause-standard
description: >
  Enforce root-cause analysis on every fix. Treat causes, not symptoms.
  Use when: fixing bugs, resolving errors, debugging failures, reviewing fixes.
  Use when: a fix was applied but the problem recurred.
  Use when: reviewing someone else's fix for completeness.
  Don't use when: the fix is trivial and obvious (typo, missing import).
  Don't use when: doing new feature work (not a fix).
  Output: Fix that addresses the underlying mechanism with explanation of why it prevents recurrence.
  Anti-patterns: Symptom-fixing, "it works now" without understanding why, retry-until-it-works, suppressing errors.
---

# Root-Cause Standard: Treat Causes, Not Symptoms

## Why This Matters

Symptom-fixing creates regressions, increases token cost over time, and turns the organization into recurring firefights. A fix that doesn't address the root cause will break again.

## The Standard

Any meaningful fix MUST include:

1. **Clear problem definition** — What exactly is broken? What's the expected behavior vs actual behavior?
2. **Likely root causes** — What could cause this? List at least 2-3 hypotheses.
3. **Evidence supporting the root cause** — How do you know THIS is the cause? Logs, traces, reproduction steps.
4. **Fix that addresses the cause** — Not the symptom. The mechanism that created the failure.
5. **Recurrence prevention** — Why won't this happen again?

## The Test

> If you cannot explain what created the failure and why your fix prevents recurrence, the work is not complete.

## Fix Template

```markdown
## Fix: [Brief description]

**Problem:** [What broke — specific error, behavior, impact]
**Root cause:** [The underlying mechanism that caused it]
**Evidence:** [How you confirmed this was the cause]
**Fix applied:** [What you changed and why it addresses the cause]
**Recurrence prevention:** [Why this won't happen again]
```

## Examples

### ❌ Symptom Fix
> "MC was returning 500 errors. Restarted the server. It works now."

**Why bad:** No understanding of WHY it was 500ing. Will happen again.

### ✅ Root-Cause Fix
> "MC was returning 500 errors. Checked logs: `Error: ENOSPC: no space available`. Disk was at 99% because .next cache grew unbounded. Cleared cache (freed 2GB), added .next to .gitignore, and set up a cron to clear cache weekly. Root cause: Next.js dev server accumulates cache without cleanup."

### ❌ Symptom Fix
> "The cron job was timing out. Increased timeout from 300s to 600s."

**Why bad:** Doubling timeout masks the real problem. The job shouldn't take that long.

### ✅ Root-Cause Fix
> "The cron job was timing out at 300s. Profiled the execution: the agent was reading all 636 QMD docs before starting work (180s just on file reads). Root cause: the skill prompt didn't specify to skip QMD indexing. Fixed the prompt to be task-specific. Job now completes in 45s."

## Enforcement

When reviewing a fix (yours or another agent's), ask:
1. Can they explain what caused the failure?
2. Can they explain why this fix prevents recurrence?
3. Is there a regression test or monitoring to catch it if it happens again?

If any answer is "no" — the fix is incomplete. Send it back.

## When to Skip

- **Typos and missing imports** — obvious cause, no analysis needed
- **First-time setup** — not a regression, just configuration
- **External service outages** — document, but can't fix someone else's infrastructure

## Log to REGRESSIONS.md

Significant failures (not typos) get logged:
```markdown
## [Date] — [Brief title]
**Symptom:** [What was observed]
**Root cause:** [What actually caused it]
**Fix:** [What was done]
**Prevention:** [What stops recurrence]
**Lesson:** [What we learned]
```
