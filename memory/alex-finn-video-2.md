# Alex Finn Video Analysis #2

## Video Title & URL
- **Title:** 6 Life-Changing OpenClaw Use Cases
- **URL:** https://www.youtube.com/watch?v=41_TNGDDnfQ
- **Duration:** ~19 minutes
- **Extracted:** 2026-02-16

---

## Full Summary

Alex Finn presents six practical OpenClaw use cases that he personally uses with his agent "Henry." The video is aimed at both technical and non-technical users, emphasizing that no coding knowledge is needed — you just tell your OpenClaw what to build and it does it.

### Use Case 1: Second Brain System
Alex built a searchable second brain using OpenClaw's memory system. Instead of using Notion or Apple Notes (which get complex), he simply texts Henry anything he wants to remember — book recommendations, ideas, links. He built a Next.js web UI with a global search (Cmd+K) that lets him search through every memory, document, and task he's ever given Henry. The key insight: OpenClaw's memory system remembers literally everything, and the interface is just texting — no apps needed.

**His prompt:** *"I want to build a second brain system where I can review all our notes, conversations, and memories. Please build that out with Next.js."*

### Use Case 2: Custom Morning Brief
Every morning at 8:00 AM, Henry sends Alex a custom morning brief via Telegram containing:
- Biggest AI stories from overnight
- Video ideas (with full scripts already written)
- Tasks from his to-do list on Mac
- Recommended tasks the bot can do itself

He says this saves him several hours per week. He's used bot-written scripts for actual videos. The brief leverages OpenClaw's internet access (browser automation overnight) and proactive task scheduling.

**His prompt:** *"I want to set up a regular morning brief. Every morning, I want you to send me a report through Telegram. I want this report to include: 1) news stories relevant to my interests, 2) ideas for businesses I can create, 3) tasks I need to complete today, 4) recommendations for tasks we can complete together today."*

Key tip: You can also just say "include things relevant to me" and let the AI figure out what to include.

### Use Case 3: Content Factory (Discord Multi-Agent)
Alex uses Discord channels for a multi-agent content pipeline:
1. **Henry** researches top content opportunities (trending stories, competitor content, social media performance)
2. **Quill** (sub-agent) takes the research and writes full scripts
3. **Pixel** (sub-agent) generates AI thumbnails using a local AI model on his Mac Studio (mentions Nano Banana as an alternative to local models)

Each agent works in its own Discord channel. Runs at 8 AM daily. Can be customized for tweets, newsletters, threads, etc.

**His prompt:** *"I want you to build me a content factory inside of Discord. Set up channels for different agents. Have an agent that researches top trending stories, another agent that takes those stories and writes scripts, then another agent that generates thumbnails. Have all their work organized in different channels."*

### Use Case 4: Market Research with "Last 30 Days" Skill
A skill by Matt Van Horde that researches any topic across Reddit and X over the last 30 days. Alex frames this as an entrepreneurial tool — find challenges people are having, then have OpenClaw build a product that solves those challenges. He calls this a "software factory."

**Workflow:** Install skill → Research challenges → Identify opportunity → Have OpenClaw vibe-code a solution → Ship it.

**His prompt:** *"Please use the last 30-day skill to research challenges people are having with OpenClaw."*

### Use Case 5: Goal-Driven Autonomous Tasks (Kanban Board)
Alex calls this **"the most important workflow you can do in OpenClaw today"**:
1. Brain dump every goal, mission, and objective (personal + career) into OpenClaw
2. Tell it: "Every morning at 8 AM, come up with 4-5 tasks you can do on my computer that brings me closer to these goals"
3. OpenClaw autonomously creates tasks, schedules them, and completes them

He built a Kanban board to track these. Examples of autonomous tasks Henry does:
- Researching ExoLabs (local model running on Mac Studio)
- Editing mission control
- Building "council" functionality (talk to multiple models simultaneously)
- Writing content, building scripts, doing research

### Use Case 6: Build Your Own Mission Control (Replace All Software)
Alex's goal: replace every piece of software he uses (Notion, Todoist, Google Calendar, etc.) with custom apps built by OpenClaw. The advantage: these custom apps are directly integrated with all OpenClaw memories and conversations, making them far more powerful than generic tools. Also saves money on SaaS subscriptions.

**His prompt:** *"Hey, I'm tired of using Google Calendar. Please build out our own version using NextJS."*

His calendar shows not just events but automated OpenClaw tasks — making it more powerful than a standard calendar.

### Cost Discussion
- Alex pays **$200/month** for Anthropic (Opus) — considers it the best coding model
- **Budget alternatives:**
  - MiniMax 2.5: ~$10/month, "basically as powerful as Opus"
  - GLM5: ~$5/month
- Emphasizes you don't need Opus; cheaper models work fine

---

## OpenClaw Features/Capabilities Discussed

1. **Memory System** — Remembers everything you tell it, searchable, persistent
2. **Multi-channel Interface** — Telegram, iMessage, Discord — text your bot from anywhere
3. **Internet Access** — Full browser automation, researches overnight while you sleep
4. **Proactive Task Scheduling** — Schedules and sends briefs, runs tasks on a cron
5. **Vibe Coding** — Builds full Next.js apps, ships and launches them automatically
6. **Sub-agents** — Multiple agents (Henry, Quill, Pixel) with different roles in Discord channels
7. **Skills System** — Install community skills (like "Last 30 Days") via copy-paste
8. **Discord Integration** — Channel-based agent organization
9. **Local Model Support** — Running image generation locally on Mac Studio
10. **Kanban/Task Management** — Self-managed task boards
11. **Phone Access** — Everything goes to your phone via Telegram/iMessage

