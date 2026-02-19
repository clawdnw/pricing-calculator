# Landing Page Template System

**Purpose:** Enable <2hr client delivery for custom landing pages.

## Quick Start

```bash
cd /Users/tylernw/.openclaw/workspace/client-templates/landing-pages

# Generate from example config
python3 generate.py --config config.example.json --output my-landing.html

# Generate NW landing page
python3 generate.py --config nw-landing-config.json --output nw-landing.html
```

## How It Works

1. **Create a config file** — Copy `config.example.json` and customize
2. **Run the generator** — `python3 generate.py --config your-config.json --output output.html`
3. **Deliver** — Send the HTML file to the client or deploy

## Config Structure

**Two schema formats supported:**

### Option 1: Simple Theme (recommended for quick setup)
```json
{
  "meta": { "title": "...", "description": "..." },
  "theme": {
    "mode": "dark",
    "primary": "#6366f1",
    "accent": "#8b5cf6",
    "background": "#0a0a0f"
  },
  "brand": { "name": "...", "tagline": "..." },
  "sections": { ... }
}
```

### Option 2: Full Branding (auto-detects light/dark, more control)
```json
{
  "meta": { ... },
  "branding": {
    "companyName": "Your Brand",
    "tagline": "...",
    "logo": "/logo.svg",
    "colors": {
      "primary": "#FF6B35",
      "secondary": "#004E89",
      "accent": "#F7B801",
      "text": "#1a1a1a",
      "background": "#ffffff"
    },
    "fonts": {
      "heading": "Inter",
      "body": "Source Sans Pro"
    }
  },
  "sections": { ... }
}
```

**Note:** Mode is auto-detected from background brightness if not specified. Light backgrounds (brightness > 128) = light mode.

## Sections

All sections are optional — set `enabled: false` to hide.

| Section | Purpose |
|---------|---------|
| `hero` | Main headline, CTA, first impression |
| `socialProof` | Stats bar (clients, delivery time, etc) |
| `features` | Feature cards with icons |
| `pricing` | 1-3 pricing plans |
| `testimonials` | Client quotes |
| `faq` | Accordion FAQ |
| `cta` | Final call-to-action |

## Icons

Available icons: `zap`, `shield`, `star`, `check`, `rocket`, `heart`, `clock`, `mail`

## Customization

1. **Colors** — Use `theme` (simple) or `branding.colors` (full control)
   - Primary: main brand color (buttons, highlights)
   - Accent: secondary color (hover states, accents)
   - Background: page background color
   - Text: body text color (optional, auto-detected from mode)
2. **Content** — Edit headlines, descriptions, features in config
3. **Sections** — Enable/disable sections with `enabled: true/false`
4. **Pricing** — Add/remove plans, adjust features
5. **Light/Dark Mode** — Set `theme.mode` or let it auto-detect from background color

## Delivery Checklist

Before delivering to a client:
- [ ] Config matches client requirements
- [ ] All placeholder content replaced
- [ ] Colors match client brand (if specified)
- [ ] Contact email/href updated
- [ ] Generated HTML tested in browser
- [ ] Mobile responsive verified

## Files

```
landing-pages/
├── README.md                 # This file
├── generate.py               # Generator script
├── config.example.json       # Example config with all options
├── nw-landing-config.json    # NW Global Enterprise landing page
└── nw-landing.html           # Generated output
```

## Live Demo

The NW landing page is served at: `localhost:3333/landing-demo.html`
