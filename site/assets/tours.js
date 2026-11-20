/* Rome Golf Cart Guide – tour data and listing */
const VIATOR_PID = 'P00328677';
const VIATOR_MCID = '42383';
const WHATSAPP_NUMBER = '393938552086';
const GYG_PARTNER = 'EQTZMZ9';

const IMG = id => 'https://images.unsplash.com/photo-' + id + '?auto=format&fit=crop&w=700&h=525&q=70';
const PAGE_LANG = (document.documentElement.lang || 'en').slice(0,2);
const LOC = {es:{viator:'es-ES/', gyg:'es-es', widget:'es-ES'}, de:{viator:'de-DE/', gyg:'de-de', widget:'de-DE'}}[PAGE_LANG] || null;
const viator = (path, id) => 'https://www.viator.com/' + (LOC ? LOC.viator : '') + path + '?pid=' + VIATOR_PID + '&mcid=' + VIATOR_MCID + '&medium=link&campaign=rgcg-' + id;
const gyg = (path, id) => 'https://www.getyourguide.com/' + (LOC ? LOC.gyg + '/-t' + (path.match(/-t(\d+)\/?$/)||[])[1] + '/' : path) + '?partner_id=' + GYG_PARTNER + '&utm_medium=online_publisher&cmp=rgcg-' + id;
const waLink = msg => 'https://wa.me/' + WHATSAPP_NUMBER + '?text=' + encodeURIComponent(msg);

/* type: private | group | both · price: lowest "from" price per person in USD (null = see live price)
   hours: used by filters · maxGroup: largest group the tour takes · wa: WhatsApp message instead of a Viator link */
