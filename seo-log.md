# Registro SEO + GEO: romegolfcartguide.com

Le voci più recenti stanno in cima.

## 2026-11-24: GO #4, correzione Natale e Vespa in ES/DE
**Dati visti:**
- Search Console, ultimi 7 giorni:
  - best: 102 impressioni, pos. 32, 2 clic;
  - prezzi: 28 impressioni, pos. 10.5;
  - notte: 21 impressioni, pos. 10.6;
  - Natale ES 18 impressioni a pos. 10.5 e DE 12 a pos. 10.6, leggermente giù da 7–9 dopo la riscrittura (oscillazione normale);
  - Vespa EN: pos. 8.8;
  - scheda gyg-aqueducts: pos. 9.4;
  - "worth it": pos. 6.7.
- GA4, primi dati: 1 sessione, 1 `affiliate_click`, 1 `finder_search`. Probabilmente il test di Shay su Viator.

**Fatto:**
1. **Correzione Natale EN/ES/DE.** Il 20/11 avevo scritto che l'albero della città sta di solito a Piazza Venezia. Secondo RomaSette (4/12/2025), nel 2025 l'albero era a **Piazza del Popolo**, acceso l'8/12 alle 18:30 insieme alle luminarie di Via del Corso.
   - Aggiornati tabella, lista dei luoghi, percorso (ora parte da Piazza del Popolo) e FAQ, con "data 2026 non ancora annunciata".
   - Mercatino di Navona: ancora nessuna data di apertura ufficiale (finestra dal 1/12 al 6/1; RomaVisiteGuidate, aggiornato il 2/11).
   - Data "verificato" passata al 24/11.
