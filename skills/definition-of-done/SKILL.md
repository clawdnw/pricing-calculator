---
name: definition-of-done

triggers:
  - "task complete"
  - "marking done"
  - "is this done"
  - "review"
related:
  - "[[mc-task-management]]"
  - "[[operator-doctrine]]"
  - "[[root-cause-standard]]"
description: >
  Prevents fake completion. A task is NOT done because someone says it is.
  Use when: marking a task as complete, reviewing completed work, or auditing task quality.
  Use when: someone claims work is done but can't point to the output.
  Don't use when: work is still in progress (just update activity).
  Don't use when: the task was explicitly killed or archived.
  Output: Task verified as genuinely complete with durable output.
  Anti-patterns: "Done!" without output, completed tasks with no location, "it works" without verification.
---

# Definition of Done

## The Rule

> A task is NOT complete because someone says it is.

## A Task is Complete ONLY When

1. **Output exists in a durable location**
   - File path, URL, repo, deployment — something concrete
   - NOT "I did it" or "it's in my session"

2. **Output is usable without additional explanation**
   - Someone else can find it, open it, and use it
   - No tribal knowledge required

3. **Output matches the objective**
   - Does it solve the problem stated in the task?
   - Not "close enough" — actually matches

4. **Review is completed** (if review was required)
   - Reviewer approved it
   - Feedback was addressed

5. **MC task is updated** with:
   - `status: "complete"`
   - `outputLocation` — where the work lives
   - `completionEvidence` — what was produced and how it meets criteria
   - Final activity log entry

## The Test

> If someone asks "What did this actually produce?" and the answer is unclear, the task is not done.

## Task Completion Template

When marking a task complete, update these fields:
```json
{
  "status": "complete",
  "outputLocation": "[file path / URL / repo]",
  "completionCriteria": "[what success looks like]",
  "completionEvidence": "[proof it meets criteria]"
}
```

And add an activity entry:
```json
{
  "timestamp": "[ISO]",
  "action": "COMPLETE: [what was produced and where it lives]",
  "by": "[agent]"
}
```

## Review Tasks (Moving to Review, Not Complete)

When a task needs Tyler's review:
```json
{
  "status": "review",
  "reviewers": ["tyler"],
  "reviewInstructions": "[where to find the thing, what to check, how to evaluate, criteria for moving to complete]"
}
```

## Enforcement

When auditing completed tasks, check:
- [ ] `outputLocation` is set and valid
- [ ] `completionEvidence` explains what was produced
- [ ] The output actually exists at the location
- [ ] The output matches the task description
- [ ] Activity log shows the completion

If ANY check fails → task is NOT done. Reopen it.

## Examples

### ❌ Fake Complete
```
status: "complete"
outputLocation: ""
completionEvidence: ""
activity: [{ action: "Done" }]
```
**Why bad:** Where is the output? What was produced? This proves nothing.

### ✅ Real Complete
```
status: "complete"
outputLocation: "https://clawdnw.github.io/portfolio/"
completionCriteria: "Portfolio page live with cards for all demos"
completionEvidence: "19KB single HTML deployed via GitHub Pages. Dark theme, 4 project cards, responsive. curl returns 200."
activity: [{ action: "COMPLETE: Portfolio index deployed to https://clawdnw.github.io/portfolio/" }]
```
