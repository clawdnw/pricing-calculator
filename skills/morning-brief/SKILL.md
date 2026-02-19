---
name: morning-brief

triggers:
  - "morning cron"
  - "daily brief"
  - "morning summary"
related:
  - "[[operational-self-check]]"
  - "[[operating-loop]]"
  - "[[revenue-research]]"
description: >
  Generate Tyler's daily morning brief with weather, email, calendar, kanban status, and proactive tasks.
  Use when: morning cron fires, or Tyler asks for a brief/status update.
  Don't use when: Tyler asks a specific question (just answer it), or for afternoon/nightly work sessions.
  Output: Formatted brief sent to Discord #general, plus memory log.
---

# Morning Brief Skill

## Steps
1. Weather: `curl -s "wttr.in/Goodyear+Arizona?format=3"`
2. Email: `gog gmail search 'newer_than:12h is:unread' --max 5`
3. Calendar: `gog calendar events primary --from <today> --to <tomorrow>`
4. Kanban status: Read `mission-control-app/data/tasks.json` — count by status, list in-progress items
5. Day check: Weekday = Tyler has class. Weekend/holiday = free.
6. Overnight work: Read `memory/YYYY-MM-DD.md` for what was done
7. Proactive tasks: 3-5 things to do today that move toward $40K revenue goal

## Output Template
```
☀️ **Morning Brief — [Day, Date]**

**Weather:** [conditions]

**📧 Email:** [count] unread — [flag anything important or "nothing urgent"]

**📅 Today:** [events or "no events scheduled"]
[If weekday: "Class day — Tyler in apprenticeship"]

**📋 Kanban:**
- In Progress: [count] ([list titles])
- Not Started: [count]
- Blocked: [count] ⚠️ [if any, flag them]
- Complete (recent): [count done in last 24h]

**🌙 Overnight:** [what I worked on]

**⚡ Today's Focus:**
1. [task — why it matters]
2. [task — why it matters]
3. [task — why it matters]

**💡 Opportunity:** [one business idea or lead spotted]
```

## Delivery
- Send to Discord #general: channel ID `1471999180288426135`
- Log to `memory/YYYY-MM-DD.md`
- Update `memory/heartbeat-state.json` timestamps

## Success Criteria
- Brief sent before 8:15 AM MST
- All 7 data sources checked
- No hallucinated events or emails
- Proactive tasks are actionable, not vague
