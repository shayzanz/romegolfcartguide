# Content for guide pages. Each page: slug, title, desc, h1, lead, img, img_alt, answer, body (HTML), tours (list key), faqs [(q,a)], related [slugs]
U = lambda i, w=1600: f"https://images.unsplash.com/photo-{i}?auto=format&fit=crop&w={w}&q=70"

COLOSSEUM = "1567613747183-fcc1e30a18eb"
COLOSSEUM2 = "1462747772350-460bb4aad7f4"
COLOSSEUM_NIGHT = "1722312864179-d4c4c5ac05bb"
FORUM_NIGHT = "1678970388666-e50b8006ab51"
FORUM = "1704841632993-148afae64231"
PANTHEON = "1570054623147-dbccfd1efa98"
TREVI = "1569397906655-7a1fce6866d2"
NAVONA = "1661693800496-6a803cba5ff9"
TRASTEVERE = "1586102724225-3503518c3b1c"
TRATTORIA = "1569230516306-5a8cb5586399"
GELATO = "1723248954986-5c24d9333f94"
VATICAN = "1748189748849-bda21f8e1e43"
CRUISE = "1598275452245-bd4ee1a97694"

PAGES = [
dict(
slug="best-golf-cart-tours-rome",
nav="Best tours 2026",
title="The 8 Best Golf Cart Tours in Rome (2026), Ranked by Category",
desc="The best golf cart tours in Rome for 2026: best private tour, best value, best for families, best night tour, best catacombs tour and more, with ratings and prices.",
h1="The best golf cart tours in Rome for 2026",
lead="Our picks by category, based on ratings, number of reviews, what's included and price.",
img=COLOSSEUM2, img_alt="The Colosseum in Rome",
answer="The best golf cart tour in Rome overall is a private city highlights tour with hotel pickup (rated 4.9/5 on GetYourGuide). For value, the 1.5-hour Biga Tours express tour from $69 is hard to beat; for families, the VIP tour with Trevi skip-the-line, gelato and supplì (4.8/5 from 858 reviews); and for evenings, the Rome By Night private tour (4.9/5).",
body="""
<p>Ratings and review counts are as shown on GetYourGuide in October 2026. We check them regularly.</p>

<h2>1. Best overall: Private Guided City Highlights Tour</h2>
<p>A private cart, an English-speaking guide and pickup included, rated <b>4.9 out of 5 from 250 reviews</b>. It covers the classic sights (Colosseum, Pantheon, Trevi, Piazza Navona) at your pace. The safest choice for a first visit.</p>

<h2>2. Best for families: VIP Golf Cart with Trevi Skip-the-Line, Gelato &amp; Supplì</h2>
<p>The most reviewed tour in our list, <b>4.8 out of 5 from 858 reviews</b>. Kids love the gelato and the supplì (Rome's fried rice ball), and skip-the-line access at the Trevi Fountain saves time in the busiest spot of the day. Private, 2–2.5 hours.</p>

<h2>3. Best small-group tour: Trevi Access, Gelato &amp; Supplì</h2>
<p>The shared version of the tour above, <b>4.9 out of 5 from 297 reviews</b>. Same treats and Trevi access at a lower price, with other travellers on board.</p>

<h2>4. Best for big groups and a custom route: Rolling Rome private tour</h2>
<p>Rolling Rome is one of the most established golf cart operators in the city, with thousands of reviews across platforms. You choose the stops, they pick you up at your central hotel, and they can run two carts for groups of up to 14. A full-day version with lunch is available.</p>

<h2>5. Best value: Biga Tours Rome Express</h2>
<p>From <b>$69 per person</b> for 1.5 hours, it's the cheapest way to see the headline sights by cart. Small groups (max 7 per cart), headsets and water included, free child seats for ages 2–12.</p>

<h2>6. Best night tour: Rome By Night Golf Cart Tour</h2>
<p>Two hours through Rome lit up after dark, private with pickup included, <b>4.9 out of 5 from 161 reviews</b>. Guides speak English, Italian, Spanish or German. See our <a href="/rome-night-golf-cart-tour/">night tour guide</a>.</p>

<h2>7. Best with drinks: Evening Golf Cart Tour with Aperitivo</h2>
<p>A 3-hour sunset-to-evening tour that ends with an Italian aperitivo, <b>4.8 out of 5 from 389 reviews</b>. Small group or private.</p>

<h2>8. Best beyond the center: Appian Way, Catacombs and Aqueducts</h2>
<p>A 4-hour small-group tour (max 5 people) out along the ancient Appian Way, with a catacomb visit and the Roman aqueducts, <b>4.8 out of 5</b>. See our <a href="/catacombs-appian-way-golf-cart-tour/">catacombs guide</a>.</p>

<h2>How we picked</h2>
<ul>
<li>Average rating of 4.6 or higher, with a meaningful number of reviews</li>
<li>Clear inclusions: guide, cart size, pickup, food</li>
<li>Free cancellation where possible</li>
<li>One clear winner per type of traveller, not just the cheapest</li>
</ul>
<p>Read more on <a href="/about/">how we compare tours</a>.</p>
""",
tours="best",
faqs=[
("What is the best golf cart tour in Rome?","For most visitors, a private city highlights tour with hotel pickup. The Private Guided City Highlights Tour by Golf Cart is rated 4.9/5 from 250 reviews on GetYourGuide."),
("What's the best golf cart tour in Rome for families?","The VIP golf cart tour with Trevi skip-the-line, gelato and supplì: private, 2–2.5 hours, rated 4.8/5 from 858 reviews."),
("What's the cheapest good golf cart tour in Rome?","The Biga Tours Rome Express, about 1.5 hours from $69 per person."),
("Is there a good night golf cart tour in Rome?","Yes. The Rome By Night private tour is 2 hours with pickup included and rated 4.9/5 from 161 reviews."),
],
related=["private-golf-cart-tour-rome","golf-cart-tour-rome-price","rome-night-golf-cart-tour","golf-cart-tour-rome-with-kids"],
),
# ------------------------------------------------------------------
dict(
slug="private-golf-cart-tour-rome",
nav="Private tours",
title="Private Golf Cart Tour in Rome: Prices, Pickup & Best Options (2026)",
desc="Private golf cart tours in Rome compared: prices from about $81 per person, hotel pickup, how long they last, what you see and which one to book.",
h1="Private golf cart tours in Rome",
lead="Your own cart, your own guide and your own route. Here's what a private tour costs and which ones are worth booking.",
img=COLOSSEUM, img_alt="The Colosseum in Rome",
answer="A private golf cart tour in Rome usually lasts 2.5–3 hours and costs about $81–230 per person, or roughly $400–800 for the whole cart. Most include pickup at hotels in the historic center, and you can choose the stops.",
body="""
<h2>What makes a tour "private"</h2>
<p>On a private tour the cart, the driver and the guide are only for your group. In practice that changes three things:</p>
<ul>
<li><b>You choose the route.</b> Want more time at the Colosseum and skip the Spanish Steps? Just say so.</li>
<li><b>You choose the pace.</b> Stop for photos, an espresso or a gelato whenever you like.</li>
<li><b>They usually pick you up.</b> Most private tours collect you at your hotel if it's in the historic center, often inside the ancient Aurelian Walls.</li>
</ul>

<h2>How much a private golf cart tour costs</h2>
<p>Prices are listed per person but depend heavily on group size, because you're really paying for the cart and the guide's time.</p>
<div class="tablewrap"><table>
<thead><tr><th>Tour</th><th>Length</th><th>From</th><th>Hotel pickup</th></tr></thead>
<tbody>
<tr><td>Entry-level private city tour</td><td>About 3 h</td><td>$81 pp</td><td>Meeting point</td></tr>
<tr><td>Rolling Rome private tour</td><td>2.5–3 h</td><td>$107 pp</td><td>Yes, central hotels</td></tr>
<tr><td>IterItaly with coffee and gelato</td><td>3 h</td><td>$121 pp</td><td>Yes, free</td></tr>
<tr><td>Premium private tour</td><td>About 3 h</td><td>$227 pp</td><td>Yes</td></tr>
<tr><td>Full day with lunch</td><td>About 7 h</td><td>About $236 pp</td><td>Yes</td></tr>
</tbody></table></div>
<p>Some operators charge for the cart instead: for example, a 4-hour private tour for up to 7 people with pickup is listed from about $499 in total. For a group of 5–7, that often works out cheaper per person than a shared tour.</p>

<h2>Private or small group?</h2>
<p>If you're two people on a budget, a shared small-group tour (from $69) is great value. Go private if you're a family or group of 4 or more, travelling with someone who can't walk far, celebrating something, or simply want to decide the stops yourself.</p>

<h2>Tips before you book</h2>
<ul>
<li>Add your hotel name and address when booking. Many operators need it at least 24 hours ahead to plan the pickup.</li>
<li>If your hotel is outside the center, ask for the nearest pickup point.</li>
<li>Larger groups can book two carts: some operators take up to 14 people.</li>
<li>Tips aren't included. About 10% is common on a private tour if you enjoyed it.</li>
</ul>
""",
tours="private",
faqs=[
("How much is a private golf cart tour in Rome?","From about $81 per person for an entry-level 3-hour tour, up to around $230 per person for premium options. Priced per cart, expect roughly $400–800."),
("Do private golf cart tours include hotel pickup?","Most do, for hotels in Rome's historic center. If your hotel is further out, the tour starts from a central meeting point."),
("How many people fit in a private golf cart?","Carts usually seat 5–7 passengers. Some operators send a second cart so groups of up to 14 can tour together."),
("Can we choose the route on a private tour?","Yes. That's the main advantage: tell the guide which sights matter to you, or let them suggest a route."),
],
related=["golf-cart-tour-rome-hotel-pickup","golf-cart-tour-rome-price","golf-cart-tour-rome-seniors","golf-cart-tour-rome-with-kids"],
),
# ------------------------------------------------------------------
dict(
slug="golf-cart-tour-rome-hotel-pickup",
nav="Hotel pickup",
title="Golf Cart Tours in Rome with Hotel Pickup (2026 Guide)",
desc="Which Rome golf cart tours pick you up at your hotel, which areas they cover, what it costs and how to arrange it. Compare tours with hotel pickup.",
h1="Golf cart tours with hotel pickup",
lead="Walk out of your hotel, step into the cart. Here's which tours collect you and how it works.",
img=TRASTEVERE, img_alt="Street in Trastevere, Rome",
answer="Most private golf cart tours in Rome include free pickup and drop-off at hotels in the historic center, usually inside the Aurelian Walls. Shared small-group tours normally start from a meeting point instead. Add your hotel details when you book, ideally 24 hours ahead.",
body="""
<h2>Which areas are covered</h2>
<p>Golf carts are slow and best on short distances, so pickup is offered in the historic center. Operators often define it as anywhere inside the Aurelian Walls, the ancient city walls that wrap around central Rome. That typically includes:</p>
<ul>
<li>Centro Storico: Pantheon, Piazza Navona, Campo de' Fiori</li>
<li>Spanish Steps, Via del Corso and Piazza del Popolo</li>
<li>Monti, the Colosseum area and Termini</li>
<li>Trastevere and the Jewish Ghetto</li>
</ul>
<p>Hotels near the Vatican (Prati), EUR, or further out may be outside the area. In that case the operator gives you a nearby meeting point, or you take a short taxi.</p>

<h2>Is pickup free?</h2>
<p>On most private tours it's included. Some premium tours charge extra (one luxury tour lists €45 for pickup from central hotels), and shared tours rarely offer it at all. Check the listing before you book.</p>

<h2>How to make sure it works</h2>
<ul>
<li>Write your hotel name and full address in the booking notes. Some operators ask for it at least 24 hours in advance.</li>
<li>Note the time: the guide usually waits outside the main entrance.</li>
<li>Save the operator's WhatsApp number from your confirmation in case of traffic delays.</li>
<li>Many tours can also drop you somewhere else at the end, like a restaurant in the center.</li>
</ul>
""",
tours="pickup",
faqs=[
("Do golf cart tours in Rome pick you up from your hotel?","Most private tours do, for hotels in the historic center. Shared small-group tours usually start from a meeting point near the Pantheon, Termini or Villa Borghese."),
("Is hotel pickup free?","Usually yes on private tours. A few premium tours charge extra, around €45, so check the listing."),
("My hotel is near the Vatican. Can they pick me up?","Sometimes. Prati is just outside the core area, so ask the operator; if not, they'll suggest a close meeting point."),
],
related=["private-golf-cart-tour-rome","golf-cart-tour-rome-seniors","golf-cart-tour-rome-price","one-day-in-rome-by-golf-cart"],
),
# ------------------------------------------------------------------
dict(
slug="golf-cart-tour-rome-price",
nav="Prices",
title="How Much Is a Golf Cart Tour in Rome? Prices Compared (2026)",
desc="Golf cart tour prices in Rome: small group from about $69, private from about $81 per person, full day and cruise excursions. What's included and how to save.",
h1="How much does a golf cart tour in Rome cost?",
lead="Real prices from listed tours, what changes the price, and how to pay less.",
img=TREVI, img_alt="The Trevi Fountain in Rome",
answer="Golf cart tours in Rome start at about $69 per person for a 1.5-hour shared tour. Classic 3-hour shared tours cost about $100–150 per person, private tours about $81–230 per person ($400–800 per cart), and cruise day trips from Civitavecchia start around €790 per group.",
body="""
<h2>Price by tour type</h2>
<div class="tablewrap"><table>
<thead><tr><th>Format</th><th>Length</th><th>Typical price</th></tr></thead>
<tbody>
<tr><td>Shared express</td><td>1.5 h</td><td>From $69 per person</td></tr>
<tr><td>Shared classic (max 7 per cart)</td><td>2.5–3 h</td><td>$100–150 per person</td></tr>
<tr><td>Shared with gelato or food</td><td>3 h</td><td>About $99–130 per person</td></tr>
<tr><td>Catacombs and Appian Way</td><td>2.5 h</td><td>From about $108 per person</td></tr>
<tr><td>Private</td><td>2.5–4 h</td><td>$81–230 per person, or $400–800 per cart</td></tr>
<tr><td>Full day</td><td>6–7 h</td><td>From about $204–240 per person</td></tr>
<tr><td>Cruise day trip from Civitavecchia</td><td>About 8 h</td><td>From about €790 per group</td></tr>
</tbody></table></div>
<p>Prices are the lowest "from" prices listed by sellers in 2026. The final price depends on your date, group size and options.</p>

<h2>What's usually included</h2>
<ul>
<li>The electric cart and a driver-guide, usually English-speaking</li>
<li>Often bottled water and headsets so you can hear the guide</li>
<li>On some tours: gelato, coffee, a pasta tasting, or hotel pickup</li>
</ul>
<p>Usually <b>not</b> included: entry tickets to monuments (tours stop outside), meals unless stated, and tips.</p>

<h2>What makes it cheaper or pricier</h2>
<ul>
<li><b>Shared vs private:</b> the biggest difference. Shared is cheaper for 1–3 people.</li>
<li><b>Group size:</b> private tours get cheaper per person as you add people, up to about 6–7.</li>
<li><b>Length:</b> express tours cost about half of a 3-hour tour.</li>
<li><b>Extras:</b> food, hotel pickup and catacomb entry add to the price.</li>
</ul>

<h2>How to save</h2>
<ul>
<li>Two people? Book a shared express or classic tour.</li>
<li>Five to seven people? Compare the private per-cart price; it's often the cheapest per head.</li>
<li>Pick tours with free cancellation so you can change plans if the weather turns.</li>
</ul>
""",
tours="cheap",
faqs=[
("What's the cheapest golf cart tour in Rome?","Shared express tours of about 1.5 hours start from around $69 per person."),
("Is a golf cart tour in Rome worth the money?","For most first-time visitors, yes: you see 6–8 major sights in about 3 hours without walking 10+ km, which is especially useful in summer heat or with kids and older travellers."),
("Do I need to pay entry tickets?","Not for the standard tour, which stops outside the monuments. Tickets are extra if you want to go inside the Colosseum or museums."),
("Should I tip?","It's optional. €5–10 per person, or about 10% on a private tour, is common."),
],
related=["private-golf-cart-tour-rome","golf-cart-vs-walking-tour-rome","one-day-in-rome-by-golf-cart","golf-cart-tour-rome-hotel-pickup"],
),
# ------------------------------------------------------------------
dict(
slug="rome-night-golf-cart-tour",
nav="Night tours",
title="Rome Night Golf Cart Tour: See the City Lit Up (2026)",
desc="Night golf cart tours in Rome: what you see after dark, best months, how long they last and how to book a private evening tour.",
h1="Night golf cart tours in Rome",
lead="Cooler air, quieter streets and the monuments lit up. Rome after dark is a different city.",
img=COLOSSEUM_NIGHT, img_alt="The Colosseum lit up at night",
answer="Night golf cart tours in Rome usually run for about 2 hours, starting around sunset. You see the Colosseum, Trevi Fountain, Piazza Navona and other landmarks lit up, with fewer crowds and cooler temperatures. They're most popular from May to September, and private evening tours can be arranged year-round.",
body="""
<h2>Why go at night</h2>
<ul>
<li><b>It's cooler.</b> In July and August, afternoon temperatures in Rome regularly pass 30°C. An evening tour avoids the worst of it.</li>
<li><b>Fewer crowds.</b> The Trevi Fountain at 10pm is far calmer than at noon.</li>
<li><b>The lighting.</b> The Colosseum, the Roman Forum and the fountains are floodlit, which makes for great photos.</li>
<li><b>Easy dinner plans.</b> Many tours can drop you at a restaurant in the center at the end.</li>
</ul>

<h2>What you'll typically see</h2>
<ul>
<li>The Colosseum and the Roman Forum lit up</li>
<li>Piazza Venezia and the Vittoriano</li>
<li>The Trevi Fountain and the Pantheon</li>
<li>Piazza Navona with its street life</li>
<li>Often St. Peter's Square or the Gianicolo viewpoint over the rooftops</li>
</ul>

<h2>Practical tips</h2>
<ul>
<li>Book for 30–60 minutes before sunset to see the city in daylight and then lit up.</li>
<li>Bring a light jacket: open carts get breezy after dark, even in summer.</li>
<li>Night tours are fewer than day tours, so book a few days ahead in high season.</li>
<li>For a specific evening or a private night tour, message us and we'll check who's available.</li>
</ul>
""",
tours="night",
faqs=[
("How long is a night golf cart tour in Rome?","Usually about 2 hours, sometimes longer on private tours."),
("What time do night tours start?","Typically around sunset: about 8–9pm in summer and 5–6pm in winter."),
("Can I combine a night tour with dinner?","Yes. Many guides will drop you at a restaurant in the center at the end, and some food tours run in the evening."),
],
related=["rome-golf-cart-food-tour","private-golf-cart-tour-rome","one-day-in-rome-by-golf-cart","golf-cart-tour-rome-price"],
),
# ------------------------------------------------------------------
dict(
slug="rome-golf-cart-food-tour",
nav="Food & gelato",
title="Rome Golf Cart Food Tour: Gelato, Pasta & Trastevere (2026)",
desc="Golf cart tours in Rome with food: gelato stops, espresso, Roman pasta tastings and evening food routes in Trastevere and Testaccio. Prices and options.",
h1="Golf cart tours with gelato and food",
lead="Sightseeing with something to eat along the way: from a simple gelato stop to a full pasta tasting.",
img=TRATTORIA, img_alt="Trattoria tables on a cobblestone street in Trastevere",
answer="Several Rome golf cart tours include food: some add a gelato or espresso stop to a 3-hour sightseeing route, while others finish with a tasting of classic Roman pastas in a trattoria. Expect about $99–130 per person on a shared tour and more for private food tours.",
body="""
<h2>Three kinds of food tour</h2>
<ul>
<li><b>Gelato stop:</b> a classic highlights tour with a break at an artisan gelateria. The easiest option for families.</li>
<li><b>Coffee and gelato:</b> private tours that include an espresso and a gelato along the way.</li>
<li><b>Pasta tasting:</b> sightseeing that ends in a trattoria with three Roman classics. Think cacio e pepe, carbonara and amatriciana.</li>
</ul>

<h2>Where the food stops happen</h2>
<p><b>Trastevere</b> is the most popular area: narrow cobbled streets, ivy-covered houses and trattorias with tables outside. <b>Testaccio</b>, the old working-class district by the former slaughterhouse, is where Romans go for traditional cooking and has a covered market. Some tours also stop in the Jewish Ghetto, known for fried artichokes.</p>

<h2>Good to know</h2>
<ul>
<li>Tell the operator about allergies or a vegetarian diet when you book. Roman pasta is easy to adapt, but they need to know.</li>
<li>Evening food tours combine well with Rome lit up. See our <a href="/rome-night-golf-cart-tour/">night tour guide</a>.</li>
<li>Drinks other than water are usually extra unless the listing says otherwise.</li>
</ul>
""",
tours="food",
faqs=[
("Which Rome golf cart tours include gelato?","Several classic 3-hour tours include a gelato stop, and some private tours include both coffee and gelato. Use the 'Gelato or food stop' filter on our homepage."),
("Is there a golf cart tour with pasta?","Yes. One popular tour offers a version that ends with a tasting of three classic Roman pasta dishes in a local trattoria."),
("Can food tours handle allergies?","Usually, if you tell the operator when booking."),
],
related=["rome-night-golf-cart-tour","golf-cart-tour-rome-with-kids","private-golf-cart-tour-rome","golf-cart-tour-rome-price"],
),
# ------------------------------------------------------------------
dict(
slug="catacombs-appian-way-golf-cart-tour",
nav="Catacombs",
title="Catacombs & Appian Way Golf Cart Tour from Rome (2026)",
desc="Golf cart tours to the Roman Catacombs and the ancient Appian Way: what's included, how long it takes, prices from about $108 and how to book.",
h1="Catacombs and Appian Way by golf cart",
lead="The ancient road out of Rome and the underground burial tunnels beneath it. Hard to reach on foot, easy by cart.",
img=FORUM, img_alt="Ancient Roman ruins",
answer="Catacombs and Appian Way golf cart tours take about 2.5 hours from central Rome and cost from about $108 per person. They drive out along the ancient Via Appia Antica and include entry with a guided visit of about 30–35 minutes inside one of the Christian catacombs.",
body="""
<h2>Why go by golf cart</h2>
<p>The Appian Way (Via Appia Antica) starts just outside the city walls and runs south for kilometres, with the catacombs spread along it. Public transport is slow and walking takes hours. A golf cart covers it comfortably, stops wherever you want, and gets you back to the center by lunchtime.</p>

<h2>What you see</h2>
<ul>
<li><b>Circus Maximus</b> on the way out, with views of the Palatine Hill</li>
<li><b>The Appian Way</b>, the original Roman paving stones, tombs and pine trees</li>
<li><b>The Catacombs</b>: underground tunnels used by early Christians to bury their dead. Visits inside are always led by the catacomb's own guides, and photos are usually not allowed underground.</li>
</ul>

<h2>Tips</h2>
<ul>
<li>Morning departures (around 9:45am) are the norm. The catacombs close for lunch and on certain weekdays, so the operator plans around them.</li>
<li>It's cooler underground (around 15°C), so bring a layer in summer.</li>
<li>Wear shoes with grip: the catacomb steps can be uneven.</li>
<li>Combine it with a classic tour on another day, or ask about full-day options that do both.</li>
</ul>
""",
tours="catacombs",
faqs=[
("How long is a catacombs golf cart tour?","About 2.5 hours from central Rome, or longer as part of a full-day tour."),
("Is the catacomb entry included?","On the dedicated catacombs tours, yes: entry and a guided visit of about 30–35 minutes."),
("Is it suitable for people with limited mobility?","The cart part is easy, but the catacombs involve stairs underground. Ask the operator before booking."),
],
related=["one-day-in-rome-by-golf-cart","private-golf-cart-tour-rome","golf-cart-tour-rome-price","golf-cart-vs-walking-tour-rome"],
),
# ------------------------------------------------------------------
dict(
slug="civitavecchia-cruise-golf-cart-tour-rome",
nav="Cruise passengers",
title="Golf Cart Tour of Rome from Civitavecchia Cruise Port (2026)",
desc="Shore excursion by golf cart: private transfer from Civitavecchia port to Rome, 5 hours by cart and back to the ship on time. Prices from about €790 per group.",
h1="Rome by golf cart from Civitavecchia cruise port",
lead="One day in port, the whole of Rome, and no stress about getting back to the ship.",
img=CRUISE, img_alt="Cruise ship in port",
answer="Golf cart shore excursions from Civitavecchia include a private transfer to Rome (about 1–1.5 hours each way), around 5 hours touring the center by golf cart, and the return to your ship on time. They're private for your group and start from about €790 per group.",
body="""
<h2>How the day works</h2>
<ul>
<li><b>Pickup at the port.</b> Your driver meets you at Civitavecchia, Rome's cruise port, timed to your ship.</li>
<li><b>Transfer to Rome</b> by car or van, about 80 km.</li>
<li><b>About 5 hours by golf cart</b> through the historic center: Colosseum, Pantheon, Trevi, Piazza Navona, the Jewish Ghetto and back streets big buses can't reach.</li>
<li><b>Back to the ship</b> with a safe margin before all-aboard.</li>
</ul>

<h2>Why it suits cruise passengers</h2>
<ul>
<li>You see far more than on a coach tour, because carts get into the narrow streets.</li>
<li>No train timetables or taxis to sort out.</li>
<li>Private: your group only, at your pace, with lunch stops on request.</li>
</ul>

<h2>What to tell us when you ask</h2>
<ul>
<li>Ship name and date in port</li>
<li>Arrival and all-aboard times</li>
<li>Number of people, and anyone with limited mobility</li>
</ul>
<p>Message us on WhatsApp and we'll check availability with local operators who specialise in cruise days.</p>
""",
tours="cruise",
faqs=[
("How far is Rome from Civitavecchia?","About 80 km. The transfer takes about 1–1.5 hours each way depending on traffic."),
("How much is a golf cart shore excursion from Civitavecchia?","From about €790 per group for a private day with transfers and around 5 hours by cart."),
("Will we be back to the ship on time?","Cruise-day operators plan the schedule around your all-aboard time and leave a safety margin."),
],
related=["private-golf-cart-tour-rome","one-day-in-rome-by-golf-cart","golf-cart-tour-rome-seniors","golf-cart-tour-rome-price"],
),
# ------------------------------------------------------------------
dict(
slug="golf-cart-tour-rome-seniors",
nav="Seniors & accessibility",
title="Rome Golf Cart Tours for Seniors & Limited Mobility (2026)",
desc="The easiest way to see Rome without long walks: golf cart tours for seniors and wheelchair users. Hotel pickup, accessibility, wheelchair space and tips.",
h1="Golf cart tours for seniors and limited mobility",
lead="Rome is hilly, cobbled and spread out. A golf cart takes the walking out of it.",
img=PANTHEON, img_alt="The Pantheon in Rome",
answer="Golf cart tours are one of the easiest ways for seniors and people with limited mobility to see Rome: the cart drives right up to the main sights and most private tours include hotel pickup. Many operators accept wheelchairs; a folded wheelchair usually takes the space of two seats, so mention it when booking.",
body="""
<h2>Why it works</h2>
<p>A classic walking tour of Rome easily means 10 km or more on cobblestones, with steps and hills. On a golf cart you ride between the sights and only get off for photos, sometimes without leaving your seat. The Pantheon is one of the few places where a short walk is usually needed, because carts can't reach the door.</p>

<h2>Wheelchairs and walkers</h2>
<ul>
<li>Several tours are listed as wheelchair accessible. The passenger transfers to a seat and the folded chair travels on the cart.</li>
<li>A folded wheelchair takes about two seats, so a 5-seat cart has room for 3 passengers plus the chair.</li>
<li>Electric wheelchairs usually don't fit. Ask the operator first.</li>
</ul>

<h2>How to choose</h2>
<ul>
<li><b>Go private</b> so you set the pace and get out only when you want.</li>
<li><b>Pick hotel pickup</b> so there's no walk to a meeting point.</li>
<li><b>Choose morning or evening</b> in summer to avoid the heat.</li>
<li><b>Tell the operator</b> about any needs when booking: they'll plan the route and the stops.</li>
</ul>
""",
tours="seniors",
faqs=[
("Are golf cart tours in Rome good for elderly travellers?","Yes, they're one of the most comfortable ways to see the city: no long walks, shade from the cart's roof, and hotel pickup on most private tours."),
("Can I bring a wheelchair on a golf cart tour?","Usually a folded manual wheelchair, which takes about two seats. Tell the operator when you book."),
("Do you have to walk at all?","Very little. Most sights are seen from the cart or a few steps away; the Pantheon usually needs a short walk."),
],
related=["golf-cart-tour-rome-hotel-pickup","private-golf-cart-tour-rome","golf-cart-tour-rome-with-kids","golf-cart-vs-walking-tour-rome"],
),
# ------------------------------------------------------------------
dict(
slug="golf-cart-tour-rome-with-kids",
nav="With kids",
title="Rome Golf Cart Tour with Kids: Family Guide (2026)",
desc="Golf cart tours in Rome for families: child seats, minimum ages, gelato stops, hotel pickup and which tours suit kids best.",
h1="Golf cart tours in Rome with kids",
lead="Kids love the cart, parents love not carrying anyone. Here's what to know before you book.",
img=GELATO, img_alt="Gelato being served in an Italian gelateria",
answer="Golf cart tours are great for families in Rome: kids enjoy the ride and nobody gets tired of walking. Some operators provide free child seats for ages 2–12 but don't accept infants under 2, while others allow babies in a pram or stroller. Private tours with hotel pickup and a gelato stop are the easiest option.",
body="""
<h2>Ages and child seats</h2>
<ul>
<li>Policies differ by operator. One popular operator provides child seats or boosters for free for ages 2–12 and doesn't accept infants under 2 for safety reasons.</li>
<li>Other tours allow infants in a pram or stroller, and some are marked as not suitable for babies. Check the listing.</li>
<li>Always tell the operator each child's age when booking so the right seats are ready.</li>
</ul>

<h2>Making it fun for kids</h2>
<ul>
<li><b>Pick a tour with gelato.</b> It's the highlight for most children.</li>
<li><b>Ask about the stories.</b> Gladiators at the Colosseum, chariot races at Circus Maximus, and throwing a coin into the Trevi Fountain.</li>
<li><b>Try the Aventine keyhole.</b> Peeking through it to see St. Peter's dome is a favourite.</li>
<li><b>Keep it short</b> for young kids: a 1.5–2.5-hour tour is plenty.</li>
</ul>

<h2>Practical tips</h2>
<ul>
<li>Private tours let you stop for bathroom breaks and snacks whenever you need.</li>
<li>Bring hats and water in summer.</li>
<li>Larger families can book two carts on some tours, up to 14 people.</li>
</ul>
""",
tours="kids",
faqs=[
("Are golf cart tours in Rome suitable for children?","Yes. They're one of the most family-friendly ways to see Rome. Check each tour's age policy and request child seats."),
("Can I bring a baby?","It depends on the operator: some don't accept infants under 2, others allow babies in a pram or stroller."),
("Which tour is best for kids?","A private tour with hotel pickup and a gelato stop, ideally 2.5–3 hours or less."),
],
related=["rome-golf-cart-food-tour","private-golf-cart-tour-rome","golf-cart-tour-rome-hotel-pickup","one-day-in-rome-by-golf-cart"],
),
# ------------------------------------------------------------------
dict(
slug="golf-cart-vs-walking-tour-rome",
nav="Golf cart vs walking",
title="Golf Cart vs Walking Tour vs Hop-On Bus in Rome: Which Is Best?",
desc="Compare a golf cart tour with a walking tour, hop-on hop-off bus and Vespa in Rome: price, sights covered, effort and who each one suits.",
h1="Golf cart, walking tour or hop-on bus?",
lead="An honest comparison of the main ways to see Rome in a few hours.",
img=NAVONA, img_alt="Fountain in Piazza Navona",
answer="A golf cart tour covers 6–8 major sights in about 3 hours with almost no walking and gets into narrow streets buses can't reach, but costs more (from about $69, typically $100+ per person). A walking tour is cheaper but means 10+ km on cobblestones, and a hop-on bus is cheap but stays on the big roads.",
body="""
<h2>Side by side</h2>
<div class="tablewrap"><table>
<thead><tr><th></th><th>Golf cart</th><th>Walking tour</th><th>Hop-on bus</th><th>Vespa / Fiat 500</th></tr></thead>
<tbody>
<tr><td>Typical price</td><td>$69–230 pp</td><td>Low, or tip-based</td><td>About $30 pp</td><td>Varies</td></tr>
<tr><td>Sights in 3 hours</td><td>6–8</td><td>3–5</td><td>Many, but from the road</td><td>5–7</td></tr>
<tr><td>Walking</td><td>Very little</td><td>A lot</td><td>Little</td><td>Little</td></tr>
<tr><td>Narrow historic streets</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr>
<tr><td>Live guide</td><td>Yes</td><td>Yes</td><td>Usually audio</td><td>Sometimes</td></tr>
<tr><td>Good for kids and seniors</td><td>Very</td><td>Hard</td><td>OK</td><td>Limited</td></tr>
</tbody></table></div>

<h2>When a golf cart is the best choice</h2>
<ul>
<li>You only have one or two days in Rome</li>
<li>It's summer and hot</li>
<li>You're travelling with kids, grandparents or anyone who can't walk far</li>
<li>You want a guide's stories without a long walk</li>
</ul>

<h2>When something else makes more sense</h2>
<ul>
<li><b>Walking tour:</b> you're on a tight budget, love walking, and want to go inside sites like the Colosseum or the Vatican Museums, which carts don't enter.</li>
<li><b>Hop-on bus:</b> you want flexible transport across the whole city over a full day.</li>
<li><b>Vespa:</b> you're a confident rider (or happy riding pillion) and want something more adventurous.</li>
</ul>
<p>Many visitors do a golf cart tour on day one to get their bearings, then book a guided visit inside the Colosseum or the Vatican on another day.</p>
""",
tours="classic",
faqs=[
("Is a golf cart tour better than a walking tour in Rome?","For covering a lot in little time with no effort, yes. For going inside monuments or saving money, a walking tour is better."),
("Do golf carts go inside the Colosseum?","No. Carts stop outside for photos and stories. You need a separate ticket or guided tour to go inside."),
("Can golf carts drive in Rome's historic center?","Yes. Licensed tour carts are street-legal and can reach narrow streets in the center where big buses can't go."),
],
related=["golf-cart-tour-rome-price","one-day-in-rome-by-golf-cart","private-golf-cart-tour-rome","golf-cart-tour-rome-seniors"],
),
# ------------------------------------------------------------------
dict(
slug="one-day-in-rome-by-golf-cart",
nav="One day in Rome",
title="One Day in Rome by Golf Cart: The Perfect Itinerary (2026)",
desc="How to see Rome in one day with a golf cart tour: morning route, where to have lunch, what to visit inside in the afternoon and evening ideas.",
h1="One day in Rome: an itinerary built around a golf cart tour",
lead="Only one day? Use the cart to see the big sights in the morning, then go inside one of them in the afternoon.",
img=VATICAN, img_alt="St. Peter's Square from above",
answer="To see Rome in one day, take a 3-hour golf cart tour in the morning (around 9–10am) to cover the Colosseum, Circus Maximus, the Aventine keyhole, the Pantheon, Piazza Navona, Trevi and the Spanish Steps. Have lunch in the center, then spend the afternoon inside the Colosseum or the Vatican Museums, and finish with dinner in Trastevere.",
body="""
<h2>Morning: golf cart tour (9:30am–12:30pm)</h2>
<p>Start early: traffic is lighter and the Trevi Fountain is less crowded. A classic 3-hour route usually covers:</p>
<ul>
<li>The Colosseum and the Arch of Constantine</li>
<li>Circus Maximus and the view of the Palatine Hill</li>
<li>The Aventine Hill: the famous keyhole and the Orange Garden viewpoint</li>
<li>The Mouth of Truth and the Theatre of Marcellus</li>
<li>Piazza Venezia, the Pantheon and Piazza Navona</li>
<li>The Trevi Fountain and the Spanish Steps</li>
</ul>
<p>Ask the guide to drop you near your lunch spot at the end.</p>

<h2>Lunch (1pm)</h2>
<p>Stay in the center: the streets around the Pantheon and Campo de' Fiori are full of trattorias. Try one of the four Roman pastas: carbonara, cacio e pepe, amatriciana or gricia.</p>

<h2>Afternoon: go inside one sight (2:30–5:30pm)</h2>
<p>Golf carts don't go inside monuments, so pick one to visit properly, with tickets booked in advance:</p>
<ul>
<li><b>The Colosseum and Roman Forum</b> for ancient Rome</li>
<li><b>The Vatican Museums, Sistine Chapel and St. Peter's</b> for art</li>
<li><b>The Borghese Gallery</b> for a shorter, quieter visit (booking essential)</li>
</ul>

<h2>Evening: Trastevere</h2>
<p>Cross the river to Trastevere for an aperitivo and dinner among ivy-covered streets. In summer, consider swapping the morning for a <a href="/rome-night-golf-cart-tour/">night golf cart tour</a> instead.</p>
""",
tours="classic",
faqs=[
("Can you see Rome in one day?","You can see the highlights. A 3-hour golf cart tour covers 6–8 major sights in the morning, leaving the afternoon to visit one monument inside."),
("What time should I book the golf cart tour?","Around 9–10am for the lightest traffic and the calmest Trevi Fountain, or an evening tour in summer."),
("Should I visit the Colosseum or the Vatican?","Ancient history fans should pick the Colosseum and Forum; art lovers the Vatican Museums. Doing both in one afternoon is too rushed."),
],
related=["golf-cart-vs-walking-tour-rome","rome-night-golf-cart-tour","private-golf-cart-tour-rome","golf-cart-tour-rome-price"],
),
]

