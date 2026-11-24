# Builds Spanish and German sections, plus hreflang links and a language switcher on every page.
import html, json, os, re
import pages_es, pages_de

LANGS = [pages_es, pages_de]
V = "20261106"
LASTMOD = {}
_M = {"es": ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"],
      "de": ["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"]}
def local_date(iso, c):
    y, m, d = iso.split("-")
    return (f"Actualizado el {int(d)} de {_M['es'][int(m)-1]} de {y}" if c == "es"
            else f"Aktualisiert am {int(d)}. {_M['de'][int(m)-1]} {y}")

def nav(L, CART, WA_ICON):
    c = L["code"]
    return f"""<header class="bar">
  <div class="wrap">
    <a class="brand" href="/{c}/"><span class="brand-dot">{CART}</span>Rome Golf Cart Guide</a>
    <nav>
      <a href="/{c}/#tours">{L['nav_tours']}</a>
      <a href="/{c}/{L_SLUG(L,'best')}/">{L['nav_best']}</a>
      <a href="/{c}/{L_SLUG(L,'price')}/">{L['nav_price']}</a>
      <a class="phone js-wa" href="#" data-msg="{html.escape(L['wa_msg'])}">{WA_ICON}<span class="num-txt">+39 393 855 2086</span></a>
    </nav>
  </div>
</header>
"""

def L_SLUG(L, key):
    mod = pages_es if L["code"] == "es" else pages_de
    target = {"best": "best-golf-cart-tours-rome", "price": "golf-cart-tour-rome-price"}[key]
    return next(p["slug"] for p in mod.PAGES if p["en"] == target)

def footer(L, mod, WA_ICON):
    c = L["code"]
    links = "".join(f'<li><a href="/{c}/{p["slug"]}/">{html.escape(p["nav"])}</a></li>' for p in mod.PAGES)
    return f"""<footer>
  <div class="wrap cols">
    <div>
      <b>Rome Golf Cart Guide</b>
      <p>{html.escape(L['footer_about'])}</p>
      <p style="font-size:.85rem">{html.escape(L['footer_note'])}</p>
    </div>
    <div><b>{L['footer_guides']}</b><ul>{links}</ul></div>
    <div><b>{L['footer_info']}</b><ul><li><a href="/{c}/">{L['nav_tours']}</a></li><li><a href="/privacy.html">{L['footer_privacy']}</a></li><li><a href="#" class="js-wa" data-msg="{html.escape(L['wa_msg'])}">{L['footer_contact']}</a></li></ul></div>
  </div>
  <div class="wrap" style="margin-top:26px;font-size:.82rem">© <span class="yr"></span> RomeGolfCartGuide.com</div>
</footer>
<a class="fab js-wa" href="#" data-msg="{html.escape(L['wa_msg'])}" aria-label="WhatsApp">{WA_ICON.replace('width="18" height="18" ','')}</a>
<script src="/assets/i18n.js?v={V}"></script>
<script src="/assets/tours.js?v={V}"></script>
</body>
</html>
"""

def localize_head(h, L):
    h = h.replace('<html lang="en">', f'<html lang="{L["code"]}">')
    h = h.replace('<meta property="og:site_name"', f'<meta property="og:locale" content="{L["locale"]}">\n<meta property="og:site_name"')
    return h

def related(L, mod, slugs, U):
    by = {p["slug"]: p for p in mod.PAGES}
    return '<div class="related">' + "".join(
        f'<a href="/{L["code"]}/{s}/"><img loading="lazy" src="{U(by[s]["img"],200)}" alt="" width="72" height="56">{html.escape(by[s]["h1"])}</a>'
        for s in slugs if s in by) + "</div>"

def faq_html(faqs):
    return '<div class="faq">' + "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in faqs) + "</div>"

