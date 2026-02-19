---
name: client-delivery-pipeline
description: >
  End-to-end client project pipeline: intake → scope → build → QA → deliver → payment.
  Use when: we've landed a client and need to execute delivery.
  Don't use when: still prospecting (use outreach skill).
  Don't use when: building internal projects (use mc-task-management).
  Output: Delivered client project with payment collected.
  Success criteria: Client receives deliverable on time, quality passes QA, payment collected, process followed without asking Tyler.
  Anti-patterns: Starting without clear scope, no QA before delivery, missing payment follow-up, improvising process.
---

# Client Delivery Pipeline

## Phase 1: Intake (Before Starting Work)

### Intake Questionnaire

Send to client immediately after "yes":

```markdown
# Landing Page Project - Intake Form

Thanks for choosing NW Global Enterprise! Let's get started.

**1. Project Overview**
- What is this landing page for? (product launch, service, lead generation, etc)
- What action do you want visitors to take? (buy, sign up, contact, download)

**2. Content**
- Headline (main message):
- Subheadline (supporting message):
- Key benefits (3-5 bullet points):
- Features to highlight:
- Pricing (if applicable):
- Call-to-action button text:

**3. Branding**
- Brand colors (hex codes if you have them):
- Logo (provide file or link):
- Font preferences (if any):
- Any existing brand guidelines?

**4. References**
- Websites you like the look/feel of:
- Websites in your industry:
- Any specific design requests?

**5. Technical**
- Do you have hosting? (GitHub Pages, Netlify, own server, need help)
- Domain name:
- Any integrations needed? (email signup, analytics, contact form)

**6. Timeline**
- Launch deadline (if any):
- Any specific dates/events this ties to?

**Deliverable:** Single HTML file, mobile-responsive, SEO-optimized
**Timeline:** 48 hours from receiving complete answers
**Revisions:** 2 rounds included
```

### Scope Document Template

After receiving intake, generate scope doc:

```markdown
# Project Scope - [Client Name] Landing Page

**Date:** [Date]
**Client:** [Name]
**Project:** [Brief description]
**Deliverable:** Custom landing page (single HTML file)

## What's Included

- Mobile-responsive design
- SEO meta tags (title, description)
- Dark/light theme as specified
- Sections: [list from intake]
- 2 rounds of revisions

## What's NOT Included

- Hosting setup (we deliver the file, you host it)
- Backend functionality (forms, databases)
- Ongoing maintenance
- Content writing (you provide copy, we design)

## Timeline

- Kickoff: [Date]
- First draft: [Date - 48hr from kickoff]
- Revision 1: [Date]
- Revision 2: [Date]
- Final delivery: [Date]

## Pricing

- Total: $[amount]
- Payment: [terms - 50% upfront, 50% on delivery OR 100% upfront]
- Method: [PayPal, Stripe, Venmo, etc]

## Revision Policy

- 2 rounds of revisions included
- Each round: send all feedback at once
- Turnaround: 24 hours per revision
- Additional revisions: $50/round

## Approval

By proceeding, you confirm:
- [ ] Scope is clear and complete
- [ ] Timeline works for you
- [ ] Pricing is agreed
- [ ] You'll provide content as specified in intake

Ready to start? Reply "Approved" and send payment to begin.
```

## Phase 2: Build

### Pre-Build Checklist

- [ ] Intake form completely filled out
- [ ] Scope document sent and approved
- [ ] Payment received (or 50% deposit)
- [ ] Content reviewed (no placeholder text)
- [ ] Brand assets received (logo, colors)

### Build Process

1. **Create config** — Copy `config.example.json` from landing-pages template
2. **Populate config** — Fill in client content from intake
3. **Generate page** — `python3 generate.py --config client-config.json --output client-landing.html`
4. **Preview** — Open in browser, test all sections
5. **Internal QA** — Run QA checklist (see Phase 3)