const TOURS = [
  { id:'rolling-private', rank:1, badge:'Most reviewed',
    name:'Rome by Golf Cart: Private Tour', by:'Rolling Rome',
    type:'private', hours:3, dur:'2.5–3 h, or full day', price:107, pickup:true, treat:false, maxGroup:14, access:true,
    img:'1567613747183-fcc1e30a18eb', alt:'The Colosseum in Rome',
    text:'Pick the sights you care about, or let your guide plan the route. They collect you from your hotel in the center, and bigger families can book two carts (up to 14 people).',
    incl:['Hotel pickup','Your own route','Full-day option with lunch'], note:'Free cancellation 24 h',
    path:'tours/Rome/Rome-by-Golf-Cart-Private-Tour/d511-7377P1' },
  { id:'biga-express', rank:2, badge:'Lowest price',
    name:'Rome Express Golf Cart Tour', by:'Biga Tours',
    type:'group', hours:1.5, dur:'1.5 h', price:69, pickup:false, treat:false, maxGroup:14, kids:true,
    img:'1570054623147-dbccfd1efa98', alt:'The Pantheon in Rome',
    text:'The quickest way to see the headline sights: Pantheon, Trevi, Piazza Navona and the Colosseum from outside. Starts near the Pantheon. Free child seats for ages 2–12.',
    incl:['Max 7 per cart','Headsets','Water'], note:'Free cancellation',
    path:'tours/Rome/Golf-Cart-Driving-Tour-Rome-Express/d511-387632P6' },
  { id:'iteritaly-private', rank:3, badge:'Great for families',
    name:'Private Golf Cart Tour with Coffee & Gelato', by:'IterItaly',
    type:'private', hours:3, dur:'3 h', price:121, pickup:true, treat:true, maxGroup:6, kids:true,
    img:'1723248954986-5c24d9333f94', alt:'Gelato being served in a gelateria',
    text:'A relaxed private half-day with an English-speaking driver. Pickup at your central hotel and stops for an espresso and a gelato along the way.',
    incl:['Free hotel pickup','Coffee','Gelato'], note:'Free cancellation 24 h',
    path:'tours/Rome/Rome-Golf-Cart-Private-Tour/d511-65297P1' },
  { id:'key-sights', rank:4,
    name:'Rome Key Sights, with optional pasta tasting', by:'Private or small group',
    type:'both', hours:3, dur:'About 3 h', price:130, pickup:true, treat:true, maxGroup:7, food:true,
    img:'1569230516306-5a8cb5586399', alt:'Trattoria tables on a cobblestone street in Trastevere',
    text:'Choose a small group (max 7) or a private cart. The food option ends with three classic Roman pastas in a local trattoria. Hotel pickup available in the center.',
    incl:['Max 7 people','Pasta tasting option','Hotel pickup option'], note:'',
    path:'tours/Rome/Rome-Key-Sights-Golf-Cart-Tour/d511-450436P3' },
  { id:'city-center-private', rank:5,
    name:'Private Tour of the City Center', by:'Private tour',
    type:'private', hours:3, dur:'About 3 h', price:81, pickup:false, treat:false, maxGroup:6,
    img:'1661693800496-6a803cba5ff9', alt:'Fountain in Piazza Navona',
    text:'The most affordable way to get a cart to yourselves. Fully flexible: tell the guide what you want to see.',
    incl:['Private cart','Flexible route'], note:'Free cancellation 24 h',
    path:'tours/Rome/Golf-Cart-Tour-Private-Experience-of-Romes-City-Center/d511-133237P6' },
  { id:'four-hours', rank:6,
    name:'4-Hour Sightseeing Tour', by:'Private or group',
    type:'both', hours:4, dur:'3.5–4 h', price:106, pickup:true, treat:false, maxGroup:7,
    img:'1748189748849-bda21f8e1e43', alt:'St. Peter\'s Square from above',
    text:'More time to see more, including St. Peter\'s Square. Private with hotel pickup, or a cheaper 3.5-hour shared version from a meeting point.',
    incl:['Hotel pickup (private)','Includes Vatican area'], note:'',
    path:'tours/Rome/Rome-Private-Group-4-Hours-Golf-Cart-Sightseeing-Tour/d511-140194P1' },
  { id:'private-gelato', rank:7,
    name:'Private Highlights Tour with Gelato', by:'Private tour',
    type:'private', hours:3, dur:'About 3 h', price:null, pickup:false, treat:true, maxGroup:6,
    img:'1569397906655-7a1fce6866d2', alt:'The Trevi Fountain',
    text:'A storytelling tour: legends and gossip behind the Colosseum and Trevi, plus quiet back streets most visitors miss, and a gelato stop.',
    incl:['Private cart','Gelato'], note:'',
    path:'tours/Rome/Rome-Private-Highlights-Golf-Cart-Tour-with-Gelato/d511-349270P1' },
  { id:'pinnacle', rank:8,
    name:'Premium Private Golf Cart Tour', by:'Private tour',
    type:'private', hours:3, dur:'About 3 h', price:227, pickup:true, treat:false, maxGroup:6,
    img:'1462747772350-460bb4aad7f4', alt:'The Colosseum under a cloudy sky',
    text:'Hotel pickup included and a guide who stops wherever something catches your eye. A good pick for a special occasion.',
    incl:['Hotel pickup','Stop anywhere'], note:'',
    path:'tours/Rome/Rome-Golf-Cart-Tour-Discover-the-Pinnacle-Experience/d511-422323P2' },
  { id:'tailorable', rank:9,
    name:'Tailor-made Private Tour', by:'Private tour',
    type:'private', hours:3, dur:'About 3 h', price:null, pickup:false, treat:false, maxGroup:6,
    img:'1704841632993-148afae64231', alt:'Ruins of the Roman Forum',
    text:'Planned to avoid the busy roads, so only about an hour of the tour is spent driving and the rest at the sights.',
    incl:['Private cart','Less time in traffic'], note:'',
    path:'tours/Rome/Rome-Tailorable-Private-Golf-Cart-Tour/d511-450436P5' },
  /* ---- GetYourGuide ---- */
  { id:'gyg-vip-trevi', rank:2.5, badge:'4.8 · 858 reviews', src:'gyg',
    name:'VIP Golf Cart with Trevi Skip-the-Line, Gelato & Supplì', by:'Private tour',
    type:'private', hours:2.5, dur:'2–2.5 h', price:null, pickup:true, treat:true, maxGroup:6, kids:true,
    img:'1569397906655-7a1fce6866d2', alt:'The Trevi Fountain',
    text:'A private cart with skip-the-line access to the Trevi Fountain area, plus a gelato and a supplì, Rome\'s fried rice ball. One of the most reviewed golf cart tours on GetYourGuide.',
    incl:['Trevi skip-the-line','Gelato & supplì','Private cart'], note:'Rated 4.8/5 on GetYourGuide',
    gyg:'rome-l33/rome-private-sightseeing-tour-by-golf-cart-t618369/' },
  { id:'gyg-private-highlights', rank:3.5, badge:'4.9 · 250 reviews', src:'gyg',
    name:'Private Guided City Highlights Tour by Golf Cart', by:'Private tour',
    type:'private', hours:2.5, dur:'About 2–3 h', price:null, pickup:true, treat:false, maxGroup:6, access:true,
    img:'1661693800496-6a803cba5ff9', alt:'Fountain in Piazza Navona',
    text:'A private highlights tour with an English-speaking guide and pickup included. Very highly rated, and a good all-round choice for a first visit.',
    incl:['Pickup included','Private cart','Live guide'], note:'Rated 4.9/5 on GetYourGuide',
    gyg:'rome-l33/golf-cart-tour-of-rome-with-guide-t27124/' },
  { id:'gyg-trevi-group', rank:4.5, badge:'4.9 · 297 reviews', src:'gyg',
    name:'Rome by Golf Cart: Trevi Access, Gelato & Supplì', by:'Small group',
    type:'group', hours:2.5, dur:'2–2.5 h', price:null, pickup:false, treat:true, maxGroup:7, kids:true,
    img:'1723248954986-5c24d9333f94', alt:'Gelato being served in a gelateria',
    text:'The shared version of the Trevi tour: skip-the-line access at the fountain, gelato and supplì, at a lower price than going private.',
    incl:['Small group','Trevi skip-the-line','Gelato & supplì'], note:'Rated 4.9/5 on GetYourGuide',
    gyg:'rome-l33/rome-time-traveler-private-golf-cart-tour-t560865/' },
  { id:'gyg-private-local', rank:5.5, src:'gyg',
    name:'Private Golf Cart Tour: Highlights of the City', by:'Private tour',
    type:'private', hours:2.5, dur:'About 2–3 h', price:null, pickup:true, treat:false, maxGroup:6,
    img:'1462747772350-460bb4aad7f4', alt:'The Colosseum',
    text:'Private tour with a local guide in English or Italian and pickup included. Rated 4.9 out of 5 by 209 travellers on GetYourGuide.',
    incl:['Pickup included','English or Italian','Private cart'], note:'Rated 4.9/5 on GetYourGuide',
    gyg:'rome-l33/rome-golf-cart-tour-with-local-guide-t796792/' },
  { id:'gyg-express', rank:6.5, src:'gyg',
    name:'Golf Cart Tour: Express Highlights of Rome', by:'Private group',
    type:'private', hours:1.5, dur:'About 1–1.5 h', price:null, pickup:true, treat:false, maxGroup:6,
    img:'1570054623147-dbccfd1efa98', alt:'The Pantheon',
    text:'A short private loop of the headline sights with a live guide in English or Italian. Pickup available. Rated 4.6 out of 5 from 506 reviews.',
    incl:['Short tour','Pickup available','Live guide'], note:'Rated 4.6/5 on GetYourGuide',
    gyg:'rome-l33/golf-cart-tour-express-highlights-of-rome-t865494/' },
  { id:'gyg-night', rank:7.5, badge:'Night', src:'gyg',
    name:'Rome By Night Golf Cart Tour', by:'Private tour',
    type:'private', hours:2, dur:'2 h', price:null, pickup:true, treat:false, maxGroup:6, night:true, access:true,
    img:'1722312864179-d4c4c5ac05bb', alt:'The Colosseum lit up at night',
    text:'Two hours through Rome lit up after dark, private, with pickup included. Guides speak English, Italian, Spanish or German. Rated 4.9 out of 5 from 161 reviews.',
    incl:['Night','Pickup included','4 languages'], note:'Rated 4.9/5 on GetYourGuide',
    gyg:'rome-l33/rome-2-hour-golf-cart-sightseeing-tour-at-night-t403921/' },
  { id:'gyg-aperitivo', rank:8.5, src:'gyg',
    name:'Evening Golf Cart Tour with Drinks and Aperitivo', by:'Small group or private',
    type:'both', hours:3, dur:'3 h', price:null, pickup:false, treat:true, maxGroup:7, night:true, food:true,
    img:'1678970388666-e50b8006ab51', alt:'The Roman Forum lit up at night',
    text:'A sunset-to-evening tour that ends with an Italian aperitivo. Small group or private. Rated 4.8 out of 5 from 389 reviews.',
    incl:['Evening','Drinks & aperitivo','Small group or private'], note:'Rated 4.8/5 on GetYourGuide',
    gyg:'rome-l33/rome-evening-golf-cart-tour-with-drinks-t214599/' },
  { id:'gyg-catacombs-private', rank:9.5, src:'gyg',
    name:'Private Golf Cart Tour of the Appian Way & Catacombs', by:'Private tour',
    type:'private', hours:2.5, dur:'About 2–3 h', price:null, pickup:true, treat:false, maxGroup:6, catacombs:true,
    img:'1704841632993-148afae64231', alt:'Ancient Roman ruins',
    text:'A private cart out along the ancient Appian Way to the catacombs, with pickup included and a guide in English or Italian.',
    incl:['Catacombs','Appian Way','Pickup included'], note:'',
    gyg:'rome-l33/rome-private-golf-cart-tour-of-catacomb-ancient-appian-way-t853159/' },
  { id:'gyg-aqueducts', rank:9.6, src:'gyg',
    name:'Appian Way, Catacombs and Aqueducts Golf Cart Tour', by:'Small group (max 5)',
    type:'group', hours:4, dur:'4 h', price:null, pickup:false, treat:false, maxGroup:5, catacombs:true,
    img:'1748189748849-bda21f8e1e43', alt:'Ancient Rome',
    text:'A longer half-day out of the center: the Appian Way, a catacomb visit and the Roman aqueducts, in a small group of up to 5. Rated 4.8 out of 5.',
    incl:['Max 5 people','Catacombs','Aqueducts'], note:'Rated 4.8/5 on GetYourGuide',
    gyg:'rome-l33/rome-appian-way-catacombs-and-aqueducts-golf-cart-tour-t1187202/' },
  { id:'cruise', rank:11, badge:'Cruise passengers',
    name:'Cruise Day: Civitavecchia to Rome by Golf Cart', by:'Arranged by us with a local operator',
    type:'private', hours:8, dur:'About 8 h with transfers', price:null, priceText:'from €790 per group', pickup:true, treat:false, maxGroup:6, cruise:true,
    img:'1598275452245-bd4ee1a97694', alt:'Cruise ship in port',
    text:'Private transfer from the port, about 5 hours by golf cart around Rome, and back to the ship on time. Send us your ship and date.',
    incl:['Port pickup and return','Private cart','Timed to your ship'], note:'',
    wa:'Hi! I\'m arriving by cruise in Civitavecchia and want a golf cart tour of Rome. Ship and date: … People: …' },
  { id:'custom', rank:12,
    name:'Night, food or custom tour', by:'Arranged by us with a local operator',
    type:'private', hours:3, dur:'2–8 h, you choose', price:null, priceText:'quote in minutes', pickup:true, treat:true, maxGroup:20, night:true, food:true,
    img:'1678970388666-e50b8006ab51', alt:'The Roman Forum lit up at night',
    text:'A night tour, a food route through Trastevere, a guide who speaks Spanish, French or German, or several carts for a big group. Message us and we\'ll set it up.',
    incl:['Night tours','Other languages','Big groups'], note:'',
    wa:'Hi! I\'d like a custom golf cart tour in Rome (night / food / language / big group). Details: …' }
];

