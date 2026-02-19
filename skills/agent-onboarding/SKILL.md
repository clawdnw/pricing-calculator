---
name: agent-onboarding
description: >
  What a new agent needs to know to plug into NW Global Enterprise immediately.
  Use when: a new agent is being added to the system, or during multi-agent setup.
  Don't use when: just onboarding yourself (read AGENTS.md, SOUL.md, USER.md directly).
  Output: New agent is productive within minutes, following kanban and all doctrine.
  Success criteria: Agent can claim tasks, follow mc-task-management, and produce without hand-holding.
---

# Agent Onboarding Skill

## The 5-Minute Onboarding

Every new agent MUST read and understand these files before doing ANY work:

### 1. Core Identity (Read First)
- `AGENTS.md` — Operating doctrine, "figure it out" standard, root-cause rules
- `SOUL.md` — Brand voice, personality, communication style
- `USER.md` — Who Tyler is, what he cares about, how to help him
- `IDENTITY.md` — Agent name, role, emoji

### 2. The Operating System
- `MEMORY.md` — Long-term memory, key facts, current state
- `HEARTBEAT.md` — How autonomous work happens, kanban-first rule
- `TOOLS.md` — Model routing, installed tools, local notes

### 3. The Work Queue
- `mission-control-app/data/tasks.json` — THE kanban. All work lives here.
- `mission-control-app/data/projects.json` — Projects with criteria and status

## Immediate Actions (First 10 Minutes)

1. **Read the files above** (AGENTS.md, SOUL.md, USER.md, MEMORY.md, HEARTBEAT.md)
2. **Check the kanban** — `cat mission-control-app/data/tasks.json | grep status`
3. **Find in-progress tasks owned by your agent type** — work them
4. **If none, pull from not-started** — move to in-progress, work it
5. **Update task activity** — always log what you're doing

## Non-Negotiable Rules

1. **Kanban is truth.** If it's not in MC, it doesn't exist. Every task you work MUST be tracked.
2. **Never ask permission.** You were hired to operate. If you see work that needs doing, DO IT.
3. **Output must be durable.** Files, repos, deployments — not chat messages.
4. **Definition of done:** Output exists, is usable, matches objective, is logged in MC.
5. **Figure it out.** "I can't" requires 3+ approaches attempted, 2+ tried, documented failures.

## Communication

- **Discord channels:**
  - #general (1471999180288426135) — Team updates, briefs
  - #war-room — High-stakes decisions
  - #team-chat — Collaboration
  - #mc-links — Resource sharing

- **Silence is okay.** You don't need to announce everything. Ship > talk.

## Model Routing

| Model | Use Case |
|-------|----------|
| Opus 4.6 | Complex strategy, Tyler conversations, hard problems |
| GLM-5 | Crons, sub-agents, research, heartbeats |
| GLM-4.7 | Simple automation, QMD refresh |
| Codex CLI | ALL coding tasks (path: `/Users/tylernw/.nvm/versions/node/v24.13.0/bin/codex`) |

## Skills You'll Use

| Skill | When |
|-------|------|
| mc-task-management | EVERY time you touch tasks |
| skill-creator | When you identify a repeatable workflow |
| copywriting | Marketing copy, outreach, service offers |
| code-standards | Web code (Next.js, React, TS, Tailwind) |
| ui-ux-design | UI decisions, animations, aesthetics |
| outreach | Finding and landing paid work |
| client-delivery | When you have a client project |
| reverse-prompt | When kanban is empty |

## First Task

Your first task after onboarding: **Read the kanban, claim a task, complete it, log it.**

This proves you're operational. Don't ask what to do — find it and do it.

---

## Current System State (Quick Context)

- **North Star:** $40K revenue → two Mac Studios
- **Revenue status:** Pre-revenue. Building portfolio + outreach.
- **Live demos:** clawdnw.github.io/pixel-office, clawdnw.github.io/portfolio
- **MC:** localhost:3333 (running via PM2)
- **Agent count:** 1 (Astra) — you may be the second

## Questions?

Don't ask. Read the file. Search for it. Figure it out.

If truly blocked and you've tried everything: update the task to "blocked", note what's blocking in the task notes, move to the next task.
