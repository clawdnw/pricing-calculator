# Skill Graph — NW Global Enterprise

_Interconnected skill map. Skills reference each other via [[wikilinks]]._
_This file is the table of contents — full skill content loads on demand._

---

## Skill Categories

### 🧠 Core Doctrine (Always Active)
These shape all behavior. Referenced by every other skill.

| Skill | Triggers | Related |
|-------|----------|---------|
| [[operator-doctrine]] | agent stuck, "can't", failure | [[root-cause-standard]], [[definition-of-done]] |
| [[autonomy-charter]] | idle, no tasks, new idea | [[reverse-prompt]], [[kill-authority]] |
| [[identity-communication]] | writing output, communication | [[copywriting]], [[channel-doctrine]] |
| [[token-governance]] | model selection, cost concern | [[operating-loop]], [[operational-self-check]] |
| [[definition-of-done]] | completing task, marking done | [[mc-task-management]], [[root-cause-standard]] |
| [[root-cause-standard]] | fixing bugs, debugging | [[operator-doctrine]], [[living-principles]] |
| [[kill-authority]] | low-value work, scope creep | [[autonomy-charter]], [[executive-authority]] |
| [[executive-authority]] | unilateral decisions, escalation | [[kill-authority]], [[channel-doctrine]] |

### 📋 Task Management (Work Execution)
How tasks flow from creation to completion.

| Skill | Triggers | Related |
|-------|----------|---------|
| [[mc-task-management]] | create/update/move tasks | [[definition-of-done]], [[mission-control-doctrine]] |
| [[mission-control-doctrine]] | MC setup, audit, "what's happening" | [[mc-task-management]], [[operating-loop]] |
| [[operating-loop]] | heartbeat, drift detection | [[operational-self-check]], [[reverse-prompt]] |
| [[operational-self-check]] | heartbeat, system check | [[operating-loop]], [[morning-brief]] |
| [[reverse-prompt]] | idle, no tasks, kanban empty | [[autonomy-charter]], [[mc-task-management]] |
| [[task-handoff]] | multi-agent coordination | [[mc-task-management]], [[agent-onboarding]] |

### 💰 Revenue (Money-Making)
Everything related to generating income.

| Skill | Triggers | Related |
|-------|----------|---------|
| [[revenue-doctrine]] | revenue opportunity, pricing | [[outreach]], [[client-delivery-pipeline]] |
| [[revenue-research]] | market research, competitor analysis | [[revenue-doctrine]], [[last30days]] |
| [[outreach]] | find work, post offers | [[copywriting]], [[revenue-doctrine]] |
| [[client-delivery-pipeline]] | client landed, execute delivery | [[code-standards]], [[ui-ux-design]] |
| [[client-delivery]] | delivering to client | [[client-delivery-pipeline]], [[definition-of-done]] |

### 🛠️ Building (Creating Things)
Skills for producing deliverables.

| Skill | Triggers | Related |
|-------|----------|---------|
| [[code-standards]] | writing code, reviewing code | [[ui-ux-design]], [[client-delivery]] |
| [[ui-ux-design]] | building UI, design decisions | [[code-standards]], [[landing-page-generator]] |
| [[landing-page-generator]] | create landing page | [[copywriting]], [[ui-ux-design]] |
| [[copywriting]] | marketing copy, headlines, CTAs | [[landing-page-generator]], [[outreach]] |
| [[skill-creator]] | new skill needed, upgrade skill | [[living-principles]], [[self-improvement-loop]] |

### 📡 Content & Intelligence
Producing and gathering information.

| Skill | Triggers | Related |
|-------|----------|---------|
| [[x-post-automation]] | post to X, X automation | [[x-intelligence]], [[copywriting]] |
| [[x-intelligence]] | X sweep, trends, monitoring | [[x-post-automation]], [[last30days]] |
| [[last30days]] | research topic, trending | [[revenue-research]], [[x-intelligence]] |
| [[morning-brief]] | morning cron, daily brief | [[operational-self-check]], [[operating-loop]] |

### 🔄 Learning & Improvement
How the system gets better over time.

| Skill | Triggers | Related |
|-------|----------|---------|
| [[self-improvement-loop]] | article dropped, failure, discovery | [[living-principles]], [[skill-creator]] |
| [[living-principles]] | repeated failure, new heuristic | [[self-improvement-loop]], [[root-cause-standard]] |
| [[agent-onboarding]] | new agent, multi-agent setup | [[task-handoff]], [[channel-doctrine]] |

### 🔧 Operations
Scheduling, routing, and system management.

| Skill | Triggers | Related |
|-------|----------|---------|
| [[nightly-work]] | 11 PM cron, autonomous work | [[mc-task-management]], [[reverse-prompt]] |
| [[channel-doctrine]] | wrong channel, moderation | [[identity-communication]], [[executive-authority]] |

---

## Skill Flow Patterns

### New Task Creation
```
[[reverse-prompt]] → [[autonomy-charter]] (value gate) → [[mc-task-management]] (create task)
```

### Task Execution
```
[[mc-task-management]] (pull task) → [[code-standards]] or [[copywriting]] (do work) → [[definition-of-done]] (verify) → [[mc-task-management]] (complete)
```

### Revenue Pipeline
```
[[revenue-research]] → [[revenue-doctrine]] (validate) → [[outreach]] (find client) → [[client-delivery-pipeline]] (deliver) → [[mc-task-management]] (track)
```

### Content Pipeline
```
[[x-intelligence]] (gather) → [[last30days]] (research) → [[copywriting]] (write) → [[x-post-automation]] (post)
```

### Failure Recovery
```
error detected → [[root-cause-standard]] (diagnose) → [[living-principles]] (encode lesson) → [[self-improvement-loop]] (upgrade)
```

### Heartbeat Loop
```
[[operating-loop]] → [[operational-self-check]] → [[mc-task-management]] (pull work) → execute → [[definition-of-done]] (verify)
```

---

## Three-Space Architecture

### Self-Space (Identity)
- `SOUL.md` — personality, values, communication style
- `IDENTITY.md` — who am I (name, role, emoji)
- `USER.md` — who Tyler is
- `VISION.md` — where we're going

### Notes-Space (Memory)
- `MEMORY.md` — long-term curated memory
- `memory/YYYY-MM-DD.md` — daily raw logs
- `memory/tyler-resources/` — proactive resources for Tyler
- `PRINCIPLES.md` — decision heuristics
- `REGRESSIONS.md` — failure log

### Ops-Space (Execution)
- `skills/` — all operational skills (this graph)
- `mission-control-app/` — the dashboard
- `HEARTBEAT.md` — heartbeat checklist
- `TOOLS.md` — environment-specific notes
- `AGENTS.md` — operating doctrine

---

_This graph is a living document. When skills are added or relationships change, update this file._
_Last updated: 2026-02-19_