const LANGS = {
  'gyg-private-local':['English','Italian'], 'gyg-express':['English','Italian'], 'gyg-catacombs-private':['English','Italian'],
  'gyg-night':['English','Italian','Spanish','German'], 'cruise':['English','Italian'],
  'custom':['English','Italian','Spanish','German','French']
};
TOURS.forEach(t => { t.langs = LANGS[t.id] || ['English']; t.page = t.id !== 'custom' ? '/tour/' + t.id + '/' : null; });
const I18N = (window.RGCG_I18N || {})[PAGE_LANG] || null;
const UI = Object.assign({private:'Private cart', group:'Shared small group', both:'Private or shared', pickup:'Hotel pickup available', meeting:'Meeting point',
  from:'from', pp:'per person', price:'price', livePrice:"See today's price", book:'See dates & book', on:'on', ask:'Ask on WhatsApp',
  widgetTitle:'Photos and live ratings from GetYourGuide', widgetNote:'Real carts and current traveller ratings, updated automatically by GetYourGuide.',
  empty:null, langs:{}}, I18N ? I18N.ui : {});
if (I18N) TOURS.forEach(t => {
  const tr = I18N.tours[t.id] || {};
  Object.assign(t, tr);
  if (t.badge && I18N.badges[t.badge]) t.badge = I18N.badges[t.badge];
  if (t.by && I18N.by && I18N.by[t.by]) t.by = I18N.by[t.by];
  if (t.note && I18N.notes[t.note]) t.note = I18N.notes[t.note];
  if (t.note && /^Rated/.test(t.note)) t.note = '';
  if (t.badge && /reviews$/.test(t.badge)) t.badge = t.badge.replace('reviews', PAGE_LANG === 'es' ? 'reseñas' : 'Bewertungen');
  t.page = null;
});

