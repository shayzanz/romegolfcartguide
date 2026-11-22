import json, os, re, html, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES, ABOUT, U

SITE = "https://romegolfcartguide.com"
# Google Analytics 4 Measurement ID (G-XXXXXXXXXX). Empty = no cookie banner and no analytics.
GA_ID = "G-3G5VQ96CPJ"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
UPDATED = "October 2026"
UPDATED_ISO = "2026-10-28"
BY_SLUG = {p["slug"]: p for p in PAGES}

WA_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-3.3-.8-2.8-1.1-4.5-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .5l-.4.6-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.2.1.8-.1 1.3z"/></svg>'
CART = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#16181d" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 15h16M6 15V9h12v6M8 9l1.5-4h5L16 9"/><circle cx="8" cy="17.5" r="1.8"/><circle cx="16" cy="17.5" r="1.8"/></svg>'

def head(title, desc, path, img, extra_ld=()):
    url = SITE + path
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in extra_ld)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Rome Golf Cart Guide">
<meta property="og:image" content="{U(img,1200)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1f4fd1">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css?v=20261120">
{ld}</head>
<body>
"""

NAV = f"""<header class="bar">
  <div class="wrap">
    <a class="brand" href="/"><span class="brand-dot">{CART}</span>Rome Golf Cart Guide</a>
    <nav>
      <a href="/#tours">Tours</a>
      <a href="/#guides">Guides</a>
      <a href="/golf-cart-tour-rome-price/">Prices</a>
      <a href="/best-golf-cart-tours-rome/">Best tours 2026</a>
      <a class="phone js-wa" href="#" data-msg="Hi! I'd like help choosing a golf cart tour in Rome.">{WA_ICON}<span class="num-txt">+39 393 855 2086</span></a>
    </nav>
  </div>
</header>
"""

def footer():
    links = "".join(f'<li><a href="/{p["slug"]}/">{p["nav"]}</a></li>' for p in PAGES)
    return f"""<footer>
  <div class="wrap cols">
    <div>
      <b>Rome Golf Cart Guide</b>
      <p>An independent guide to golf cart tours in Rome. We are not a tour operator: tours are run by local operators and booked through the platform shown on each listing.</p>
      <p style="font-size:.85rem">Prices and details can change. Always check the final price, what's included and the cancellation policy before you pay. Photos: Unsplash.</p>
    </div>
    <div>
      <b>Guides</b>
      <ul>{links}</ul>
    </div>
    <div>
      <b>Info</b>
      <ul><li><a href="/">All tours</a></li><li><a href="/about/">About &amp; how we compare</a></li><li><a href="/privacy.html">Privacy policy</a></li><li><a href="#" class="js-wa" data-msg="Hi!">Contact on WhatsApp</a></li></ul>
    </div>
  </div>
  <div class="wrap" style="margin-top:26px;font-size:.82rem">© <span class="yr"></span> RomeGolfCartGuide.com</div>
</footer>

<a class="fab js-wa" href="#" data-msg="Hi! I'd like help choosing a golf cart tour in Rome." aria-label="Chat with us on WhatsApp">{WA_ICON.replace('width="18" height="18" ','')}</a>
<script src="/assets/tours.js?v=20261106"></script>
</body>
</html>
"""

DISCLOSE = '<p class="disclose">We earn a small commission when you book through our links, at no extra cost to you. Bookings, payment and customer service are handled by Viator or GetYourGuide. Tour photos show the places you\'ll visit, not the operators\' own carts.</p>'

def aside(msg):
    return f"""<aside class="aside">
  <h3>Not sure which tour?</h3>
  <p>Send us your dates, group size and hotel area. We reply on WhatsApp with the two or three tours that fit best.</p>
  <a class="btn btn-wa js-wa" href="#" data-msg="{html.escape(msg)}">Message us on WhatsApp</a>
  <a class="btn btn-line" href="/#tours">Compare all tours</a>
