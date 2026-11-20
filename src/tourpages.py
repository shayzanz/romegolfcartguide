# Builds /tour/<id>/ pages from the TOURS data in assets/tours.js
import json, subprocess, html, os

def load_tours():
    js = r"""
const fs=require('fs'), vm=require('vm');
const code=fs.readFileSync(process.argv[1],'utf8');
const stub={documentElement:{lang:'en'},querySelectorAll:()=>[],querySelector:()=>null,createElement:()=>({setAttribute(){}}),body:{appendChild(){}}};
const ctx={document:stub, console, window:{}};
vm.runInNewContext(code+';this.__T=TOURS;', ctx);
process.stdout.write(JSON.stringify(ctx.__T));
"""
    return json.loads(subprocess.check_output(["node", "-e", js, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "assets", "tours.js")]))

# Indicative stops (name, lat, lng, note)
P = {
 'colosseum':  ("Colosseum", 41.8902, 12.4922, "Photo stop and the story of the gladiator games."),
 'circus':     ("Circus Maximus", 41.8861, 12.4851, "The ancient chariot track below the Palatine Hill."),
 'aventine':   ("Aventine Hill keyhole", 41.8833, 12.4797, "The famous keyhole view of St. Peter's dome and the Orange Garden."),
 'truth':      ("Mouth of Truth", 41.8881, 12.4814, "The marble mask from the film Roman Holiday."),
 'marcellus':  ("Theatre of Marcellus", 41.8919, 12.4799, "Older than the Colosseum, in the Jewish Ghetto."),
 'venezia':    ("Piazza Venezia", 41.8958, 12.4826, "The white Vittoriano monument."),
 'campidoglio':("Capitoline Hill", 41.8933, 12.4828, "View over the Roman Forum."),
 'pantheon':   ("Pantheon", 41.8986, 12.4769, "Usually a short walk in: carts can't reach the door."),
 'navona':     ("Piazza Navona", 41.8992, 12.4731, "Bernini's Four Rivers fountain."),
 'trevi':      ("Trevi Fountain", 41.9009, 12.4833, "Time to throw your coin."),
 'spanish':    ("Spanish Steps", 41.9060, 12.4828, "Many tours end here or at your hotel."),
 'popolo':     ("Piazza del Popolo", 41.9107, 12.4763, "The twin churches and the obelisk."),
 'borghese':   ("Villa Borghese", 41.9128, 12.4852, "Rome's central park and the Pincio terrace."),
 'stpeter':    ("St. Peter's Square", 41.9022, 12.4567, "Bernini's colonnade and the basilica, from outside."),
 'castel':     ("Castel Sant'Angelo", 41.9031, 12.4663, "Hadrian's tomb on the Tiber."),
 'gianicolo':  ("Gianicolo Hill", 41.8916, 12.4614, "The best free view over Rome's rooftops."),
 'trastevere': ("Trastevere", 41.8897, 12.4703, "Ivy-covered lanes and trattorias."),
 'monterone':  ("Start near the Pantheon", 41.8975, 12.4755, "Meeting point in the center (Via Monterone)."),
 'caracalla':  ("Baths of Caracalla", 41.8791, 12.4924, "Huge ruins of Roman public baths."),
 'sebastiano': ("Porta San Sebastiano", 41.8735, 12.5015, "The gate where the Appian Way begins."),
 'appia':      ("Appian Way", 41.8668, 12.5027, "Original Roman paving stones, tombs and pines."),
 'callixtus':  ("Catacombs", 41.8590, 12.5115, "Guided visit underground."),
 'aqueducts':  ("Park of the Aqueducts", 41.8530, 12.5600, "Giant arches of the Roman aqueducts."),
}
R = {
 'classic':  ['colosseum','circus','aventine','truth','marcellus','venezia','pantheon','navona','trevi','spanish'],
 'express':  ['monterone','pantheon','navona','trevi','venezia','colosseum'],
 'vatican':  ['colosseum','circus','venezia','pantheon','navona','castel','stpeter','trevi','spanish'],
 'trevi':    ['popolo','spanish','trevi','pantheon','navona','venezia','colosseum'],
 'night':    ['colosseum','campidoglio','venezia','trevi','pantheon','navona','castel','stpeter'],
 'evening':  ['gianicolo','trastevere','navona','pantheon','trevi','venezia','colosseum'],
 'food':     ['colosseum','circus','aventine','venezia','pantheon','navona','trevi','trastevere'],
 'catacombs':['colosseum','circus','caracalla','sebastiano','appia','callixtus'],
 'aqueducts':['colosseum','caracalla','sebastiano','appia','callixtus','aqueducts'],
 'borghese': ['popolo','borghese','spanish','trevi','pantheon','navona','venezia','colosseum'],
}
ROUTE_FOR = {
 'rolling-private':'classic','biga-express':'express','iteritaly-private':'classic','key-sights':'food',
 'city-center-private':'classic','four-hours':'vatican','private-gelato':'classic','pinnacle':'borghese',
 'tailorable':'classic','gyg-vip-trevi':'trevi','gyg-private-highlights':'classic','gyg-trevi-group':'trevi',
 'gyg-private-local':'classic','gyg-express':'express','gyg-night':'night','gyg-aperitivo':'evening',
 'gyg-catacombs-private':'catacombs','gyg-aqueducts':'aqueducts','cruise':'classic',
}
EXTRA = {
 'cruise': "<p>The day starts with a private transfer from Civitavecchia port (about 80 km, 1–1.5 hours each way). The map shows the part of the day spent by golf cart in Rome.</p>",
 'biga-express': "<p>The tour starts from the operator's office near the Pantheon and ends outside the Colosseum. Carts seat 7 and a tour runs with up to two carts.</p>",
 'rolling-private': "<p>Because it's private, the route is yours to change: tell the guide which sights matter most. Half-day tours usually cover 6–8 sights; the full-day version covers roughly twice as many with a lunch break.</p>",
}