/* Named lists used by guide pages: <div data-tours="private"></div> */
const LISTS = {
  all:      t => true,
  best:     t => ['gyg-private-highlights','gyg-vip-trevi','gyg-trevi-group','rolling-private','biga-express','gyg-night','gyg-aperitivo','gyg-aqueducts'].includes(t.id),
  private:  t => t.type !== 'group' && !t.cruise && !t.catacombs,
  pickup:   t => t.pickup && !t.cruise,
  treat:    t => t.treat,
  food:     t => t.treat || t.food,
  night:    t => t.night,
  catacombs:t => t.catacombs,
  cruise:   t => t.cruise || t.id === 'rolling-private',
  seniors:  t => t.pickup && t.type !== 'group' && !t.cruise,
  kids:     t => t.kids || (t.pickup && t.type === 'private' && !t.cruise),
  cheap:    t => t.price !== null && t.price < 110,
  classic:  t => t.hours >= 2 && t.hours <= 4 && !t.wa && !t.catacombs && !t.night
};

const ICON = {
  clock:'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
  pin:'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 21s7-6.3 7-12a7 7 0 0 0-14 0c0 5.7 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
  ppl:'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.6 3.4-5.5 6.5-5.5s5.7 1.9 6.5 5.5M16 4.8a3.5 3.5 0 0 1 0 6.4M18 14.8c1.8.7 3 2.4 3.5 5.2"/></svg>'
};

