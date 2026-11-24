# RomeGolfCartGuide.com: istruzioni per Claude

Sito di confronto dei golf cart tour a Roma (EN, ES, DE). Guadagna con link affiliati Viator e GetYourGuide, più contatti WhatsApp per tour su richiesta.
Proprietario: Shay. Parla italiano, non è tecnico: spiegazioni brevi, in italiano semplice, passo per passo.

## Ruolo
Claude è il responsabile della crescita SEO + GEO/AEO (traffico da Google e dalle risposte delle AI). Obiettivo finale: più conversioni (clic sui link affiliati e contatti WhatsApp).

## Regole di lavoro
- **Si lavora solo quando Shay scrive GO.** Niente giri automatici o task programmati.
- Con il GO: analizza i dati, sistema titoli, meta, testi, link interni, schema e FAQ, crea contenuti nuovi dove c'è domanda, pubblica (commit + push su `main`) e aggiorna `seo-log.md`.
- **Niente post sui social e nessuna azione su piattaforme esterne** (Reddit, Quora, Pinterest, Google Search Console, GA4, Cloudflare, Namecheap, GitHub settings…) senza l'ok di Shay sulla modifica precisa. Leggere i dati va bene.
- Niente installazioni sul computer di Shay.
- Testi con tono umano: frasi semplici e concrete, niente formule da AI ("in today's fast-paced world", "nestled", "unlock", "elevate", "seamless", "hidden gem", "whether you're… or…").
- Mai inventare: recensioni, testimonianze, persone, esperienze in prima persona, prezzi o rating non verificati. Rating e prezzi solo da Viator/GYG verificati, con la data del controllo.
- Non copiare testi o foto dei concorrenti.

## Come è fatto il sito
- **Hosting: Cloudflare Workers (static assets)** dal 22/11/2026. Netlify è stato abbandonato perché il piano Free saltava i deploy ("Skipped" per i crediti).
  - Ogni push su `main` viene pubblicato da Cloudflare Workers Builds (progetto `romegolfcartguide`, URL di prova `romegolfcartguide.shayzanz.workers.dev`).
  - Config: `wrangler.jsonc` (assets da `./site`, `worker/index.js` fa solo il redirect 301 da www al dominio senza www).
  - DNS su Cloudflare: Namecheap punta ai nameserver Cloudflare. Il TXT `google-site-verification` serve a Search Console: non toccarlo.
  - www: record A `192.0.2.1` proxied + route `www.romegolfcartguide.com/*` sul worker.
  - `netlify.toml` è rimasto solo per storico.
- `site/`: il sito pubblicato. Non c'è build lato host: si genera in locale con build.py e si committa `site/`. Cache degli asset in `site/_headers`.
- `src/build.py`: genera tutto il sito. Si lancia con `python3 src/build.py` dalla root del repo (serve node per `tourpages.py`).
  - `src/pages.py`: guide in inglese (slug, title, desc, h1, body HTML, faqs, tours, related, immagini Unsplash per ID).
  - `src/pages_es.py`, `src/pages_de.py`: guide in spagnolo e tedesco (campo `en` = slug inglese corrispondente, serve per hreflang).
  - `src/tourpages.py`: pagine `/tour/<id>/` con mappa Leaflet e percorso.
  - `src/intl.py`: home e guide ES/DE, hreflang e selettore lingua.
  - `src/templates/index.html` (home EN) e `src/templates/privacy.html`.
- File statici modificati a mano, direttamente in `site/assets/`:
  - `tours.js`: dati dei tour e link affiliati.
  - `i18n.js`: traduzioni dei tour.
  - `style.css`.
  - `consent.js`: banner cookie + GA4 + eventi. Il GA_ID si imposta in `src/build.py`, non qui.
- Generati da build.py: `sitemap.xml`, `robots.txt` (bot AI ammessi), `llms.txt`, chiave IndexNow `f9bbe2b124ca40a0a1f067f7f63f2e9f.txt`.
- Dopo modifiche a CSS o JS, aggiorna il parametro `?v=` nei riferimenti (cache di 1 ora su /assets/).
- Prima di pubblicare: build senza errori, nessun link interno rotto, JSON-LD valido, controllo con Playwright di almeno una pagina EN, una ES e una DE.
- Dopo la pubblicazione: ping IndexNow degli URL nuovi o cambiati (POST a api.indexnow.org con key e keyLocation sul dominio).

## Link affiliati (non cambiare i codici)
- Viator: `pid=P00328677&mcid=42383&medium=link&campaign=rgcg-<id>`
- GetYourGuide: `partner_id=EQTZMZ9`, campagna `cmp=rgcg-<id>`. Widget GYG con `data-gyg-partner-id="EQTZMZ9"`.
- WhatsApp: +39 393 855 2086.

