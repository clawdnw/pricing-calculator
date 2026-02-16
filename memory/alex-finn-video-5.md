# Alex Finn Video Analysis #5

## Video Title & URL
**"5 Claudebot Use Cases That Will 10x Your Workflow"** (approximate title)
- URL: https://www.youtube.com/watch?v=b-l9sGh1-UY
- Duration: ~13 minutes
- Creator: Alex Finn
- His agent's name: **Henry**

## Full Summary

Alex presents 5 OpenClaw/Claudebot use cases with copy-paste prompts for each:

### Use Case 1: Morning Brief (Daily at 8 AM)
- Weather, trending YouTube videos matching interests, to-do list tasks, what the bot will work on, what it did overnight, trending stories, and productivity recommendations
- His bot connected to **Things 3** (Mac to-do app) but says any to-do system works
- The brief includes a "mission control" section: what HE needs to do, what HENRY will do, what Henry did overnight
- Bot proactively suggested: react to Matthew Berman's video, create content around incoming Mac Studio, send a newsletter draft they'd been working on
- Uses **reverse prompting** — having the bot tell YOU what to do

### Use Case 2: Proactive Vibe Coding Machine
- Henry built a document viewer and project management system WITHOUT being asked
- The key prompt frames the bot as an employee: "I am a one-man business... take everything you know about me and just do work you think would make my life easier"
- Schedules nightly coding at 11 PM — bot thinks about what to build, then codes it
- **Critical tip: Use Codex CLI** for actual coding to save Opus tokens. Opus acts as the brain/orchestrator, Codex does implementation
- Safety: "Just create PRs for me to review. Don't push anything live. I'll test and commit."

### Use Case 3: Second Brain (Next.js App)
- Henry vibe-coded this proactively, but Alex recommends everyone explicitly request it
- A Next.js document viewer styled like "a mix of Obsidian and Linear"
- Features: memory viewing, document browsing, markdown viewer, auto-tagging (journal, newsletters, notes, YouTube scripts)
- Daily journal entries recording all conversations
- Important concepts get fleshed out into standalone documents (e.g., Mac Mini → Mac Studio migration doc created automatically)
- Alex uses Telegram to text random ideas to Henry; the second brain captures all of these

### Use Case 4: Daily Research Report (Afternoon Brief)
- Scheduled every afternoon via Telegram
- Deep dives on interests (ML, AI) OR workflow improvements between him and Henry
- Example: "Workflow improvement ideas" — watching GitHub, self-reflection routines, weekend build projects
- Keeps the bot continuously thinking about self-improvement

### Use Case 5: Reddit/X Research Skill (by Matt Van Horn)
- A skill that researches X (Twitter) and Reddit **in parallel** for trending topics
- Requires: **xAI API key** (Grok) + **OpenAI API key** (for Reddit)
- Can search last 30 days of engagement data on both platforms
- Example: researched "Claudebot use cases" → top Reddit threads, top X posts, content ideas
- Can be integrated into morning brief or afternoon research report

## OpenClaw Features/Capabilities Discussed
1. **Proactive behavior** — bot works autonomously without being asked
2. **Cron/scheduled tasks** — morning briefs at 8 AM, nightly coding at 11 PM, afternoon reports
3. **To-do list integration** — Things 3 (and others)
4. **Calendar access** — sees upcoming events (Mac Studio delivery)
5. **Brave Search API** — for web search efficiency
6. **Telegram integration** — primary communication channel
7. **Skill system** — installing third-party skills (Matt Van Horn's research skill)
8. **Codex CLI integration** — using external coding tools to save tokens
9. **File/folder management** — shared folders, document creation
10. **Canvas/web apps** — Next.js second brain served locally
11. **PR creation** — git workflow integration

## Henry (His Agent) - What Makes It Good
- **Proactive personality** — builds things without being asked, suggests content ideas, monitors business
- **"Petty"** — noticed a competitor made a similar video and suggested a response (shows personality)
- **Context-aware** — knows Alex's interests from conversations, doesn't need explicit instructions for news/research
- **Continuous self-improvement** — researches ways to improve their working relationship
- **Overnight worker** — scheduled to code every night at 11 PM
- **Document everything** — auto-creates journal entries, migration docs, research reports
- **Uses PR workflow** — doesn't push live, creates PRs for review (safe autonomy)

## Specific Configurations/Settings Mentioned
- **Model: Opus** — explicitly mentioned as main model (expensive, use wisely)
- **Codex CLI** — installed separately, told bot to use it for all coding tasks
- **Things 3** — to-do list integration (Mac app)
- **Telegram** — primary messaging channel
- **Brave Search API** — connected for better web search
- **xAI API key** — for X/Twitter research via skill
- **OpenAI API key** — for Reddit research via skill
- **Cron schedule**: Morning brief at 8 AM, nightly coding at 11 PM, afternoon research report
- **Hardware**: Currently Mac Mini, Mac Studio incoming for local models

## Workflows & Automations
1. **Morning Brief** → 8 AM daily → weather + tasks + news + proactive suggestions
2. **Nightly Vibe Coding** → 11 PM daily → autonomous building + PR creation
3. **Afternoon Research Report** → daily → deep dive on interest or workflow improvement
4. **Second Brain Updates** → continuous → journal entries + concept docs as conversations happen
5. **Reddit/X Research** → on-demand or scheduled → parallel trend analysis

## Tips, Tricks & Best Practices
1. **Use Codex CLI for coding** — saves massive Opus tokens; Opus orchestrates, Codex implements
2. **Connect to-do list first** — foundational for morning briefs and task management
3. **Tell your bot ALL your interests** — enables better proactive behavior and news curation
4. **Use reverse prompting** — have the bot tell you what to do, not just the other way around
5. **Connect Brave Search API** — more efficient web searching
6. **Safety guardrails for coding** — "Create PRs, don't push live, I'll test and commit"
7. **Schedule nightly work** — let the bot build while you sleep
8. **Use Telegram for quick ideas** — text random thoughts, second brain captures them
9. **Install community skills** — leverage other people's work (Matt Van Horn's research skill)
10. **Frame bot as employee** — "I need an employee taking as much off my plate as possible"