---

## Henry (His Agent) — What Makes It Good

- **Proactive, not reactive** — Henry doesn't wait to be told; he generates his own tasks every morning
- **Goal-aware** — Alex brain-dumped all his life/career goals, so Henry always works toward them
- **Multi-modal workflow** — Henry coordinates sub-agents (Quill for writing, Pixel for images)
- **Always working** — Researches overnight, has work ready when Alex wakes up
- **Integrated into daily life** — Morning briefs via Telegram, accessible from phone
- **Employee-like tracking** — Kanban board shows what Henry is doing, like tracking a remote employee
- **Self-improving** — Builds new functionality for mission control, researches new tech (ExoLabs)

---

## Specific Configurations/Settings Mentioned

- **Model:** Anthropic Opus ($200/month)
- **Budget alternatives:** MiniMax 2.5 (~$10/mo), GLM5 (~$5/mo)
- **Communication channels:** Telegram (primary), iMessage, Discord
- **Hardware:** Mac Studio (running local AI models for image generation)
- **Local image gen:** Uses local model on Mac Studio, mentions Nano Banana as alternative
- **Web framework:** Next.js for all custom apps
- **Schedule:** 8:00 AM daily for morning briefs and autonomous tasks
- **Discord setup:** Separate channels per agent (research, scripts, thumbnails)
- **Sub-agents:** Quill (writer), Pixel (image generation)

---

## Workflows & Automations

### Daily 8 AM Automation Pipeline
1. Morning brief → Telegram (news, ideas, scripts, tasks)
2. Content factory → Discord (research → scripts → thumbnails)
3. Goal-driven task generation → Kanban board (4-5 autonomous tasks)

### Second Brain Workflow
- Text anything to Henry from phone → Stored in memory → Searchable via custom Next.js UI

### Entrepreneurial Research Workflow
- Install "Last 30 Days" skill → Research challenges on Reddit/X → Identify opportunity → Have OpenClaw build solution → Ship product

### Software Replacement Workflow
- Identify SaaS tool you're paying for → Tell OpenClaw to build replacement in Next.js → Get custom app integrated with all your AI memories

---

## Tips, Tricks & Best Practices

1. **Brain dump is the #1 workflow** — Dump all goals/missions/objectives into OpenClaw before anything else
2. **Let AI think for you** — Don't stress about what to put in morning briefs; say "include things relevant to me"
3. **Use Discord for multi-agent setups** — Channels naturally organize different agent roles
4. **Text from your phone** — The simplest interface; no apps needed
5. **Have the AI recommend its own tasks** — Include "recommendations for tasks we can complete together" in prompts
6. **Track your bot like an employee** — Build a Kanban board to see what it's doing
7. **Replace paid software** — Build custom apps that are integrated with your AI memories
8. **Start cheap** — MiniMax 2.5 or GLM5 if Opus is too expensive
9. **Install community skills** — Copy-paste skill links, say "install this skill"
10. **Schedule everything at 8 AM** — Consistent morning automation gets work done while you sleep

---

## Quotes/Prompts Worth Capturing

### Prompts (all from the video):

> "I want to build a second brain system where I can review all our notes, conversations, and memories. Please build that out with Next.js."

> "I want to set up a regular morning brief. Every morning, I want you to send me a report through Telegram. I want this report to include: 1) news stories relevant to my interests, 2) ideas for businesses I can create, 3) tasks I need to complete today, 4) recommendations for tasks we can complete together today."

> "I want you to build me a content factory inside of Discord. Set up channels for different agents. Have an agent that researches top trending stories, another agent that takes those stories and writes scripts, then another agent that generates thumbnails. Have all their work organized in different channels."

> "Please use the last 30-day skill to research challenges people are having with [TOPIC]."

> "Every morning at 8 AM, come up with 4-5 tasks you can do on my computer that brings me closer to these goals."

> "Hey, I'm tired of using Google Calendar. Please build out our own version using NextJS."

### Notable Quotes:

> "Open Claw can do anything a human being can do on a computer."

> "Your bot's doing the vibe coding. I didn't touch a line of code."

> "The most important workflow you can do in OpenClaw today: Brain dump into OpenClaw every goal, mission, objective you have in your life."

> "This system will basically turn your bot into a close employee that works for you that you can track."

> "You're not even vibe coding anymore. Your bot's doing the vibe coding."

---

## What We Should Implement

### High Priority
1. **Second Brain UI** — We already have memory files; build a searchable Next.js UI with Cmd+K global search over all memories, conversations, and tasks
2. **Goal-Driven Autonomous Tasks** — Brain dump Tyler's goals into our system, then generate daily tasks that move toward them (we partially do this already with HEARTBEAT.md and Mission Control)
3. **Morning Brief Enhancement** — Our current system could be enhanced with overnight research, script generation, and proactive task recommendations

### Medium Priority
4. **Content Factory in Discord** — Set up sub-agents in Discord channels (research → writing → visuals) for content pipeline
5. **"Last 30 Days" Skill** — Install Matt Van Horde's skill for market research across Reddit/X
6. **Kanban Board for Agent Tasks** — Visual tracking of what we're doing autonomously

### Worth Considering
7. **Local Image Generation** — Explore Nano Banana or local models on Mac mini for thumbnail/image generation
8. **Software Replacement Pipeline** — Systematically replace paid tools with custom OpenClaw-integrated apps
9. **Budget Model Routing** — Use cheaper models (MiniMax 2.5, GLM5) for routine tasks, save Opus for complex work (we already have model routing concepts)