</aside>"""

def related(slugs):
    items = []
    for s in slugs:
        p = BY_SLUG[s]
        items.append(f'<a href="/{s}/"><img loading="lazy" src="{U(p["img"],200)}" alt="" width="72" height="56">{html.escape(p["h1"])}</a>')
    return '<div class="related">' + "".join(items) + "</div>"

def faq_html(faqs):
    return '<div class="faq">' + "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q,a in faqs) + "</div>"

import tourpages as _tp
_TOURS = {t["id"]: t for t in _tp.load_tours()}
_LISTS = _tp.load_lists()

def tour_links(key, limit=8):
    """Plain HTML links to the tour detail pages in a list, so crawlers find them without JavaScript."""
    ids = [i for i in _LISTS.get(key, []) if i != "custom"][:limit]
    if not ids:
        return ""
    links = " · ".join(f'<a href="/tour/{i}/">{html.escape(_TOURS[i]["name"])}</a>' for i in ids)
    return f'<p class="tourlinks"><b>Route maps and details:</b> {links}</p>'

def tour_block(p):
    if p.get("tours"):
        return f'<div class="tourlist-wrap" data-tours="{p["tours"]}"></div>' + tour_links(p["tours"])
    return f'<div data-gyg-ids="{p["gyg_ids"]}" data-gyg-title="" data-gyg-note=""></div>'

MONTHS_EN = ["January","February","March","April","May","June","July","August","September","October","November","December"]
def nice_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS_EN[int(m)-1]} {y}"

# Seasonal strip shown under the hero on the home pages and at the top of related guides.
# Remove after 6 January 2027 (set SEASON_ON = False).
SEASON_ON = True
SEASON = {
    "en": '<div class="season"><div class="wrap"><b>Christmas 2026:</b> St. Peter\'s tree is lit on 7 December. <a href="/rome-christmas-lights-tour/">Dates, best spots and evening tours &rarr;</a></div></div>',
    "es": '<div class="season"><div class="wrap"><b>Navidad 2026:</b> el árbol de San Pedro se enciende el 7 de diciembre. <a href="/es/luces-navidad-roma-carrito-golf/">Fechas, dónde ver las luces y tours de tarde &rarr;</a></div></div>',
    "de": '<div class="season"><div class="wrap"><b>Weihnachten 2026:</b> Der Baum am Petersplatz leuchtet ab 7. Dezember. <a href="/de/weihnachtsbeleuchtung-rom-golfcart/">Termine, beste Orte und Abendtouren &rarr;</a></div></div>',
} if SEASON_ON else {"en": "", "es": "", "de": ""}

def guide(p):
    path = f'/{p["slug"]}/'
    mod = p.get("modified", UPDATED_ISO)
    lds = [
        {"@context":"https://schema.org","@type":"Article","headline":p["h1"],"description":p["desc"],
         "image":U(p["img"],1200),"dateModified":mod,"datePublished":UPDATED_ISO,
         "author":{"@type":"Organization","name":"Rome Golf Cart Guide","url":SITE+"/about/"},
         "publisher":{"@type":"Organization","name":"Rome Golf Cart Guide","url":SITE+"/"},
         "mainEntityOfPage":SITE+path},
        {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
            {"@type":"ListItem","position":2,"name":p["nav"],"item":SITE+path}]},
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faqs"]]},
    ]
    wa = f"Hi! I'm reading your guide about {p['nav'].lower()} and need help choosing a golf cart tour in Rome. Dates: … People: …"
    return head(p["title"], p["desc"], path, p["img"], lds) + NAV + f"""
<main>
<section class="pagehead">
  <img class="bg" src="{U(p['img'])}" alt="{html.escape(p['img_alt'])}" fetchpriority="high">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> / {html.escape(p['nav'])}</div>
    <h1>{html.escape(p['h1'])}</h1>
    <p>{html.escape(p['lead'])}</p>
  </div>
</section>

