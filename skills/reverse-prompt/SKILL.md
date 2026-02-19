---
name: reverse-prompt

triggers:
  - "idle"
  - "no tasks"
  - "kanban empty"
  - "nothing to do"
related:
  - "[[autonomy-charter]]"
  - "[[mc-task-management]]"
  - "[[nightly-work]]"
description: >
  Procedural skill for finding productive work when the kanban has no in-progress or not-started tasks.
  Use when: kanban is empty, heartbeat has nothing to work, or idle between tasks.
  Don't use when: kanban has work (just do the work). Don't use when: Tyler gave explicit instructions (just follow them).
  Output: 2-5 new MC tasks created in tasks.json, highest-priority one moved to in-progress.
  Success criteria: Never idle. Always producing or preparing work.
  Anti-patterns: Creating vague tasks ("improve things"), creating tasks you'll never do, creating 20 tasks instead of doing 1.
---

# Reverse Prompt Skill

## The Question
"What can I do RIGHT NOW that moves us closer to $40K revenue or makes Tyler's life measurably better?"

## Decision Tree

```
1. Check revenue pipeline
   → Do we have active client inquiries? → Follow up (client-delivery skill)
   → Do we have outreach posts live? → Check responses
   → Neither? → Create outreach task

2. Check portfolio gaps
   → Is every demo live and working? → If not, fix it
   → Do we have <3 portfolio pieces? → Build another demo
   → Can existing demos be improved? → Upgrade quality

3. Check Tyler's needs (USER.md)
   → School: study tools, schedule, reminders
   → Life: date planning, travel, logistics
   → Work: anything blocking his productivity

4. Check MC health
   → Projects missing tasks? → Break them down
   → Stale tasks (no activity >48h)? → Either work them or archive
   → Skills that could be built? → Build one

5. Check for compounding infrastructure
   → Repeated workflow without a skill? → Build the skill
   → Manual process that could be automated? → Automate it
   → Documentation gaps? → Fill them
```

## Value Gate (Every Task Must Pass)

Before creating any task, answer:
1. What problem does this solve?
2. Who benefits (efficiency/revenue/leverage/learning)?
3. Is it one-time or compounding? (Prefer compounding)
4. Expected upside (time saved, money earned, capability gained)?
5. Full cost (time, complexity, tokens)?

If unclear → refine or kill. Don't create busywork.

**Kill filter:** If it requires a large team → delete. If it can't generate value within 90 days → park it.

## Task Creation Rules

When creating new tasks, EVERY task must have:
- Clear, specific title (not "improve stuff")
- Description of what "done" looks like
- Project assignment
- Owner
- Tags
- Completion criteria

**Good task:** "Build portfolio index page linking all demos — single HTML page at clawdnw.github.io with cards for each demo, deployed via GitHub Pages"

**Bad task:** "Work on portfolio"

## Output
After running this skill:
1. 2-5 new tasks created in tasks.json
2. Highest-priority task moved to in-progress
3. Start working that task immediately
4. Log reasoning to memory/YYYY-MM-DD.md

## Priority Framework
1. 🔴 Revenue-generating (client work, outreach, portfolio for selling)
2. 🟠 Revenue-enabling (demos, skills, tools that make delivery faster)
3. 🟡 Tyler-supporting (school, life, productivity)
4. 🟢 Infrastructure (MC, skills, automation, maintenance)
5. 🔵 Nice-to-have (everything else)

Only create tasks at levels 4-5 if levels 1-3 are fully stocked.
