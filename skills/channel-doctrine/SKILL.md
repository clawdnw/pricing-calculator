---
name: channel-doctrine
description: >
  Communication architecture — which channel is for what, moderation rules, and convergence requirements.
  Use when: moderating multi-agent discussions, deciding where to post something, or enforcing channel boundaries.
  Use when: a discussion is happening in the wrong channel.
  Use when: a discussion ends without a decision.
  Don't use when: just sending a routine message (just send it).
  Don't use when: working solo (channels matter for multi-agent coordination).
  Output: Discussion ends in decision, task assignments, or war-room escalation.
  Anti-patterns: Debate in intel-feed, discussions without outcomes, war-room ending with "good points" instead of committed plans.
---

# Channel Doctrine

## Channel Purposes (Enforce Strictly)

### #intel-feed — Intake Only
- **What goes here:** Links, posts, videos, raw information
- **What does NOT go here:** Debate, execution, conclusions
- **Job:** Extract and synthesize into usable artifacts (structured notes, takeaways, use cases, implementation candidates)
- **Only synthesized output moves to team-chat**

### #general — Announcements and Briefs
- Morning briefs, status updates, milestone announcements
- Not for discussion — use team-chat for that

### #team-chat — Moderated Convergence
- Where the company converges under moderation
- **Every discussion opens with:** purpose, scope, required outcome
- Agents respond concisely and on-topic
- Moderator stops drift and repetition
- **Discussion converts into:** decisions and tasks

### #war-room — Structured Conflict Until Alignment
- High-stakes decisions, serious disagreements, strategic pivots, critical fixes
- Positions are steel-manned
- Weak arguments discarded, strong arguments survive
- **War-room does NOT end with "good points"**
- **War-room ends with:** committed plan + immediate tasks in MC

## The Convergence Rule

> Every multi-agent discussion MUST end in one of three outcomes:
> 1. A decision
> 2. Task assignments
> 3. War-room escalation
>
> A discussion that ends without convergence **failed**.

## Moderation Protocol

### Opening a Discussion
```
**Purpose:** [Why we're discussing this]
**Scope:** [What's in/out of scope]
**Required outcome:** [Decision / Task list / Recommendation]
**Time limit:** [How long this should take]
```

### During Discussion
- Call on agents in sequence (not free-for-all)
- Enforce concise, on-topic responses
- Stop drift: "That's out of scope for this discussion"
- Stop repetition: "Already covered — moving on"
- Stop parallel monologues: "One topic at a time"

### Closing a Discussion
```
**Decision:** [What was decided]
**Tasks created:** [List of MC tasks with owners]
**Next check-in:** [When we revisit]
```

## War-Room Protocol

1. State the stakes clearly
2. Each position gets a fair hearing (steel-man, not straw-man)
3. Challenge assumptions with evidence
4. Discard weak arguments explicitly
5. Converge on strongest path
6. Commit to plan with immediate tasks
7. Log everything in MC

## Anti-Patterns

- ❌ Debate in #intel-feed (it's intake only)
- ❌ Discussions that end with "interesting" but no actions
- ❌ War-room that ends with "good points from everyone" (that's not alignment)
- ❌ Using #general for back-and-forth discussion
- ❌ Unmoderated free-for-all conversations
