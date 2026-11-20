# Registro SEO + GEO: romegolfcartguide.com

Le voci più recenti stanno in cima.

## 2026-11-20: GO #1, Natale, quick win, schede tour
**Dati visti:**
- Search Console ultimi 7 giorni: 37 righe query/pagina, pochi clic. Le pagine Natale ES/DE sono in posizione 6–9 ("luces navidad roma", "Weihnachtsbeleuchtung Rom"). La guida notturna è ferma a pos. 12–13 per "rome golf cart tour at night" e varianti "evening". "biga tours" è a pos. 20 sulla pagina best e a 29 sulla scheda.
- Bing Webmaster: ancora nessun dato. GA4: appena installato.

**Fatto:**
1. **Natale EN/ES/DE riscritte** come guida informativa sulle luci di Natale 2026, con il tour come modo comodo per vederle (le ricerche sono informative: "luces navidad roma"). Contenuto:
   - tabella delle date verificate il 20/11, con lo stato di ogni voce: albero di San Pedro 7/12 ore 17:30 da Vatican News; mercatino di Navona dal 1/12 al 6/1 secondo l'avviso comunale; luminarie di Via del Corso montate il 6–7/11;
   - percorso serale in 6 tappe;
   - FAQ nuove con le date;
   - title e H1 con "2026" e "dates".
   - Tolta l'affermazione non verificata sull'albero principale a Piazza del Popolo: ora c'è Piazza Venezia.
2. **Striscia "Christmas 2026"** con link alla guida Natale:
   - nelle 3 home e sulle pagine best, prezzi e notte, in tutte e 3 le lingue;
   - si spegne con `SEASON_ON = False` in build.py, **da togliere dopo il 6 gennaio 2027**.
3. **Quick win:**
   - title della home accorciato (da 86 a 58 caratteri) e meta con "golf buggy";
   - guida notturna con title, H1 e meta su "at night / evening", più 2 FAQ;
   - pagina prezzi con 2 FAQ ("per person", "private");
   - pagina best con FAQ "golf buggy".
4. **Schede tour e guide:**
   - ogni guida EN ha ora link HTML statici alle schede dei tour elencati (prima erano solo via JS);
   - ogni scheda tour linka la guida di riferimento con anchor descrittivo (es. aqueducts → guida catacombe);
   - le schede Biga Tours, Rolling Rome e IterItaly hanno il nome dell'operatore nel title.
5. Tecnico:
   - `modified` per pagina: data visibile, dateModified nello schema e lastmod in sitemap;
   - CSS `?v=20261120`.

**URL toccati:**
- /rome-christmas-lights-tour/, /es/luces-navidad-roma-carrito-golf/, /de/weihnachtsbeleuchtung-rom-golfcart/
- /, /es/, /de/
- /rome-night-golf-cart-tour/, /golf-cart-tour-rome-price/, /best-golf-cart-tours-rome/ (più le versioni ES/DE di best, prezzi e notte, solo striscia)
- tutte le /tour/*/

**Da misurare al prossimo GO:**
- posizioni e clic delle pagine Natale (obiettivo: top 5 su "luces navidad roma" e "Weihnachtsbeleuchtung Rom", prime impressioni EN su "rome christmas lights 2026");
- night guide sotto pos. 10;
- primi eventi GA4.
- Da ricontrollare il ~27/11: il giorno di apertura del mercatino di Navona e l'accensione di Via del Corso, poi aggiornare la tabella.
- **Non ritoccare** le pagine sopra prima del 1° dicembre, salvo l'aggiornamento delle date di Natale.

## 2026-11-20: setup e audit iniziale
**Dati visti:**
- Search Console dal 28 ottobre al 18 novembre (via Windsor.ai): circa 470 impressioni, 6 clic, 37 pagine con impressioni.
- Ahrefs DR: 0.
- Crawl interno di 62 pagine.

**Fatto:**
- Sito messo su GitHub (`shayzanz/romegolfcartguide`, pubblico). Struttura: `src/` contiene gli script che generano il sito, `site/` il sito pubblicato.
- `netlify.toml` spostato nella root del repo, con `publish = "site"`, così Netlify pubblica da GitHub senza build.
- Percorsi degli script resi relativi al repo, non più legati alla cartella di lavoro.
- Rimossa la cartella `/pins/`, che non serviva più.
- Aggiunti il banner cookie e GA4 (`site/assets/consent.js`):
  - GA si carica solo dopo "Accetta";
  - testi in EN/ES/DE;
  - link "Cookie settings" nel footer di ogni pagina;
  - eventi `affiliate_click`, `whatsapp_click`, `tour_details_click`, `finder_search`.
  - GA4 attivo con ID `G-3G5VQ96CPJ` (impostato in `src/build.py`). Testato su EN/ES/DE, privacy e schede tour: nessuna richiesta a Google prima di "Accetta".
- Aggiornata la privacy: sezione su Google Analytics, base giuridica (consenso), conservazione 14 mesi, elenco dei cookie.
- Scritto l'audit iniziale (`seo/audit-2026-11-20.md`) con il piano di crescita.

**Perché:** pubblicare direttamente da GitHub e misurare le conversioni prima di iniziare a ottimizzare.

**Da misurare al prossimo GO:**
- impressioni e posizioni delle pagine Natale;
- primi eventi GA4;
- query nuove in Search Console.