function tourRow(t){
  const isWa = !!t.wa;
  const href = isWa ? waLink(t.wa) : t.gyg ? gyg(t.gyg, t.id) : viator(t.path, t.id);
  const via = t.gyg ? 'GetYourGuide' : 'Viator';
  const kind = UI[t.type];
  const price = t.price !== null
    ? `<div class="price"><small>${UI.from}</small><strong>$${t.price}</strong><small>${UI.pp}</small></div>`
    : `<div class="price"><small>${UI.price}</small><strong style="font-size:1.2rem">${t.priceText || UI.livePrice}</strong></div>`;
  const btn = isWa
    ? `<a class="btn btn-wa" href="${href}" target="_blank" rel="noopener">${UI.ask}</a>`
    : `<a class="btn btn-sky" href="${href}" target="_blank" rel="sponsored nofollow noopener">${UI.book}</a><div class="via">${UI.on} ${via}</div>`;
  return `<article class="tour">
    <div class="ph"><img loading="lazy" width="700" height="525" src="${IMG(t.img)}" alt="${t.alt}">${t.badge ? `<span class="badge">${t.badge}</span>` : ''}</div>
    <div>
      <h3>${t.name}</h3>
      <div class="by">${t.by}</div>
      <ul class="facts">
        <li>${ICON.clock}${t.dur}</li>
        <li>${ICON.ppl}${kind}</li>
        <li>${ICON.pin}${t.pickup ? UI.pickup : UI.meeting}</li>
        <li class="lang">${t.langs.map(l => UI.langs[l] || l).join(', ')}</li>
      </ul>
      <p>${t.text}</p>
      <div class="incl">${t.incl.map(x => `<span>${x}</span>`).join('')}</div>
      ${t.page ? `<a class="more" href="${t.page}">Details and route map</a>` : ''}
    </div>
    <div class="side">${price}<div style="width:100%">${btn}${t.note ? `<div class="note" style="margin-top:8px">${t.note}</div>` : ''}</div></div>
  </article>`;
}