ABOUT = dict(
slug="about",
title="About Rome Golf Cart Guide: How We Compare Tours",
desc="Who runs Rome Golf Cart Guide, how we compare golf cart tours in Rome, and how we make money.",
h1="About this guide",
lead="Run from Rome, to help visitors find the right golf cart tour quickly.",
img=TRASTEVERE, img_alt="Street in Trastevere, Rome",
)

# ---------------- November 2026 additions ----------------
def G(path, cid, text):
    return f'<a href="https://www.getyourguide.com/rome-l33/{path}/?partner_id=EQTZMZ9&utm_medium=online_publisher&cmp=rgcg-{cid}" target="_blank" rel="sponsored nofollow noopener">{text}</a>'

SPANISH_STEPS = TRASTEVERE

PAGES += [
dict(
slug="see-rome-without-walking",
nav="Rome without walking",
title="How to See Rome Without Walking: 7 Easy Ways Compared (2026)",
desc="The easiest ways to see Rome without long walks: golf cart, Vespa with a driver, vintage Fiat 500, hop-on bus, private driver and more, compared by price, comfort and what you'll see.",
h1="How to see Rome without walking",
lead="Rome is hilly, cobbled and spread out. These are the easiest ways to see it if long walks aren't an option.",
img=COLOSSEUM, img_alt="The Colosseum in Rome",
answer="The easiest way to see Rome without walking is a golf cart tour: in about 3 hours you see 6–8 major sights, mostly from the cart, and private tours usually pick you up at your hotel. Other good options are a Vespa or vintage Fiat 500 tour with a local driver, a private car with driver, or a hop-on hop-off bus, which is cheapest but can't enter the narrow historic streets.",
body="""
<h2>The options at a glance</h2>
<div class="tablewrap"><table>
<thead><tr><th>Option</th><th>Walking needed</th><th>Narrow historic streets</th><th>Guide</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>Golf cart tour</td><td>Very little</td><td>Yes</td><td>Yes, live</td><td>Seniors, families, first-timers</td></tr>
<tr><td>Vespa with a driver</td><td>Very little</td><td>Yes</td><td>Driver-guide</td><td>Couples, adventurous travellers</td></tr>
<tr><td>Vintage Fiat 500 with a driver</td><td>Very little</td><td>Yes</td><td>Driver-guide</td><td>Couples, photos, small groups</td></tr>
<tr><td>Private car with driver</td><td>Little</td><td>Partly</td><td>Optional</td><td>Bigger groups, full days</td></tr>
<tr><td>Hop-on hop-off bus</td><td>Some, to and from stops</td><td>No</td><td>Usually audio</td><td>Budget, flexible timing</td></tr>
<tr><td>Taxi between sights</td><td>Some</td><td>Partly</td><td>No</td><td>Short hops, independent travellers</td></tr>
<tr><td>E-bike tour</td><td>None, but you pedal</td><td>Yes</td><td>Yes</td><td>Active travellers who dislike walking</td></tr>
</tbody></table></div>

<h2>1. Golf cart tour: the easiest overall</h2>
<p>Electric carts with a driver-guide can drive into the historic center and stop right next to the Colosseum, the Trevi Fountain area, the Pantheon and Piazza Navona. Most tours last 2.5–3 hours and cover 6–8 sights. Private tours usually include hotel pickup in the center and can carry a folded wheelchair. Read more in our <a href="/golf-cart-tour-rome-seniors/">guide for seniors and limited mobility</a> or compare <a href="/best-golf-cart-tours-rome/">the best golf cart tours</a>.</p>

<h2>2. Vespa with a driver</h2>
<p>You ride as a passenger behind a professional driver, or in a sidecar. It's more of an experience than a tour, and great for photos. It's less suitable for anyone who finds getting on and off a scooter difficult. See our <a href="/vespa-tour-rome/">Vespa tour guide</a>.</p>

<h2>3. Vintage Fiat 500 with a driver</h2>
<p>A 1960s Fiat 500 with a local driver: iconic, comfortable to sit in, and small enough for the narrow lanes. Cars usually take 2–3 guests. See our <a href="/fiat-500-tour-rome/">Fiat 500 tour guide</a>.</p>

<h2>4. Hop-on hop-off bus</h2>
<p>The cheapest way to cover a lot of ground, but buses stay on the main roads, so you still walk from the stops to the Pantheon, Trevi and Navona. Fine for an overview, less so if walking is the problem.</p>

<h2>Tips for a low-walking day in Rome</h2>
<ul>
<li>Book tours with <b>hotel pickup</b> so there's no walk to a meeting point.</li>
<li>Go <b>early morning or evening</b> in summer: midday heat makes even short walks hard.</li>
<li>For the Colosseum and Vatican, book <b>timed tickets</b> to avoid standing in queues, and ask about accessible routes.</li>
<li>Combine one golf cart tour for the overview with one visit inside a monument, rather than many stops.</li>
</ul>
""",
tours="seniors", tours_title="Golf cart tours with hotel pickup",
faqs=[
("What is the easiest way to see Rome without walking?","A golf cart tour: the cart drives up to the main sights, you see 6–8 of them in about 3 hours, and private tours usually include hotel pickup."),
("Can you see Rome in a wheelchair?","Yes. Many golf cart tours accept a folded manual wheelchair, which takes about two seats. Tell the operator when booking."),
("Is the hop-on hop-off bus good if I can't walk much?","Partly. It covers a lot, but stays on main roads, so you still need to walk from the stops to sights like the Pantheon and Trevi Fountain."),
],
related=["golf-cart-tour-rome-seniors","vespa-tour-rome","fiat-500-tour-rome","golf-cart-vs-walking-tour-rome"],
),
# ------------------------------------------------------------------
dict(
slug="vespa-tour-rome",
nav="Vespa tours",
title="Vespa Tour in Rome: Sidecar, With a Driver or Self-Ride? (2026 Guide)",
desc="Vespa tours in Rome compared: sidecar tours, riding as a passenger with a driver, night tours and photoshoot tours. Ratings, duration and how to choose.",
h1="Vespa tours in Rome",
lead="Rome from the back of a Vespa, or from a sidecar. Here's how the different formats compare and which ones travellers rate highest.",
img=TRASTEVERE, img_alt="Street in Trastevere, Rome",
answer="Most Vespa tours in Rome are 1.5–3 hours with a professional driver: you ride as a passenger or in a sidecar, so no licence is needed. Highly rated options include the 1.5-hour Highlights Vespa Sidecar Tour with Gelato (4.9/5 from 844 reviews on GetYourGuide) and the 3-hour Sidecar Tour with Hotel Transfers & Gelato (5/5 from 268 reviews).",
body=f"""
<p>Ratings and review counts as shown on GetYourGuide in November 2026.</p>

<h2>Three ways to do a Vespa tour</h2>
<ul>
<li><b>Sidecar:</b> you sit in a sidecar next to the driver. The easiest to get in and out of, and the most photogenic.</li>
<li><b>Passenger with a driver:</b> you ride behind a professional driver, who is also your guide. Private and flexible.</li>
<li><b>Self-ride:</b> you drive your own Vespa behind a guide. You need a valid licence and real scooter experience: Rome traffic is not the place to learn.</li>
</ul>

<h2>Highly rated Vespa tours</h2>
<div class="tablewrap"><table>
<thead><tr><th>Tour</th><th>Length</th><th>Rating</th></tr></thead>
<tbody>
<tr><td>{G('rome-highlights-vespa-tour-with-coffee-and-gelato-t401080','vespa-highlights','Highlights Vespa Sidecar Tour with Gelato')}</td><td>1.5 h</td><td>4.9 (844 reviews)</td></tr>
<tr><td>{G('rome-vespa-sidecar-tour-90-minute-panoramic-experience-t977450','vespa-panoramic','90-Minute Panoramic Sidecar Experience')}</td><td>1.5 h</td><td>4.9 (717 reviews)</td></tr>
<tr><td>{G('rome-vespa-sidecar-tour-with-pick-up-drop-off-and-gelato-t701881','vespa-hotel','Sidecar Tour with Hotel Transfers &amp; Gelato')}</td><td>3 h</td><td>5.0 (268 reviews)</td></tr>
<tr><td>{G('rome-by-night-vespa-guided-tour-t26098','vespa-night','Vespa Tour by Night with Driver &amp; Private Guide')}</td><td>3 h</td><td>4.9 (91 reviews)</td></tr>
<tr><td>{G('vespa-with-driver-private-tour-in-rome-t26052','vespa-halfday','Half-Day Tour with Private Driver')}</td><td>3 h</td><td>5.0 (68 reviews)</td></tr>
<tr><td>{G('rome-vespa-tour-with-professional-photoshoot-as-a-passenger-t619291','vespa-photo','Vespa Tour with Professional Photoshoot')}</td><td>1.5 h</td><td>4.8 (32 reviews)</td></tr>
</tbody></table></div>

<h2>Vespa or golf cart?</h2>
<p>A Vespa is more fun and more "Roman Holiday", but it's best for one or two people who are comfortable on a scooter. A <a href="/best-golf-cart-tours-rome/">golf cart</a> is better for families, older travellers, anyone with a bag or a camera to hold, and rainy days, since most carts have a roof.</p>

<h2>Tips</h2>
<ul>
<li>Helmets are provided and mandatory. Wear closed shoes and avoid long, loose clothes.</li>
<li>Night tours are cooler in summer and the lit-up monuments look great from a moving Vespa.</li>
<li>Tell the operator your height and weight if you're unsure about fitting in a sidecar.</li>
</ul>
""",
gyg_ids="401080,977450,701881,26098", tours_title="Photos and live ratings",
faqs=[
("Do I need a licence for a Vespa tour in Rome?","Not if you ride as a passenger or in a sidecar, which is how most tours work. Self-ride tours require a valid licence."),
("How long is a Vespa tour in Rome?","Usually 1.5 to 3 hours."),
("What is the best Vespa tour in Rome?","Among the highest rated on GetYourGuide are the Highlights Vespa Sidecar Tour with Gelato (4.9/5, 844 reviews) and the Sidecar Tour with Hotel Transfers & Gelato (5/5, 268 reviews)."),
("Vespa or golf cart: which is better?","Vespa for couples who want an adventure; golf cart for families, seniors and anyone who prefers a seat with a roof."),
],
related=["fiat-500-tour-rome","see-rome-without-walking","best-golf-cart-tours-rome","rome-night-golf-cart-tour"],
),
# ------------------------------------------------------------------
dict(
slug="fiat-500-tour-rome",
nav="Fiat 500 tours",
title="Vintage Fiat 500 Tour in Rome: Best Options & Prices (2026)",
desc="Vintage Fiat 500 tours in Rome: with a driver or driving yourself in a convoy, photo tours, evening tours. Ratings, duration and tips.",
h1="Vintage Fiat 500 tours in Rome",
lead="The little 1960s car that became a symbol of Italy, with a local behind the wheel. Here's how to pick the right tour.",
img=NAVONA, img_alt="Fountain in Piazza Navona",
answer="Vintage Fiat 500 tours in Rome usually last 1.5–3 hours with a local driver, and cars take 2–3 guests. The most reviewed is the City Tour in a Retro Fiat 500 with Photo Stops (4.9/5 from 952 reviews on GetYourGuide). If you want to drive yourself, there are convoy tours, which require a valid driving licence.",
body=f"""
<p>Ratings and review counts as shown on GetYourGuide in November 2026.</p>

<h2>With a driver or behind the wheel?</h2>
<ul>
<li><b>With a driver (most tours):</b> a local drives and tells stories, you enjoy the ride and the photos.</li>
<li><b>Self-drive convoy:</b> you drive a vintage Fiat 500 behind a guide's car. Fun, but the cars have manual gearboxes and Rome traffic is intense. A valid driving licence is required; non-EU visitors should check whether an International Driving Permit is needed.</li>
</ul>

<h2>Highly rated Fiat 500 tours</h2>
<div class="tablewrap"><table>
<thead><tr><th>Tour</th><th>Length</th><th>Rating</th></tr></thead>
<tbody>
<tr><td>{G('rome-retro-fiat-500-and-photography-service-t951294','fiat-photo','City Tour in a Retro Fiat 500 with Photo Stops')}</td><td>1.5 h</td><td>4.9 (952 reviews)</td></tr>
<tr><td>{G('drive-a-fiat-500-vintage-car-in-rome-in-a-convoy-tour-t38619','fiat-drive','Driving Tour with a Vintage Fiat 500 (self-drive)')}</td><td>About 1.5–2 h</td><td>4.9 (243 reviews)</td></tr>
<tr><td>{G('rome-vintage-fiat-500-cabriolet-semi-private-city-tour-t463578','fiat-cabrio','Small-Group Tour in a Fiat 500 Cabriolet')}</td><td>2 h</td><td>4.9 (180 reviews)</td></tr>
<tr><td>{G('rome-vintage-fiat-500-guided-city-tour-t429799','fiat-guided','Vintage Fiat 500 Guided City Tour')}</td><td>3 h</td><td>5.0 (13 reviews)</td></tr>
<tr><td>{G('evening-tour-of-rome-in-vintage-fiat-500-t595473','fiat-evening','Evening Tour aboard a Vintage Fiat 500')}</td><td>2 h</td><td>5.0 (4 reviews)</td></tr>
</tbody></table></div>

<h2>Fiat 500 or golf cart?</h2>
<p>A Fiat 500 is the more iconic, photogenic choice for a couple. A <a href="/best-golf-cart-tours-rome/">golf cart</a> fits more people (usually 5–7), is easier to get in and out of, and often includes hotel pickup.</p>

<h2>Tips</h2>
<ul>
<li>The cars are small: travel light and tell the operator if anyone is very tall.</li>
<li>Photo tours are popular for proposals and anniversaries; book a few days ahead.</li>
<li>Older cars have little or no air conditioning, so in summer pick a morning or evening slot.</li>
</ul>
""",
gyg_ids="951294,38619,463578,429799", tours_title="Photos and live ratings",
faqs=[
("How long is a Fiat 500 tour in Rome?","Usually 1.5 to 3 hours."),
("Can I drive the Fiat 500 myself?","Yes, on convoy tours, with a valid driving licence. Most tours have a local driver instead."),
("How many people fit in a vintage Fiat 500?","Usually 2–3 guests plus the driver."),
("What's the most popular Fiat 500 tour in Rome?","The City Tour in a Retro Fiat 500 with Photo Stops is the most reviewed on GetYourGuide, rated 4.9/5 from 952 reviews."),
],
related=["vespa-tour-rome","see-rome-without-walking","best-golf-cart-tours-rome","golf-cart-vs-walking-tour-rome"],
),
# ------------------------------------------------------------------
dict(
slug="is-a-golf-cart-tour-in-rome-worth-it",
nav="Is it worth it?",
title="Is a Golf Cart Tour in Rome Worth It? Honest Pros & Cons (2026)",
desc="Is a golf cart tour in Rome worth the money? Honest pros and cons, who it's best for, who should skip it, and how to get the most from it.",
h1="Is a golf cart tour in Rome worth it?",
lead="An honest look at what you get, what you don't, and who should book one.",
img=TREVI, img_alt="The Trevi Fountain in Rome",
answer="A golf cart tour in Rome is worth it if you have limited time, are travelling with kids or older people, or visit in summer heat: you see 6–8 major sights in about 3 hours with almost no walking. It's less worth it if you're on a tight budget or mainly want to go inside the Colosseum or Vatican, since carts only stop outside.",
body="""
<h2>Pros</h2>
<ul>
<li><b>You cover a lot fast.</b> 6–8 major sights in about 3 hours, which would take most of a day on foot.</li>
<li><b>Almost no walking.</b> Ideal for seniors, young kids, limited mobility or a recovering knee.</li>
<li><b>A local guide on board.</b> You get the stories, not just the sights.</li>
<li><b>Narrow streets.</b> Carts reach places big buses can't.</li>
<li><b>Hotel pickup</b> on most private tours.</li>
</ul>

<h2>Cons</h2>
<ul>
<li><b>Price.</b> From about $69 per person for a short shared tour, and $100+ for most classic or private tours. A walking tour is cheaper.</li>
<li><b>You stay outside.</b> Tours stop outside the Colosseum, Vatican and other monuments; tickets to go in are separate.</li>
<li><b>Traffic.</b> Rome's traffic can slow you down at peak times. Morning tours are smoother.</li>
<li><b>Weather.</b> Most carts have a roof, but open sides mean you'll feel the cold in winter and the wind in rain.</li>
</ul>

<h2>Who should book one</h2>
<ul>
<li>First-time visitors with 1–2 days in Rome</li>
<li>Families with young children</li>
<li>Travellers with grandparents or anyone who can't walk far</li>
<li>Cruise passengers with one day in port</li>
<li>Anyone visiting in July or August</li>
</ul>

<h2>Who might skip it</h2>
<ul>
<li>Budget travellers who enjoy walking</li>
<li>Repeat visitors who already know the main sights</li>
<li>People whose priority is the inside of museums and churches</li>
</ul>

<h2>How to get the most out of it</h2>
<ul>
<li>Book a <b>morning</b> tour (9–10am) for lighter traffic and a calmer Trevi Fountain.</li>
<li>Go <b>private</b> if you're 4 or more: per person it's often similar to a shared tour.</li>
<li>Use it on <b>day one</b> to get your bearings, then pick one monument to visit inside.</li>
<li>Check the <b>cancellation policy</b>: most tours have free cancellation up to 24 hours before.</li>
</ul>
""",
tours="best", tours_title="Our top-rated picks",
faqs=[
("Is a golf cart tour in Rome worth the money?","For first-timers, families, seniors and summer visitors, usually yes: you see 6–8 sights in about 3 hours with almost no walking. Budget travellers who like walking may prefer a walking tour."),
("Do golf cart tours go inside the Colosseum?","No. They stop outside for photos and stories; entry tickets are separate."),
("Are golf cart tours in Rome safe?","Yes. Tours use licensed, street-legal carts with professional driver-guides, and many carts have seatbelts."),
],
related=["golf-cart-vs-walking-tour-rome","best-golf-cart-tours-rome","golf-cart-tour-rome-price","one-day-in-rome-by-golf-cart"],
),
# ------------------------------------------------------------------
dict(
slug="rome-christmas-lights-tour",
nav="Christmas lights tour",
title="Rome Christmas Lights Tour by Golf Cart: Trees, Markets & Lights (2026)",
desc="See Rome's Christmas lights by golf cart: Via del Corso and Via Condotti lights, the Spanish Steps and Piazza del Popolo trees, St. Peter's nativity and the Piazza Navona market.",
h1="Rome's Christmas lights by golf cart",
lead="December evenings in Rome are magical, and cold. A night tour by cart is the easiest way to see the lights.",
img=COLOSSEUM_NIGHT, img_alt="The Colosseum lit up at night",
answer="Rome's Christmas lights usually go on around 8 December and stay up until Epiphany on 6 January. A 2–3 hour evening golf cart tour can cover the lights on Via del Corso and Via dei Condotti, the trees at the Spanish Steps and Piazza del Popolo, the Christmas market in Piazza Navona, and the tree and nativity scene in St. Peter's Square.",
body="""
<h2>What to see</h2>
<ul>
<li><b>Via del Corso:</b> lights stretch along the main shopping street between Piazza Venezia and Piazza del Popolo.</li>
<li><b>Via dei Condotti and the Spanish Steps:</b> the luxury street leading to the Steps, usually with a big tree at the top.</li>
<li><b>Piazza del Popolo:</b> in recent years home to the city's main Christmas tree.</li>
<li><b>Piazza Navona:</b> Rome's traditional Christmas market, with stalls, sweets and a carousel, open until Epiphany.</li>
<li><b>St. Peter's Square:</b> the Vatican's giant tree and life-size nativity scene, usually lit in early December.</li>
<li><b>Trastevere:</b> lights strung between the ivy-covered buildings, perfect for dinner afterwards.</li>
</ul>

<h2>Key dates</h2>
<ul>
<li><b>Around 8 December</b> (Feast of the Immaculate Conception): the city's lights and main trees are usually switched on.</li>
<li><b>Early December:</b> the St. Peter's Square tree and nativity are usually unveiled.</li>
<li><b>Until 6 January</b> (Epiphany): lights, markets and decorations stay up.</li>
</ul>
<p>Exact dates change every year, so check the city's official announcements closer to the time.</p>

<h2>Why by golf cart</h2>
<ul>
<li>The lights are spread across the center: on foot it's several kilometres in the cold.</li>
<li>Carts reach the narrow streets where the best lights are.</li>
<li>Most carts have a roof and some operators provide blankets. Ask when booking.</li>
</ul>

<h2>Tips for a December evening tour</h2>
<ul>
<li>Book a slot starting around <b>5–6pm</b>, just after dark.</li>
<li>Dress warmly: open-sided carts get cold, and December evenings in Rome are often around 5–10°C.</li>
<li>Avoid 24–25 December and 31 December unless the operator confirms it's running.</li>
<li>For a private Christmas lights route, message us and we'll arrange it with a local operator.</li>
</ul>
""",
tours="night", tours_title="Evening and night tours",
faqs=[
("When are the Christmas lights on in Rome?","Usually from around 8 December until Epiphany on 6 January."),
("Where are the best Christmas lights in Rome?","Via del Corso, Via dei Condotti and the Spanish Steps, Piazza del Popolo, Piazza Navona's Christmas market and St. Peter's Square."),
("Is there a Christmas market in Rome?","Yes, the traditional market in Piazza Navona, usually open until 6 January."),
("Is a golf cart tour good in December?","Yes, if you dress warmly. Evening tours are the best way to see the lights without walking several kilometres in the cold."),
],
related=["rome-night-golf-cart-tour","rome-golf-cart-food-tour","best-golf-cart-tours-rome","one-day-in-rome-by-golf-cart"],
),
]
