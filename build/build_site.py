#!/usr/bin/env python3
"""Rebuilds the catalogue site. Run from anywhere:  python3 build/build_site.py
Writes index.html at the repo root, with every photo embedded in the file."""
import base64, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
EMBED = os.path.join(HERE, "photos")
S = HERE
_cache = {}
def img64(name):
    if name not in _cache:
        with open(os.path.join(EMBED, name + ".jpg"), "rb") as f:
            _cache[name] = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
    return _cache[name]

def logo64():
    for p in (os.path.join(HERE, "logo.jpg"),):
        if os.path.exists(p):
            mime = "png" if p.endswith("png") else "jpeg"
            with open(p, "rb") as f:
                return f"data:image/{mime};base64," + base64.b64encode(f.read()).decode()
    return None

CATS = [
    ("seating", "Seating"),
    ("tables", "Tables & Desks"),
    ("cabinets", "Cabinets & Sideboards"),
    ("bedroom", "The Cherry Bedroom Suite"),
    ("lighting", "Lighting"),
    ("mirrors", "Mirrors"),
    ("fireplace", "Fireplace & Metalware"),
    ("rugs", "Rugs & Carpets"),
    ("art", "Paintings & Prints"),
]

ITEMS = [
 ("seating", "Victorian Mahogany Armchair",
  "Victorian mahogany open armchair upholstered in blue silk with a gold fleur-de-lis pattern. Button back, scrolled arms and turned front legs on brass castors.",
  ["IMG_9998","IMG_9999","IMG_0001","IMG_0002"]),
 ("seating", "Matching Fleur-de-Lis Footstool",
  "The armchair's matching footstool in the same blue fleur-de-lis silk, on turned mahogany legs with brass castors.",
  ["IMG_0003","IMG_0004","IMG_0005"]),
 ("seating", "Set of Six Dining Chairs",
  "Set of six mahogany dining chairs with arched, crossbanded and inlaid backs and upholstered seats, on square tapered legs with spade feet. Four side chairs and two carvers with arm rests.",
  ["IMG_9955","IMG_9956"]),
 ("tables", "Leather-Top Pedestal Desk",
  "Mahogany twin-pedestal desk with a gilt-tooled burgundy leather top and brass swan-neck handles, on bracket feet. Splits into three sections for moving.",
  ["IMG_0010","IMG_0006","IMG_0008","IMG_0012","IMG_0007","IMG_0009"]),
 ("tables", "Octagonal Burr Walnut Centre Table",
  "Octagonal burr walnut table with crossbanded borders, turned column supports and splayed legs. Photographed in its shipping crate with its wrapped tops and pedestal sections.",
  ["IMG_4036","IMG_4035","IMG_4037","IMG_4038","2ABFB7D6-6DA3-486E-9E46-DF19FAD7D658","IMG_0023","IMG_0024"]),
 ("tables", "Mahogany Console Table",
  "Mahogany console table with a frieze drawer, on fluted baluster supports joined by a turned stretcher, with scroll feet.",
  ["IMG_9954","IMG_9952","IMG_9953"]),
 ("tables", "Drop-Leaf Work Table",
  "Mahogany drop-leaf work table with two drawers, on sabre legs with castors.",
  ["IMG_9949","IMG_9950","IMG_9951"]),
 ("tables", "Georgian Side Table",
  "Mahogany single-drawer side table on square tapered legs joined by a stretcher.",
  ["IMG_9980","IMG_9981"]),
 ("tables", "Tripod Wine Table",
  "Mahogany wine table with a circular top on a turned column and tripod base.",
  ["IMG_9977"]),
 ("tables", "Marble-Top Cast Iron Table",
  "Green-painted cast iron table base with its own round marble top in white with grey veining, photographed in its packing case.",
  ["IMG_0028","IMG_MARBLETOP"]),
 ("cabinets", "Bow-Front Cocktail Cabinet",
  "Bow-fronted mahogany cocktail cabinet with a mirrored interior, twin doors and ball-and-claw feet.",
  ["IMG_0022","IMG_0016","IMG_0017","IMG_0018","IMG_0019","IMG_0020","IMG_0021"]),
 ("cabinets", "Demi-Lune Sideboard",
  "Demi-lune mahogany sideboard with two frieze drawers over cupboard doors, on square tapered legs with spade feet.",
  ["IMG_0026","IMG_0025","IMG_0027"]),
 ("bedroom", "Cherry Wood Sleigh Bed",
  "French style cherry wood sleigh bed, photographed disassembled for transport. Headboard, footboard, rails and slats are all present.",
  ["IMG_9958","IMG_9959","IMG_9960","IMG_9961","IMG_9968","IMG_9969","IMG_9970","IMG_9971","IMG_9972","IMG_9979","IMG_9988","IMG_9989"]),
 ("bedroom", "Cherry Wood Armoire",
  "Cherry wood armoire with arched panel doors, a fitted interior with tie rack and a shaped cornice. Photographed disassembled for transport.",
  ["IMG_9964","IMG_9962","IMG_9963","IMG_9965","IMG_9966","IMG_9967","IMG_9990"]),
 ("bedroom", "Cherry Wood Chest of Drawers",
  "Cherry wood chest of three long drawers in the same French style, with key and tassel.",
  ["IMG_9974","IMG_9973","IMG_9975","IMG_9976","IMG_9982"]),
 ("lighting", "Brass Chandelier with Raspberry Shades",
  "Large multi-arm brass chandelier with two tiers of arms and pleated raspberry silk shades, photographed during unpacking.",
  ["IMG_0039","IMG_0043","IMG_0041","IMG_0042","IMG_0040"]),
 ("lighting", "Set of Six Twin-Arm Wall Lights",
  "Six gilt brass twin-arm wall lights with rope-twist arms and pleated raspberry shades, matching the chandelier.",
  ["IMG_0036","IMG_0037","IMG_0038"]),
 ("lighting", "Brass Barley-Twist Table Lamp",
  "Brass barley-twist table lamp with a pleated cream shade.",
  ["IMG_9957"]),
 ("mirrors", "Serpentine Giltwood Overmantel Mirror",
  "Large serpentine giltwood overmantel mirror with carved shell cresting. Maker's label to the reverse: Made in Belgium, ref. 0979.211.",
  ["IMG_4040","IMG_4039","IMG_4041","IMG_4042","IMG_4043","IMG_4044"]),
 ("mirrors", "Arch-Top Giltwood Mantle Mirror",
  "Arch-topped giltwood mantle mirror, retailed by Sandringham Fine Arts Ltd of Harrogate (label to reverse).",
  ["IMG_9992","IMG_9991","IMG_9993","IMG_9994","IMG_9995","IMG_9996","IMG_9997"]),
 ("fireplace", "Mahogany Coal Purdonium",
  "Victorian mahogany coal purdonium with brass handle and metal liner.",
  ["IMG_0013","IMG_0014","IMG_0015"]),
 ("fireplace", "Copper Helmet Coal Scuttle",
  "Copper helmet coal scuttle with shovel.",
  ["IMG_0031","IMG_0032"]),
 ("fireplace", "Fireside Companion Set",
  "Wrought iron fireside companion set on stand.",
  ["IMG_0033"]),
 ("fireplace", "Brass Fireplace Fender",
  "Brass and iron fireplace fender.",
  ["IMG_9986","IMG_9987"]),
 ("rugs", "Carmel 'Royal' Wool Carpet",
  "Large cream and brown geometric wool carpet by Carmel Carpets ('Royal' range, made in Israel).",
  ["IMG_4046","IMG_4047"]),
 ("rugs", "Persian Medallion Carpet",
  "Large red-ground Persian carpet with central medallion in reds and blues.",
  ["IMG_4052","IMG_4053","IMG_4055","IMG_4056","IMG_4057"]),
 ("art", "Shipping off Hove (Warde, 1870)",
  "Oil on canvas of sailing vessels in heavy seas beneath white cliffs. Signed in red 'Warde 1870, Hove' with an anchor motif. Ornate giltwood frame.",
  ["IMG_4033","IMG_0044","IMG_0045","IMG_4032"]),
 ("art", "Patrick Cullen, 'French Windows'",
  "Signed limited edition print, numbered 389/760 and pencil-signed by the artist, with certificate of authenticity.",
  ["IMG_4022","IMG_4017","IMG_4020","IMG_4019","IMG_4021","IMG_4045"]),
 ("art", "G.C. Winter, 'The End of a Perfect Day'",
  "Watercolour dated 1927, titled 'The End of a Perfect Day, 4 Miles to Horley Station', in a dark wood frame.",
  ["IMG_4023","IMG_4024","IMG_4025"]),
 ("art", "G.C. Winter, The Old Inn",
  "Companion watercolour of an old inn, its walls signed 'Billiards' and 'Noakes & Co Ales'.",
  ["IMG_4026","IMG_4027"]),
 ("art", "H. Adams, Silver Birches by a Lake",
  "Oil on canvas of silver birches at the water's edge in autumn, signed, in an ornate gilt frame.",
  ["IMG_4028","IMG_4029"]),
 ("art", "H. Adams, Lakeside at Sunset",
  "The companion oil: the same lakeside under an orange evening sky, signed, in a matching gilt frame.",
  ["IMG_4030","IMG_4031"]),
 ("art", "'London Bridge from Southwark Bridge'",
  "Hand-coloured panoramic engraving of the Thames, 'London Bridge &c. from Southwark Bridge'.",
  ["IMG_4009","IMG_4010"]),
 ("art", "'Blackfriars from Southwark Bridge'",
  "Hand-coloured panoramic engraving of the Thames with St Paul's beyond, from the same series.",
  ["IMG_4012"]),
 ("art", "Thames Panorama Engraving",
  "A further hand-coloured Thames panorama engraving from the same series.",
  ["IMG_4013","IMG_4014"]),
 ("art", "Thatched Cottage Watercolour",
  "Watercolour of a thatched cottage in a country garden, signed, in a gilt frame.",
  ["IMG_4011"]),
]

