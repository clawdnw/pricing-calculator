#!/usr/bin/env python3
"""
Landing Page Generator - Generate premium landing pages from JSON config.

Usage:
  python generate.py --config config.json --output landing.html
"""

import argparse
import json
from pathlib import Path


ICONS = {
    "zap": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>""",
    "shield": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>""",
    "star": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>""",
    "check": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>""",
    "rocket": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"></path><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"></path><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"></path><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"></path></svg>""",
    "heart": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>""",
    "clock": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>""",
    "mail": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>""",
}


def generate_css(config: dict) -> str:
    # Support both schema formats:
    # - theme.primary, theme.accent, theme.background (original)
    # - branding.colors.primary, branding.colors.accent, branding.colors.background (new)
    theme = config.get("theme", {})
    branding = config.get("branding", {})
    colors = branding.get("colors", {})
    
    # Color extraction with fallback chain
    primary = theme.get("primary") or colors.get("primary", "#6366f1")
    accent = theme.get("accent") or colors.get("accent", "#8b5cf6")
    bg = theme.get("background") or colors.get("background", "#0a0a0f")
    text_override = colors.get("text")  # Optional override
    
    # Mode detection: explicit theme.mode or infer from background
    mode = theme.get("mode")
    if not mode:
        # Infer from background color brightness
        bg_hex = bg.lstrip('#')
        r, g, b = int(bg_hex[0:2], 16), int(bg_hex[2:4], 16), int(bg_hex[4:6], 16)
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        mode = "light" if brightness > 128 else "dark"

    # Light vs dark theme variables
    if mode == "light":
        text_color = text_override or "#1a1a2e"
        muted_color = "#6b7280"
        card_bg = "rgba(0,0,0,0.02)"
        border_color = "rgba(0,0,0,0.1)"
        hero_gradient = f"radial-gradient(ellipse at top, {primary}15, transparent 50%)"
    else:
        text_color = text_override or "#e5e5e5"
        muted_color = "#a1a1aa"
        card_bg = "rgba(255,255,255,0.03)"
        border_color = "rgba(255,255,255,0.1)"
        hero_gradient = f"radial-gradient(ellipse at top, {primary}15, transparent 50%)"

    return f"""
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    :root {{
      --primary: {primary};
      --accent: {accent};
      --bg: {bg};
      --text: {text_color};
      --muted: {muted_color};
      --card: {card_bg};
      --border: {border_color};
    }}
    html {{ scroll-behavior: smooth; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; }}
    section {{ padding: 80px 0; }}

    /* Hero */
    .hero {{
      min-height: 90vh;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      background: {hero_gradient};
      padding: 120px 24px;
    }}
    .hero h1 {{ font-size: clamp(2.5rem, 8vw, 4.5rem); font-weight: 800; letter-spacing: -0.03em; margin-bottom: 1.5rem; line-height: 1.1; }}
    .hero p {{ font-size: 1.25rem; color: var(--muted); max-width: 600px; margin: 0 auto 2.5rem; }}
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 14px 32px;
      border-radius: 12px;
      font-weight: 600;
      font-size: 1rem;
      text-decoration: none;
      transition: all 0.2s ease;
    }}
    .btn-primary {{ background: var(--primary); color: white; }}
    .btn-primary:hover {{ background: var(--accent); transform: translateY(-2px); box-shadow: 0 8px 30px {primary}40; }}
    .btn-secondary {{ background: transparent; border: 1px solid var(--border); color: var(--text); margin-left: 12px; }}
    .btn-secondary:hover {{ border-color: var(--muted); background: {"rgba(0,0,0,0.02)" if mode == "light" else "rgba(255,255,255,0.05)"}; }}

    /* Stats */
    .stats {{
      display: flex;
      justify-content: center;
      gap: 60px;
      padding: 40px 0;
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      margin: 60px 0;
    }}
    .stat {{ text-align: center; }}
    .stat-value {{ font-size: 2.5rem; font-weight: 800; color: var(--primary); }}
    .stat-label {{ font-size: 0.875rem; color: var(--muted); margin-top: 4px; }}

    /* Section headers */
    .section-header {{ text-align: center; margin-bottom: 60px; }}
    .section-header h2 {{ font-size: 2.5rem; font-weight: 700; letter-spacing: -0.02em; }}
    .section-header p {{ color: var(--muted); margin-top: 12px; font-size: 1.1rem; }}

    /* Features */
    .features-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 24px;
    }}
    .feature-card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 32px;
      transition: all 0.3s ease;
    }}
    .feature-card:hover {{
      border-color: var(--primary);
      transform: translateY(-4px);
      box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }}
    .feature-icon {{
      width: 48px;
      height: 48px;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
    }}
    .feature-icon svg {{ width: 24px; height: 24px; color: white; }}
    .feature-card h3 {{ font-size: 1.25rem; font-weight: 600; margin-bottom: 8px; }}
    .feature-card p {{ color: var(--muted); font-size: 0.95rem; }}

    /* Pricing */
    .pricing-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 24px;
      max-width: 800px;
      margin: 0 auto;
    }}
    .pricing-card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 40px;
      text-align: center;
      transition: all 0.3s ease;
    }}
    .pricing-card.highlighted {{
      border-color: var(--primary);
      background: linear-gradient(180deg, rgba(99,102,241,0.1), transparent);
      transform: scale(1.02);
    }}
    .pricing-card h3 {{ font-size: 1.25rem; margin-bottom: 12px; }}
    .price {{ font-size: 3rem; font-weight: 800; }}
    .price span {{ font-size: 1rem; font-weight: 400; color: var(--muted); }}
    .pricing-features {{ list-style: none; margin: 24px 0; text-align: left; }}
    .pricing-features li {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 8px 0;
      color: var(--muted);
    }}
    .pricing-features svg {{ width: 18px; height: 18px; color: var(--primary); flex-shrink: 0; }}

    /* Testimonials */
    .testimonials-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 24px;
    }}
    .testimonial-card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 32px;
    }}
    .testimonial-card p {{ font-size: 1.1rem; font-style: italic; margin-bottom: 20px; }}
    .testimonial-author {{ font-weight: 600; }}
    .testimonial-role {{ font-size: 0.875rem; color: var(--muted); }}

    /* FAQ */
    .faq-list {{ max-width: 700px; margin: 0 auto; }}
    .faq-item {{ border-bottom: 1px solid var(--border); }}
    .faq-question {{
      width: 100%;
      background: none;
      border: none;
      padding: 24px 0;
      text-align: left;
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--text);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .faq-answer {{ padding-bottom: 24px; color: var(--muted); }}

    /* Final CTA */
    .final-cta {{
      text-align: center;
      padding: 100px 24px;
      background: radial-gradient(ellipse at bottom, rgba(139,92,246,0.2), transparent 60%);
    }}
    .final-cta h2 {{ font-size: 3rem; font-weight: 800; margin-bottom: 16px; }}
    .final-cta p {{ color: var(--muted); font-size: 1.2rem; margin-bottom: 32px; }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--border);
      padding: 40px 24px;
      text-align: center;
    }}
    .footer-links {{ display: flex; justify-content: center; gap: 32px; margin-bottom: 20px; }}
    .footer-links a {{ color: var(--muted); text-decoration: none; font-size: 0.9rem; }}
    .footer-links a:hover {{ color: var(--text); }}
    .copyright {{ color: var(--muted); font-size: 0.85rem; }}

    /* Responsive */
    @media (max-width: 768px) {{
      .stats {{ flex-direction: column; gap: 30px; }}
      .hero h1 {{ font-size: 2.5rem; }}
      .section-header h2 {{ font-size: 2rem; }}
      .final-cta h2 {{ font-size: 2rem; }}
      .pricing-grid {{ grid-template-columns: 1fr; }}
    }}
    """


