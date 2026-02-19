---
name: nightly-work

triggers:
  - "nightly cron"
  - "autonomous work"
  - "11 PM"
related:
  - "[[mc-task-management]]"
  - "[[reverse-prompt]]"
  - "[[operating-loop]]"
description: >
  Autonomous nightly work session — build, research, or maintain systems while Tyler sleeps.
  Use when: nightly cron fires (11 PM MST), or during any autonomous work session.
  Don't use when: Tyler is actively chatting (just respond to him). Don't use when: morning brief time (use morning-brief).
  Output: Tangible progress on MC kanban tasks, logged to memory/YYYY-MM-DD.md.
  Success criteria: At least 1 task progressed or completed. Evidence logged. No messages to Tyler.
---

# Nightly Work Skill

## Decision Tree

```
1. Read mission-control-app/data/tasks.json
2. Is there an in-progress task owned by astra?
   → YES: Work it. Update activity. Move forward.
   → NO: Is there a not-started task?
     → YES: Move highest-priority to in-progress. Work it.
     → NO: Use reverse-prompt skill to generate work.
3. After working, update task status + activity in tasks.json
4. Log what you did to memory/YYYY-MM-DD.md
5. DO NOT message Tyler — he's sleeping.
```

## Work Priorities (when choosing from not-started)
1. Revenue-critical tasks (project: revenue-generation)
2. Portfolio/demo tasks (project: portfolio-demos)
3. MC improvements (project: mission-control)
4. Tyler support (project: tyler-support)
5. Infrastructure/skills (maintenance)

## What "Work" Means
- **Building:** Write code, create files, deploy things
- **Researching:** Web search with written findings in memory/
- **Improving:** Upgrade skills, fix bugs, clean data
- **Preparing:** Draft outreach posts, service offers, proposals

## What "Work" Does NOT Mean
- ❌ Checking email repeatedly
- ❌ Running operational checks for 30 minutes
- ❌ "Planning" without producing artifacts
- ❌ Updating status without doing anything

## Output Template (memory log)
```markdown
## Nightly Work Session — [Date]

### Task Worked: [task title] (t-XXX)
- **Status change:** [from] → [to]
- **What I did:** [concrete description]
- **Where it lives:** [file path, URL, etc.]
- **Time spent:** ~[X] minutes
- **Next steps:** [what remains]
```

## Sub-Agent Strategy
For complex build tasks (code, multi-file changes, research):
- Use `sessions_spawn` to delegate the actual building
- You orchestrate: pick task, spawn sub-agent with clear instructions, monitor output
- This lets you work multiple tasks if the first sub-agent finishes quickly
- Sub-agents use `zai/glm-5` by default — capable enough for most building

## Build Something Cool
Tyler wants to wake up to something he can test. Prioritize tasks that produce VISIBLE, TESTABLE output:
- A new page or feature he can click on
- A polished UI improvement he can see
- A deployed demo he can share
- A tool or resource he can use

Invisible infrastructure work is fine sometimes, but the DEFAULT should be: "Tyler can see and touch what I built."

## Rules
- Focus on ONE primary task (but can spawn parallel sub-agents)
- Must update tasks.json with progress
- Must update data/agent-status.json with current work
- Must log to daily memory file
- Must stay within 5-minute timeout
- If task requires Tyler input → mark blocked, move to next
- No Discord messages between 23:00-07:00 MST