STORY_HTML = '''<p class="pagenote">Each item is numbered, please quote it in any enquiry, click a photo to enlarge and use the arrows to browse</p>'''

CONTACT_HTML = '''<div class="contactcard">
    <p class="eyebrow">Enquiries</p>
    <h2>Get in touch</h2>
    <p>Contact the family with any questions about the collection, including condition, dimensions, viewing or sale with the button below.</p>
    <p>Please quote the item number shown on each photograph</p>
    <a class="mailbtn" href="mailto:bridget.magee@gmail.com?subject=Catalogue%20enquiry">Email</a>
  </div>'''

SHARED_JS = '''<script>
(function() {
  var TABS = ['showroom', 'gallery', 'contacts'];
  function selectTab(which) {
    TABS.forEach(function(k) {
      var on = (k === which);
      document.getElementById('tab-' + k).setAttribute('aria-selected', on ? 'true' : 'false');
      document.getElementById('panel-' + k).hidden = !on;
    });
    window.scrollTo(0, 0);
  }
  TABS.forEach(function(k) {
    document.getElementById('tab-' + k).addEventListener('click', function() { selectTab(k); });
  });

  var root = document.documentElement;
  var tbtn = document.getElementById('themetoggle');
  function effective() {
    var t = root.getAttribute('data-theme');
    if (t) return t;
    return (window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches) ? 'dark' : 'light';
  }
  function paintBtn() { tbtn.textContent = effective() === 'dark' ? '\\u2600\\uFE0E' : '\\u263D'; }
  try {
    var saved = localStorage.getItem('magee-theme');
    if (saved === 'light' || saved === 'dark') root.setAttribute('data-theme', saved);
  } catch (e) {}
  paintBtn();
  tbtn.addEventListener('click', function() {
    var next = effective() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('magee-theme', next); } catch (e) {}
    paintBtn();
  });

  // Carousels: visibility is controlled with inline styles only, so no
  // stylesheet processing can ever show more than one slide at a time.
  function show(car, idx) {
    var slides = car.querySelectorAll('.slide');
    var n = slides.length;
    idx = ((idx % n) + n) % n;
    slides.forEach(function(s, i) { s.style.display = (i === idx) ? 'block' : 'none'; });
    car.dataset.idx = idx;
    var count = car.querySelector('.count');
    if (count) count.textContent = (idx + 1) + ' / ' + n;
  }
  document.querySelectorAll('.carousel').forEach(function(car) {
    show(car, 0);
    var prev = car.querySelector('.prev'), next = car.querySelector('.next');
    if (prev) prev.addEventListener('click', function(e) { e.stopPropagation(); show(car, +car.dataset.idx - 1); });
    if (next) next.addEventListener('click', function(e) { e.stopPropagation(); show(car, +car.dataset.idx + 1); });
  });

  var lb = document.getElementById('lightbox');
  var lbimg = document.getElementById('lbimg');
  var lbcap = document.getElementById('lbcap');
  var cur = { car: null, idx: 0 };
  function setLb() {
    var slides = cur.car.querySelectorAll('.slide');
    var card = cur.car.closest('.card');
    lbimg.src = slides[cur.idx].src;
    lbimg.alt = slides[cur.idx].alt;
    lbcap.textContent = 'No. ' + card.querySelector('.numchip').textContent + ' \\u00B7 ' + slides[cur.idx].alt;
  }
  function openLb(car, idx) {
    cur.car = car; cur.idx = idx;
    show(car, idx); setLb();
    lb.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function stepLb(d) {
    if (!cur.car) return;
    var n = cur.car.querySelectorAll('.slide').length;
    cur.idx = ((cur.idx + d) % n + n) % n;
    setLb(); show(cur.car, cur.idx);
  }
  function closeLb() {
    lb.classList.remove('open');
    document.body.style.overflow = '';
  }
  document.querySelectorAll('.carousel .slide').forEach(function(img) {
    img.addEventListener('click', function() {
      var car = img.closest('.carousel');
      openLb(car, +car.dataset.idx);
    });
  });
  lb.querySelector('.lbprev').addEventListener('click', function() { stepLb(-1); });
  lb.querySelector('.lbnext').addEventListener('click', function() { stepLb(1); });
  lb.querySelector('.lbclose').addEventListener('click', closeLb);
  lb.querySelector('.lbgoto').addEventListener('click', function() {
    if (!cur.car) return;
    var id = cur.car.closest('.card').id;
    closeLb(); selectTab('showroom');
    var el = document.getElementById(id);
    if (el) el.scrollIntoView({ block: 'center' });
  });
  lb.addEventListener('click', function(e) { if (e.target === lb) closeLb(); });
  document.addEventListener('keydown', function(e) {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') closeLb();
    if (e.key === 'ArrowLeft') stepLb(-1);
    if (e.key === 'ArrowRight') stepLb(1);
  });

  // Gallery: built from the showroom photos so the page carries each image once.
  var masonry = document.getElementById('masonry');
  if (masonry) {
    document.querySelectorAll('#panel-showroom .card').forEach(function(card) {
      var cat = card.closest('section.cat').id.replace('cat-', '');
      card.querySelectorAll('.slide').forEach(function(s, i) {
        var im = document.createElement('img');
        im.src = s.src; im.alt = s.alt;
        im.className = 'gimg'; im.dataset.cat = cat;
        im.addEventListener('click', function() { openLb(card.querySelector('.carousel'), i); });
        masonry.appendChild(im);
      });
    });
    document.querySelectorAll('.fchip').forEach(function(ch) {
      ch.addEventListener('click', function() {
        document.querySelectorAll('.fchip').forEach(function(c) { c.classList.remove('on'); });
        ch.classList.add('on');
        var cat = ch.dataset.cat;
        document.querySelectorAll('.gimg').forEach(function(g) {
          g.style.display = (cat === 'all' || g.dataset.cat === cat) ? '' : 'none';
        });
      });
    });
  }

  var form = document.getElementById('msgform');
  if (form) form.addEventListener('submit', function(e) {
    e.preventDefault();
    document.getElementById('msgstatus').textContent = 'Message sending is not connected yet. It will be linked to an email soon.';
  });
})();
</script>'''

