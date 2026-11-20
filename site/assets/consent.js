/* Cookie consent + Google Analytics 4 (loaded only after "Accept").
   Set GA_ID to the Measurement ID (G-XXXXXXXXXX). Empty = no banner, no analytics. */
(function () {
  var GA_ID = '';
  var KEY = 'rgcg_consent';          // stores {v:'granted'|'denied', t:timestamp}
  var MAX_AGE = 1000 * 60 * 60 * 24 * 180; // ask again after 6 months
  if (!GA_ID) return;

  var lang = (document.documentElement.lang || 'en').slice(0, 2);
  var T = {
    en: { text: 'We use Google Analytics cookies to count visits and see which tours people click, so we can improve the site. Only if you agree.', ok: 'Accept', no: 'Reject', more: 'Privacy policy', settings: 'Cookie settings' },
    es: { text: 'Usamos cookies de Google Analytics para contar las visitas y ver qué tours interesan más, y así mejorar la web. Solo si estás de acuerdo.', ok: 'Aceptar', no: 'Rechazar', more: 'Política de privacidad', settings: 'Configurar cookies' },
    de: { text: 'Wir nutzen Cookies von Google Analytics, um Besuche zu zählen und zu sehen, welche Touren angeklickt werden. Nur mit deiner Zustimmung.', ok: 'Akzeptieren', no: 'Ablehnen', more: 'Datenschutz', settings: 'Cookie-Einstellungen' }
  }[lang] || null;
  if (!T) T = { text: '', ok: 'Accept', no: 'Reject', more: 'Privacy policy', settings: 'Cookie settings' };

  function read() {
    try {
      var c = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (c && Date.now() - c.t < MAX_AGE) return c.v;
    } catch (e) {}
    return null;
  }
  function save(v) { try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {} }

  var loaded = false;
  function loadGA() {
    if (loaded) return; loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag('consent', 'default', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'granted' });
    gtag('js', new Date());
    gtag('config', GA_ID);
    var s = document.createElement('script');
    s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
  }
  function deleteGACookies() {
    document.cookie.split(';').forEach(function (c) {
      var n = c.split('=')[0].trim();
      if (n === '_ga' || n.indexOf('_ga_') === 0) {
        ['', '.' + location.hostname, location.hostname].forEach(function (d) {
          document.cookie = n + '=; Max-Age=0; path=/' + (d ? '; domain=' + d : '');
        });
      }
    });
  }

  // ---- conversion events (sent only when consent was given) ----
  function track(name, params) { if (loaded && window.gtag) gtag('event', name, params); }
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a');
    if (!a) return;
    var href = a.href || '';
    var where = location.pathname;
    if (/viator\.com/.test(href) || /getyourguide\.com/.test(href)) {
      var m = href.match(/[?&](?:campaign|cmp)=rgcg-([^&]+)/);
      track('affiliate_click', {
        partner: /viator/.test(href) ? 'viator' : 'getyourguide',
        tour_id: m ? decodeURIComponent(m[1]) : '',
        link_text: (a.textContent || '').trim().slice(0, 60),
        page_path: where,
        transport_type: 'beacon'
      });
    } else if (a.classList.contains('js-wa') || /wa\.me|whatsapp/.test(href)) {
      track('whatsapp_click', { page_path: where, transport_type: 'beacon' });
    } else if (a.matches('[href*="/tour/"]')) {
      track('tour_details_click', { tour_path: a.getAttribute('href'), page_path: where });
    }
  }, true);
  var finder = document.getElementById('go');
  if (finder) finder.addEventListener('click', function () {
    var v = function (id) { var el = document.getElementById(id); return el ? el.value : ''; };
    track('finder_search', { people: v('f-people'), tour_type: v('f-type'), pickup: v('f-pickup'), guide_lang: v('f-lang') });
  });

  // ---- banner ----
  var css = '.cc{position:fixed;left:16px;right:16px;bottom:16px;z-index:999;max-width:560px;margin:0 auto;background:#16181d;color:#fff;border-radius:14px;padding:16px 18px;box-shadow:0 10px 30px rgba(0,0,0,.25);font:15px/1.45 Figtree,system-ui,sans-serif}' +
    '.cc p{margin:0 0 12px}.cc a{color:#ffcb3d}.cc .b{display:flex;gap:10px}' +
    '.cc button{flex:1;height:42px;border-radius:10px;border:2px solid #fff;font:700 15px Figtree,system-ui,sans-serif;cursor:pointer}' +
    '.cc .ok{background:#ffcb3d;border-color:#ffcb3d;color:#16181d}.cc .no{background:transparent;color:#fff}';
  function banner() {
    if (document.querySelector('.cc')) return;
    if (!document.getElementById('cc-css')) { var st = document.createElement('style'); st.id = 'cc-css'; st.textContent = css; document.head.appendChild(st); }
    var d = document.createElement('div');
    d.className = 'cc'; d.setAttribute('role', 'dialog'); d.setAttribute('aria-label', T.settings);
    d.innerHTML = '<p>' + T.text + ' <a href="/privacy.html">' + T.more + '</a></p><div class="b"><button class="no" type="button">' + T.no + '</button><button class="ok" type="button">' + T.ok + '</button></div>';
    d.querySelector('.ok').onclick = function () { save('granted'); d.remove(); loadGA(); };
    d.querySelector('.no').onclick = function () { save('denied'); d.remove(); deleteGACookies(); if (loaded) location.reload(); };
    document.body.appendChild(d);
  }

  // "Cookie settings" link in every footer, to change the choice at any time
  function addSettingsLink() {
    var uls = document.querySelectorAll('footer ul');
    var ul = uls.length ? uls[uls.length - 1] : document.querySelector('footer');
    if (!ul) return;
    var li = document.createElement(ul.tagName === 'UL' ? 'li' : 'p');
    var a = document.createElement('a'); a.href = '#'; a.textContent = T.settings;
    a.onclick = function (e) { e.preventDefault(); banner(); };
    li.appendChild(a); ul.appendChild(li);
  }

  function start() {
    addSettingsLink();
    var c = read();
    if (c === 'granted') loadGA();
    else if (c === null) banner();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
