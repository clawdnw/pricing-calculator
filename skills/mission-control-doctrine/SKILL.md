---
name: mission-control-doctrine
description: >
  Mission Control as the single source of truth — what it must contain, how to maintain it, and enforcement rules.
  Use when: setting up MC for the first time, auditing MC completeness, or when Tyler asks "what's happening?"
  Use when: something exists that isn't in MC (it needs to be added).
  Don't use when: doing routine task updates (use mc-task-management skill).
  Don't use when: building MC features (use code-standards skill).
  Output: MC reflects everything happening in the company.
  Anti-patterns: Work existing outside MC, stale task statuses, missing output locations, "I'll update MC later."
---

# Mission Control Doctrine

## The Rule (Absolute)

> If it isn't visible in Mission Control, it is assumed not to exist.

MC is not a nice-to-have. It's the operating substrate that makes autonomy real — progress observable, decisions auditable, work retrievable.

## What MC Must Represent

### Tasks (each with ALL of these)
- Clear name
- Associated project
- Single owner
- Status: Not Started / In Progress / Blocked / Review / Complete
- Progress notes (activity log)
- Durable output location (repo/doc/path/link)
- Reviewers if needed
- Critiques/comments that affect the work
- Completion criteria and evidence (when done)

### Projects (each with ALL of these)
- Purpose and strategic relevance
- Revenue/leverage potential
- Active tasks (linked)
- Owner
- Current phase
- Risks and blockers

### Direction & State
- Current priorities (ranked)
- Active objectives with status
- Revenue initiatives underway
- Pending decisions (things waiting on Tyler)
- Recent wins
- Known risks

## Maintenance Rules

1. **Every task update happens in tasks.json** — not in chat, not in memory, not verbally
2. **Every completed task has an output location** — where does the work live?
3. **Every blocked task explains the blocker** — what's preventing progress?
4. **Projects are updated when tasks complete** — progress bars should reflect reality
5. **Direction & State is updated when priorities shift**

## The Tyler Test

> If Tyler asks "what's happening?" — MC should answer it completely. If it doesn't, that's not a cue for a long explanation. It's a cue to improve MC.

## Enforcement

When you notice work happening outside MC:
1. Create the task in MC immediately
2. Log it properly with all required fields
3. Continue the work
4. Never let it slide — "I'll add it later" is a lie

## Audit Checklist

Run this periodically (during heartbeats):
- [ ] Every in-progress task has recent activity (last 48h)
- [ ] Every completed task has an output location
- [ ] Every blocked task explains why
- [ ] Every project has accurate task counts
- [ ] Direction & State reflects current reality
- [ ] No orphaned tasks (tasks without a project)
- [ ] No stale statuses (in-progress for >1 week with no activity)