ANIM_JS = '''<script>
(function() {
  document.documentElement.classList.add('anim');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es) {
      es.forEach(function(e) {
        if (e.isIntersecting) { e.target.classList.add('vis'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.card').forEach(function(c, i) {
      c.style.transitionDelay = (i % 3) * 70 + 'ms';
      io.observe(c);
    });
  } else {
    document.querySelectorAll('.card').forEach(function(c) { c.classList.add('vis'); });
  }
})();
</script>'''

LIGHTBOX_HTML = '''<div class="lb" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer">
  <img id="lbimg" src="" alt="">
  <div class="lbcap" id="lbcap"></div>
  <button class="lbprev" type="button" aria-label="Previous photo">&#8249;</button>
  <button class="lbnext" type="button" aria-label="Next photo">&#8250;</button>
  <button class="lbclose" type="button" aria-label="Close">&#10005;</button>
  <button class="lbgoto" type="button">View item</button>
</div>'''

LB_CSS = '''.lb { position:fixed; inset:0; z-index:100; background:rgba(10,10,10,.93); display:none; align-items:center; justify-content:center; }
.lb.open { display:flex; }
.lb img { max-width:92vw; max-height:84vh; object-fit:contain; border-radius:8px; }
.lb .lbcap { position:absolute; bottom:18px; left:50%; transform:translateX(-50%); color:#EEE; font-size:12px; letter-spacing:.06em; background:rgba(0,0,0,.55); padding:5px 12px; border-radius:20px; max-width:70vw; text-align:center; }
.lb button { position:absolute; background:rgba(255,255,255,.12); color:#EEE; border:none; cursor:pointer; border-radius:8px; }
.lb button:hover { background:rgba(255,255,255,.25); }
.lb .lbclose { top:16px; right:16px; width:42px; height:42px; font-size:20px; }
.lb .lbprev, .lb .lbnext { top:50%; transform:translateY(-50%); width:44px; height:64px; font-size:28px; }
.lb .lbprev { left:14px; } .lb .lbnext { right:14px; }
.lb .lbgoto { bottom:16px; right:16px; padding:9px 16px; font-size:12px; letter-spacing:.08em; }'''