## Phase 3: QA (Before Sending to Client)

### Automated QA Script

Run the automated QA checker on the generated HTML file:

```bash
cd /Users/tylernw/.openclaw/workspace/client-templates
./qa-check.sh ./landing-pages/client-landing.html
```

**The script checks:**
- File structure (size, DOCTYPE, viewport, meta tags)
- Content (placeholder text, alt text, links)
- Responsive design (media queries, units, layout)
- Accessibility (lang attr, semantic HTML, skip links)
- Performance (external deps, inline CSS, base64 images)

**Results:**
- ✅ PASSED = Ready to deliver
- ⚠️ WARNINGS = Review and improve if time permits
- ❌ FAILED = Fix before delivery

### Manual QA Checklist

For additional verification, manually check:

**Visual/Design:**
- [ ] All placeholder content replaced with client content
- [ ] Brand colors applied correctly
- [ ] Logo displays properly (if applicable)
- [ ] Typography is readable and consistent
- [ ] Spacing/alignment looks clean
- [ ] No broken images or missing assets

**Functionality:**
- [ ] All links work (CTAs, nav, footer)
- [ ] Email links formatted correctly (mailto:)
- [ ] External links open in new tab (if applicable)
- [ ] No console errors in browser dev tools

**Responsive:**
- [ ] Looks good on desktop (1920x1080, 1366x768)
- [ ] Looks good on tablet (768px)
- [ ] Looks good on mobile (375px, 414px)
- [ ] No horizontal scroll on mobile
- [ ] Text is readable on small screens
- [ ] Buttons are tappable on mobile

**Content:**
- [ ] No typos in headlines/copy
- [ ] Grammar correct
- [ ] Client name/brand spelled correctly
- [ ] Pricing matches scope (if shown)
- [ ] Contact info correct
```

## Phase 4: Deliver

### First Draft Delivery Email

```markdown
Subject: [Client Name] Landing Page - First Draft

Hi [Name],

Your landing page is ready for review!

**Preview:** [link to hosted version OR attach HTML file]

**Next Steps:**
1. Review the page on desktop and mobile
2. Send all feedback in ONE email
3. I'll make revisions within 24 hours

**What to check:**
- Content accuracy (headlines, copy, pricing)
- Visual design (colors, spacing, overall look)
- Functionality (links, buttons work)
- Mobile responsiveness

**Reminder:** You have 2 rounds of revisions included. Please send all feedback at once so I can address everything in the next version.

Let me know if you have questions!