<section class="section">
  <div class="wrap article-grid">
    <article class="prose">
      <p class="updated">Updated {nice_date(mod) if "modified" in p else UPDATED}</p>
      <div class="answer"><b>Quick answer</b><p>{html.escape(p['answer'])}</p></div>
      {p['body']}
    </article>
    {aside(wa)}
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2>{p.get('tours_title','Tours that fit')}</h2>
    {tour_block(p)}
    {DISCLOSE}
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2>Questions people ask</h2>
    {faq_html(p['faqs'])}
    <h2 style="margin-top:56px">Related guides</h2>
    {related(p['related'])}
  </div>
</section>
</main>
""" + footer()

def about():
    p = ABOUT
    path = "/about/"
    lds = [{"@context":"https://schema.org","@type":"Organization","name":"Rome Golf Cart Guide","url":SITE+"/",
            "logo":SITE+"/favicon.svg","areaServed":"Rome, Italy",
            "contactPoint":{"@type":"ContactPoint","telephone":"+39-393-855-2086","contactType":"customer support","availableLanguage":["English","Italian"]}}]
    body = """
<h2>Why this guide exists</h2>
<p>There are dozens of golf cart tours in Rome, sold across several booking sites, and they look almost identical at first glance. The differences that matter, like hotel pickup, group size, length, food stops and price, are buried in long listings. We put them side by side so you can choose in a minute.</p>

<h2>How we compare tours</h2>
<ul>
<li><b>Public information only.</b> We use what operators and booking platforms publish: price, duration, inclusions, pickup area, group size and cancellation policy.</li>
<li><b>Popularity and track record.</b> We favour operators with a long history of bookings and consistently strong ratings on the major platforms.</li>
<li><b>Fit, not just price.</b> We group tours by who they suit: families, seniors, cruise passengers, food lovers, people on a budget.</li>
<li><b>Regular updates.</b> Prices and details change, so we review listings regularly and show the update date on each page.</li>
</ul>

<h2>How we make money</h2>
<p>When you book through our links, the booking platform pays us a small commission. It costs you nothing extra and doesn't change the price you pay. For tours we arrange directly on WhatsApp, the local operator pays us a commission. We never accept payment to rank a tour higher.</p>

<h2>What we are not</h2>
<p>We don't run tours or own golf carts. Each tour is run by a licensed local operator, and bookings made through Viator or GetYourGuide are handled by those platforms, including payment, changes and refunds.</p>

<h2>Get in touch</h2>
<p>Questions, corrections, or you run a golf cart tour in Rome and want to be listed? Message us on WhatsApp at +39 393 855 2086.</p>
"""
    return head(p["title"], p["desc"], path, p["img"], lds) + NAV + f"""
<main>
<section class="pagehead">
  <img class="bg" src="{U(p['img'])}" alt="{html.escape(p['img_alt'])}" fetchpriority="high">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> / About</div>
    <h1>{p['h1']}</h1>
    <p>{p['lead']}</p>
  </div>
</section>
<section class="section"><div class="wrap article-grid"><article class="prose">{body}</article>{aside("Hi! I have a question about Rome Golf Cart Guide.")}</div></section>
</main>
""" + footer()

def not_found():
    return head("Page not found | Rome Golf Cart Guide", "This page doesn't exist.", "/404.html", "1586102724225-3503518c3b1c").replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"') + NAV + """