/* Static lists on guide pages */
document.querySelectorAll('[data-tours]').forEach(el => {
  const key = el.dataset.tours;
  const f = LISTS[key] || LISTS.all;
  const BEST = ['gyg-private-highlights','gyg-vip-trevi','gyg-trevi-group','rolling-private','biga-express','gyg-night','gyg-aperitivo','gyg-aqueducts'];
  const sorter = key === 'best' ? (a,b) => BEST.indexOf(a.id) - BEST.indexOf(b.id) : (a,b) => a.rank - b.rank;
  el.innerHTML = TOURS.filter(f).sort(sorter).slice(0, parseInt(el.dataset.limit || '8', 10)).map(tourRow).join('');
});

/* Interactive finder on the homepage */
const $ = s => document.querySelector(s);
if ($('#list')) {
  const chips = [...document.querySelectorAll('.chip')];
  const on = f => chips.find(c => c.dataset.f === f).getAttribute('aria-pressed') === 'true';
  const keep = t => {
    const people = Math.max(1, parseInt($('#f-people').value || '1', 10));
    const type = $('#f-type').value;
    if (type === 'private' && t.type === 'group') return false;
    if (type === 'group' && t.type === 'private') return false;
    if ($('#f-pickup').value === 'hotel' && !t.pickup) return false;
    if (people > t.maxGroup) return false;
    const lang = $('#f-lang') ? $('#f-lang').value : 'any';
    if (lang !== 'any' && !t.langs.includes(lang)) return false;
    if (on('short') && t.hours > 2) return false;
    if (on('classic') && (t.hours < 2.5 || t.hours > 3.5)) return false;
    if (on('long') && t.hours < 4) return false;
    if (on('treat') && !t.treat) return false;
    if (on('cheap') && (t.price === null || t.price >= 100)) return false;
    return true;
  };
  const render = () => {
    const s = $('#f-sort').value;
    const list = TOURS.filter(keep);
    if (s === 'price') list.sort((a,b) => (a.price ?? 9999) - (b.price ?? 9999));
    else if (s === 'dur') list.sort((a,b) => a.hours - b.hours);
    else list.sort((a,b) => a.rank - b.rank);
    $('#list').innerHTML = list.length ? list.map(tourRow).join('')
      : `<div class="empty">No tour matches all of these. Clear a filter, or <a href="${waLink('Hi! I could not find a matching golf cart tour. What I need: …')}" target="_blank" rel="noopener">tell us on WhatsApp</a>: we can often find a guide in your language or a bigger cart.</div>`;
    $('#count').textContent = list.length + (list.length === 1 ? ' tour' : ' tours');
  };
  const setChips = active => chips.forEach(c => c.setAttribute('aria-pressed', active.includes(c.dataset.f) ? 'true' : 'false'));
  const reset = () => { $('#f-people').value = 2; if ($('#f-lang')) $('#f-lang').value = 'any'; $('#f-type').value = 'all'; $('#f-pickup').value = 'any'; $('#f-sort').value = 'rec'; setChips([]); };
  const DUR = ['short','classic','long'];
  chips.forEach(c => c.addEventListener('click', () => {
    const pressed = c.getAttribute('aria-pressed') === 'true';
    if (DUR.includes(c.dataset.f)) chips.filter(x => DUR.includes(x.dataset.f)).forEach(x => x.setAttribute('aria-pressed','false'));
    c.setAttribute('aria-pressed', pressed ? 'false' : 'true');
    render();
  }));
  ['#f-people','#f-type','#f-pickup','#f-sort','#f-lang'].forEach(s => $(s) && $(s).addEventListener('change', render));
  $('#go').addEventListener('click', () => { render(); $('#tours').scrollIntoView(); });
  $('#reset').addEventListener('click', () => { reset(); render(); });
  const QUICK = {
    group:   () => { $('#f-type').value = 'group'; },
    private: () => { $('#f-type').value = 'private'; },
    treat:   () => setChips(['treat']),
    long:    () => setChips(['long']),
    first:   () => setChips(['classic']),
    family:  () => { $('#f-type').value = 'private'; $('#f-pickup').value = 'hotel'; $('#f-people').value = 4; },
    cheap:   () => setChips(['cheap'])
  };
  document.querySelectorAll('[data-quick]').forEach(el => el.addEventListener('click', e => {
    e.preventDefault(); reset(); QUICK[el.dataset.quick](); render(); $('#tours').scrollIntoView();
  }));
  render();
}

