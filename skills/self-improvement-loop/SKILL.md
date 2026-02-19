---
name: self-improvement-loop

triggers:
  - "article dropped"
  - "failure"
  - "new discovery"
  - "lesson learned"
related:
  - "[[living-principles]]"
  - "[[skill-creator]]"
  - "[[root-cause-standard]]"
description: >
  How we level up — converting articles, failures, and discoveries into permanent capability upgrades.
  Use when: Tyler drops an article/link, an agent fails at something, or a new tool/technique is discovered.
  Use when: reviewing what went wrong and encoding prevention.
  Don't use when: doing routine task execution (just do the work).
  Don't use when: the improvement is trivial (fix it inline, no need for a loop).
  Output: Knowledge converted into durable improvements (skills, docs, tools, MC tasks).
  Anti-patterns: "Interesting notes" without application, reading articles without extracting actions, failing without encoding lessons.
---

# Self-Improvement Loop

## The Principle

> Useful knowledge is not collected as "interesting notes." It is converted into improvements and encoded into durable docs and workflows.

## The Loop (When Article/Link is Dropped)

### Step 1: Summarize
One agent produces a strict, concise summary:
- Key points (bullet list, not paragraphs)
- What's new/different from what we already do
- Relevance to our goals

### Step 2: Extract Actions
Another agent (or the same one) extracts:
- Actionable steps and tools
- What we can implement NOW
- What requires more research
- What doesn't apply to us

### Step 3: Create MC Tasks
For each actionable improvement:
- Create task in Mission Control
- Assign owner
- Define explicit outcome
- Set priority based on impact

### Step 4: Implement
Execute the tasks. Ship the improvements.

### Step 5: Encode Results
Update durable documentation:
- `AGENTS.md` — behavioral rules
- `SOUL.md` — communication/personality
- `skills/` — new or updated skills
- `TOOLS.md` — tool configurations
- `MEMORY.md` — lessons learned
- `PRINCIPLES.md` — decision heuristics
- `REGRESSIONS.md` — failure patterns

## The Loop (When Something Fails)

### Step 1: Acknowledge
Don't hide it. Don't minimize it. State what failed and the impact.

### Step 2: Root Cause
Follow the root-cause-standard skill. Find the mechanism, not the symptom.

### Step 3: Fix
Address the root cause. Verify the fix works.

### Step 4: Encode Prevention
- If it's a behavioral failure → update AGENTS.md or relevant skill
- If it's a technical failure → update TOOLS.md or build a skill
- If it's a process failure → update the process (HEARTBEAT.md, cron config, etc.)
- Log in REGRESSIONS.md

### Step 5: Verify Loop Closure
Ask: "If this exact situation happens again, will the system handle it correctly without human intervention?"

If no → the encoding is incomplete. Iterate.

## High-Priority Tool Upgrades

Actively pursue these when opportunities arise:
- **QMD** — reduce token cost searching internal markdown
- **Persistent memory** — reduce repeated context loading
- **Model routing** — reduce compute cost while maintaining quality
- **Browser automation** — Playwright/Chromium for dynamic sites

## Meta Principle

> We optimize for learning rate, not merely task completion. Task completion is finite. Learning compounds. Friction becomes signal. Mistakes become data.

## Anti-Patterns

- ❌ Reading an article and saying "interesting" without creating tasks
- ❌ Failing at something and just retrying the same approach
- ❌ Building a fix without encoding the lesson
- ❌ "Mental notes" about improvements (write it down or it doesn't exist)
- ❌ Improvements that live only in one agent's session (must be in durable files)