<main><section class="section"><div class="wrap prose">
<h1>This page doesn't exist</h1>
<p>The link may be old or mistyped. Here's where to go instead:</p>
<p><a class="btn btn-sky" href="/">See all golf cart tours</a></p>
</div></section></main>
""" + footer()

def home():
    h = open(os.path.join(ROOT, "src", "templates", "index.html")).read()
    h = re.sub(r"<style>.*?</style>", '<link rel="stylesheet" href="/assets/style.css?v=20261120">', h, flags=re.S)
    h = re.sub(r"<script>\s*/\* ===== Settings.*?</script>", '<script src="/assets/tours.js?v=20261106"></script>', h, flags=re.S)
    h = h.replace('<meta name="theme-color" content="#1f4fd1">', '<meta name="theme-color" content="#1f4fd1">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">')
    h = re.sub(r'<header class="bar">.*?</header>\n', NAV, h, flags=re.S)
    h = re.sub(r"<footer>.*</html>", footer().strip(), h, flags=re.S)
    # remove old fab (footer() already adds one)
    h = h.replace('<a class="fab js-wa"', '<a class="fab js-wa"', 1)
    # guides section before the FAQ
    cards = "".join(f'<a class="guide" href="/{p["slug"]}/"><img loading="lazy" src="{U(p["img"],600)}" alt="{html.escape(p["img_alt"])}" width="600" height="400"><b>{html.escape(p["h1"])}</b><span>{html.escape(p["lead"])}</span></a>' for p in PAGES)
    guides = f"""<section class="section" id="guides" style="padding-top:0">
  <div class="wrap">
    <h2>Guides to help you choose</h2>
    <p class="intro">Short, practical answers to the questions people ask before booking.</p>
    <div class="guides">{cards}</div>
  </div>
</section>

<section class="section" id="faq\""""
    h = h.replace('<section class="section" id="faq"', guides, 1)
    # seasonal strip (remove after 6 January 2027)
    h = h.replace('</section>', '</section>\n' + SEASON["en"], 1)
    # text links inside home content
    h = h.replace("<a href=\"#\" class=\"js-wa\" data-msg=\"Hi! I'm interested in a night golf cart tour in Rome. Date: … People: …\">Ask about night tours</a>", '<a href="/rome-night-golf-cart-tour/">Read the night tour guide</a>')
    h = h.replace("<a href=\"#\" class=\"js-wa\" data-msg=\"Hi! I'm interested in a golf cart tour to the Catacombs and Appian Way. Date: … People: …\">Ask about this tour</a>", '<a href="/catacombs-appian-way-golf-cart-tour/">Read the catacombs guide</a>')
    h = h.replace('<a href="#tours" data-quick="long">See full-day options</a>', '<a href="/civitavecchia-cruise-golf-cart-tour-rome/">Read the cruise guide</a>')
    return h

def write(rel, content):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(content)

home_html = home()
# drop duplicate fab: keep only last
if home_html.count('class="fab js-wa"') > 1:
    first = home_html.find('<a class="fab js-wa"')
    end = home_html.find('</a>', first) + 4
    home_html = home_html[:first] + home_html[end:]
write("index.html", home_html)
for p in PAGES:
    write(f'{p["slug"]}/index.html', guide(p))
write("about/index.html", about())
write("404.html", not_found())
shutil.copy(os.path.join(ROOT, "src", "templates", "privacy.html"), os.path.join(OUT, "privacy.html"))