def guide(p, L, mod, ctx):
    head, U, SITE = ctx["head"], ctx["U"], ctx["SITE"]
    c = L["code"]
    path = f"/{c}/{p['slug']}/"
    dmod = p.get("modified", "2026-11-06")
    if "modified" in p:
        LASTMOD[path] = dmod
    lds = [
        {"@context":"https://schema.org","@type":"Article","headline":p["h1"],"description":p["desc"],"inLanguage":c,
         "image":U(p["img"],1200),"dateModified":dmod,"datePublished":"2026-11-06",
         "author":{"@type":"Organization","name":"Rome Golf Cart Guide","url":SITE+"/about/"},
         "publisher":{"@type":"Organization","name":"Rome Golf Cart Guide","url":SITE+"/"},"mainEntityOfPage":SITE+path},
        {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":L["crumbs_home"],"item":SITE+f"/{c}/"},
            {"@type":"ListItem","position":2,"name":p["nav"],"item":SITE+path}]},
        {"@context":"https://schema.org","@type":"FAQPage","inLanguage":c,"mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in p["faqs"]]},
    ]
    h = localize_head(head(p["title"], p["desc"], path, p["img"], lds), L)
    return h + nav(L, ctx["CART"], ctx["WA_ICON"]) + f"""
<main>
<section class="pagehead">
  <img class="bg" src="{U(p['img'])}" alt="{html.escape(p['img_alt'])}" fetchpriority="high">
  <div class="wrap">
    <div class="crumbs"><a href="/{c}/">{L['crumbs_home']}</a> / {html.escape(p['nav'])}</div>
    <h1>{html.escape(p['h1'])}</h1>
    <p>{html.escape(p['lead'])}</p>
  </div>
</section>
<section class="section">
  <div class="wrap article-grid">
    <article class="prose">
      <p class="updated">{local_date(dmod, c) if "modified" in p else L['updated']}</p>
      <div class="answer"><b>{L['quick']}</b><p>{html.escape(p['answer'])}</p></div>
      {p['body']}
    </article>
    <aside class="aside">
      <h3>{L['aside_h']}</h3>
      <p>{L['aside_p']}</p>
      <a class="btn btn-wa js-wa" href="#" data-msg="{html.escape(L['wa_msg'])}">{L['aside_wa']}</a>
      <a class="btn btn-line" href="/{c}/#tours">{L['aside_all']}</a>
    </aside>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2>{L['fits_h']}</h2>
    {('<div data-gyg-ids="' + p['gyg_ids'] + '" data-gyg-title="" data-gyg-note=""></div>') if p.get('gyg_ids') else ('<div class="tourlist-wrap" data-tours="' + p['tours'] + '"></div>')}
    <p class="disclose">{html.escape(L['disclose'])}</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2>{L['faq_h']}</h2>
    {faq_html(p['faqs'])}
    <h2 style="margin-top:56px">{L['related_h']}</h2>
    {related(L, mod, p['related'], U)}
  </div>
</section>
</main>
""" + footer(L, mod, ctx["WA_ICON"])

