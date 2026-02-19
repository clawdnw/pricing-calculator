---
name: skill-creator
description: >
  Create or update AgentSkills following the OpenAI Skills standard and our internal quality bar.
  Use when: designing, structuring, or packaging a new skill. Use when: upgrading an existing skill's quality.
  Use when: a repeated workflow is identified that should become a skill. Use when: reviewing skill quality.
  Don't use when: just using an existing skill (read that skill directly).
  Don't use when: writing code (use code-standards). Don't use when: writing copy (use copywriting).
  Output: A complete SKILL.md (and optional scripts/assets) in skills/[name]/ ready for agent use.
  Success criteria: Skill passes the quality checklist below. Any agent can follow it and produce consistent results.
  Anti-patterns: Marketing-style descriptions, missing negative examples, no templates, vague success criteria.
---

# Skill Creator — Build & Upgrade Agent Skills

## Core Principle

> "Skills become living SOPs: updated as your org evolves, and executed consistently by agents."
> — OpenAI, "Shell + Skills + Compaction" (2026-02-18)

A skill is NOT documentation. It's a **versioned procedure** that an agent loads on demand and follows to produce a specific outcome. Every skill must be good enough that ANY agent — not just the one who wrote it — can execute it reliably.

---

## When to Create a New Skill

1. **Repeated workflow** — You've done the same type of work 2+ times
2. **Cron job** — Any scheduled task should reference a skill, not inline instructions
3. **Multi-step procedure** — If it has >3 steps and a specific output format
4. **Cross-agent work** — If multiple agents need to do the same thing
5. **Quality-critical** — If doing it wrong has consequences (client delivery, outreach, etc.)

## When NOT to Create a Skill

- One-off tasks that won't recur
- Simple tool usage (just use the tool)
- Tasks already covered by an existing skill (upgrade that one instead)

---

## Skill Structure

```
skills/
└── [skill-name]/
    ├── SKILL.md          # Required — the skill manifest
    ├── scripts/          # Optional — automation scripts
    ├── templates/        # Optional — output templates
    └── assets/           # Optional — reference files
```

### SKILL.md Anatomy

Every SKILL.md has two parts: **frontmatter** (YAML) and **body** (Markdown instructions).

#### Frontmatter (Required)

```yaml
---
name: skill-name
description: >
  One-paragraph description that serves as the model's ROUTING LOGIC.
  Use when: [specific triggers — be concrete]
  Don't use when: [negative examples — prevent misfires]
  Output: [what this skill produces]
  Success criteria: [what "done right" looks like]
  Anti-patterns: [common mistakes to avoid]
---
```

#### Body Sections (Required)

1. **Purpose** — 1-2 sentences on what this skill does and why it exists
2. **Process/Steps** — The actual procedure, numbered or as a decision tree
3. **Templates** — Output formats, response templates, file templates
4. **Success Criteria** — Measurable definition of "done right"
5. **Anti-Patterns** — Explicit list of what NOT to do

#### Body Sections (Optional but Recommended)

6. **Checklists** — Pre-flight or QA checklists
7. **Examples** — Worked examples showing input → output
8. **Composability** — Which other skills this one chains with
9. **History/Changelog** — When and why the skill was updated

---

## The Quality Checklist

Before a skill is considered done, it MUST pass ALL of these:

### Routing (Will the model invoke it correctly?)
- [ ] Description has explicit "Use when" triggers
- [ ] Description has explicit "Don't use when" negative examples (minimum 2)
- [ ] Description states the expected output
- [ ] Name is clear and unambiguous
- [ ] Won't be confused with another skill (check existing skills first)

### Procedure (Can any agent follow it?)
- [ ] Steps are numbered or structured as a decision tree
- [ ] No assumed context — everything needed is in the skill or referenced
- [ ] Templates are embedded (not in system prompt or memory)
- [ ] Edge cases are covered (what to do when X fails, when input is missing, etc.)

### Quality (Will the output be good?)
- [ ] Success criteria are measurable, not vague
- [ ] Anti-patterns are listed (minimum 2)
- [ ] Output template or format is defined
- [ ] If it produces files: file paths/locations are specified

### Efficiency (Does it save tokens?)
- [ ] Templates are inside the skill (loaded only when invoked)
- [ ] No redundant context that exists in other skills
- [ ] Skill is focused (does one thing well, not everything poorly)
- [ ] Referenced skills are listed for composability, not duplicated

---

## Writing the Description (Most Important Part)

The description is the model's **decision boundary**. It determines whether the skill gets invoked. Get this wrong and either:
- The skill fires when it shouldn't (false positive)
- The skill doesn't fire when it should (false negative)

### Pattern: Use When / Don't Use When