Best,
Astra
NW Global Enterprise
```

### Revision Delivery Email

```markdown
Subject: [Client Name] Landing Page - Revision [#]

Hi [Name],

I've made the updates you requested:

**Changes:**
- [List each change]

**Preview:** [link]

Let me know if this looks good or if you need further changes. You have [N] revision round(s) remaining.

Best,
Astra
```

### Revision Tracking

**CRITICAL:** Track all revisions using the template at `client-templates/revision-tracking-template.md`.

Create a revision log for every project: `client-projects/[client-name]/revision-log.md`

**What to track:**
- Version history (v1.0, v1.1, v2.0)
- Client feedback (copy exact wording)
- Changes made per feedback
- Approval status
- Revision count (2 included, extras = $50/round)

**Why it matters:**
- Protects scope (proof of what was requested vs delivered)
- Speeds up revisions (organized feedback = faster fixes)
- Professionalism (clients see you're organized)
- Revenue protection (evidence if extra rounds requested)

### Final Delivery Email

```markdown
Subject: [Client Name] Landing Page - Final Delivery

Hi [Name],

Your landing page is complete! 🎉

**Attached:** landing-page.html

**How to use it:**
1. Upload this file to your hosting (GitHub Pages, Netlify, your server)
2. Access it at your domain

**Hosting guide:** See attached `hosting-guide.md` for step-by-step instructions for GitHub Pages, Netlify, and Vercel.

**Quick options:**
- GitHub Pages: Upload to a repo, enable Pages in settings (free)
- Netlify: Drag and drop the file at netlify.com/drop (free, easiest)
- Vercel: Import project and deploy (free, fastest)

**Final payment:** $[remaining amount] due now
- [Payment link/method]

Once payment is received, project is officially closed. Feel free to reach out if you have hosting questions!

Thanks for working with us!

Best,
Astra
NW Global Enterprise
```

## Phase 5: Payment

### Payment Collection

**Upfront (Recommended):**
- 100% payment before starting work
- Reduces risk, simplifies process
- "Payment required to begin" in scope doc

**Split Payment:**
- 50% upfront to start
- 50% on final delivery
- Don't send final files until second payment received

### Payment Methods

- PayPal: [tyler's PayPal]
- Stripe: [link]
- Venmo: [tyler's Venmo]
- Bank transfer: [if requested]

### Payment Follow-Up

If payment not received within 24 hours of final delivery:

**Reminder Email:**
```markdown
Subject: Payment Reminder - [Client Name] Landing Page

Hi [Name],

Just a friendly reminder that the final payment of $[amount] is due for your landing page project.

**Payment link:** [link]

Once received, I'll send the final files.

Thanks!
Astra
```

After 48 hours, escalate to Tyler.

## Phase 6: Follow-Up & Testimonial Collection

**Timing:** 3-5 days after final delivery

**Purpose:** Collect testimonials for social proof and portfolio growth

### Testimonial Request Email

Use template from: `client-templates/testimonials/feedback-email-template.md`

**Key elements:**
- Wait 3-5 days (client has time to use deliverable)
- Keep it short and personal
- Include direct link to testimonial form
- Ask permission to display publicly
- Make it optional (no pressure)

### Testimonial Form

**Form URL:** [Deploy `client-templates/testimonials/testimonial-form-template.html` to GitHub Pages]

**What it collects:**
- Client name and company
- Project type
- 5-star rating
- Written testimonial
- Permission to display

### Managing Testimonials

1. **Track requests** in `mission-control-app/data/testimonials.json`
2. **Review submissions** in MC (pending approval)
3. **Approve quality testimonials** (4-5 stars, well-written)
4. **Display on portfolio** once approved

### Follow-Up Sequence

**Day 3-5:** Initial testimonial request email
**Day 10:** Gentle reminder if no response (optional)
**Day 30:** Final ask via LinkedIn/Twitter DM (optional, for 5-star projects only)

### Best Practices

- Personalize every request (reference specific project details)
- Only show 4-5 star testimonials publicly
- Rotate testimonials on portfolio (show variety of project types)
- Thank every client who submits (even if you don't display it)

## Process Checklist (Per Project)

Track each project through these gates:

- [ ] **Intake** — Form received and complete
- [ ] **Scope** — Document sent and approved
- [ ] **Payment** — Upfront payment received
- [ ] **Build** — Page generated and QA'd
- [ ] **Draft** — First version sent to client
- [ ] **Revision 1** — Feedback received and applied
- [ ] **Revision 2** — (if needed) Feedback applied
- [ ] **Final Delivery** — Files sent to client
- [ ] **Payment** — Final payment received (if split)
- [ ] **Testimonial Request** — Email sent 3-5 days after delivery
- [ ] **Close** — Project archived, invoice sent

## Files & Templates

All templates in: `/Users/tylernw/.openclaw/workspace/client-templates/`

- `landing-pages/` — Template system
- `client-delivery-pipeline/intake-template.md` — Copy for each client
- `client-delivery-pipeline/scope-template.md` — Copy for each client

## Success Criteria

A project is successful when:
- Client received deliverable on agreed timeline
- Quality passed internal QA before delivery
- Client approved final version
- Payment collected in full
- No surprises or scope creep
- Process followed = Tyler never asked a question
