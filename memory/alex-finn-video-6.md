# Alex Finn Video #6 — Claude Opus 4.6 Deep Dive

**Date Analyzed:** 2026-02-16
**Video URL:** https://www.youtube.com/watch?v=iGkhfUvRV6o
**Video Title:** Claude Opus 4.6 — Historic Leap for AI (ClawBot + Claude Code)
**Duration:** ~17:28
**Creator:** Alex Finn

---

## Full Summary

Alex Finn covers the release of Claude Opus 4.6, calling it a "historic leap for AI." He walks through the key improvements, demonstrates how to get Opus 4.6 working in both ClawBot (OpenClaw) and Claude Code, and shows real workflows taking advantage of the new capabilities.

**Key improvements covered:**

1. **1 Million Token Context Window** — Best in industry. For ClawBot: massively better memory, less compaction loss, can reference conversations from days/weeks ago. For Claude Code: can explore much larger codebases.

2. **128K Token Output** — Can do more tasks in one go. ClawBot can handle more complex single prompts. He demonstrated having it research Opus 4.6 AND generate use cases AND write a video script all in one prompt. Claude Code can write more code per prompt ("one-shotting").

3. **Agent Teams (Agent Swarms)** — Built-in capability for spinning up multiple sub-agents. ClawBot can parallelize research tasks. Claude Code can have multiple instances attacking different parts of a codebase simultaneously. This is DIFFERENT from sub-agents — agent teams are separate sessions that can communicate with each other.

4. **Faster Speed** — Despite being smarter, Opus 4.6 is faster than previous Opus.

5. **Same Price** — No price increase for all these improvements.

**ClawBot (OpenClaw) Demo:**
- Opus 4.6 wasn't natively supported yet at time of recording
- Alex figured out a workaround: a prompt that has ClawBot research the model and edit its own config to support it
- Prompt provided in video description
- Once upgraded, he recommends "reverse prompting" — asking the AI what workflows it can now do with the new capabilities
- Key workflow: "True Second Brain Queries" — can now hold enough context to answer questions based on 20+ past conversations
- Key workflow: "Overnight Autonomous Projects" — longer-running tasks benefit from 1M context window
- Recommendation: Tell ClawBot to take advantage of the 1M context window during overnight proactive tasks

**Claude Code Demo:**
- Opus 4.6 available directly via `/model` command
- **Effort Levels** (new): Low/Medium/High — accessible via left/right arrow keys when Opus selected
  - $200 plan → High effort always
  - $100 plan → Medium effort (can probably do High)
  - $20 plan → Low effort
  - Use low effort for simple tasks (changing button colors)
  - Saves tokens and avoids hitting Claude Max limits
- **Agent Teams** must be enabled manually (disabled by default)
  - He asked Claude Code to read the docs and enable it
  - It edited the settings file automatically
  - Trigger with "please use an agent team" in your prompt
- Demo: Built a full project management app (NextJS) with dashboard, kanban board, calendar, settings page — in ~6 minutes using agent teams
  - Multiple agents spawned: Store Builder, Layout Builder, Dashboard Builder, Calendar Builder, Task Builder, Pages Builder
  - Each has own context (not shared)
  - Can communicate upward to team lead
  - Navigate between agents with Shift+Up/Down
  - Can give direct commands to individual agents OR go through team lead
  - Ctrl+O to expand view

---

## OpenClaw Features/Capabilities Discussed

1. **Memory & Context** — 1M token window means dramatically less compaction loss
2. **Overnight Autonomous Tasks** — Long-running proactive work while user sleeps
3. **Self-Configuration** — ClawBot can edit its own config to support new models
4. **Second Brain Queries** — Cross-referencing many past conversations for answers
5. **Reverse Prompting** — Asking the AI what to do rather than telling it
6. **Sub-agent Spawning** — Already existed, but improved with Opus 4.6
7. **Integration with Claude Code** — ClawBot can use Claude Code for building apps

---

## Henry (His Agent) — What Makes It Good

