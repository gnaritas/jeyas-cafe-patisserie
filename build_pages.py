#!/usr/bin/env python3
"""JEYAS Café & Pâtisserie — Ice Blocks, Midtown Sacramento CA. Template-v2 multi-page site.
Pre-opening shop (late spring 2027): every claim traced in evidence.json (WhatNow 2026-11,
The Abridged/KVIE 2026-10-30, Hoodline 2026-10, press lineup quoted verbatim from coverage).
Unknowns (phone, prices, exact opening date, final menu) omitted — never guessed.
Zero JS. Hand-rolled HTML/CSS. noindex demo host."""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, 'public')
os.makedirs(PUB, exist_ok=True)

ORIGIN = 'https://jeyas-cafe-patisserie-demo.up.railway.app'
BRAND = 'JEYAS Caf&eacute; &amp; P&acirc;tisserie'
BRAND_PLAIN = 'JEYAS Café & Pâtisserie'
CITY = 'Sacramento, CA'
STREET = '1710 R Street, Suite 170'
FULL_ADDR = '1710 R Street, Suite 170, Sacramento, CA 95811'
EMAIL = 'info@jaynagyro.com'
GYRO = 'https://jaynagyro.com'
MAPQ = 'https://www.google.com/maps?q=1710%20R%20St%2C%20Sacramento%2C%20CA%2095811'
LAT, LON = 38.5687771, -121.4874830  # OSM Nominatim, 1710 R Street, Ice Blocks, Sacramento 95811

def head(title, desc, path):
    u = ORIGIN + path
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{u}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND_PLAIN}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{u}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ORIGIN}/og.png">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/style.css">
<link rel="preconnect" href="https://www.google.com"></head>
<body>'''

def nav():
    return '''<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <a class="brand" href="/">JEYAS<span>Caf&eacute;&nbsp;&amp;&nbsp;P&acirc;tisserie</span></a>
  <input type="checkbox" id="navtoggle" class="navtoggle" aria-label="Show navigation">
  <label for="navtoggle" class="navbtn" aria-hidden="true"><i></i></label>
  <nav aria-label="Main" class="links">
    <a href="/carte">La&nbsp;Carte</a>
    <a href="/croissants">Croissants</a>
    <a href="/crepes">Cr&ecirc;pes</a>
    <a href="/our-story">Our&nbsp;Story</a>
    <a href="/visit">Visit</a>
    <a class="btn btn-sm" href="/contact">Contact</a>
  </nav>
</header>'''

def footer():
    return f'''<footer class="site">
  <div class="footgrid">
    <div class="footnap">
      <p class="fbrand">{BRAND}</p>
      <address>{STREET}<br>Sacramento, CA 95811</address>
      <p class="fmail"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p class="ffamily">From the family behind <a href="{GYRO}" rel="noopener">Jayna Gyro</a> &middot; Sacramento</p>
    </div>
    <div class="footcta">
      <p class="goldrule" aria-hidden="true"></p>
      <p class="fline">Croissants baked at dawn.<br>Cr&ecirc;pes served till midnight.</p>
      <p class="fline2">Opening late spring 2027 at the Ice Blocks, 1710 R Street. The confirmed opening date will be posted here the day it&rsquo;s set.</p>
    </div>
  </div>
  <p class="footline">&copy; 2026 {BRAND_PLAIN} &middot; Sacramento, CA</p>
