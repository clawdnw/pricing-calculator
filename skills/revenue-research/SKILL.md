---
name: revenue-research

triggers:
  - "market research"
  - "competitor analysis"
  - "pricing research"
  - "revenue opportunity"
related:
  - "[[revenue-doctrine]]"
  - "[[outreach]]"
  - "[[last30days-lite]]"
description: >
  Research revenue opportunities, competitor pricing, and freelance market demand.
  Use when: afternoon research cron fires, or when evaluating a new service offering or market.
  Don't use when: just checking email or doing operational tasks.
  Output: Research file in memory/ plus Discord summary.
---

# Revenue Research Skill

## Research Topics (pick ONE per session)
1. **r/forhire + r/slavelabour** — what services are people buying right now?
2. **Competitor pricing** — what do similar services cost? Where's our sweet spot?
3. **AI/automation trends** — what's emerging that we can productize?
4. **Lead generation** — specific people/companies looking for what we offer
5. **Platform analysis** — which freelance platforms have best ROI for our skills?

## Process
1. Pick ONE topic (don't try to cover everything)
2. Run 2-3 web_search queries, focused and specific
3. Extract actionable findings (not summaries of summaries)
4. Write to `memory/research-YYYY-MM-DD.md`
5. Send 3-5 bullet summary to Discord #general (1471999180288426135)

## Output Template (research file)
```markdown
# Research: [Topic] — [Date]

## Key Findings
- [Finding 1 with evidence/source]
- [Finding 2]
- [Finding 3]

## Actionable Next Steps
1. [Specific action we can take]
2. [Specific action]

## Market Data
- [Pricing, demand signals, competitor info]

## Sources
- [URL 1]
- [URL 2]
```

## Success Criteria
- Research completed in <5 minutes (stay within cron timeout)
- At least 3 concrete findings with sources
- At least 1 actionable next step that can become an MC task
- Summary actually sent to Discord

## Anti-Patterns
- ❌ Spending 15 minutes on broad searches with no findings
- ❌ Writing "interesting" notes without actionable steps
- ❌ Researching topics we've already covered (check memory/ first)
- ❌ Timing out because scope was too broad