## Dati e strumenti
- Search Console: proprietà `sc-domain:romegolfcartguide.com`, letta tramite Windsor.ai (connettore `searchconsole`).
- GA4: via Windsor.ai (connettore `googleanalytics4`). Eventi: `affiliate_click` (partner, tour_id, page_path), `whatsapp_click`, `tour_details_click`, `finder_search`. Il banner cookie raccoglie i dati solo dopo "Accetta", quindi GA vede solo una parte delle visite. I clic dentro il widget GYG (iframe) non sono tracciati.
- Bing Webmaster via Windsor (connettore `bing_webmaster`, account `https://romegolfcartguide.com/`): utile per la parte GEO, perché ChatGPT e Copilot usano l'indice di Bing.
- Pinterest via Windsor (connettore `pinterest_organic`, account `bestplacesitaly5`): solo lettura delle statistiche, non pubblica.
- Ahrefs e Ubersuggest: piani gratuiti, dati limitati.
- Le conversioni reali sono nelle dashboard Viator e GetYourGuide: chiedere a Shay gli export quando servono.

## Procedura di ogni GO
Shay scrive GO circa ogni 1–2 giorni. A ogni GO, nell'ordine:
1. **Dati**:
   - Search Console via Windsor: ultimi 7 e 28 giorni contro il periodo precedente, per query e per pagina;
   - GA4 via Windsor (proprietà `565301251`): eventi `affiliate_click` e `whatsapp_click` per pagina e tour, pagine di ingresso;
   - Ahrefs e Ubersuggest dove il piano gratuito lo permette (DR, volumi, idee di keyword).
2. **Scelta**: 1–3 interventi a più alto impatto, partendo dal piano in `seo/audit-2026-11-20.md` e dai dati nuovi. Cosa guardare:
   - query in posizione 5–20;
   - pagine con impressioni ma CTR basso;
   - domande nuove;
   - stagionalità;
   - pagine che portano clic affiliati.
3. **Lavoro**: modifiche al sito o contenuti nuovi.
   - Non riscrivere la stessa pagina più di una volta ogni 10–14 giorni: Google ha bisogno di tempo per rivalutarla. Annota nel log quando una pagina è stata toccata.
4. **Verifica e pubblicazione**: build, controlli, commit e push su `main` (Cloudflare pubblica da solo in circa 1 minuto; verifica su workers.dev), ping IndexNow. Dal workspace api.indexnow.org non è raggiungibile: usa il browser dell'app con richieste GET `?url=...&key=...` in modalità no-cors.
5. **Log**: aggiorna `seo-log.md`.
6. **Report a Shay** in italiano semplice, 5–10 righe: cosa è cambiato nei dati, cosa ho fatto, cosa gli chiedo (solo se serve un suo ok per azioni esterne, con il testo esatto pronto da approvare).

## Quiz "Find your tour" (dal 23/11/2026)
- File: `site/assets/quiz.js`, caricato da build.py su tutte le pagine che usano tours.js.
- Pulsante in basso a sinistra dopo il 40% di scroll, nascosto finché c'è il banner cookie; si apre solo al clic.
- 3 domande (persone, interesse, esigenza); mostra fino a 3 tour da `TOURS`, filtrati e ordinati per rank.
- Link affiliati con campagna `rgcg-<id>-q`, così le prenotazioni da quiz si distinguono nelle dashboard Viator/GYG.
- Eventi GA4: `quiz_open`, `quiz_complete` (people, interest, need, results), `affiliate_click`/`whatsapp_click` con `source=quiz`.
- Idee in sospeso: pagina o sezione "golf buggy" (oggi pos. ~25 sulla pagina best; aggiungere una sezione alla best dopo il 2/12 per la regola dei 10–14 giorni).

## Backlink (approvato da Shay il 24/11)
- Al prossimo GO preparare un piano per i primi 10 link onesti: blog di viaggio (bambini, anziani, crociere Civitavecchia), Reddit/Quora con link solo quando serve, Medium/LinkedIn, forum di crociere.
- Per ognuno: dove, a chi, messaggio pronto. Shay approva e pubblica o invia lui.
- Mai link comprati, scambi in massa o spam.
- Dati per i report (Ubersuggest, 24/11): "golf cart tour rome" circa 12.100 ricerche/mese a livello globale, CPC circa 5 $; varianti principali tra 30 e 210 ricerche/mese.

## Pinterest
- Account `bestplacesitaly5` (nome "Best Places Italy"), bacheca "Rome Travel Tips".
- Il 9 novembre 2026 Shay ha caricato 10 pin (1000×1500) programmati uno al giorno.
- Le immagini si generano con Playwright: font Bricolage Grotesque e Figtree, colori blu `#1f4fd1` e giallo `#ffcb3d`, illustrazioni SVG. Niente foto di persone, niente marchi altrui.
- Al primo GO dopo il 27 novembre 2026, e poi quando le statistiche lo suggeriscono, Claude dice a Shay che è il momento di nuovi pin. Prepara le immagini PNG (inviate una per una, non in zip), con titolo, descrizione e link, e gli spiega passo passo come caricarli e programmarli.
- Shay li carica a mano: Claude non pubblica su Pinterest.

## Registro
Ogni sessione GO aggiunge una voce in cima a `seo-log.md`:
- data;
- dati visti;
- cosa è stato cambiato e perché;
- URL toccati;
- cosa misurare la prossima volta.
