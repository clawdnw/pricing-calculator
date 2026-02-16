# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

### QMD (Quick Markdown Search)
- Path: `/Users/tylernw/.bun/bin/qmd`
- Collection: `workspace` — all .md files in workspace indexed
- BM25 search works without Ollama: `qmd search "query"`
- Vector search needs Ollama: `qmd vsearch "query"` (not yet set up)
- Update index after file changes: `qmd update`

### Installed Skills (ClawHub)
- `qmd` — local markdown search/indexing
- `elite-longterm-memory` — multi-layer memory system (needs evaluation, requires OpenAI key for full features)
- `landing-page-generator` — generate landing pages for service offers
- `x-post-automation` — X/Twitter post automation

### Codex CLI
- Path: `/Users/tylernw/.nvm/versions/node/v24.13.0/bin/codex`
- Version: 0.98.0
- Use for ALL coding tasks. Don't burn Claude tokens on implementation.

### Discord Server
- Guild ID: `1468801612800851990`
- Channels:
  - #general: `1471999180288426135`
  - #intel-feed: `1472828706425798749`
  - #team-chat: `1472828707948335155`
  - #war-room: `1472828709051301977`
  - #mc-links: `1472828710309855366`

### GitHub
- Org: `NW-Global-Enterprise`
- MC Repo: `NW-Global-Enterprise/mission-control`
- Auth account: `clawdnw`

### Agent Avatars
- Location: `/Users/tylernw/Documents/Agents/`
- Files: ASTRA-Avatar.jpeg, CLAWDNW-Avatar.jpeg, CODEX-Avatar.jpeg, SHURI-Avatar.jpeg

---

Add whatever helps you do your job. This is your cheat sheet.
