# Overnight Research — 2026-02-16

## 1. Fixed-Scope Service Offers (AI-Augmented Dev Shop)

Based on r/forhire, r/slavelabour, and market signals. These are offers where AI tooling (Codex CLI, Lovable, etc.) gives us 5-10x speed advantage over traditional freelancers.

### Offer A: Landing Pages & Small Business Sites
- **Price:** $300–$750 per page/site
- **Delivery:** 2–5 days
- **What:** Conversion-focused landing pages, small biz sites (1-5 pages), portfolio sites
- **Why it works:** Massive demand on Reddit/Fiverr. Most freelancers charge $500+ and take 1-2 weeks. With AI + landing-page-generator skill, we can ship in hours. High volume, low complexity.
- **Competition:** Flooded but most sellers are slow/mediocre. Speed + quality = differentiation.

### Offer B: Telegram/Discord Bots & AI Chatbots
- **Price:** $200–$1,000 depending on complexity
- **Delivery:** 3–7 days
- **What:** Custom Telegram bots, Discord bots, AI-powered customer service chatbots, notification/monitoring bots
- **Why it works:** Active demand on r/slavelabour (multiple [TASK] posts for Telegram bots). We literally run this stack daily. Deep domain knowledge.
- **Competition:** Moderate. Most offerings are basic; AI-integrated bots command premium.

### Offer C: Custom Dashboards & Internal Tools
- **Price:** $500–$2,000
- **Delivery:** 5–10 days
- **What:** Admin dashboards, data visualization tools, internal CRUD apps, Airtable/Notion replacements
- **Why it works:** Businesses need these constantly but can't justify hiring full-time. Codex CLI can scaffold these fast. Higher ticket = fewer clients needed.
- **Competition:** Low on Reddit marketplaces, higher on Upwork.

### Offer D: Automation & Integration Scripts
- **Price:** $100–$500
- **Delivery:** 1–3 days
- **What:** Zapier-replacement scripts, API integrations, web scrapers, data pipeline automations, cron-based monitors
- **Why it works:** Quick wins, repeat customers. "I need X connected to Y" is a universal pain point. AI makes these trivial.
- **Competition:** Low barrier but also low ticket. Best as upsell or entry point.

### Offer E: AI Tool Setup & Agent Configuration
- **Price:** $200–$800
- **Delivery:** 1–5 days
- **What:** Set up AI agents (OpenClaw, n8n, custom), configure LLM workflows, build RAG pipelines, deploy local models
- **Why it works:** Emerging niche. Founders/operators want AI leverage but don't know how to set it up. We ARE the target user — credibility is built-in.
- **Competition:** Very low. Most "AI consultants" are vaporware. Hands-on setup is rare.

### Recommendation
**Start with A (landing pages) and B (bots)** — fastest to first dollar, highest demand density. Use A as lead gen for C and E. Post on r/forhire and r/slavelabour first (free), then expand to Fiverr/Twitter.

---

## 2. QMD Skill — Assessment

**Already installed** at `/Users/tylernw/.bun/bin/qmd` with a `workspace` collection.

### What It Does
- Local search engine for Markdown files. BM25 keyword search (instant) + optional vector search (requires Ollama, slower).
- Index markdown collections, search by keyword or semantic similarity.
- By Tobi Lütke (Shopify founder) — quality tool.

### Current State
- BM25 search works now: `qmd search "query"` — no external dependencies
- Vector search (`qmd vsearch`) needs Ollama running with a local model — not set up yet
- Hybrid search (`qmd query`) = vector + LLM rerank, slowest mode

### Verdict: Already Useful, Worth Keeping
- **Use now:** `qmd search` for fast keyword lookups across workspace markdown
- **Future:** Set up Ollama when Mac Studios arrive for vector search
- **Action:** Set up a cron job to run `qmd update` hourly to keep the index fresh
- No further installation needed — it's already there.

---

## 3. Persistent Memory Solutions

### What We Already Have

**A. OpenClaw Built-in Memory**
- `memory_search` — semantic search across MEMORY.md + memory/*.md
- `memory_get` — snippet retrieval
- MEMORY.md (curated) + daily files (raw logs)
- **This is already solid for our use case.** The main cost is loading MEMORY.md in full each main session.

**B. Elite Longterm Memory Skill (installed)**
- 5-layer architecture: hot RAM, warm (LanceDB vectors), cold (git-notes), MEMORY.md, optional cloud backup
- **Requires OPENAI_API_KEY** for vector embeddings — adds API cost
- Overkill for current scale. The complexity-to-benefit ratio is poor right now.
- **Verdict: Skip for now.** Revisit when workspace grows beyond what built-in memory_search handles.

**C. QMD (already covered above)**
- Complements memory_search: QMD searches files on disk, memory_search searches agent memory
- Together they cover both angles without external API costs

### Practical Approaches to Reduce Context Loading

1. **Keep MEMORY.md lean** — aggressively prune. If it's over ~4K tokens, it's too long. Archive old sections to `memory/archive/`.
2. **Use memory_search before loading** — don't load full MEMORY.md blindly; search first, pull only relevant snippets.
3. **Daily files as source of truth for recent context** — MEMORY.md for stable facts only, not running logs.
4. **Structured sections in MEMORY.md** — clear headers so memory_search scores well on relevant chunks.
5. **QMD for workspace docs** — route "find in my files" queries to QMD instead of burning tokens reading files.

### Verdict
**We don't need a new tool.** The built-in memory system + QMD + disciplined file hygiene is sufficient. The bottleneck isn't the tooling — it's keeping MEMORY.md pruned and well-structured. I'll make that a periodic maintenance task.

---

## Action Items
- [ ] Draft service offer copy for landing pages (Offer A) and bot building (Offer B)
- [ ] Create posts for r/forhire and r/slavelabour
- [ ] Set up hourly `qmd update` cron job
- [ ] Audit and prune MEMORY.md (target: <4K tokens)
- [ ] Create MC tasks for service offer launch