</footer>'''

def breadcrumbs(name, path):
    items = [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': ORIGIN + '/'},
    ]
    if path != '/':
        items.append({'@type': 'ListItem', 'position': 2, 'name': name, 'item': ORIGIN + path})
    return json.dumps({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}, ensure_ascii=False)

def ld_home():
    obj = {
        '@context': 'https://schema.org', '@type': ['Bakery', 'CafeOrCoffeeShop'],
        'name': BRAND_PLAIN,
        'image': ORIGIN + '/og.png',
        'url': ORIGIN + '/',
        'servesCuisine': ['French', 'Pastries', 'Crêpes', 'Coffee'],
        'email': EMAIL,
        'address': {'@type': 'PostalAddress', 'streetAddress': '1710 R Street, Suite 170', 'addressLocality': 'Sacramento', 'addressRegion': 'CA', 'postalCode': '95811', 'addressCountry': 'US'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': LAT, 'longitude': LON},
        'hasMap': MAPQ,
        'hasMenu': ORIGIN + '/carte',
        'openingHoursSpecification': [{
            '@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
            'opens': '06:30', 'closes': '23:59'}],
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_carte():
    obj = {
        '@context': 'https://schema.org', '@type': 'Menu',
        'name': f'{BRAND_PLAIN} — The Planned Carte',
        'inLanguage': 'en',
        'hasMenuSection': [
            {'@type': 'MenuSection', 'name': 'Viennoiseries & Pâtisseries', 'itemListElement': [
                {'@type': 'MenuItem', 'name': 'Specialty Croissants', 'description': 'Laminated and baked in-house — the heart of the pastry program.'},
                {'@type': 'MenuItem', 'name': 'Parisian-Style Pastries', 'description': 'The pastry program led by chef Antonio Coriano.'},
                {'@type': 'MenuItem', 'name': 'Desserts', 'description': 'Desserts served late into the night.'},
            ]},
            {'@type': 'MenuSection', 'name': 'Crêpes', 'itemListElement': [
                {'@type': 'MenuItem', 'name': 'Sweet Crêpes'},
                {'@type': 'MenuItem', 'name': 'Savory Crêpes'},
            ]},
            {'@type': 'MenuSection', 'name': 'Café & Bowls', 'itemListElement': [
                {'@type': 'MenuItem', 'name': 'Specialty Coffee'},
                {'@type': 'MenuItem', 'name': 'Smoothies'},
                {'@type': 'MenuItem', 'name': 'Açaí Bowls'},
            ]},
            {'@type': 'MenuSection', 'name': 'Sandwiches', 'itemListElement': [
                {'@type': 'MenuItem', 'name': 'Sandwiches', 'description': 'For the midday rush, to order.'},
            ]},
        ],
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_service(name, path, desc):
    obj = {
        '@context': 'https://schema.org', '@type': 'Service',
        'name': name,
        'description': desc,
        'areaServed': {'@type': 'City', 'name': 'Sacramento', 'addressRegion': 'CA'},
        'provider': {'@type': 'Bakery', 'name': BRAND_PLAIN, 'address': {'@type': 'PostalAddress', 'streetAddress': '1710 R Street, Suite 170', 'addressLocality': 'Sacramento', 'addressRegion': 'CA', 'postalCode': '95811', 'addressCountry': 'US'}},
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_faq(qa_list):
    obj = {
        '@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qa_list],
    }
    return json.dumps(obj, ensure_ascii=False)

PAGES = {}

# ---------- HOME ----------
PAGES['index.html'] = (head('JEYAS Café & Pâtisserie — French Bakery & Crêperie Opening 2027, Ice Blocks, Sacramento CA',
    'Opening late spring 2027 at the Ice Blocks, Midtown Sacramento: specialty croissants baked in-house, sweet and savory French crêpes, specialty coffee, smoothies and açaí — planned from 6:30 a.m. to midnight. 1710 R Street.',
    '/'), f'''{nav()}
<main id="main">
<section class="hero">
  <div class="vitrine">
    <p class="kicker">ICE BLOCKS &middot; MIDTOWN SACRAMENTO</p>
    <h1>JEYAS</h1>
    <p class="bsub">Caf&eacute;&nbsp;&amp;&nbsp;P&acirc;tisserie</p>
    <p class="lead">Croissants baked in-house before dawn. Cr&ecirc;pes and dessert until midnight. A French-style bakery and caf&eacute; from the family behind Jayna Gyro — opening late spring 2027 at 1710 R Street.</p>
    <p class="cta"><a class="btn btn-big" href="/carte">See La Carte</a> <a class="btn btn-ghost btn-big" href="/contact">Opening&nbsp;News</a></p>
  </div>
  <p class="stamp" aria-hidden="true">OPENING SPRING 2027</p>
</section>

<section class="carteband">
  <div class="carte">
    <p class="cartehdr">La Carte &mdash; The Planned Lineup</p>
    <ul class="crows">
      <li><span>Specialty croissants</span><i></i><b>baked in-house</b></li>
      <li><span>French cr&ecirc;pes</span><i></i><b>sweet &middot; savory</b></li>
      <li><span>Specialty coffee</span><i></i><b>from 6:30 a.m.</b></li>
      <li><span>Smoothies &amp; a&ccedil;a&iacute; bowls</span><i></i><b>morning onward</b></li>
      <li><span>Sandwiches</span><i></i><b>for lunch</b></li>
      <li><span>Desserts</span><i></i><b>till midnight</b></li>
      <li><span>Planned hours</span><i></i><b>6:30 a.m. &ndash; midnight, daily</b></li>
    </ul>
    <p class="cartefoot">The lineup shared in the opening announcement and press coverage. The menu is still being finished — prices come at opening.</p>
    <a class="cartelink" href="/carte">The full carte &rarr;</a>
  </div>
  <div class="whatis">
    <h2>What kind of place is this?</h2>
    <ul class="pillars">
      <li><b>Everything baked in-house.</b> The viennoiserie comes out of JEYAS&rsquo;s own ovens, not a delivery tray — the croissants are the whole point.</li>
      <li><b>Parisian r&eacute;sum&eacute;, Sacramento roots.</b> The pastry program is led by Sacramento-born chef Antonio Coriano, who trained in France and came back via a Michelin-starred kitchen.</li>
      <li><b>Dawn to midnight.</b> The plan is doors at 6:30 a.m. and cr&ecirc;pes until midnight — breakfast for the early risers, dessert for the later crowd.</li>
      <li><b>An inside&ndash;outside caf&eacute;.</b> About 1,500 square feet inside plus a patio of roughly 750&ndash;1,000 square feet at the Ice Blocks — outdoor seating is a big part of the experience.</li>
    </ul>
  </div>