import tourpages, intl
TOUR_URLS = tourpages.build(head, NAV, footer, U, SITE, write)
INTL_URLS, GROUPS = intl.build(dict(head=head, U=U, SITE=SITE, write=write, CART=CART, WA_ICON=WA_ICON, SEASON=SEASON))
# sitemap
LASTMOD = {f'/{p["slug"]}/': p["modified"] for p in PAGES if "modified" in p}
LASTMOD.update(intl.LASTMOD)
urls = ["/"] + [f'/{p["slug"]}/' for p in PAGES] + TOUR_URLS + INTL_URLS + ["/about/"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{SITE}{u}</loc><lastmod>{LASTMOD.get(u, UPDATED_ISO)}</lastmod></url>\n" for u in urls) + "</urlset>\n"
write("sitemap.xml", sm)

write("robots.txt", f"""User-agent: *
Allow: /

# AI search and assistants are welcome
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Bingbot
Allow: /

Sitemap: {SITE}/sitemap.xml
""")

llms = f"""# Rome Golf Cart Guide

> Independent comparison of golf cart tours in Rome, Italy: prices, duration, hotel pickup, private vs small-group, food, night, catacombs and cruise-port tours. Updated {UPDATED}.

Key facts:
- Golf cart tours in Rome usually last 2.5–3 hours (express 1.5 h, full day 6–8 h) and cover 6–8 major sights from outside, with photo stops.
- Prices: shared express from about $69 per person; shared classic about $100–150 per person; private about $81–230 per person or $400–800 per cart; cruise day trips from Civitavecchia from about €790 per group.
- Most private tours include pickup at hotels in the historic center (inside the Aurelian Walls). Shared tours start from a meeting point.
- Carts usually seat 5–7. A folded wheelchair takes about two seats. Some operators give free child seats for ages 2–12 and don't accept infants under 2.
- Tours stop outside monuments; entry tickets (Colosseum, Vatican) are not included.
- Personal help choosing a tour: WhatsApp +39 393 855 2086.

## Main page
- [Compare all golf cart tours in Rome]({SITE}/): filterable list with prices, duration, pickup and booking links

## Guides
""" + "".join(f'- [{p["h1"]}]({SITE}/{p["slug"]}/): {p["answer"]}\n' for p in PAGES) + f"""
## About
- [About and how we compare tours]({SITE}/about/)
"""
write("llms.txt", llms)

write("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="16" fill="#ffcb3d"/><g fill="none" stroke="#16181d" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M7 19h18M9.5 19v-6h13v6M11.5 13l1.6-4.5h5.8l1.6 4.5"/><circle cx="11.5" cy="22" r="2"/><circle cx="20.5" cy="22" r="2"/></g></svg>\n')

open(os.path.join(ROOT, "netlify.toml"), "w").write("""# Netlify reads this file from the repo root. The site is pre-built into /site by src/build.py.
[build]
  publish = "site"
  command = ""

[[redirects]]
  from = "https://www.romegolfcartguide.com/*"
  to = "https://romegolfcartguide.com/:splat"
  status = 301
  force = true

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=3600, must-revalidate"
""")
print("built", len(PAGES)+5, "pages")

write("f9bbe2b124ca40a0a1f067f7f63f2e9f.txt", "f9bbe2b124ca40a0a1f067f7f63f2e9f")

intl.finalize(OUT, SITE, GROUPS)
print("intl pages", len(INTL_URLS))
with open(os.path.join(OUT, "llms.txt"), "a") as f:
    f.write("\n## Other languages\n- [Español: tours en carrito de golf por Roma](https://romegolfcartguide.com/es/)\n- [Deutsch: Golfcart-Touren in Rom](https://romegolfcartguide.com/de/)\n")

# ---- cookie consent + GA4 on every page ----
_cj = os.path.join(OUT, "assets", "consent.js")
_c = open(_cj).read()
_c = re.sub(r"var GA_ID = '[^']*';", f"var GA_ID = '{GA_ID}';", _c, count=1)
open(_cj, "w").write(_c)
_tag = '<script src="/assets/consent.js?v=20261120" defer></script>'
for _root, _, _files in os.walk(OUT):
    for _f in _files:
        if _f.endswith(".html"):
            _p = os.path.join(_root, _f); _h = open(_p).read()
            if "consent.js" not in _h:
                _h = _h.replace("</body>", _tag + "\n</body>", 1)
                open(_p, "w").write(_h)

# ---- seasonal strip on the guides most related to Christmas ----
if SEASON_ON:
    for _lang, _paths in {"en": ["best-golf-cart-tours-rome", "rome-night-golf-cart-tour", "golf-cart-tour-rome-price"],
                          "es": ["es/mejores-tours-carrito-golf-roma", "es/roma-de-noche-carrito-golf", "es/precio-tour-carrito-golf-roma"],
                          "de": ["de/beste-golfcart-touren-rom", "de/rom-bei-nacht-golfcart", "de/golfcart-tour-rom-preise"]}.items():
        for _p in _paths:
            _f = os.path.join(OUT, _p, "index.html"); _h = open(_f).read()
            if 'class="season"' not in _h:
                _h = _h.replace('<section class="section">', SEASON[_lang] + '\n<section class="section">', 1)
                open(_f, "w").write(_h)

# ---- host-agnostic headers (Cloudflare Pages and Netlify both read /_headers) ----
write("_headers", """/assets/*
  Cache-Control: public, max-age=3600, must-revalidate
""")