Alex doesn't name his agent "Henry" in this video (that may be from earlier videos). Key traits of his setup:
- Runs overnight autonomous projects (SaaS features, research, investing)
- Uses reverse prompting to discover new workflows
- Has extensive memory/conversation history that benefits from larger context
- Building "Creator Buddy" — his SaaS product — via the agent
- Treats the agent as a true employee with autonomy

---

## Specific Configurations/Settings Mentioned

1. **Opus 4.6 Config Workaround** — Prompt that makes ClawBot research and self-configure for Opus 4.6 (prompt in video description)
2. **Effort Levels in Claude Code** — `/model` → arrow keys → Low/Medium/High
3. **Agent Teams Enablement** — Disabled by default, enabled via settings file edit
4. **Model Selection** — `/model` command in Claude Code, Opus as default

---

## Workflows & Automations

1. **Reverse Prompting for New Capabilities** — "Now that we are on Claude Opus 4.6, based on what you know about me and the workflows we've done in the past, how can you take advantage of its new functionality to perform new workflows?"
2. **Overnight Autonomous Projects** — Long-running tasks leveraging 1M context
3. **True Second Brain Queries** — Deep contextual Q&A across conversation history
4. **Agent Team App Building** — "Please use an agent team to create [X]" in Claude Code
5. **Research + Content Pipeline** — Had it research Opus 4.6 and write his video script in one prompt

---

## Tips, Tricks & Best Practices

1. **Use effort levels strategically** — Low for simple tasks, High for complex. Saves tokens and money.
2. **Say "please use an agent team"** to trigger swarm mode in Claude Code
3. **Reverse prompt after upgrades** — Let the AI tell YOU what new workflows are possible
4. **Tell overnight tasks to leverage new capabilities** explicitly
5. **Agent teams > sub-agents** — Separate sessions, own context, can communicate, can be addressed individually
6. **Shift+Up/Down** to navigate between agent team members in Claude Code
7. **Ctrl+O** to expand agent team view
8. **Benchmarks are "fake and stupid"** — Judge by real-world usage instead
9. **Consider switching from Codex to Claude Code** for coding due to Opus 4.6 improvements

---

## Quotes/Prompts Worth Capturing

**Config Workaround Prompt (paraphrased):**
> Research Claude Opus 4.6 and figure out how to edit your own config to support this new model.

**Reverse Prompt for New Workflows:**
> "Now that we are on Claude Opus 4.6, based on what you know about me and the workflows we've done in the past, how can you take advantage of its new functionality to perform new workflows?"

**Overnight Task Enhancement:**
> "When you do your overnight tasks now, your proactive overnight tasks, make sure you take advantage of that 1 million token context window."

**Agent Team Trigger:**
> "Please use an agent team to create a new project management app for us using NextJS."

**Agent Teams Enable Prompt:**
> "I'm looking to enable agent teams, which just became available in Claude Opus 4.6. Can you read the docs and help me figure out how to enable it?"

**On the hierarchy:**
> "It really feels like for the first time it's not like we have just an agent working for us. We have an agent working for us who has agents working for them. This is now a hierarchy company."

---

## What We Should Implement

1. **✅ Already have sub-agents** — But should evaluate if OpenClaw's sub-agent system matches the "agent teams" pattern (separate sessions with own context + inter-agent communication)
2. **Effort Level Routing** — Consider implementing effort-level awareness for token economy (already in our AGENTS.md doctrine)
3. **Reverse Prompting After Upgrades** — When we upgrade models, run a reverse prompt to discover new workflows
4. **Explicit Context Window Leverage** — Tell overnight/heartbeat tasks to take advantage of available context
5. **Self-Configuration Capability** — We can already do this (editing our own configs), good to know Alex promotes this pattern
6. **Second Brain Query Pattern** — Ensure our memory system (MEMORY.md + daily files) is optimized for deep cross-referencing
7. **"Agent Team" Trigger Phrase** — Consider whether we should support explicit sub-agent swarm requests from Tyler

---

*Analysis by Astra | Source: Alex Finn YouTube*
