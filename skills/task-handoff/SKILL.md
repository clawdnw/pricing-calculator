---
name: task-handoff
description: >
  When one agent passes work to another agent — documents state, updates ownership, ensures zero context loss.
  Use when: handing off a task to another agent, picking up a task from another agent, or multi-agent coordination.
  Don't use when: you're continuing your own work (just update the task activity).
  Output: Task transferred with all context in MC, receiving agent can continue seamlessly.
  Success criteria: Receiving agent can pick up the task without asking clarifying questions.
  Anti-patterns: Handoff without context in task notes, verbal handoffs not logged, owner field not updated.
---

# Task Handoff Skill

## Why This Matters

Agents don't have shared memory. If context lives in one agent's session but not in MC, it's lost when that agent goes away. Every handoff must transfer ALL context into the task itself.

## The Handoff Protocol

### When Handing Off (Sending Agent)

1. **Update task status** to `blocked` or `not-started` (depending on situation)
2. **Add comprehensive note** in task.notes array with:
   - What you've done so far (specific, not vague)
   - What's left to do
   - Any blockers or decisions needed
   - Where the work lives (file paths, URLs)
   - Any gotchas or lessons learned
3. **Update owner field** to the receiving agent
4. **Add activity log entry** noting the handoff

### Handoff Note Template
```json
{
  "id": "[uuid]",
  "by": "[sending-agent]",
  "timestamp": "[ISO timestamp]",
  "body": "HANDOFF to [receiving-agent]\n\n**Completed:**\n- [specific thing 1]\n- [specific thing 2]\n\n**Remaining:**\n- [specific next step 1]\n- [specific next step 2]\n\n**Work location:** [file path or URL]\n\n**Blockers/decisions:** [any blockers or decisions needed]\n\n**Gotchas:** [anything that might trip up the next agent]\n\n**Context:** [any other context needed to continue]"
}
```

### When Picking Up (Receiving Agent)

1. **Read the entire task** — description, notes, activity, outputLocation
2. **Check for blockers** — if blocked, don't start until unblocked
3. **Verify work location exists** — files, URLs, repos
4. **Ask clarifying questions IN TASK NOTES** if anything is unclear (not in chat)
5. **Update status to in-progress** and begin work
6. **Log your start** in activity

## Example Handoff

### Sending Agent (Astra) → Receiving Agent (Shuri)

**Task:** t-105 - MC: Upgrade to portfolio-worthy quality

**Note added by Astra:**
```
HANDOFF to Shuri

**Completed:**
- Added Direction & State section to dashboard
- Built projects tab with progress bars
- Populated calendar with cron events
- All pages return 200

**Remaining:**
- Add micro-interactions (button hover states, card transitions)
- Improve loading states with skeleton screens
- Add subtle background gradients for depth

**Work location:** /Users/tylernw/.openclaw/workspace/mission-control-app/app/page.tsx

**Context:**
- Using Framer Motion for animations
- Dark theme colors defined in globals.css
- PM2 keeping server alive, don't need to restart manually
```

**Shuri picks up:**
- Reads note, understands exactly what's done and what's needed
- Checks the code at the specified path
- Starts work on micro-interactions
- Logs progress in task activity

## Context Preservation Rules

### ALWAYS Include in Handoff
- What's done (be specific — files, commits, deployments)
- What's left (next actionable steps)
- Where work lives (paths, URLs, branches)
- Any decisions already made
- Any gotchas discovered

### NEVER Assume
- That the receiving agent read the chat history
- That the receiving agent knows where files are
- That context is obvious
- That something is "simple" or "easy"

## Multi-Agent Workflow

### Parallel Work (Multiple Agents, Different Tasks)
- Each agent owns their task completely
- Update tasks.json independently
- No handoff needed — just status updates

### Sequential Work (Agent A → Agent B → Agent C)
- Agent A completes their part
- Agent A hands off with full context
- Agent B picks up, works, hands off to C
- Agent C completes

### Collaborative Work (Multiple Agents, Same Task)
- One agent is owner (makes final decisions)
- Others contribute via notes
- All activity logged in one task

## Emergency Handoff

If an agent session dies or is interrupted:

1. **Check task activity** for last logged action
2. **Check task notes** for any context
3. **Check memory/YYYY-MM-DD.md** for daily log
4. **Resume from last known state**
5. **Add note** explaining the interruption and resumption

## Quality Checklist

Before considering a handoff complete:
- [ ] Owner field updated to receiving agent
- [ ] Handoff note added with all required sections
- [ ] Activity log shows handoff action
- [ ] Work location specified and verified
- [ ] Receiving agent can continue without clarifying questions

---

*The goal: Zero context loss between agents. If it's not in the task, it doesn't exist.*