def render_section(section_name: str, data: dict) -> str:
    if not data.get("enabled", True):
        return ""

    if section_name == "hero":
        return f"""
    <section class="hero">
      <div class="container">
        <h1>{data['headline']}</h1>
        <p>{data['subheadline']}</p>
        <a href="{data['cta']['href']}" class="btn btn-primary">{data['cta']['text']}</a>
        {f'<a href="{data["secondaryCta"]["href"]}" class="btn btn-secondary">{data["secondaryCta"]["text"]}</a>' if data.get('secondaryCta') else ''}
      </div>
    </section>
    """

    if section_name == "socialProof":
        stats_html = "\n".join([
            f'<div class="stat"><div class="stat-value">{s["value"]}</div><div class="stat-label">{s["label"]}</div></div>'
            for s in data['stats']
        ])
        return f"""
    <section><div class="container"><div class="stats">{stats_html}</div></div></section>
    """

    if section_name == "features":
        features_html = "\n".join([
            f"""
        <div class="feature-card">
          <div class="feature-icon">{ICONS.get(f['icon'], ICONS['star'])}</div>
          <h3>{f['title']}</h3>
          <p>{f['description']}</p>
        </div>"""
            for f in data['items']
        ])
        return f"""
    <section id="features">
      <div class="container">
        <div class="section-header"><h2>{data['headline']}</h2></div>
        <div class="features-grid">{features_html}</div>
      </div>
    </section>
    """

    if section_name == "pricing":
        plans_html = "\n".join([
            f"""
        <div class="pricing-card {'highlighted' if p.get('highlighted') else ''}">
          <h3>{p['name']}</h3>
          <div class="price">{p['price']} <span>{p['period']}</span></div>
          <ul class="pricing-features">
            {''.join([f'<li>{ICONS["check"]}{feat}</li>' for feat in p['features']])}
          </ul>
          <a href="#" class="btn btn-primary">{p['cta']}</a>
        </div>"""
            for p in data['plans']
        ])
        return f"""
    <section id="pricing">
      <div class="container">
        <div class="section-header"><h2>{data['headline']}</h2></div>
        <div class="pricing-grid">{plans_html}</div>
      </div>
    </section>
    """

    if section_name == "testimonials":
        testimonials_html = "\n".join([
            f"""
        <div class="testimonial-card">
          <p>"{t['quote']}"</p>
          <div class="testimonial-author">{t['author']}</div>
          <div class="testimonial-role">{t['role']}</div>
        </div>"""
            for t in data['items']
        ])
        return f"""
    <section>
      <div class="container">
        <div class="section-header"><h2>{data['headline']}</h2></div>
        <div class="testimonials-grid">{testimonials_html}</div>
      </div>
    </section>
    """

    if section_name == "faq":
        faq_html = "\n".join([
            f"""
        <div class="faq-item">
          <button class="faq-question">{q['question']}</button>
          <div class="faq-answer">{q['answer']}</div>
        </div>"""
            for q in data['items']
        ])
        return f"""
    <section>
      <div class="container">
        <div class="section-header"><h2>{data['headline']}</h2></div>
        <div class="faq-list">{faq_html}</div>
      </div>
    </section>
    """

    if section_name == "cta":
        return f"""
    <section class="final-cta">
      <div class="container">
        <h2>{data['headline']}</h2>
        <p>{data['subheadline']}</p>
        <a href="{data['buttonHref']}" class="btn btn-primary">{data['buttonText']}</a>
      </div>
    </section>
    """

    return ""


def render_footer(data: dict) -> str:
    if not data.get("enabled", True):
        return ""

    links_html = "\n".join([
        f'<a href="{link["href"]}">{link["text"]}</a>'
        for link in data.get("links", [])
    ])

    return f"""
    <footer>
      <div class="container">
        <div class="footer-links">{links_html}</div>
        <p class="copyright">&copy; {data.get('copyright', '2026')}</p>
      </div>
    </footer>
    """


def generate_page(config: dict) -> str:
    meta = config.get("meta", {})
    sections = config.get("sections", {})
    footer = config.get("footer", {})

    css = generate_css(config)

    sections_html = "\n".join([
        render_section(name, data)
        for name, data in sections.items()
    ])

    footer_html = render_footer(footer)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{meta.get('title', 'Landing Page')}</title>
  <meta name="description" content="{meta.get('description', '')}">
  <style>{css}</style>
</head>
<body>
{sections_html}
{footer_html}
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Generate landing page from config")
    parser.add_argument("--config", required=True, help="Path to config JSON")
    parser.add_argument("--output", default="landing.html", help="Output file path")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)

    html = generate_page(config)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Landing page generated: {args.output}")
    print(f"   Config: {args.config}")


if __name__ == "__main__":
    main()