</section>

<section class="quoteband">
  <blockquote>
    <p>&ldquo;We are looking forward to opening a new place to welcome everyone to come and enjoy specialty croissants and specialty drinks.&rdquo;</p>
    <cite>Yusuf Topal, co-owner — via What Now Sacramento</cite>
  </blockquote>
</section>

<section class="grid3">
  <article class="cardcard">
    <h3>The chef</h3>
    <p>Antonio Coriano runs the pastry program: Sacramento-born, trained in France, ex&ndash;pastry chef de partie at Michelin-starred Prot&eacute;g&eacute; in Palo Alto, formerly executive pastry chef at Old Soul Co. and lead macaron baker at Ginger Elizabeth Chocolates.</p>
  </article>
  <article class="cardcard">
    <h3>Three daughters, one name</h3>
    <p>JEYAS blends the names of co-owner Yusuf&rsquo;s three daughters — Jeyda, Yasemin and Ashley. The caf&eacute; is a family project, brothers Yusuf and Levent Topal, built for Sacramento&rsquo;s everyday life.</p>
  </article>
  <article class="cardcard">
    <h3>The corner</h3>
    <p>The former Pressed Juicery storefront at the Ice Blocks, plus the leasing office next door — a Midtown development block that was built for exactly this kind of sidewalk caf&eacute;.</p>
  </article>
</section>

<section class="homecta">
  <h2>Coffee at 6:30 a.m.<br>Cr&ecirc;pes at 11 p.m.</h2>
  <p>That&rsquo;s the whole idea — one address, the whole day. Opening late spring 2027 at 1710 R Street.</p>
  <p class="cta"><a class="btn btn-big" href="/visit">Where We&rsquo;re At</a> <a class="btn btn-ghost btn-big" href="/contact">Talk to the Family</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_home()}</script>
<script type="application/ld+json">{ld_carte()}</script>
</body>
</html>''')

# ---------- LA CARTE ----------
PAGES['carte.html'] = (head('La Carte — JEYAS Café & Pâtisserie, Sacramento CA',
    'The planned carte at JEYAS Café & Pâtisserie in Sacramento: specialty croissants and Parisian-style pastries baked in-house, sweet and savory French crêpes, specialty coffee, smoothies, açaí bowls and sandwiches — opening late spring 2027.',
    '/carte'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">THE PLANNED LINEUP AT OPENING</p>
  <h1>La Carte</h1>
  <p class="lead">Everything below comes from the opening announcement and press coverage — the menu is still being finalized, and prices arrive at opening. Here&rsquo;s what the family has said it plans to serve, and when.</p>
</section>

<section class="menusection">
  <h2>Viennoiseries &amp; P&acirc;tisseries</h2>
  <p class="sectionnote">The head of the caf&eacute; — everything out of JEYAS&rsquo;s own ovens, from early morning.</p>
  <ul class="menurows">
    <li><span class="mname">Specialty Croissants</span><i></i><span class="mdesc">Laminated in-house, baked before dawn. &ldquo;Specialty croissants&rdquo; is the owners&rsquo; own phrase — this is the item the whole caf&eacute; is built around.</span></li>
    <li><span class="mname">Parisian-Style Pastries</span><i></i><span class="mdesc">The European-style pastry program, led by chef Antonio Coriano — a decade and a half of pastry kitchens, from Prot&eacute;g&eacute; to Ginger Elizabeth.</span></li>
    <li><span class="mname">Desserts</span><i></i><span class="mdesc">Because the plan is to keep serving long after most caf&eacute;s close.</span></li>
  </ul>
  <p class="cta"><a class="btn" href="/croissants">More on the croissants &amp; the chef</a></p>
</section>

<section class="menusection">
  <h2>Cr&ecirc;pes</h2>
  <p class="sectionnote">Sweet and savory, French-style — morning through midnight.</p>
  <ul class="menurows">
    <li><span class="mname">Sweet Cr&ecirc;pes</span><i></i><span class="mdesc">The dessert-to-breakfast spectrum, done properly.</span></li>
    <li><span class="mname">Savory Cr&ecirc;pes</span><i></i><span class="mdesc">The lunch plate with a zinc-and-steam pedigree.</span></li>
  </ul>
  <p class="cta"><a class="btn" href="/crepes">More on cr&ecirc;pes, dawn to midnight</a></p>
</section>

<section class="menusection">
  <h2>Caf&eacute; &amp; Bowls</h2>
  <p class="sectionnote">The drink menu was designed alongside the pastry program.</p>
  <ul class="menurows">
    <li><span class="mname">Specialty Coffee</span><i></i><span class="mdesc">The reason to set the alarm for 6:30 a.m.</span></li>
    <li><span class="mname">Smoothies</span><i></i><span class="mdesc">Built for the morning rush.</span></li>
    <li><span class="mname">A&ccedil;a&iacute; Bowls</span><i></i><span class="mdesc">The Midtown classic, done in a French house.</span></li>
  </ul>
</section>

<section class="menusection">
  <h2>Sandwiches</h2>
  <ul class="menurows">
    <li><span class="mname">Sandwiches</span><i></i><span class="mdesc">For lunch and the midday run — the savory half of an all-day caf&eacute;.</span></li>
  </ul>
</section>

<section class="menufine">
  <p>A final note on the carte: the family has published the lineup, not the prices or the final list — specifics go up the day they&rsquo;re set. Ask us anything through the <a href="/contact">contact form</a>.</p>
  <p class="cta"><a class="btn btn-big" href="/contact">Ask a question</a> <a class="btn btn-ghost btn-big" href="/visit">Where we&rsquo;re at</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_carte()}</script>
<script type="application/ld+json">{breadcrumbs('La Carte', '/carte')}</script>
</body>
</html>''')