ANIM_CSS = '''
@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior:smooth; }
  body { transition: background-color .35s ease, color .35s ease; }
  .card, .tabs, .contactcard, .jumps a, .fchip, .tabs button, .themetoggle, .msgform input, .msgform textarea, .msgform button { transition: background-color .3s ease, color .3s ease, border-color .3s ease, transform .3s ease, box-shadow .3s ease; }
  .anim .card { opacity:0; transform:translateY(16px); transition: opacity .55s ease, transform .55s ease, background-color .3s ease; }
  .anim .card.vis { opacity:1; transform:translateY(0); }
  .lb.open { animation: lbfade .2s ease; }
  .lb.open img { animation: lbzoom .24s ease; }
  @keyframes lbfade { from { opacity:0; } to { opacity:1; } }
  @keyframes lbzoom { from { transform:scale(.965); opacity:.5; } to { transform:scale(1); opacity:1; } }
  .gimg { transition: transform .3s ease, box-shadow .3s ease; }
  .gimg:hover { transform:translateY(-4px) scale(1.015); box-shadow:0 10px 26px rgba(0,0,0,.16); }
  .jumps a:hover, .fchip:hover { transform:translateY(-1px); }
  .cnav { transition: opacity .25s ease, background-color .25s ease; }
}'''


