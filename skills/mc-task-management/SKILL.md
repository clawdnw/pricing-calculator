---
name: mc-task-management

triggers:
  - "create task"
  - "update task"
  - "move task"
  - "kanban"
  - "complete task"
  - "mark done"
related:
  - "[[definition-of-done]]"
  - "[[mission-control-doctrine]]"
  - "[[operating-loop]]"
description: >
  Create, update, and manage tasks in Mission Control's kanban board.
  Use when: creating new tasks, moving tasks between statuses, adding completion evidence,
  writing review instructions, or pulling work from the kanban during heartbeats.
  Don't use when: just reading/viewing tasks (use the API directly), or for project-level
  changes (edit data/projects.json directly).
  Outputs: Updated tasks.json with proper metadata.
---

# MC Task Management Skill

## Data Location
- Tasks: `mission-control-app/data/tasks.json`
- Projects: `mission-control-app/data/projects.json`
- API: `http://localhost:3333/api/tasks` (GET, POST, PATCH, DELETE)

## Task Schema (required fields)
```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "project": "string (slug matching project name)",
  "owner": "astra | tyler",
  "status": "not-started | in-progress | blocked | review | complete",
  "tags": ["string"],
  "notes": [],
  "outputLocation": "where the work product lives (path, URL, etc.)",
  "reviewers": ["who needs to review"],
  "completionCriteria": "what must be true for this to be done",
  "completionEvidence": "proof it's done (filled when moving to complete)",
  "reviewInstructions": "what/why/how to review (filled when moving to review)",
  "createdAt": "ISO timestamp",
  "updatedAt": "ISO timestamp",
  "createdBy": "astra | tyler",
  "activity": [{"timestamp": "", "action": "", "by": ""}]
}
```

## Project Slugs
- `mission-control` → Mission Control
- `portfolio-demos` → Portfolio & Demos
- `revenue-generation` → Revenue Generation
- `tyler-support` → Tyler Support

## Status Transitions

### → not-started
Default for new tasks. Must have: title, description, project, owner, tags.

### → in-progress
Agent is actively working this. Activity log must note what's being done.

### → blocked
Something prevents progress. Notes MUST explain: what's blocking, who can unblock, what's needed.

### → review
Work is done but needs review. MUST have ALL of:
- `outputLocation`: where the thing is
- `reviewInstructions`: what needs review, why, how to review it, criteria for moving to complete
- `reviewers`: who reviews it

### → complete
Work is done and verified. MUST have ALL of:
- `outputLocation`: where the finished work lives
- `completionCriteria`: what had to be true
- `completionEvidence`: proof those criteria are met, what was accomplished

## Heartbeat Work Loop
1. Read tasks.json
2. Find `in-progress` tasks where `owner` is you — work them
3. If none in-progress, find highest-priority `not-started` task, move to `in-progress`, work it
4. After working, update activity log and status
5. If done → add evidence → move to `review` or `complete`

## Definition of Done (Enforced)

A task is NOT complete because someone says it is. Complete means ALL of:
- Output exists in a durable location (file, URL, repo)
- Output is usable without additional explanation
- Output matches the original objective
- Review is completed if reviewers were assigned
- MC task has outputLocation, completionCriteria, and completionEvidence filled

If someone asks "What did this produce?" and the answer is unclear → task is NOT done.

## Value Gate (Before Creating Tasks)

Every task must answer:
1. What problem does this solve?
2. Who benefits?
3. One-time or compounding?
4. Expected upside?
5. Full cost (time, tokens)?

If unclear → refine or kill. Don't create vague tasks that waste future execution time.

## Anti-Patterns (NEVER)
- ❌ Creating tasks without a project
- ❌ Moving to complete without completionEvidence
- ❌ Moving to review without reviewInstructions
- ❌ Working on something not tracked in MC
- ❌ Leaving tasks in-progress with no activity for >24h
- ❌ "Fake completion" — marking done without durable output
- ❌ Tasks that don't pass the value gate

## Templates

### New Task (via API)
```bash
curl -X POST http://localhost:3333/api/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Task title",
    "description": "What needs to happen",
    "tags": ["tag1"],
    "project": "project-slug",
    "owner": "astra",
    "createdBy": "astra"
  }'
```

### Move Task (via API)
```bash
curl -X PATCH http://localhost:3333/api/tasks/TASK_ID \
  -H "Content-Type: application/json" \
  -d '{"status": "complete"}'
```

### Direct File Edit (for bulk updates)
Read `mission-control-app/data/tasks.json`, modify, write back.
