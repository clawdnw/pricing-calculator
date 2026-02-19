---
name: client-delivery
description: >
  End-to-end SOP for freelance/client project delivery: intake → build → QA → deliver → payment.
  Use when: we've landed a paid gig and need to execute the delivery pipeline.
  Don't use when: still looking for work (use outreach skill). Don't use when: building internal projects (use mc-task-management).
  Output: Delivered client project with QA evidence, tracked in MC kanban.
  Success criteria: Client receives deliverable on time, quality passes QA checklist, payment collected.
  Anti-patterns: Starting without clear scope, no QA before delivery, missing payment follow-up.
---

# Client Delivery Skill

## Pipeline Stages

### Stage 1: Intake
**Goal:** Crystal-clear scope before any work begins.

Checklist:
- [ ] Client name and contact method
- [ ] What they want (specific deliverables)
- [ ] Reference examples (links, screenshots)
- [ ] Timeline and deadline
- [ ] Budget confirmed and payment terms agreed
- [ ] Revision policy stated (e.g., "2 rounds of revisions included")
- [ ] Create MC task with project: `client-[name]`, all details in description

Template response to client:
```
Thanks for reaching out! To make sure I deliver exactly what you need:

1. What's the main goal of this [page/bot/project]?
2. Do you have any examples of what you like? (links, screenshots)
3. What's your timeline?
4. Budget range?

Once I have these, I'll send a scope summary for your confirmation before starting.
```

### Stage 2: Scope Confirmation
**Goal:** Written agreement before work starts.

Template:
```
Here's what I'll deliver:

**Project:** [name]
**Deliverables:** [specific list]
**Timeline:** [date]
**Price:** $[amount]
**Revisions:** [X] rounds included
**Payment:** [terms — 50% upfront, 50% on delivery / full on delivery / etc.]

Does this look right? Once confirmed, I'll start immediately.
```

### Stage 3: Build
**Goal:** Execute using our skills and tools.

Process:
1. Create MC task(s) for the project
2. Use appropriate skills:
   - Landing pages → landing-page-generator + copywriting + ui-ux-design + code-standards
   - Discord bots → code-standards
   - Other web projects → code-standards + ui-ux-design
3. Build in a dedicated directory: `projects/client-[name]/`
4. Commit progress to git
5. Update MC task activity as you build

### Stage 4: Internal QA
**Goal:** Catch issues before the client sees it.

QA Checklist:
- [ ] Does it match the scope exactly?
- [ ] Mobile responsive?
- [ ] All links work?
- [ ] No placeholder text remaining?
- [ ] Load time acceptable (<3 seconds)?
- [ ] Cross-browser tested (Chrome, Safari, Firefox)?
- [ ] Accessibility basics (contrast, alt text, focus states)?
- [ ] Copy is error-free (spelling, grammar)?
- [ ] Would Tyler show this to someone? (portfolio-worthy standard)

### Stage 5: Deliver
**Goal:** Clean handoff with clear next steps.

Template:
```
Your [project] is ready! 🎉

**Live preview:** [link]
**Source files:** [link or attached]

What's included:
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]

Take a look and let me know if you'd like any changes (you have [X] rounds of revisions included).

Once approved, I'll send the final files and [payment details].
```

### Stage 6: Revisions
**Goal:** Handle feedback professionally and efficiently.

Rules:
- Respond within 4 hours during business hours
- Track each revision round in MC task notes
- If scope creep: "That's a great idea! It's outside the original scope, but I can add it for $[amount]. Want me to include it?"
- After agreed revision rounds: additional changes quoted separately

### Stage 7: Payment & Close
**Goal:** Get paid, get testimonial, update portfolio.

Process:
1. Send final files after approval
2. Send invoice / confirm payment
3. Ask for testimonial:
```
Thanks for the great project! If you're happy with the work, would you mind leaving a quick review? Even 1-2 sentences helps me a lot.

[Optional: link to review platform]
```
4. Update MC task to complete with evidence
5. Add to portfolio (if client approves)
6. Log revenue in `memory/revenue-log.md`

## Revenue Tracking Template
```markdown
## [Date] — [Client Name]
- **Project:** [description]
- **Price:** $[amount]
- **Platform:** [r/slavelabour, r/forhire, Upwork, direct]
- **Delivered:** [date]
- **Paid:** [date]
- **Testimonial:** [yes/no, text if yes]
- **Portfolio-worthy:** [yes/no]
- **Lessons:** [what went well, what to improve]
```

## Pricing Quick Reference
| Service | Our Range | Market Range | Sweet Spot |
|---------|-----------|-------------|------------|
| Landing page | $200-600 | $100-2000 | $300-500 |
| Discord bot | $100-400 | $5-500 | $150-300 |
| Simple website | $300-800 | $200-5000 | $400-700 |
| AI consulting (hourly) | $100-200 | $100-895 | Build track record first |