def home(L, mod, ctx):
    head, U, SITE = ctx["head"], ctx["U"], ctx["SITE"]
    c = L["code"]
    path = f"/{c}/"
    lds = [{"@context":"https://schema.org","@type":"FAQPage","inLanguage":c,"mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in L["home_faqs"]]}]
    h = localize_head(head(L["home_title"], L["home_desc"], path, "1586102724225-3503518c3b1c", lds), L)
    points = "".join(f'<span><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>{html.escape(x)}</span>' for x in L["home_points"])
    cards = "".join(f'<a class="guide" href="/{c}/{p["slug"]}/"><img loading="lazy" src="{U(p["img"],600)}" alt="{html.escape(p["img_alt"])}" width="600" height="400"><b>{html.escape(p["h1"])}</b><span>{html.escape(p["lead"])}</span></a>' for p in mod.PAGES)
    return h + nav(L, ctx["CART"], ctx["WA_ICON"]) + f"""
<main>
<section class="hero">
  <img class="bg" src="{U('1586102724225-3503518c3b1c', 2000)}" alt="Trastevere, Roma" fetchpriority="high">
  <div class="wrap" style="padding-bottom:70px">
    <h1>{html.escape(L['home_h1'])}</h1>
    <p>{html.escape(L['home_lead'])}</p>
  </div>
</section>
{ctx.get("SEASON", {}).get(c, "")}
<section class="section" id="tours">
  <div class="wrap">
    <div class="points" style="margin:0 0 26px">{points}</div>
    <h2>{html.escape(L['tours_h'])}</h2>
    <p class="intro">{html.escape(L['tours_intro'])}</p>
    <div class="tourlist-wrap" data-tours="all" data-limit="20"></div>
    <p class="disclose">{html.escape(L['disclose'])}</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2>{html.escape(L['guides_h'])}</h2>
    <div class="guides">{cards}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2>{html.escape(L['faq_h'])}</h2>
    {faq_html(L['home_faqs'])}
  </div>
</section>
<section style="padding:0">
  <div class="wrap">
    <div class="help">
      <div class="txt">
        <h2>{html.escape(L['help_h'])}</h2>
        <p>{html.escape(L['help_p'])}</p>
        <a class="btn btn-wa js-wa" href="#" data-msg="{html.escape(L['wa_msg'])}">WhatsApp</a>
        <span class="num">+39 393 855 2086</span>
      </div>
      <img loading="lazy" src="{U('1569230516306-5a8cb5586399',1000)}" alt="Trastevere">
    </div>
  </div>
</section>
</main>
""" + footer(L, mod, ctx["WA_ICON"])

def build(ctx):
    write = ctx["write"]
    urls = []
    groups = {"/": {"en": "/"}}
    for mod in LANGS:
        L = mod.LANG
        c = L["code"]
        write(f"{c}/index.html", home(L, mod, ctx))
        urls.append(f"/{c}/")
        groups["/"][c] = f"/{c}/"
        for p in mod.PAGES:
            write(f"{c}/{p['slug']}/index.html", guide(p, L, mod, ctx))
            urls.append(f"/{c}/{p['slug']}/")
            g = groups.setdefault(f"/{p['en']}/", {"en": f"/{p['en']}/"})
            g[c] = f"/{c}/{p['slug']}/"
    return urls, groups

SWITCH_CSS = """
.langs{display:flex;gap:2px;margin-left:18px}
.langs a{margin:0!important;padding:4px 7px;border-radius:6px;font-size:.82rem!important;font-weight:700!important;color:var(--slate)!important}
.langs a[aria-current]{background:var(--ink);color:#fff!important}
@media(max-width:820px){.bar nav .langs a{display:inline-block!important}}
"""

def finalize(out, SITE, groups):
    """Add hreflang links and the language switcher to every HTML page."""
    by_path = {}
    for g in groups.values():
        for lang, path in g.items():
            by_path[path] = g
    for root, _, files in os.walk(out):
        for f in files:
            if not f.endswith(".html") or f == "404.html":
                continue
            fp = os.path.join(root, f)
            rel = "/" + os.path.relpath(fp, out).replace("index.html", "")
            h = open(fp).read()
            m = re.search(r'<html lang="(\w+)"', h)
            cur = m.group(1) if m else "en"
            g = by_path.get(rel)
            if g:
                alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{p}">\n' for l, p in g.items())
                alt += f'<link rel="alternate" hreflang="x-default" href="{SITE}{g["en"]}">\n'
                h = h.replace("</head>", alt + "</head>", 1)
            homes = groups["/"]
            target = lambda l: (g or {}).get(l) or homes[l]
            CUR = ' aria-current="true"'
            sw = '<span class="langs">' + "".join(
                f'<a href="{target(l)}" hreflang="{l}"{CUR if l == cur else ""}>{l.upper()}</a>' for l in ("en","es","de")) + '</span>'
            h = h.replace('<a class="phone js-wa"', sw + '<a class="phone js-wa"', 1)
            open(fp, "w").write(h)