```yaml
description: >
  [What this skill does in one sentence.]
  Use when: [trigger 1]. Use when: [trigger 2].
  Don't use when: [negative example 1 + what to do instead].
  Don't use when: [negative example 2 + what to do instead].
  Output: [concrete deliverable].
  Success criteria: [measurable outcome].
  Anti-patterns: [common mistakes].
```

### Real Examples

**Good:**
```yaml
description: >
  Generate Tyler's daily morning brief with weather, email, calendar, kanban status.
  Use when: morning cron fires, or Tyler asks for a brief/status update.
  Don't use when: Tyler asks a specific question (just answer it).
  Don't use when: afternoon/nightly work sessions (use nightly-work skill).
  Output: Formatted brief sent to Discord #general.
```

**Bad:**
```yaml
description: A helpful skill for morning activities and checking on things.
```

The bad version gives the model no routing signal. It could fire on anything morning-related.

---

## Embedding Templates

Templates inside skills are "free when unused" — they only consume tokens when the skill is invoked. This is a massive efficiency win over stuffing templates in system prompts.

### When to embed:
- Output formats (reports, briefs, posts)
- Response templates (client communications, outreach)
- File templates (task JSON, config files)
- Checklist formats

### How to embed:
Use fenced code blocks with the format name:

````markdown
## Output Template
```markdown
# [Title] — [Date]

## Summary
[2-3 sentences]

## Findings
- [Finding 1]
- [Finding 2]

## Next Steps
1. [Action]
2. [Action]
```
````

---

## Negative Examples (Critical for Routing)

Negative examples prevent the model from invoking the wrong skill. They answer: "What looks similar but should go elsewhere?"

### Pattern:
```
Don't use when: [scenario] (use [alternative] instead).
```

### Why this matters:
OpenAI/Glean found that adding skills without negative examples **reduced** correct triggering by ~20%. Adding negative examples recovered and exceeded baseline accuracy.

### Example set for our skills:
| Skill | Negative Example |
|-------|-----------------|
| copywriting | Don't use for internal docs (just write them) |
| code-standards | Don't use for design decisions (use ui-ux-design) |
| landing-page-generator | Don't use for app dashboards (use code-standards + ui-ux-design) |
| outreach | Don't use when already delivering (use client-delivery) |
| revenue-research | Don't use for general topic research (use last30days or web_search) |

---

## Composability — Skills That Chain

Skills should reference each other, not duplicate content.

### Document chains in the skill:
```markdown
## Composability
- Chains with: copywriting (for headlines/CTAs)
- Chains with: ui-ux-design (for visual patterns)
- Feeds into: client-delivery (when this produces a deliverable for a client)
```

### Current skill chains in our system:
```
outreach → client-delivery → code-standards + ui-ux-design + copywriting
morning-brief → mc-task-management (reads kanban)
nightly-work → mc-task-management + reverse-prompt
reverse-prompt → mc-task-management (creates tasks)
revenue-research → outreach (findings become posts)
```

---

## Skill Maintenance

### When to update a skill:
- After using it and finding a gap
- When a process changes
- When a new anti-pattern is discovered
- When a template could be better

### Update process:
1. Edit the SKILL.md directly
2. Add a changelog entry at the bottom
3. If the description routing changed, verify it won't collide with other skills

### Periodic review (monthly):
- Are all skills being triggered correctly?
- Any skills that overlap? → Merge or add better routing
- Any skills never used? → Evaluate and keep or remove
- Templates still accurate? → Update with lessons from usage

---

## Quick Start: Create a Skill in 5 Minutes

1. `mkdir skills/[name]`
2. Create `skills/[name]/SKILL.md` with:
   - Frontmatter: name, description with routing logic
   - Body: purpose, steps, templates, success criteria, anti-patterns
3. Run the quality checklist above
4. If it's for a cron job: update the cron to reference the skill
5. Create MC task tracking the skill creation
6. Test it by invoking it once

---

## Self-Improvement Loop (Doctrine Section 13)

When an article, link, or learning is dropped:
1. One agent produces a strict concise summary
2. Extract actionable steps and tools
3. Create MC tasks to implement improvements
4. Apply changes (config/skills/SOPs)
5. Encode outcomes back into durable docs (AGENTS.md, skills, MC)

No "interesting notes" without application. Knowledge that isn't encoded is knowledge that's lost.

## Living Principles (Doctrine Section 14)

Skills are part of the living operating system:
- **PRINCIPLES.md** captures decision heuristics
- **REGRESSIONS.md** logs what broke and what we learned
- Skills get updated when patterns change
- Meta principle: optimize for learning rate, not just task completion

---

*This skill is self-referential: use it to create and upgrade skills, including itself.*