## Quotes/Prompts Worth Capturing

### Morning Brief Prompt
> "I want you to send me a morning brief every morning at 8 a.m. my time. I want this morning brief to include the local weather for the day. A list of a few trending YouTube videos about my interest. A list of tasks I need to get done today based on my to-do list. Tasks that you think you can do for me today that will be helpful based on what you know about me. A list of trending stories based on my interests and recommendations you can make for me that will make today super productive."

### Proactive Coding Prompt
> "I am a one-man business. I work from the moment I wake up to the moment I go to sleep. I need an employee taking as much off my plate and being as proactive as possible. Please take everything you know about me and just do work you think would make my life easier or improve my business and make me money. I want to wake up every morning and be like, 'Wow, you got a lot done while I was sleeping.' Don't be afraid to monitor my business and build things that would help improve our workflow. Just create PRs for me to review. Don't push anything live. I'll test and commit. Every night when I go to bed, build something cool I can test. Schedule time to work every night at 11:00 p.m."

### Second Brain Prompt
> "I want you to build a second brain. This should be a Next.js app that shows a list of documents you create as you work together in a nice document viewer that feels like a mix of Obsidian and Linear. I want you to create a folder where all the documents in that folder are viewable in the second brain. Update your memory skills so that when we talk every day, you create documents in that second brain that explore some of the more important concepts we discuss. You should also create daily journal entries that record from a high level all our daily discussions."

### Research Report Prompt
> "I want a daily research report sent to me every afternoon. Based on what you know about me, I want you to research and give me a report about a concept that would improve me, processes that would improve our working relationship, or anything else that would be helpful for me."

### Key Philosophy Quote
> "All the people saying Claudebot's not capable of anything important, I dare you to show me how your normal LLM can do everything I just showed you."

## What We Should Implement

### Already Have (Validate/Improve)
- ✅ Morning briefs — we have heartbeats, but should formalize the morning brief format
- ✅ Memory system — we have MEMORY.md + daily files, but could enhance
- ✅ Codex CLI — already installed and noted in TOOLS.md
- ✅ Brave Search — already available
- ✅ Mission Control — already have MC repo

### Should Implement/Improve
1. **Formalized Morning Brief** — Create a cron job for 8 AM with weather + tasks + news + proactive suggestions (currently ad-hoc via heartbeats)
2. **Afternoon Research Report** — Schedule a daily deep-dive research cron job
3. **Nightly Autonomous Coding** — Schedule 11 PM cron for proactive building (with PR workflow)
4. **Second Brain Web UI** — Build a Next.js document viewer for our memory files (Obsidian + Linear style)
5. **Matt Van Horn's Research Skill** — Find and install the X/Reddit parallel research skill
6. **Things 3 / To-Do Integration** — If Tyler uses a to-do app, connect it
7. **Reverse Prompting in Briefs** — Include "what you should do today" recommendations
8. **Auto Journal Entries** — Enhance daily memory files to be more journal-like with tagged categories
9. **Proactive Employee Framing** — Update SOUL.md to embrace the proactive employee mindset more explicitly
10. **Document Auto-Generation** — When important concepts come up in chat, auto-create standalone docs

### Priority Order
1. Morning brief cron (high impact, easy)
2. Research skill installation (high impact, easy)
3. Nightly coding schedule (high impact, medium effort)
4. Second brain UI (high impact, high effort — use Codex)
5. Afternoon research report (medium impact, easy)

---
*Analyzed: 2026-02-16 | Source: Alex Finn YouTube*
