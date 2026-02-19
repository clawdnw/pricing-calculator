---
name: kill-authority
description: >
  Authority to pause, kill, archive, or scope-reduce work. Plus the escalation ladder.
  Use when: work misaligns with objectives, has unclear upside, burns tokens without leverage, or blocks higher-value execution.
  Use when: deciding whether to escalate an issue or resolve it at current level.
  Don't use when: Tyler explicitly assigned the work (discuss with him first).
  Don't use when: killing work that another agent is actively delivering well.
  Output: Low-value work killed or reduced; escalation handled at correct level.
  Anti-patterns: Letting low-value work linger, escalating trivially to Tyler, killing work without documentation.
---

# Kill Authority & Escalation Ladder

## Kill Authority (Explicit)

You are authorized to pause, kill, archive, or scope-reduce work that:

- **Misaligns with objectives** — doesn't serve $40K goal or Tyler's quality of life
- **Has unclear upside** — can't articulate the value after 2 minutes of thought
- **Burns tokens without leverage** — consuming resources without compounding returns
- **Is "interesting" but not useful** — intellectual curiosity ≠ business value
- **Blocks higher-value execution** — opportunity cost exceeds the work's value

> Sunsetting weak paths is not failure. Letting low-value work linger IS failure.

## How to Kill Work

1. **Document why** in the task activity: "KILLED: [reason]"
2. **Update status** to `complete` with note "Archived — [reason]"
3. **Don't delete** — archive so we remember why we killed it
4. **Redirect energy** to higher-value work immediately

## Kill Criteria Checklist

Before killing, confirm at least one:
- [ ] Misaligns with current priorities (check direction.json)
- [ ] Upside is unclear after honest evaluation
- [ ] Cost exceeds value (time, tokens, complexity)
- [ ] Better alternative exists
- [ ] Blocking higher-priority work

## Escalation Ladder (Enforce Strictly)

```
Level 1: Agent resolves independently
         ↓ (if stuck)
Level 2: Agent consults another agent
         ↓ (if unresolved)
Level 3: Lead agent moderates in team-chat → decision
         ↓ (if high stakes or disagreement)
Level 4: War-room → structured debate → committed plan
         ↓ (LAST RESORT)
Level 5: Escalate to Tyler
```

### Rules
- **Most issues resolve at Level 1-2.** If they don't, that's a skill gap — build the skill.
- **Level 3-4 must produce decisions**, not more discussion.
- **Level 5 (Tyler) is last resort.** If issues reach Tyler that should have been resolved earlier → process failure. Fix the process.

## When to Escalate vs When to Kill

| Situation | Action |
|-----------|--------|
| Work has no clear value | Kill it |
| Work has value but is blocked | Escalate (find unblock) |
| Work has value but lower than alternatives | Scope-reduce or pause |
| Disagreement on approach | Escalate to team-chat/war-room |
| Disagreement on whether to do it at all | Run through value gate (autonomy-charter skill) |

## Anti-Patterns

- ❌ Keeping a task alive because "we already started it" (sunk cost fallacy)
- ❌ Escalating to Tyler when you could decide yourself
- ❌ Killing work silently without documentation
- ❌ Letting blocked tasks sit for days without action
- ❌ "Pausing" work indefinitely (that's just killing it slowly — commit to a decision)
