---
name: living-principles
description: >
  Maintain PRINCIPLES.md and REGRESSIONS.md as living documents that encode lessons and prevent repeated failures.
  Use when: something fails repeatedly, a new decision heuristic is discovered, or during periodic maintenance.
  Use when: auditing whether past lessons are still being applied.
  Don't use when: logging routine task activity (use MC task notes).
  Don't use when: the lesson is specific to one task (log in task notes instead).
  Output: Updated PRINCIPLES.md or REGRESSIONS.md with encoded learning.
  Anti-patterns: Static principles that never update, regressions without prevention, accepting repeated failures as fate.
---

# Living Principles & Regressions

## The Philosophy

> Static prompts get stale. We are building a living operating system.

## PRINCIPLES.md — Decision Heuristics

### What Goes Here
Decision-making rules that:
- Resolve tensions between competing priorities
- Guide behavior in ambiguous situations
- Encode lessons from past experience
- Apply broadly (not to one specific task)

### Format
```markdown
## [Principle Name]
**Tension:** [What competing priorities this resolves]
**Rule:** [The heuristic — clear and actionable]
**Example:** [When this applies]
**Anti-pattern:** [What violating this looks like]
```

### When to Add a New Principle
- Same tension came up 2+ times
- A decision was hard and the resolution was generalizable
- An agent made the wrong call because no heuristic existed

### When to Update a Principle
- The principle led to a bad outcome (it was wrong)
- Circumstances changed (the principle is stale)
- A better formulation was discovered

## REGRESSIONS.md — Failure Log

### What Goes Here
Significant failures (not typos) with root causes and prevention.

### Format
```markdown
## [Date] — [Brief Title]
**Symptom:** [What was observed]
**Root cause:** [What actually caused it]
**Fix:** [What was done]
**Prevention:** [What stops recurrence]
**Lesson:** [What we learned — generalizable]
**Encoded in:** [Which file/skill was updated]
```

### When to Log
- A bug took >30 minutes to fix
- The same mistake happened twice
- A process failure caused visible impact
- A decision was reversed because it was wrong

### When NOT to Log
- Typos and trivial fixes
- First-time setup issues
- External service outages (not our fault)

## Maintenance Cadence

### Every Few Days (During Heartbeats)
1. Review recent `memory/YYYY-MM-DD.md` files
2. Check if any failures should be in REGRESSIONS.md
3. Check if any lessons should be in PRINCIPLES.md
4. Verify existing principles are still being followed

### Monthly
1. Review all principles — are they still relevant?
2. Review all regressions — are the preventions working?
3. Archive stale principles
4. Promote recurring regression lessons to principles

## The Meta Principle

> When something fails repeatedly, we do not accept it as fate. We treat it as signal, update the principle or workflow, and encode the improvement so it compounds.

## Anti-Patterns

- ❌ PRINCIPLES.md never changes (it should evolve)
- ❌ REGRESSIONS.md is empty (we definitely had failures)
- ❌ Logging a regression without updating the relevant skill/doc
- ❌ Principles that are vague ("be better") instead of actionable
- ❌ Accepting a repeated failure without investigating why the prevention didn't work