def build_cards():
    cards_by_cat = {c[0]: [] for c in CATS}
    n = 0; photos = 0
    for cat, title, desc, imgs in ITEMS:
        n += 1
        num = f"{n:02d}"
        slides = []
        for i, name in enumerate(imgs):
            photos += 1
            style = "" if i == 0 else ' style="display:none"'
            slides.append(f'<img class="slide"{style} src="{img64(name)}" alt="{html.escape(title)}, photo {i+1} of {len(imgs)}">')
        nav = ""
        if len(imgs) > 1:
            nav = ('<button class="cnav prev" type="button" aria-label="Previous photo">&#8249;</button>'
                   '<button class="cnav next" type="button" aria-label="Next photo">&#8250;</button>'
                   f'<span class="count">1 / {len(imgs)}</span>')
        cards_by_cat[cat].append(f'''<article class="card" id="item-{num}">
  <div class="carousel" data-idx="0" role="group" aria-label="{html.escape(title)} photos">
    <span class="numchip">{num}</span>
    {''.join(slides)}
    {nav}
  </div>
  <div class="cardbody">
    <h3>{html.escape(title)}</h3>
    <p>{html.escape(desc)}</p>
  </div>
</article>''')
    sections, jumps = [], []
    for slug, label in CATS:
        cards = cards_by_cat[slug]
        jumps.append(f'<a class="jump" href="#cat-{slug}">{html.escape(label)}</a>')
        sections.append(f'''<section class="cat" id="cat-{slug}">
  <header class="cathead"><h2>{html.escape(label)}</h2><span class="catcount">{len(cards)}</span></header>
  <div class="grid">{''.join(cards)}</div>
</section>''')
    return ''.join(sections), ''.join(jumps), n, photos