/* Official GetYourGuide widget: real photos and live ratings, tracked with our partner ID */
function gygWidget(container, tourIds, title, note){
  if (!tourIds.length) return;
  const box = document.createElement('div');
  box.className = 'gyg-wrap';
  box.innerHTML = (title ? `<h3>${title}</h3>` : '') + (note ? `<p>${note}</p>` : '') +
    `<div data-gyg-href="https://widget.getyourguide.com/default/activities.frame" data-gyg-locale-code="${LOC ? LOC.widget : 'en-US'}" data-gyg-widget="activities" data-gyg-number-of-items="${tourIds.length}" data-gyg-partner-id="${GYG_PARTNER}" data-gyg-tour-ids="${tourIds.join(',')}"></div>`;
  container.after(box);
}
const gygId = t => (t.gyg || '').match(/-t(\d+)\/?$/)?.[1];
document.querySelectorAll('[data-tours]').forEach(el => {
  if (el.dataset.nowidget) return;
  const ids = TOURS.filter(LISTS[el.dataset.tours] || LISTS.all).map(gygId).filter(Boolean).slice(0, 4);
  gygWidget(el, ids, UI.widgetTitle, UI.widgetNote);
});
const homeList = document.querySelector('#list');
if (homeList) gygWidget(homeList, ['618369','27124','560865','403921'], 'Real carts, real ratings', 'Photos and current traveller ratings from GetYourGuide, updated automatically.');
document.querySelectorAll('[data-gyg-ids]').forEach(el => gygWidget(el, el.dataset.gygIds.split(','), el.dataset.gygTitle || '', el.dataset.gygNote || ''));
if (document.querySelector('[data-gyg-widget]')) {
  const sc = document.createElement('script');
  sc.async = true; sc.defer = true;
  sc.src = 'https://widget.getyourguide.com/dist/pa.umd.production.min.js';
  sc.setAttribute('data-gyg-partner-id', GYG_PARTNER);
  document.body.appendChild(sc);
}

/* WhatsApp links and footer year */
document.querySelectorAll('.js-wa').forEach(a => { a.href = waLink(a.dataset.msg || 'Hi!'); a.target = '_blank'; a.rel = 'noopener'; });
document.querySelectorAll('.yr').forEach(e => e.textContent = new Date().getFullYear());
