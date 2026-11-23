/* "Find your tour in 3 questions": small button that appears after some scrolling.
   The quiz opens only on click (never automatically). Uses TOURS, UI, viator(), gyg(), waLink() from tours.js. */
(function () {
  if (typeof TOURS === 'undefined') return;
  var lang = (document.documentElement.lang || 'en').slice(0, 2);
  var T = {
    en: {
      btn: 'Find your tour in 3 questions', title: 'Find your golf cart tour', step: 'Question {n} of 3', close: 'Close', back: 'Back', again: 'Start again',
      q1: 'How many of you are going?', a1: ['1–2', '3–4', '5–6', '7 or more'],
      q2: 'What would you like most?', a2: ['The classic sights', 'Food and gelato stops', 'Rome lit up at night', 'Catacombs and the Appian Way'],
      q3: 'What matters most to you?', a3: ['Hotel pickup, little walking', 'Travelling with children', 'The best price'],
      res: 'Our picks for you', none: 'No tour matches everything. Write to us on WhatsApp and we’ll find one for you.',
      book: 'See dates & book', ask: 'Ask on WhatsApp', on: 'on', from: 'from', pp: 'pp', live: 'see price', details: 'Details',
      big: 'For 7 or more people, a private tour with two carts or a bigger vehicle works best. Ask us and we’ll arrange it.',
      wa: 'Hi! I used the tour finder on RomeGolfCartGuide. We are {p} people and would like: {i}. Can you help?'
    },
    es: {
      btn: 'Encuentra tu tour en 3 preguntas', title: 'Encuentra tu tour en carrito de golf', step: 'Pregunta {n} de 3', close: 'Cerrar', back: 'Atrás', again: 'Empezar de nuevo',
      q1: '¿Cuántos sois?', a1: ['1–2', '3–4', '5–6', '7 o más'],
      q2: '¿Qué os apetece más?', a2: ['Los monumentos clásicos', 'Paradas con comida y helado', 'Roma iluminada de noche', 'Catacumbas y Vía Apia'],
      q3: '¿Qué es lo más importante?', a3: ['Recogida en el hotel, caminar poco', 'Viajamos con niños', 'El mejor precio'],
      res: 'Nuestra selección para vosotros', none: 'Ningún tour cumple todo. Escríbenos por WhatsApp y te buscamos uno.',
      book: 'Ver fechas y reservar', ask: 'Preguntar por WhatsApp', on: 'en', from: 'desde', pp: 'p.p.', live: 'ver precio', details: 'Detalles',
      big: 'Para 7 personas o más, lo mejor es un tour privado con dos carritos o un vehículo más grande. Escríbenos y lo organizamos.',
      wa: '¡Hola! He usado el buscador de RomeGolfCartGuide. Somos {p} personas y nos gustaría: {i}. ¿Nos ayudáis?'
    },
    de: {
      btn: 'Deine Tour in 3 Fragen finden', title: 'Finde deine Golfcart-Tour', step: 'Frage {n} von 3', close: 'Schließen', back: 'Zurück', again: 'Neu starten',
      q1: 'Wie viele Personen seid ihr?', a1: ['1–2', '3–4', '5–6', '7 oder mehr'],
      q2: 'Was interessiert euch am meisten?', a2: ['Die klassischen Sehenswürdigkeiten', 'Stopps mit Essen und Eis', 'Rom bei Nacht', 'Katakomben und Via Appia'],
      q3: 'Was ist euch am wichtigsten?', a3: ['Abholung am Hotel, wenig laufen', 'Wir reisen mit Kindern', 'Der beste Preis'],
      res: 'Unsere Empfehlungen für euch', none: 'Keine Tour passt zu allem. Schreib uns auf WhatsApp, wir finden eine.',
      book: 'Termine & buchen', ask: 'Auf WhatsApp fragen', on: 'auf', from: 'ab', pp: 'p. P.', live: 'Preis ansehen', details: 'Details',
      big: 'Für 7 oder mehr Personen passt eine private Tour mit zwei Carts oder einem größeren Fahrzeug am besten. Schreib uns, wir organisieren das.',
      wa: 'Hallo! Ich habe den Tour-Finder von RomeGolfCartGuide benutzt. Wir sind {p} Personen und möchten: {i}. Könnt ihr helfen?'
    }
  }[lang] || null;
  if (!T) return;

  var track = function (name, params) { if (window.rgcgTrack) window.rgcgTrack(name, params || {}); };
  var PEOPLE = [2, 4, 6, 8];
  var INTEREST = ['classic', 'food', 'night', 'catacombs'];
  var NEED = ['pickup', 'kids', 'price'];
  var ans = [];

  function pick() {
    var people = PEOPLE[ans[0]], interest = INTEREST[ans[1]], need = NEED[ans[2]];
    var list = TOURS.filter(function (t) {
      if (t.wa) return false;
      if (people > (t.maxGroup || 6)) return false;
      if (interest === 'night' && !t.night) return false;
      if (interest === 'catacombs' && !t.catacombs) return false;
      if (interest === 'food' && !(t.food || t.treat)) return false;
      if (interest === 'classic' && (t.night || t.catacombs || t.cruise)) return false;
      if (need === 'pickup' && !t.pickup) return false;
      return true;
    });
    var score = function (t) {
      var s = t.rank || 10;
      if (need === 'kids' && t.kids) s -= 3;
      if (need === 'pickup' && t.type !== 'group') s -= 2;
      if (need === 'price') s += (t.price === null ? 4 : t.price / 40);
      return s;
    };
    list.sort(function (a, b) { return score(a) - score(b); });
    return list.slice(0, 3);
  }

  function href(t) { return t.gyg ? gyg(t.gyg, t.id + '-q') : viator(t.path, t.id + '-q'); }

  function card(t) {
    var price = t.price !== null ? T.from + ' <b>$' + t.price + '</b> ' + T.pp : T.live;
    return '<div class="qz-tour"><div><b>' + t.name + '</b><span>' + t.by + ' · ' + t.dur + ' · ' + price + '</span>' +
      (t.page && lang === 'en' ? '<a class="qz-more" href="' + t.page + '">' + T.details + '</a>' : '') + '</div>' +
      '<a class="btn btn-sky" data-src="quiz" href="' + href(t) + '" target="_blank" rel="sponsored nofollow noopener">' + T.book + '</a>' +
      '<small>' + T.on + ' ' + (t.gyg ? 'GetYourGuide' : 'Viator') + '</small></div>';
  }

  var box, fab;
  function render() {
    var n = ans.length, html = '';
    if (n < 3) {
      var q = [T.q1, T.q2, T.q3][n], a = [T.a1, T.a2, T.a3][n];
      html = '<p class="qz-step">' + T.step.replace('{n}', n + 1) + '</p><h3>' + q + '</h3><div class="qz-opts">' +
        a.map(function (x, i) { return '<button type="button" data-i="' + i + '">' + x + '</button>'; }).join('') + '</div>' +
        (n ? '<button type="button" class="qz-back">' + T.back + '</button>' : '');
    } else {
      var res = pick();
      var waMsg = T.wa.replace('{p}', T.a1[ans[0]]).replace('{i}', T.a2[ans[1]] + ', ' + T.a3[ans[2]]);
      var wa = '<a class="btn btn-wa" data-src="quiz" href="' + waLink(waMsg) + '" target="_blank" rel="noopener">' + T.ask + '</a>';
      html = '<h3>' + T.res + '</h3>' + (ans[0] === 3 ? '<p>' + T.big + '</p>' + wa : '') +
        (res.length ? res.map(card).join('') : '<p>' + T.none + '</p>' + wa) +
        '<button type="button" class="qz-back qz-again">' + T.again + '</button>';
      track('quiz_complete', { people: T.a1[ans[0]], interest: INTEREST[ans[1]], need: NEED[ans[2]], results: res.map(function (t) { return t.id; }).join(',') });
    }
    box.querySelector('.qz-body').innerHTML = html;
    box.querySelectorAll('.qz-opts button').forEach(function (b) {
      b.onclick = function () { ans.push(+b.dataset.i); render(); };
    });
    var back = box.querySelector('.qz-back');
    if (back) back.onclick = function () { if (back.classList.contains('qz-again')) ans = []; else ans.pop(); render(); };
  }

  function open() {
    if (!box) {
      box = document.createElement('div');
      box.className = 'qz'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-label', T.title);
      box.innerHTML = '<div class="qz-head"><b>' + T.title + '</b><button type="button" class="qz-x" aria-label="' + T.close + '">×</button></div><div class="qz-body"></div>';
      document.body.appendChild(box);
      box.querySelector('.qz-x').onclick = close;
    }
    ans = []; render();
    box.classList.add('on'); fab.classList.add('hide');
    track('quiz_open', { page_path: location.pathname });
  }
  function close() { box.classList.remove('on'); fab.classList.remove('hide'); }

  var css = '.qz-fab{position:fixed;left:16px;bottom:18px;z-index:90;background:#16181d;color:#fff;border:0;border-radius:999px;padding:12px 18px;font:700 15px Figtree,system-ui,sans-serif;box-shadow:0 8px 24px rgba(0,0,0,.2);cursor:pointer;opacity:0;transform:translateY(16px);pointer-events:none;transition:.25s}' +
    '.qz-fab.show{opacity:1;transform:none;pointer-events:auto}.qz-fab.hide{opacity:0;pointer-events:none}' +
    '.qz{position:fixed;left:16px;bottom:16px;z-index:95;width:min(400px,calc(100vw - 32px));max-height:calc(100vh - 32px);overflow:auto;background:#fff;color:#16181d;border-radius:16px;box-shadow:0 16px 48px rgba(0,0,0,.25);display:none;font:15px/1.45 Figtree,system-ui,sans-serif}' +
    '.qz.on{display:block}.qz-head{display:flex;justify-content:space-between;align-items:center;padding:14px 16px;border-bottom:1px solid #eceef2}' +
    '.qz-x{background:none;border:0;font-size:26px;line-height:1;cursor:pointer;color:#5b6270}.qz-body{padding:16px}' +
    '.qz h3{margin:0 0 12px;font:800 1.2rem "Bricolage Grotesque",system-ui,sans-serif}.qz-step{margin:0 0 4px;color:#5b6270;font-size:.85rem}' +
    '.qz-opts{display:grid;gap:8px}.qz-opts button{text-align:left;padding:12px 14px;border:2px solid #e3e6ec;border-radius:10px;background:#fff;font:600 15px Figtree,system-ui,sans-serif;cursor:pointer}' +
    '.qz-opts button:hover{border-color:#1f4fd1;background:#f2f5ff}.qz-back{margin-top:12px;background:none;border:0;color:#1f4fd1;font:600 14px Figtree,system-ui,sans-serif;cursor:pointer;padding:0}' +
    '.qz-tour{border:1px solid #e3e6ec;border-radius:12px;padding:12px;margin:0 0 10px;display:grid;gap:8px}.qz-tour span{display:block;color:#5b6270;font-size:.88rem;margin-top:2px}' +
    '.qz-tour .btn{width:100%;text-align:center}.qz-tour small{color:#5b6270;font-size:.78rem;text-align:center}.qz-more{font-size:.85rem;font-weight:600}' +
    '.qz .btn-wa{display:block;text-align:center;margin:8px 0 12px}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  fab = document.createElement('button');
  fab.type = 'button'; fab.className = 'qz-fab'; fab.textContent = '🔎 ' + T.btn;
  fab.onclick = open;
  document.body.appendChild(fab);

  var shown = false;
  function onScroll() {
    var doc = document.documentElement;
    var depth = (window.scrollY + window.innerHeight) / Math.max(doc.scrollHeight, 1);
    var banner = document.querySelector('.cc');
    if (!shown && depth > 0.4 && !banner) { shown = true; fab.classList.add('show'); }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
})();