def page(title, fonts_href, css, anim=False):
    sections, jumps, n_items, n_photos = build_cards()
    story = STORY_HTML
    logo_html = ''
    chips = '<button type="button" class="fchip on" data-cat="all">All</button>' + ''.join(
        f'<button type="button" class="fchip" data-cat="{slug}">{html.escape(label)}</button>' for slug, label in CATS)
    anim_css = ANIM_CSS if anim else ''
    anim_js = ANIM_JS if anim else ''
    return f'''<meta charset="utf-8">
<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="{fonts_href}">
<style>{css}
{LB_CSS}
{anim_css}</style>
<header class="masthead">
  <div class="brand">{logo_html}<h1>Private Family Catalogue</h1></div>
  <p class="sub">Furniture, lighting, mirrors, rugs &amp; paintings</p>
</header>
<nav class="tabs" role="tablist" aria-label="Site sections">
  <button role="tab" id="tab-showroom" aria-selected="true" aria-controls="panel-showroom">Showroom</button>
  <button role="tab" id="tab-gallery" aria-selected="false" aria-controls="panel-gallery">Gallery</button>
  <button role="tab" id="tab-contacts" aria-selected="false" aria-controls="panel-contacts">Contacts</button>
  <button type="button" id="themetoggle" class="themetoggle" aria-label="Switch between light and dark view"></button>
</nav>
<main class="wrap">
<div id="panel-showroom" role="tabpanel">
  {story}
  <nav class="jumps" aria-label="Categories">{jumps}</nav>
  {sections}
</div>
<div id="panel-gallery" role="tabpanel" hidden>
  <div class="filters" role="group" aria-label="Filter photos by category">{chips}</div>
  <div id="masonry" class="masonry"></div>
</div>
<div id="panel-contacts" role="tabpanel" hidden>
  {CONTACT_HTML}
</div>
</main>
{LIGHTBOX_HTML}
<footer><span>{n_items} items &middot; {n_photos} photographs</span></footer>
{SHARED_JS}
{anim_js}
'''

BASE = '''* { box-sizing:border-box; }
.wrap { max-width:1200px; margin:0 auto; padding:0 24px; }
.brand { display:flex; align-items:center; justify-content:center; gap:16px; }
.brand .logo { height:52px; width:auto; border-radius:10px; display:block; }
.carousel { position:relative; overflow:hidden; background:var(--imgbg); }
.carousel .slide { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); max-width:100%; max-height:100%; width:auto; height:auto; border-radius:12px; cursor:zoom-in; }
.count { position:absolute; bottom:10px; right:10px; z-index:5; font-size:11px; font-variant-numeric:tabular-nums; background:rgba(0,0,0,.55); color:#F5F5F2; padding:3px 8px; border-radius:20px; }
.cnav { position:absolute; top:50%; transform:translateY(-50%); z-index:5; width:32px; height:32px; border:none; border-radius:50%; cursor:pointer; background:rgba(255,255,255,.88); color:#1A1A18; font-size:18px; line-height:1; display:flex; align-items:center; justify-content:center; opacity:0; }
.carousel:hover .cnav, .cnav:focus-visible { opacity:1; }
@media (hover:none) { .cnav { opacity:1; } }
.cnav.prev { left:10px; } .cnav.next { right:10px; }
.cnav:focus-visible { outline:2px solid currentColor; }
.numchip { position:absolute; top:10px; left:10px; z-index:5; font-size:11px; font-weight:600; letter-spacing:.08em; padding:3px 9px; border-radius:8px; }
.grid { display:grid; gap:28px; }
figure { margin:0; }
.story { display:grid; grid-template-columns:minmax(150px,200px) 1fr; gap:28px; align-items:center; }
.story .portrait img { width:100%; display:block; }
@media (max-width:640px) { .story { grid-template-columns:1fr; } .story .portrait { max-width:200px; } }
.jumps { display:flex; flex-wrap:wrap; gap:10px; }
.jumps a { text-decoration:none; }
.themetoggle { position:absolute; right:20px; top:50%; transform:translateY(-50%); width:34px; height:34px; border-radius:50%; cursor:pointer; font-size:16px; line-height:1; display:flex; align-items:center; justify-content:center; }
.tabs { position:sticky; }
.filters { display:flex; flex-wrap:wrap; gap:8px; justify-content:center; padding:30px 0 22px; }
.fchip { cursor:pointer; }
.masonry { columns:4 250px; column-gap:14px; padding-bottom:24px; }
.gimg { width:100%; margin:0 0 14px; border-radius:12px; display:block; break-inside:avoid; cursor:zoom-in; }
.msgform { text-align:left; margin-top:22px; display:flex; flex-direction:column; gap:6px; }
.msgform label { font-size:12px; font-weight:600; letter-spacing:.08em; text-transform:uppercase; margin-top:10px; }
.msgform input, .msgform textarea { font:inherit; padding:10px 12px; border-radius:8px; width:100%; resize:vertical; }
.msgform button { margin-top:14px; font:inherit; font-weight:600; cursor:pointer; padding:11px 22px; border-radius:8px; align-self:flex-start; }
.msgstatus { min-height:1.2em; font-size:13.5px; margin:8px 0 0; }
footer { text-align:center; padding:48px 20px 36px; font-size:12.5px; }
@media (prefers-reduced-motion: reduce) { * { transition:none !important; animation:none !important; } }'''