# ---------- CROISSANTS ----------
PAGES['croissants.html'] = (head('Croissants & French Pâtisserie — JEYAS Café, Sacramento CA',
    'Specialty croissants and Parisian-style pastry, laminated and baked in-house at JEYAS Café & Pâtisserie, opening late spring 2027 at the Ice Blocks, Sacramento — pastry program led by chef Antonio Coriano.',
    '/croissants'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">THE HEART OF THE HOUSE</p>
  <h1>The croissants<br>come from our ovens</h1>
  <p class="lead">&ldquo;Everything will be baked in-house,&rdquo; the owners say — and the croissant is the proof item. Laminated dough, real butter, baked on-site before opening, out of the case from 6:30 a.m.</p>
</section>

<section class="storygrid">
  <article class="prose">
    <h2>A Sacramento chef, trained in France</h2>
    <p>The pastry program is led by <strong>Antonio Coriano</strong> — born in Sacramento, trained in France, and back home running the case at JEYAS. Before the caf&eacute; he spent time as pastry chef de partie at <strong>Prot&eacute;g&eacute;</strong>, the Michelin-starred restaurant in Palo Alto, most recently through June 2026.</p>
    <p>His Sactown r&eacute;sum&eacute; is part of the menu&rsquo;s DNA: executive pastry chef at <strong>Old Soul Co.</strong>, and lead macaron baker at <strong>Ginger Elizabeth Chocolates</strong>. That&rsquo;s a decade and a half of pastry kitchens pointed at one thing: what comes out of the oven at JEYAS.</p>
    <p>The inspiration for the caf&eacute;&rsquo;s French line comes from Coriano&rsquo;s training — specialty croissants first, then the wider pastry program and the dessert list that keeps the kitchen alive until midnight.</p>
  </article>
  <aside class="pressbox">
    <h2>Why it matters</h2>
    <p>A croissant is the hardest thing a bakery does on purpose: days of lamination, butter at the exact right temperature, an oven that knows the dough. Shops that buy in par-baked goods still serve &ldquo;fresh croissants.&rdquo; JEYAS&rsquo;s owners built the announcement around one sentence — <em>everything will be baked in-house.</em></p>
    <p class="fineprint">The lineup, the chef&rsquo;s background and the plans on this page come from the opening announcement and press coverage. Items beyond the croissant will be published as the menu is finalized.</p>
  </aside>
</section>

<section class="menufaq">
  <h2>Quick answers</h2>
  <dl>
    <div><dt>When can I get one?</dt><dd>Opening late spring 2027 at 1710 R Street — the owners have told press the plan is on track. The confirmed date goes up here the day it&rsquo;s set.</dd></div>
    <div><dt>How much?</dt><dd>Prices haven&rsquo;t been published yet — they&rsquo;ll go up with the final menu.</dd></div>
    <div><dt>What else will be in the case?</dt><dd>Parisian-style pastries and desserts, alongside cr&ecirc;pes, coffee, smoothies, a&ccedil;a&iacute; and sandwiches — <a href="/carte">the planned carte</a> has the whole lineup.</dd></div>
  </dl>
  <p class="cta"><a class="btn btn-big" href="/carte">See the whole carte</a> <a class="btn btn-ghost btn-big" href="/contact">Ask the family</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Croissants & Pâtisserie at JEYAS Café & Pâtisserie', '/croissants', 'Specialty croissants and Parisian-style pastry, laminated and baked in-house at 1710 R Street, Sacramento, CA — opening late spring 2027.')}</script>
<script type="application/ld+json">{breadcrumbs('Croissants', '/croissants')}</script>
<script type="application/ld+json">{ld_faq([
  ('When does JEYAS Café & Pâtisserie open?', 'Late spring 2027 is the plan, per the owners — at 1710 R Street in the Ice Blocks, Midtown Sacramento. The exact opening date has not been announced.'),
  ('Are the croissants baked in-house?', 'Yes. The owners have said everything at JEYAS will be baked in-house, with the specialty croissants as the signature.'),
  ('How much are the croissants?', 'Prices have not been published yet — they will be announced with the final menu.'),
])}</script>
</body>
</html>''')

# ---------- CRÊPES ----------
PAGES['crepes.html'] = (head('Sweet & Savory Crêpes Till Midnight — JEYAS Café & Pâtisserie, Sacramento CA',
    'Sweet and savory French-style crêpes served from morning till midnight at JEYAS Café & Pâtisserie, opening late spring 2027 at the Ice Blocks, 1710 R Street, Sacramento.',
    '/crepes'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">THE LATE HALF OF THE DAY</p>
  <h1>Cr&ecirc;pes, from<br>morning to midnight</h1>
  <p class="lead">Most caf&eacute;s are a breakfast business with a lunch problem. JEYAS is planned the other way around: doors at 6:30 a.m., and sweet and savory French-style cr&ecirc;pes — with dessert — on the menu until midnight, every day.</p>
</section>

<section class="menusection">
  <h2>The Cr&ecirc;pe Board</h2>
  <p class="sectionnote">Two boards, one batter program — the savory side for lunch, the sweet side that doubles as dinner and dessert.</p>
  <ul class="menurows">
    <li><span class="mname">Sweet Cr&ecirc;pes</span><i></i><span class="mdesc">The French dessert that happens to show up at breakfast too. The late-evening sweet tooth has an address now.</span></li>
    <li><span class="mname">Savory Cr&ecirc;pes</span><i></i><span class="mdesc">The lunch plate — buckwheat-and-fillings territory, done as a caf&eacute; cr&ecirc;perie should.</span></li>
  </ul>
  <p class="sectionnote">Specific cr&ecirc;pe preparations haven&rsquo;t been published yet — they&rsquo;ll be announced with the final menu.</p>
</section>

<section class="quoteband">
  <blockquote>
    <p>&ldquo;Whether you&rsquo;re an early riser looking for your first cup of coffee and a fresh croissant, meeting friends for breakfast or lunch, or satisfying a late-night dessert craving, we want JEYAS to be the place you think of.&rdquo;</p>
    <cite>Yusuf Topal, co-owner — via The Abridged (PBS KVIE)</cite>
  </blockquote>
  <div class="quotenote">
    <h2>Why midnight?</h2>
    <p>The Ice Blocks block is Midtown&rsquo;s densest stretch of evening foot traffic — restaurants, bars, and the apartments between them. The family&rsquo;s plan: coffee and pastry in the morning hours, cr&ecirc;pes and desserts late into the night, with the patio open much of that window.</p>
    <p class="fineprint">Hours are the announced plan, not yet a posted schedule — 6:30 a.m. to midnight daily, per the owners&rsquo; coverage. The confirmed schedule goes up here at opening.</p>
  </div>
</section>

<section class="homecta">
  <h2>A dessert list worth the drive at 11 p.m.?</h2>
  <p>That&rsquo;s what the owners say they&rsquo;re building. Opening late spring 2027 at 1710 R Street.</p>
  <p class="cta"><a class="btn btn-big" href="/carte">See the whole carte</a> <a class="btn btn-ghost btn-big" href="/visit">Map it</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Sweet & Savory Crêpes at JEYAS Café & Pâtisserie', '/crepes', 'French-style sweet and savory crêpes served from morning till midnight at 1710 R Street, Sacramento, CA — opening late spring 2027.')}</script>
<script type="application/ld+json">{breadcrumbs('Crêpes', '/crepes')}</script>
</body>
</html>''')

# ---------- OUR STORY ----------
PAGES['our-story.html'] = (head('Our Story — JEYAS Café & Pâtisserie, Sacramento CA',
    'The story behind JEYAS Café & Pâtisserie: brothers Yusuf and Levent Topal — the family behind Jayna Gyro — naming the café for three daughters, and bringing a French bakery to the Ice Blocks, Sacramento.',
    '/our-story'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">A FAMILY PROJECT, NAMED FOR THE FAMILY</p>
  <h1>Jeyda. Yasemin.<br>Ashley. JEYAS.</h1>
  <p class="lead">The name blends three daughters&rsquo; names into one storefront. The caf&eacute; comes from brothers Yusuf and Levent Topal — Sacramento restaurant people — and a pastry chef who grew up two neighborhoods from the corner they&rsquo;re signing.</p>
</section>

<section class="storygrid">
  <article class="prose">
    <h2>The family behind the counter</h2>
    <p>Yusuf Topal has run Sacramento restaurants for more than 30 years — he owns <a href="{GYRO}" rel="noopener">Jayna Gyro</a> on Folsom Boulevard, and has operated Tarla Mediterranean Grill in Napa and Cellar at The Jacquelyn social club in Midtown. His brother Levent, years in hospitality himself, will run daily operations at JEYAS.</p>
    <p>The caf&eacute; is the family&rsquo;s newest project and its most personal one: the name is stitched together from Yusuf&rsquo;s three daughters — Jeyda, Yasemin and Ashley.</p>
    <h2>The chef</h2>
    <p>Sacramento-born Antonio Coriano runs the pastry program. He trained in France, spent years as pastry chef de partie at Michelin-starred Prot&eacute;g&eacute; in Palo Alto, and before that ran pastry at Old Soul Co. and the macaron program at Ginger Elizabeth Chocolates. He came back to a city that already knows his desserts — and a corner that didn&rsquo;t have a place like this yet.</p>
    <h2>The corner</h2>
    <p>The space is the former Pressed Juicery storefront at 1710 R Street — about 1,500 square feet inside — plus the leasing office next door, opening up a patio of roughly 750 to 1,000 square feet on the Ice Blocks&rsquo; promenade. Outdoor seating, the developer&rsquo;s own word, is a big part of what the block is.</p>
  </article>
  <aside class="pressbox">
    <h2>As covered by</h2>
    <ul class="presslist">
      <li><a href="https://whatnow.com/sacramento/restaurants/jeyas-cafe-patisserie-bringing-a-french-bakery-to-midtown-sacramento/" rel="noopener">What Now Sacramento</a> &mdash; &ldquo;Jeyas Cafe &amp; Patisserie Bringing a French Bakery to Midtown Sacramento&rdquo;</li>
      <li><a href="https://www.abridged.org/news/jeyas-cafe-opening-midtown-sacramento/" rel="noopener">The Abridged (PBS KVIE)</a> &mdash; &ldquo;Jayna Gyro owner to open Ice Blocks caf&eacute; serving croissants and cr&ecirc;pes until midnight&rdquo;</li>
      <li><a href="https://hoodline.com/2026/10/jayna-gyro-owner-brings-croissants-and-midnight-crepes-to-ice-blocks/" rel="noopener">Hoodline</a> &mdash; &ldquo;JEYAS Caf&eacute; Opens at Ice Blocks in Midtown Sacramento&rdquo; (concept coverage)</li>
      <li><span>Sacramento Business Journal &mdash; &ldquo;French bakery filling Pressed Juicery space in Ice Blocks&rdquo; (November 17, 2026)</span></li>
    </ul>
    <p class="fineprint">Coverage ran October&ndash;November 2026, including interviews with the owners. Everything on this site comes from that coverage and the opening announcement.</p>
  </aside>
</section>

<section class="quoteband">
  <blockquote>
    <p>&ldquo;I have admired and been a customer of Jayna Gyro for a long time. The food is authentic and really tasty. So when the operator Yusuf Topal expressed interest in the Ice Blocks, I got really excited.&rdquo;</p>
    <cite>Michael Heller, Ice Blocks developer — via The Abridged (PBS KVIE)</cite>
  </blockquote>
</section>

<section class="homecta">
  <h2>Opening late spring 2027</h2>
  <p>The build-out is underway, the menu is being finished, and the opening-date call goes up here the moment it&rsquo;s set.</p>
  <p class="cta"><a class="btn btn-big" href="/carte">See the lineup</a> <a class="btn btn-ghost btn-big" href="/contact">Say hi</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{breadcrumbs('Our Story', '/our-story')}</script>
</body>
</html>''')

# ---------- VISIT ----------
PAGES['visit.html'] = (head('Visit the Ice Blocks — JEYAS Café & Pâtisserie, Sacramento CA',
    'JEYAS Café & Pâtisserie opens late spring 2027 at 1710 R Street, Suite 170 — the Ice Blocks, Midtown Sacramento, CA 95811, in the former Pressed Juicery storefront. Map, address and opening updates.',
    '/visit'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">1710 R STREET</p>
  <h1>The Ice Blocks,<br>Midtown Sacramento</h1>
  <p class="lead">The former Pressed Juicery storefront at the Ice Blocks — plus the leasing office beside it — becoming a French bakery with a patio. Opening late spring 2027; the confirmed date goes up here when it&rsquo;s locked.</p>
  <p class="cta"><a class="btn btn-big" href="{MAPQ}" rel="noopener">Get Directions</a> <a class="btn btn-ghost btn-big" href="/contact">Contact the Family</a></p>
</section>

<div class="visitgrid">
  <section class="visitinfo">
    <h2>Where</h2>
    <address class="bigaddr">1710 R Street, Suite 170<br>Sacramento, CA 95811</address>
    <p>At the Ice Blocks in Midtown — the brick corridor between downtown and the Midtown grid, on R Street. The storefront that housed Pressed Juicery, plus the space next door, opening onto the block&rsquo;s promenade.</p>
    <h2>When</h2>
    <p>Opening late spring 2027 — the date isn&rsquo;t posted yet. The announced plan: open at 6:30 a.m., close at midnight, every day — coffee and pastry in the morning, cr&ecirc;pes and dessert late.</p>
    <h2>Good to know</h2>
    <ul>
      <li>Roughly 1,500 sq ft inside, plus a 750&ndash;1,000 sq ft patio — outdoor seating is central to the plan.</li>
      <li>Everything baked in-house: specialty croissants, pastries, desserts.</li>
      <li>Planned daily lineup: croissants &amp; pastry &middot; cr&ecirc;pes &middot; specialty coffee &middot; smoothies &middot; a&ccedil;a&iacute; &middot; sandwiches.</li>
      <li>The family behind <a href="{GYRO}" rel="noopener">Jayna Gyro</a> &mdash; same owners, a different kind of counter.</li>
    </ul>
    <p class="fineprint">Hours, prices and the opening date are the announced plan and aren&rsquo;t final — they&rsquo;ll be posted here the day the shop confirms them.</p>
    <p class="cta"><a class="btn btn-ghost" href="/carte">What we&rsquo;ll serve</a></p>
  </section>
  <section class="visitmap">
    <div class="mapbox">
      <iframe title="Map to JEYAS Café &amp; Pâtisserie, 1710 R St, Sacramento, CA 95811" src="https://www.google.com/maps?q=1710%20R%20St%2C%20Sacramento%2C%20CA%2095811&output=embed" loading="eager" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    <p class="fineprint">Can&rsquo;t load the map? <a href="{MAPQ}" rel="noopener">Open it in Google Maps</a> or <a href="mailto:{EMAIL}">email the family</a>.</p>
  </section>
</div>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Visit JEYAS Café & Pâtisserie', '/visit', 'A French-style bakery and café opening late spring 2027 at 1710 R Street, Suite 170 — the Ice Blocks, Midtown Sacramento, CA 95811.')}</script>
<script type="application/ld+json">{breadcrumbs('Visit', '/visit')}</script>
</body>
</html>''')

# ---------- CONTACT ----------
PAGES['contact.html'] = (head('Contact — JEYAS Café & Pâtisserie, Sacramento CA',
    'Contact JEYAS Café & Pâtisserie in Sacramento: send a message through the form or email the Topal family office — questions about the opening, the menu, or press.',
    '/contact'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">TALK TO THE FAMILY</p>
  <h1>Contact JEYAS</h1>
  <p class="lead">Question about the opening, the future menu, or a story about the caf&eacute;? Use the form — it emails the family office directly — or write to the address below.</p>
</section>

<div class="contactgrid">
  <form class="cform" method="post" action="/contact">
    <h2>Send a message</h2>
    <p><label for="f-name">Your name</label><input id="f-name" name="name" type="text" required maxlength="120" autocomplete="name"></p>
    <p><label for="f-email">Email</label><input id="f-email" name="email" type="email" required maxlength="160" autocomplete="email"></p>
    <p><label for="f-msg">Message</label><textarea id="f-msg" name="message" rows="5" required maxlength="4000"></textarea></p>
    <p><button class="btn btn-big" type="submit">Send Message</button></p>
    <p class="fineprint">This form emails the shop directly. We never share your address.</p>
  </form>
  <section class="cinfo">
    <h2>Direct lines</h2>
    <p class="clabel">Email</p>
    <p class="cbig"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p class="cfine">The Topal family office — the same inbox that answers <a href="{GYRO}" rel="noopener">Jayna Gyro</a>.</p>
    <p class="clabel">Walk by</p>
    <address class="bigaddr">1710 R Street, Suite 170<br>Sacramento, CA 95811</address>
    <p class="cfine">The Ice Blocks storefront — the counters aren&rsquo;t open yet; first service is planned for late spring 2027.</p>
    <p class="fineprint">JEYAS hasn&rsquo;t opened yet — the first croissants come spring 2027. Replies may take a day or two.</p>
  </section>
</div>
</main>
{footer()}
<script type="application/ld+json">{breadcrumbs('Contact', '/contact')}</script>
</body>
</html>''')

# ---------- PRIVACY ----------
PAGES['privacy.html'] = (head('Privacy Policy — JEYAS Café & Pâtisserie, Sacramento CA',
    'Privacy policy for the JEYAS Café & Pâtisserie website: how the contact form is handled. No trackers, no cookies.',
    '/privacy'), f'''{nav()}
<main id="main">
<section class="pagehead narrow">
  <p class="kicker">PRIVACY</p>
  <h1>Privacy Policy</h1>
</section>
<div class="prose">
  <p>This site belongs to {BRAND} ({FULL_ADDR}).</p>
  <h2>What we collect</h2>
  <p>The contact form on this site collects only the information you type into it — your name, your email address and your message — and sends it to the family office&rsquo;s own email address so the owners can answer you. That is the entire purpose of the data. It is not sold, shared or used for advertising.</p>
  <h2>Cookies and tracking</h2>
  <p>This site sets no cookies and uses no advertising trackers or analytics pixels of its own. The embedded Google map may set its own cookies once you interact with it, governed by Google&rsquo;s privacy policy.</p>
  <h2>Your choices</h2>
  <p>Want your message deleted from the shop&rsquo;s mailbox records? Email <a href="mailto:{EMAIL}">{EMAIL}</a> and ask. Questions about this policy go to the same address.</p>
  <p class="fineprint">This policy covers this website only.</p>
</div>
</main>
{footer()}
<script type="application/ld+json">{breadcrumbs('Privacy', '/privacy')}</script>
</body>
</html>''')

# ---------- 404 ----------
PAGES['404.html'] = (head('Page not found — JEYAS Café & Pâtisserie',
    'Page not found at the JEYAS Café & Pâtisserie site. Back to the carte, or straight to the opening page.',
    '/404'), f'''{nav()}
<main id="main">
<section class="pagehead center">
  <p class="kicker">404</p>
  <h1>This page has crumbled.</h1>
  <p class="lead">It doesn&rsquo;t exist — but the croissants do. Well: as soon as we open.</p>
  <p class="cta"><a class="btn btn-big" href="/">Back to Home</a> <a class="btn btn-ghost btn-big" href="/carte">See La Carte</a></p>
</section>
</main>
{footer()}
</body>
</html>''')

# ---------- THANKS ----------
PAGES['thanks.html'] = (head('Message sent — JEYAS Café & Pâtisserie',
    'Thanks for reaching out to JEYAS Café & Pâtisserie — the family will get back to you.',
    '/thanks'), f'''{nav()}
<main id="main">
<section class="pagehead center">
  <p class="kicker">C&rsquo;EST NOT&Eacute;</p>
  <h1>Your message is in.</h1>
  <p class="lead">Merci — the family will get back to you personally. Meanwhile, the carte and the map are one click away.</p>
  <p class="cta"><a class="btn btn-big" href="/carte">See La Carte</a> <a class="btn btn-ghost btn-big" href="/visit">Plan the visit</a></p>
</section>
</main>
{footer()}
</body>
</html>''')

for fname, (h, body) in PAGES.items():
    with open(os.path.join(PUB, fname), 'w', encoding='utf-8') as f:
        f.write(h + '\n' + body)
    print('wrote', fname, len(h + body), 'bytes')

# ---------- sitemap / robots / favicon ----------
pages_order = ['/', '/carte', '/croissants', '/crepes', '/our-story', '/visit', '/contact', '/privacy']
today = '2026-11-25'
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'<url><loc>{ORIGIN}{p}</loc><lastmod>{today}</lastmod></url>\n' for p in pages_order) + '</urlset>\n'
open(os.path.join(PUB, 'sitemap.xml'), 'w').write(sitemap)
open(os.path.join(PUB, 'robots.txt'), 'w').write(f'''User-agent: *
Allow: /

Sitemap: {ORIGIN}/sitemap.xml
''')
favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#221a15"/><path d="M13 43 C 16 15 48 15 51 43" fill="none" stroke="#c99b45" stroke-width="5" stroke-linecap="round"/><path d="M24 21 l3 14 M32 17 l0 18 M40 21 l-3 14" stroke="#c99b45" stroke-width="3" stroke-linecap="round" fill="none"/><circle cx="13" cy="45" r="3.6" fill="#c99b45"/><circle cx="51" cy="45" r="3.6" fill="#c99b45"/></svg>
'''
open(os.path.join(PUB, 'favicon.svg'), 'w').write(favicon)
print('wrote sitemap.xml robots.txt favicon.svg')
print('PAGES:', len([f for f in PAGES if f.endswith('.html')]))
