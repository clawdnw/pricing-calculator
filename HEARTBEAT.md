# HEARTBEAT.md — Periodic Checks

Check `memory/heartbeat-state.json` for last-run times. Rotate through these — don't do all every beat. Prioritize what's stale (>4h since last check).

## Checks (rotate 2-3 per beat)

1. **Email** — `gog gmail search 'newer_than:4h is:unread' --max 5` — alert Tyler if anything important
2. **Calendar** — `gog calendar events primary --from <now> --to <+48h>` — upcoming events within 2h get flagged
3. **GitHub** — `gh notification list --all -L 5` — PRs, issues, CI failures on NW-Global-Enterprise
4. **Mission Control** — scan MC repo for stale tasks, update status if needed
5. **QMD Index** — `qmd update` if >4h since last refresh

## Proactive Work (do 1 per heartbeat if time allows)

- Reverse prompt yourself: "What task can I do right now that moves us closer to $40K?"
- Check memory/ for ideas Tyler texted — organize into ideas/research/drafts folders
- If something failed recently, start building a fix
- Draft or improve content (service offers, posts, docs)
- Update MEMORY.md if daily files have unencoded learnings

## Rules

- Late night (23:00-07:00 MST): HEARTBEAT_OK unless truly urgent
- If nothing actionable: HEARTBEAT_OK
- If alerting: send to current session (webchat) or Discord if webchat inactive
- Log check timestamps to `memory/heartbeat-state.json`
- Be an employee, not a monitor. Do work, don't just check things.