CATALOGUE_FONTS = "https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Archivo:wght@500;600&display=swap"
CATALOGUE_CSS = BASE + '''
:root { --bg:#F7F4ED; --imgbg:#F7F4ED; --panel:#FDFBF6; --ink:#27211B; --mut:#6A6154; --line:#DCD5C4; --oxb:#7A2E2A; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#1B1712; --imgbg:#1B1712; --panel:#241F19; --ink:#EDE6D8; --mut:#ABA08C; --line:#3A3428; --oxb:#C97F6F; } }
:root[data-theme="dark"] { --bg:#1B1712; --imgbg:#1B1712; --panel:#241F19; --ink:#EDE6D8; --mut:#ABA08C; --line:#3A3428; --oxb:#C97F6F; }
body { margin:0; background:var(--bg); color:var(--ink); font-family:"EB Garamond", Georgia, serif; font-size:17px; line-height:1.6; }
.masthead { text-align:center; padding:26px 24px 0; }
.masthead h1 { font-size:clamp(28px,3.6vw,42px); font-weight:500; letter-spacing:.02em; margin:0; }
.brand .logo { height:46px; }
.masthead .sub { color:var(--mut); font-style:italic; margin:4px 0 0; font-size:15px; }
.masthead:after { content:""; display:block; max-width:380px; margin:14px auto 0; border-top:1px solid var(--line); border-bottom:1px solid var(--line); height:4px; }
.tabs { display:flex; justify-content:center; gap:10px; padding:12px 0 10px; top:0; background:var(--bg); z-index:40; border-bottom:1px solid var(--line); }
.tabs button[role="tab"] { font-family:Archivo, system-ui, sans-serif; font-size:12px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; padding:8px 20px; border:1px solid transparent; border-radius:8px; background:transparent; color:var(--mut); cursor:pointer; }
.tabs button[aria-selected="true"] { color:var(--oxb); border-color:var(--oxb); background:var(--panel); }
.tabs button:focus-visible { outline:2px solid var(--oxb); outline-offset:2px; }
.themetoggle { background:transparent; border:1px solid var(--line); color:var(--oxb); }
.themetoggle:hover { border-color:var(--oxb); }
.story { grid-template-columns:260px 1fr; gap:46px; align-items:center; max-width:960px; margin:0 auto; padding:32px 0 4px; }
.storytext p { font-size:18px; }
.story .portrait img { border-radius:10px; border:1px solid var(--line); padding:5px; background:var(--panel); }
.story .portrait figcaption { color:var(--mut); font-size:13px; font-style:italic; margin-top:8px; text-align:center; }
.eyebrow { font-family:Archivo, system-ui, sans-serif; font-size:11px; font-weight:600; letter-spacing:.24em; text-transform:uppercase; color:var(--oxb); margin:0 0 10px; }
.contactcard h2 { font-size:clamp(26px,3.4vw,38px); font-weight:500; margin:0 0 14px; }
.storytext p { max-width:60ch; margin:0 0 10px; }
.storytext .note { color:var(--mut); font-style:italic; font-size:15px; }
.pagenote { text-align:center; color:var(--mut); font-style:italic; font-size:15px; max-width:60ch; margin:26px auto 0; }
.jumps { justify-content:center; padding:26px 0 4px; }
.jumps a, .fchip { font-family:Archivo, system-ui, sans-serif; color:var(--oxb); font-size:11px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; border:1px solid var(--line); border-radius:8px; padding:8px 15px; background:var(--panel); }
.jumps a:hover, .fchip:hover { border-color:var(--oxb); }
.fchip.on { background:var(--oxb); color:var(--panel); border-color:var(--oxb); }
.cat { padding:38px 0 4px; }
.cathead { display:flex; align-items:baseline; justify-content:space-between; border-bottom:2px solid var(--ink); padding-bottom:8px; margin-bottom:6px; }
.cathead h2 { font-size:clamp(24px,2.8vw,32px); font-weight:500; margin:0; }
.catcount { font-family:Archivo, system-ui, sans-serif; color:var(--mut); font-size:11px; letter-spacing:.14em; }
.grid { grid-template-columns:1fr; gap:0; }
.card { display:grid; grid-template-columns:minmax(280px,380px) 1fr; gap:26px; padding:26px 0; border-bottom:1px solid var(--line); align-items:center; }
@media (max-width:700px) { .card { grid-template-columns:1fr; } }
.carousel { aspect-ratio:4/3; border-radius:14px; }
.numchip { font-family:Archivo, system-ui, sans-serif; background:var(--panel); color:var(--oxb); border:1px solid var(--oxb); }
.cardbody h3 { font-size:24px; font-weight:500; margin:0 0 6px; line-height:1.25; }
.cardbody p { font-size:15.5px; color:var(--mut); margin:0; max-width:60ch; }
#panel-contacts { padding:56px 0; }
.contactcard { max-width:560px; margin:0 auto; background:var(--panel); border:1px solid var(--line); border-radius:14px; padding:42px 36px; }
.contactcard p { color:var(--mut); margin:0 0 10px; }
.mailbtn { display:inline-block; margin-top:16px; font-family:Archivo, system-ui, sans-serif; background:var(--oxb); color:#F7F4ED; text-decoration:none; letter-spacing:.12em; text-transform:uppercase; font-size:12px; font-weight:600; padding:12px 26px; border-radius:8px; }
.mailbtn:hover { opacity:.88; }
footer { color:var(--mut); }
@media (max-width:700px) {
  .wrap { padding:0 16px; }
  .story { grid-template-columns:1fr; gap:16px; text-align:center; padding:22px 0 0; max-width:100%; }
  .story .portrait { max-width:200px; margin:0 auto; }
  .story .portrait figcaption { font-size:12px; }
  .storytext p { font-size:16.5px; margin-left:auto; margin-right:auto; }
  .masthead { padding:18px 16px 0; }
  .masthead h1 { font-size:26px; }
  .brand { gap:10px; }
  .brand .logo { height:38px; }
  .tabs { gap:4px; padding:10px 44px 8px 8px; }
  .tabs button[role="tab"] { padding:7px 11px; font-size:11px; letter-spacing:.08em; }
  .themetoggle { right:8px; width:30px; height:30px; font-size:14px; }
  .jumps { gap:8px; padding:18px 0 2px; }
  .jumps a, .fchip { padding:7px 12px; font-size:10.5px; }
  .cat { padding:28px 0 2px; }
  .cathead h2 { font-size:22px; }
  .card { gap:16px; padding:20px 0; }
  .cardbody h3 { font-size:21px; }
  .cardbody p { font-size:15px; }
  .contactcard { padding:32px 22px; }
  .lb .lbcap { bottom:70px; max-width:86vw; }
  .lb .lbgoto { bottom:14px; right:50%; transform:translateX(50%); }
  footer { padding:34px 16px 26px; }
}'''

main = page("Private Family Catalogue", CATALOGUE_FONTS, CATALOGUE_CSS, anim=True)
cut = main.index('</style>') + len('</style>')
standalone = ('<!doctype html>\n<html lang="en">\n<head>\n' + main[:cut]
              + '\n</head>\n<body>\n' + main[cut:] + '\n</body>\n</html>\n')
out = os.path.join(REPO, "index.html")
with open(out, "w") as f:
    f.write(standalone)
print(f"wrote {out} ({os.path.getsize(out)/1024/1024:.1f} MB)")