def gyg_id(t):
    import re
    m = re.search(r"-t(\d+)/?$", t.get('gyg') or '')
    return m.group(1) if m else None

def link(t):
    if t.get('wa'):
        return None
    if t.get('gyg'):
        return f"https://www.getyourguide.com/{t['gyg']}?partner_id=EQTZMZ9&utm_medium=online_publisher&cmp=rgcg-{t['id']}-page"
    return f"https://www.viator.com/{t['path']}?pid=P00328677&mcid=42383&medium=link&campaign=rgcg-{t['id']}-page"

def build(head, NAV, footer, U, SITE, write):
    tours = load_tours()
    by = {t['id']: t for t in tours}
    urls = []
    for t in tours:
        if t['id'] == 'custom':
            continue
        route = ROUTE_FOR.get(t['id'], 'classic')
        stops = [P[k] for k in R[route]]
        kind = {'private':'Private cart','group':'Shared small group','both':'Private or shared'}[t['type']]
        via = 'GetYourGuide' if t.get('gyg') else 'Viator'
        href = link(t)
        if href:
            cta = f'<a class="btn btn-sky" href="{href}" target="_blank" rel="sponsored nofollow noopener">See dates &amp; book</a><div class="via">on {via}, free cancellation on most dates</div>'
        else:
            msg = html.escape(t['wa'])
            cta = f'<a class="btn btn-wa js-wa" href="#" data-msg="{msg}">Ask on WhatsApp</a><div class="via">We check availability with local operators</div>'
        price = f"<small>from</small><strong>${t['price']}</strong><small>per person</small>" if t.get('price') else f"<small>price</small><strong style='font-size:1.3rem'>{html.escape(t.get('priceText') or 'See today’s price')}</strong>"
        gid = gyg_id(t)
        # similar tours for the widget
        if gid:
            wid, wtitle = [gid], "Photos and live rating from GetYourGuide"
        else:
            sim = [x for x in tours if x.get('gyg') and x['id'] != t['id'] and (x['type'] == t['type'] or t['type']=='both')]
            wid, wtitle = [gyg_id(x) for x in sim[:3]], "Similar tours with photos and live ratings"
        stops_html = "".join(f"<li><b>{html.escape(n)}</b><span>{html.escape(d)}</span></li>" for n,_,_,d in stops)
        pts = json.dumps([[la, ln, n] for n,la,ln,_ in stops])
        others = [x for x in tours if x['id'] != t['id'] and x['id'] != 'custom' and (x['type'] == t['type'])][:4]
        rel = "".join(f'<a href="/tour/{x["id"]}/"><img loading="lazy" src="{U(x["img"],200)}" alt="" width="72" height="56">{html.escape(x["name"])}</a>' for x in others)
        path = f"/tour/{t['id']}/"
        urls.append(path)
        title = f"{t['name']} – Route, Price & Details | Rome Golf Cart Guide"
        desc = f"{t['name']}: {t['dur']}, {kind.lower()}, {'hotel pickup available' if t['pickup'] else 'meeting point in the center'}. See the indicative route on a map, what's included and how to book."
        ld = [{"@context":"https://schema.org","@type":"TouristTrip","name":t['name'],"description":t['text'],
               "touristType":kind,"image":U(t['img'],1200),
               "itinerary":{"@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"TouristAttraction","name":n,"geo":{"@type":"GeoCoordinates","latitude":la,"longitude":ln}}} for i,(n,la,ln,_) in enumerate(stops)]},
               **({"offers":{"@type":"Offer","price":t['price'],"priceCurrency":"USD","url":href}} if t.get('price') and href else {})},
              {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
                {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
                {"@type":"ListItem","position":2,"name":"Tours","item":SITE+"/#tours"},
                {"@type":"ListItem","position":3,"name":t['name'],"item":SITE+path}]}]
        page = head(title, desc, path, t['img'], ld).replace('</head>', '<link rel="stylesheet" href="/assets/leaflet/leaflet.css">\n</head>') + NAV + f"""
<main>
<section class="pagehead">
  <img class="bg" src="{U(t['img'])}" alt="{html.escape(t['alt'])}" fetchpriority="high">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> / <a href="/#tours">Tours</a> / {html.escape(t['by'])}</div>
    <h1>{html.escape(t['name'])}</h1>
    <p>{html.escape(t['dur'])} · {kind} · {'Hotel pickup available' if t['pickup'] else 'Meeting point in the center'}</p>
  </div>
</section>
<section class="section">
  <div class="wrap tour-hero">
    <article class="prose">
      <h2 style="margin-top:0">About this tour</h2>
      <p>{html.escape(t['text'])}</p>
      {EXTRA.get(t['id'],'')}
      <div class="incl" style="margin:14px 0 6px">{''.join(f'<span>{html.escape(x)}</span>' for x in t['incl'])}</div>
      <h2>Indicative route</h2>
      <p class="mapnote">Stops and order change with traffic, closures and, on private tours, your wishes. This is the typical route for this kind of tour, not a fixed itinerary.</p>
      <div id="map" role="img" aria-label="Map of the indicative route through Rome"></div>
      <ol class="stops">{stops_html}</ol>
      <div data-gyg-ids="{','.join(wid)}" data-gyg-title="{wtitle}" data-gyg-note="Updated automatically by GetYourGuide."></div>
      <h2>Good to know</h2>
      <ul>
        <li>Tours stop outside the monuments; entry tickets are not included unless listed.</li>
        <li>{'Add your hotel name and address when booking, ideally 24 hours ahead.' if t['pickup'] else 'You meet the guide at a central meeting point, shown in your booking confirmation.'}</li>
        <li>Tell the operator about children's ages or a wheelchair when you book.</li>
        <li>Tips are not included and are up to you.</li>
      </ul>
    </article>
    <aside class="bookbox">
      <div class="price">{price}</div>
      {cta}
      <ul>
        <li><span>Duration</span><b>{html.escape(t['dur'])}</b></li>
        <li><span>Type</span><b>{kind}</b></li>
        <li><span>Group size</span><b>Up to {t['maxGroup']}</b></li>
        <li><span>Pickup</span><b>{'Hotel, center' if t['pickup'] else 'Meeting point'}</b></li>
        <li><span>Language</span><b>{', '.join(t['langs'])}</b></li>
      </ul>
      <a class="btn btn-line js-wa" href="#" data-msg="Hi! I have a question about the tour: {html.escape(t['name'])}">Question? Ask on WhatsApp</a>
    </aside>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <h2>Similar tours</h2>
    <div class="related">{rel}</div>
    <p class="disclose">We earn a small commission when you book through our links, at no extra cost to you. Map data © OpenStreetMap contributors.</p>
  </div>
</section>
</main>
<script src="/assets/leaflet/leaflet.js"></script>
<script>
(function(){{
  var pts = {pts};
  if (!window.L) return;
  var map = L.map('map', {{scrollWheelZoom:false}});
  L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{maxZoom:18, attribution:'&copy; OpenStreetMap contributors'}}).addTo(map);
  var line = L.polyline(pts.map(function(p){{return [p[0],p[1]];}}), {{color:'#1f4fd1', weight:4, opacity:.8, dashArray:'8 8'}}).addTo(map);
  pts.forEach(function(p,i){{
    L.marker([p[0],p[1]], {{icon:L.divIcon({{className:'pin', html:String(i+1), iconSize:[26,26]}})}}).addTo(map).bindPopup('<b>'+(i+1)+'. '+p[2]+'</b>');
  }});
  map.fitBounds(line.getBounds(), {{padding:[30,30]}});
}})();
</script>
""" + footer()
        write(f"tour/{t['id']}/index.html", page)
    return urls
