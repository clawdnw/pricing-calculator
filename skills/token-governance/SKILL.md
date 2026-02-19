---
name: token-governance
description: >
  Token and model governance — tokens are compute capital, waste is process failure.
  Use when: choosing which model to use, reviewing token usage, or noticing high-cost behavior.
  Use when: an agent is burning tokens on narration, restating context, or drip-feeding updates.
  Don't use when: Tyler explicitly requested a high-cost model for a task.
  Don't use when: the task genuinely requires Opus-level reasoning.
  Output: Correct model selected, token-efficient behavior enforced.
  Anti-patterns: Using Opus for simple tasks, narrating internal reasoning, repeating MC context in chat, drip-feeding updates.
---

# Token Governance

## The Principle

> Tokens are compute capital. Waste is not a personality quirk; it is a process failure.

## Model Routing

| Model | Use For | Never Use For |
|-------|---------|---------------|
| Opus 4.6 | Tyler conversations, complex strategy, hard problems | Simple automation, research, drafts |
| GLM-5 | Crons, sub-agents, research, heartbeats, most autonomous work | Trivial checks |
| GLM-4.7 | Simple automation, QMD refresh, basic checks | Complex reasoning |
| Codex CLI | ALL coding tasks | — |

**Rule:** Use the cheapest model that can do the job. Escalate only when necessary.

## Low-Token Behavior (Default)

### DO
- Write concise, structured output
- Reference MC/docs instead of restating context
- Batch outputs (one comprehensive update vs 5 small ones)
- Prefer async updates over chat noise
- Use bullet points over paragraphs when listing

### DON'T
- Narrate internal reasoning ("Let me think about this...")
- Repeat context that exists in MC ("As we discussed previously...")
- Drip-feed updates (3 separate messages when 1 would do)
- "Think out loud" in chat
- Restate the task description back to Tyler

## High-Token Behavior (Reserved For)

Only use high-cost models and verbose output when:
- Strategic synthesis (connecting multiple data points into strategy)
- War-room debates (steel-manning positions, deep analysis)
- Final directives (comprehensive plans with full context)
- Tyler explicitly requests depth

## Token Budget Discipline

If token limits are hit early in a period:
1. **Treat it as a process failure** — not bad luck
2. **Immediately correct:**
   - Stricter structure
   - Shorter outputs
   - Better referencing (link to MC instead of restating)
   - More async execution (sub-agents on cheaper models)
   - Fewer heartbeat checks

## Enforcement

Signs of token waste:
- Agent opens with "Great question!" or filler
- Agent restates the task back before starting
- Agent narrates each step ("First, I'll check X, then Y, then Z")
- Multiple messages where one would suffice
- Using Opus for a task GLM-5 could handle

**Response:** Call it out, correct the behavior, log in REGRESSIONS.md if repeated.