2. **Nuove pagine /es/tour-vespa-roma/ e /de/vespa-tour-rom/**, versioni native della guida Vespa EN, che è in pos. 8.8. Le pagine ES/DE di solito salgono in fretta.
   - Link GYG localizzati (`es-es` / `de-de`) con campagne `-es` / `-de`; widget GYG nella lingua giusta.
   - hreflang collegato a /vespa-tour-rome/.
   - intl.py ora supporta `gyg_ids` nelle guide ES/DE.

**URL toccati:** /rome-christmas-lights-tour/, /es/luces-navidad-roma-carrito-golf/, /de/weihnachtsbeleuchtung-rom-golfcart/ (solo correzioni di date e fatti), /es/tour-vespa-roma/ e /de/vespa-tour-rom/ (nuove), home ES/DE (lista guide).

**Da misurare / prossimo GO:**
- dal 27/11: nuovi pin Pinterest;
- data di apertura del mercatino di Navona e dell'accensione di Via del Corso;
- Fiat 500 in ES/DE (EN pos. 23, 12 impressioni);
- sezione "golf buggy" sulla best dopo il 2/12.

## 2026-11-23: GO #3, quiz "Find your tour" e pagina Biga Tours
**Dati visti:**
- Search Console, ultimi 7 giorni:
  - "biga tours": 13 impressioni (pos. 19 sulla best, 29 sulla scheda); "golf buggy tour rome": pos. 25;
  - "best golf cart tour rome": pos. 3 (1 impressione);
  - "golf car roma tour": pos. 10;
  - Natale ES pos. 9;
  - anziani pos. 66, appena riscritta.
- GA4: ancora 0 eventi.
- Hosting Cloudflare: OK.

**Fatto:**
1. **Nuova pagina /biga-tours-rome-golf-cart/**, perché c'è domanda reale sul nome dell'operatore.
   - Contenuto: 3 tour di Biga (Express, City Highlights, Catacombs & Appian Way) con prezzi, durate, tappe e incluso, verificati il 23/11 sulle loro pagine di prenotazione; regole su bambini, gruppo, puntualità; quando scegliere un'alternativa; 6 FAQ.
   - Disclaimer: non affiliati a Biga Tours.
   - Pulsanti Viator: Express (`387632P6`) e City Highlights (`387632P2`). **Da verificare** che il link P2 apra il prodotto giusto: Viator dà 403 al browser automatico.
   - La scheda /tour/biga-express/ ora linka questa pagina.
2. **Quiz "Find your tour in 3 questions"** su tutte le pagine con i tour, in EN/ES/DE.
   - Pulsante discreto dopo il 40% di scroll, mai automatico.
   - Risultati da tours.js; link con campagna `-q`; eventi GA4 dedicati.
   - Testato con Playwright: desktop e mobile, 3 lingue, eventi corretti.
3. consent.js:
   - espone `window.rgcgTrack` e aggiunge il parametro `source` agli eventi di clic;
   - `?v=20261123`.

**URL toccati:** /biga-tours-rome-golf-cart/ (nuova), /tour/biga-express/, tutte le pagine (script quiz).

**Da misurare:**
- impressioni e posizione di /biga-tours-rome-golf-cart/ su "biga tours";
- eventi `quiz_open` / `quiz_complete` e clic con `source=quiz`;
- campagne `rgcg-*-q` nelle dashboard affiliati.

## 2026-11-22: GO #2, sito bloccato su Netlify, pagina anziani
**Dati visti:**
- Search Console, ultimi 7 giorni:
  - prezzi: pos. 8.8 (era 12), 20 impressioni;
  - guida notturna: pos. 10.7 (era 15.5);
  - Natale DE pos. 7.3, Natale ES pos. 11.7;
  - best: 72 impressioni a pos. 30, 1 clic;
  - home: pos. 7.8, 1 clic;
  - anziani: pos. 51, la query "rome tours for seniors with limited mobility" continua a mostrarsi.
- GA4: 0 eventi e 0 sessioni dal 20 al 22/11. GA è online (consent.js live con ID), quindi visite poche e/o consenso non dato.
- Bing: ancora vuoto.

**Problema trovato:** i deploy Netlify di 9676bed (GO #1) ed e296b64 risultano **"Skipped"**: il GO #1 non è mai andato online. È coerente con il blocco dei deploy di produzione per i crediti del piano Free di Netlify, segnalato da molti utenti sul forum. Il sito resta online con la versione 7061492.
- Proposta a Shay: spostare l'hosting su **Cloudflare Pages** (gratis, deploy da GitHub senza limiti di crediti). Aggiunto `site/_headers`, che funziona su entrambi gli host.
- **Serve l'ok di Shay** (azione su piattaforme esterne: Cloudflare, Namecheap, DNS).

**Fatto:**
1. **/golf-cart-tour-rome-seniors/ riscritta e ampliata** (da circa 300 a circa 900 parole), per coprire la domanda più ampia "rome tours for seniors with limited mobility":
   - golf cart privato;
   - accessibilità di Colosseo e Musei Vaticani, con fatti dalle pagine ufficiali verificati il 22/11 (ascensore tra primo e secondo ordine; sedie a rotelle gratuite ai Vaticani; ingresso gratuito con invalidità ≥67%);
   - piano di una giornata e alternative;
   - 6 FAQ.
   - Title e H1 più ampi; lo slug resta lo stesso.
2. `site/_headers` per la cache degli asset, indipendente dall'host.

**URL toccati:** /golf-cart-tour-rome-seniors/

**Aggiornamento 22/11, pomeriggio:**
- Hosting spostato su **Cloudflare Workers**, con Shay passo passo: nameserver da Netlify a Cloudflare, TXT di Google conservato, custom domain sul dominio principale, route + redirect per il www.
- GO #1 e GO #2 ora sono online.
- IndexNow inviato per 22 URL toccati, tramite il browser dell'app.

**Da misurare:**
- quando il sito tornerà a pubblicare: posizione della pagina anziani sulla query "limited mobility" e tutte le metriche del GO #1;
- IndexNow da inviare dopo il primo deploy riuscito, tramite il browser dell'app dall'origine del sito.

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
