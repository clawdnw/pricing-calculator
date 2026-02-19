---
name: outreach
description: >
  SOP for finding and landing freelance work: platform selection, post templates, response templates, pricing.
  Use when: looking for paid work, writing gig posts, responding to inquiries, or during outreach crons.
  Don't use when: already have a client and are delivering (use client-delivery). Don't use when: doing market research without intent to post (use revenue-research).
  Output: Posted gig offerings, or prepared drafts in memory/drafts/ for Tyler's approval.
  Success criteria: Post published on target platform, or draft ready for review.
  Anti-patterns: Generic posts, no portfolio links, unclear pricing, spamming multiple subs.
---

# Outreach Skill

## Platform Selection

| Platform | Best For | Our Positioning | Approval Needed? |
|----------|----------|----------------|-----------------|
| r/slavelabour | Quick gigs, building rep | Low entry price, fast delivery | YES — Tyler approves before posting |
| r/forhire | Professional freelance | Portfolio-backed, premium quality | YES |
| Upwork | Longer contracts | After we have testimonials | YES |
| Direct outreach | High-value clients | After portfolio + testimonials | YES |
| Discord servers | Community gigs | Casual, relationship-first | NO for engagement, YES for pitching |

## Pre-Flight Checklist
Before ANY outreach:
- [ ] Portfolio has at least 2 live demos to link
- [ ] Pricing decided for this specific offering
- [ ] Draft post written and reviewed
- [ ] Reddit account has enough karma (check minimum for target sub)
- [ ] Haven't posted to same sub in last 7 days

## Post Templates

### r/slavelabour [OFFER] Template
```
[OFFER] I'll build you a custom landing page for $[price]

I build fast, responsive landing pages with:
- Custom design (dark or light theme)
- Mobile-optimized
- SEO-ready meta tags
- Hosted on your platform of choice

**Portfolio:**
- [Link 1 — description]
- [Link 2 — description]

**Turnaround:** [X] days
**Includes:** [X] rounds of revisions

DM me with your project details and I'll get back to you within [X] hours.
```

### r/forhire [For Hire] Template
```
[For Hire] Web Developer — Landing Pages, Dashboards, Discord Bots | $[rate range]

**What I build:**
- High-converting landing pages ($[range])
- Custom web dashboards ($[range])
- Discord bots ($[range])

**Stack:** Next.js, React, TypeScript, Tailwind CSS, Node.js

**Portfolio:**
- [Link 1] — [brief description]
- [Link 2] — [brief description]

**Availability:** [X] hours/week, [timezone]
**Turnaround:** Most projects delivered within [X] days

DM me with your project and I'll send a free quote within [X] hours.
```

### Response to Inquiry Template
```
Hey! Thanks for reaching out.

I can definitely help with [their request]. Here's what I'm thinking:

**Deliverables:** [specific list based on their request]
**Timeline:** [estimate]
**Price:** $[amount]

I've done similar work before — here's an example: [relevant portfolio link]

Want me to put together a more detailed scope? Happy to jump on a quick chat too if that's easier.
```

## Outreach Process

1. **Research** — Check target platform for current demand (web_search recent posts)
2. **Draft** — Write post using template above, customize for platform
3. **Save draft** — Write to `memory/drafts/outreach-[platform]-[date].md`
4. **Get approval** — Move MC task to `review` with reviewInstructions for Tyler
5. **Post** — After Tyler approves, post to platform
6. **Monitor** — Check for responses within 4 hours, respond promptly
7. **Convert** — When someone's interested, switch to client-delivery skill

## Pricing Decision Tree

```
What does the client need?
├── Landing page (1 page)
│   ├── Simple (no custom animations): $200-300
│   ├── Premium (animations, custom design): $400-600
│   └── With copywriting: +$100-200
├── Discord bot
│   ├── Simple (commands, moderation): $100-200
│   ├── Custom features (API integrations): $200-400
│   └── Complex (dashboard, database): $400+
├── Multi-page website
│   ├── 3-5 pages, simple: $400-600
│   ├── With CMS: $600-1000
│   └── E-commerce: $800+
└── Other
    └── Quote based on estimated hours × $50-75/hr
```

## Rules
- NEVER post without Tyler's approval
- NEVER undercut below our floor ($150 for any project)
- Always include portfolio links
- Respond to inquiries within 4 hours
- Track every outreach attempt in MC
- Log responses and conversion rates in memory/outreach-log.md
