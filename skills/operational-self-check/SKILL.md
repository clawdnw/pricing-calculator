---
name: operational-self-check
description: >
  Periodic verification that all autonomous systems are working.
  Use when: every heartbeat (quick check), after cron changes, or when Tyler asks "is everything working?"
  Don't use when: Tyler asks about a specific system (just check that one thing), or during
  focused build work (self-check should take <60 seconds, not interrupt building).
  Output: Fix issues silently. Only alert Tyler if something is broken AND can't be auto-fixed.
---

# Operational Self-Check Skill

## Purpose

Prevent the pattern where systems are set up but never verified. This skill runs periodic checks to catch failures early, before Tyler notices.

## When to Run

- Every heartbeat (automatic via HEARTBEAT.md)
- After any cron job creation or modification
- When Tyler asks "is everything working?"

## Checks

### 1. Cron Job Health

**Command:** Use `cron list` to get all jobs, then `cron runs` for each job.

**Pass criteria:**
- Every enabled job has at least one successful run in its history
- No job has `consecutiveErrors > 2`
- Jobs with schedules in the past (e.g., 8 AM already happened today) have a recent run

**If fail:**
- Check the job's error message
- If timeout: increase `timeoutSeconds`
- If model error: verify model routing
- Re-run with `cron run --force` to test
- Log the issue to `memory/YYYY-MM-DD.md`

### 2. Kanban Freshness

**Check:** Read `mission-control-app/data/tasks.json`

**Pass criteria:**
- At least one task has `updatedAt` within last 24 hours
- At least one task is `in-progress` (shows active work)
- Tasks are REAL work, not seed data (check if createdBy has variety)

**If fail:**
- You're not using the kanban to drive work. Add real tasks.
- Update task status as you complete work.

### 3. Heartbeat State

**Check:** Read `memory/heartbeat-state.json`

**Pass criteria:**
- File exists and is valid JSON
- At least one check has timestamp within last 8 hours

**If fail:**
- Create the file if missing
- Run at least one check now

### 4. Proactive Work Log

**Check:** Read recent `memory/YYYY-MM-DD.md` files

**Pass criteria:**
- Today's file exists
- Contains evidence of proactive work (not just reactive responses)
- Has entries for work done without Tyler asking

**If fail:**
- You're not being proactive. Do work now.

### 5. Agent Status Accuracy

**Check:** Read `mission-control-app/data/agent-status.json`

**Pass criteria:**
- `currentTask` matches what you're actually working on
- `lastUpdate` is within last 4 hours
- `todayStats` are non-zero (unless it's early morning)

**If fail:**
- Update the file to reflect reality immediately.

## Failure Response Protocol

When ANY check fails:

1. **Fix immediately** if possible (e.g., update stale data)
2. **Log to memory** what failed and why
3. **Build a prevention mechanism** if it's a recurring issue
4. **Alert Tyler** if it's blocking revenue work or can't be fixed autonomously

## Implementation

Add to HEARTBEAT.md:

```markdown
## Self-Check (every heartbeat)

Before other checks, run the operational-self-check skill:
1. Verify all cron jobs have recent successful runs
2. Verify kanban has been updated in last 24h
3. Verify heartbeat-state.json exists and is current
4. Verify today's memory file has proactive work logged
5. Verify agent-status.json reflects reality
```

## History

- **2026-02-17:** Created after Tyler feedback that systems were set up but never verified.
