---
name: operating-loop
description: >
  The default operating loop every agent runs continuously: Observe → Clarify → Structure → Assign → Track → Converge.
  Use when: running heartbeats, moderating discussions, reviewing team state, or detecting drift.
  Use when: something feels off but you can't pinpoint what — run the loop to find the broken step.
  Don't use when: executing a specific task (just do the task).
  Don't use when: Tyler gave explicit instructions (follow them, then resume the loop).
  Output: Identified gaps in execution, corrective actions taken.
  Anti-patterns: Skipping steps, observing without acting, assigning without tracking, tracking without converging.
---

# Default Operating Loop

## The Loop (Non-Optional)

```
Observe → Clarify → Structure → Assign → Track → Converge
```

This is the leadership operating system. Run it continuously.

## Each Step

### 1. Observe
- Read Mission Control (tasks.json, projects.json, direction.json)
- Scan agent chatter and recent activity
- Detect: drift, stalls, confusion, blocked work, idle agents

**Output:** List of things that need attention

### 2. Clarify
- Turn vague ideas into concrete objectives
- Define constraints and success criteria
- Ask: "What does DONE look like?"

**Output:** Clear problem statement with measurable outcome

### 3. Structure
Choose the right mode for the work:
- **Async task** → Agent works independently, updates MC
- **Moderated team-chat** → Multiple agents need to converge
- **War-room** → High stakes, disagreement, or strategic pivot

Break work into explicit options and tasks.

**Output:** Structured work items with clear mode

### 4. Assign
- ONE owner per task (no shared ownership)
- Explicit outcome defined
- Check-in defined (when will progress be visible?)
- Logged in Mission Control

**Output:** Tasks in MC with owners and outcomes

### 5. Track
- Monitor Mission Control for progress
- Demand progress signals from owners
- Surface blockers early (don't wait for agents to report them)
- Check: Is work actually moving, or just "in progress"?

**Output:** Updated task statuses, unblocked work

### 6. Converge
- Summarize what happened
- Make decisions (don't leave things open)
- Kill weak paths
- Commit to strong paths
- Update direction.json if priorities shifted

**Output:** Decisions made, weak paths killed, strong paths funded

## Diagnosis

> If execution decays, one of these steps is missing. Your job is to identify the missing step and repair it immediately.

| Symptom | Missing Step |
|---------|-------------|
| "What are we doing?" | Clarify |
| "Who's doing this?" | Assign |
| "Is anyone working on X?" | Track |
| "We discussed this 3 times" | Converge |
| "Nobody noticed it broke" | Observe |
| "This task is too vague" | Structure |

## Heartbeat Integration

Every heartbeat is a mini-loop:
1. **Observe** — Read kanban, check systems
2. **Track** — Are in-progress tasks moving?
3. **Converge** — Complete what's done, unblock what's stuck
4. **Assign** — Pull next task if queue is empty

## Anti-Patterns

- ❌ Observing without acting (noticing problems but not fixing them)
- ❌ Assigning without tracking (tasks disappear into the void)
- ❌ Tracking without converging (endless "in progress" with no completion)
- ❌ Skipping Clarify (vague tasks that nobody can complete)
- ❌ Discussions that end without decisions, tasks, or escalation
