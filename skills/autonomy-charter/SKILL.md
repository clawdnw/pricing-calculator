---
name: autonomy-charter

triggers:
  - "new idea"
  - "proposing work"
  - "should I"
  - "value gate"
related:
  - "[[reverse-prompt]]"
  - "[[kill-authority]]"
  - "[[mc-task-management]]"
description: >
  Value creation funnel — the gate every idea/task must pass before consuming resources.
  Use when: proposing new work, evaluating ideas, during reverse-prompt, or when an agent wants to start something new.
  Use when: reviewing whether existing work should continue or be killed.
  Don't use when: Tyler explicitly assigned the task (he already passed the gate).
  Don't use when: doing routine maintenance (operational checks, heartbeats).
  Output: Idea either passes the value gate (becomes MC task) or gets killed.
  Anti-patterns: Starting work without passing the gate, "interesting" ideas that never become tasks, motion without value.
---

# Autonomy Charter & Value Creation Funnel

## The Default

> If nobody is telling you what to do, you are expected to create value. Waiting is failure. Initiative is success.

## The Value Gate (Enforced Before Work Starts)

Every proposed idea, task, or project must answer these 5 questions:

### 1. What problem does this solve?
Be specific. "Make things better" is not a problem statement.

### 2. Who benefits?
- **Efficiency** — saves time on recurring work
- **Revenue** — generates or enables income
- **Leverage** — compounds over time (skills, systems, infrastructure)
- **Learning** — builds capability for future revenue

### 3. Is it one-time or compounding?
- One-time: do it if fast and high-value
- Compounding: prioritize these — they pay dividends forever

### 4. What's the expected upside?
- Time saved (hours/week)
- Money earned (dollars)
- Capability gained (what can we do now that we couldn't before?)

### 5. What's the full cost?
- Time to build
- Complexity to maintain
- Tokens to execute
- Opportunity cost (what are we NOT doing while doing this?)

## Decision Matrix

| Answers clear? | Upside > Cost? | Action |
|---------------|----------------|--------|
| Yes | Yes | → MC task with owner and outcome |
| Yes | No | → Kill it |
| No | ? | → Refine answers or kill |
| ? | ? | → Don't start. Clarify first. |

## After Passing the Gate

The idea MUST NOT live only in chat. It becomes:
1. **MC task** with:
   - Owner
   - Explicit outcome
   - Review requirement (if needed)
   - Project association
2. **Immediately workable** — if it needs 3 more discussions before anyone can start, it's not ready

## Examples

### ✅ Passes Gate
> "Build a portfolio index page. **Problem:** No way for potential clients to see all our demos in one place. **Benefits:** Revenue (enables sales). **Compounding:** Yes — every new demo gets added automatically. **Upside:** Could convert 1 client/month at $300 = $3,600/year. **Cost:** 2 hours to build, near-zero maintenance."

### ❌ Fails Gate
> "Set up a Kubernetes cluster for MC. **Problem:** MC runs on PM2. **Benefits:** Efficiency (maybe). **Compounding:** No — it's infrastructure for infrastructure. **Upside:** Unclear. **Cost:** 8+ hours setup, ongoing maintenance, complexity. PM2 already works fine."

### ❌ Fails Gate
> "Research blockchain integration." **Problem:** None stated. **Benefits:** Learning? **Upside:** None within 90 days. **Cost:** Token burn + opportunity cost. **KILLED.**

## Kill Criteria

Kill any idea that:
- Requires a large team to work
- Can't generate cash within 90 days (park as "later" idea)
- Is "interesting" but not useful
- Has unclear upside after 2 minutes of thought
- Burns tokens without leverage
