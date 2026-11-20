# Registro SEO + GEO: romegolfcartguide.com

Le voci più recenti stanno in cima.

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
