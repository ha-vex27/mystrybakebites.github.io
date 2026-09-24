import urllib.parse
WA = "https://wa.me/233554520532?text=" + urllib.parse.quote("Hello Mystery Bakebite! I'd like to place an order 🍩")
IC = {
 'wa':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.3c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.3 8.3 0 1 1 12 20.3z"/></svg>',
 'ig':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
 'tt':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.6 5.8A4.3 4.3 0 0 1 15.5 3h-3.1v12.4a2.6 2.6 0 1 1-2.6-2.6c.3 0 .5 0 .8.1V9.7a5.7 5.7 0 1 0 4.9 5.7V9.1a7.3 7.3 0 0 0 4.3 1.4V7.4a4.3 4.3 0 0 1-3.2-1.6z"/></svg>',
 'fb':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8V6c0-.9.6-1 1-1h2.5V1.2L14.1 1C10.4 1 9.5 3.8 9.5 5.6V8H7v4h2.5v11H14V12h3.1l.4-4z"/></svg>',
 'yt':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.7 15V9l5.8 3-5.8 3z"/></svg>',
 'heart':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-7.5-4.6-9.6-9.2C.9 8.4 3 4.5 6.7 4.5c2.1 0 3.6 1.2 5.3 3.1 1.7-1.9 3.2-3.1 5.3-3.1 3.7 0 5.8 3.9 4.3 7.3C19.5 16.4 12 21 12 21z"/></svg>',
 'arrow':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 'pin':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 'phone':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 'mail':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 6 10 7 10-7"/></svg>',
 'bulb':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/></svg>',
 'brush':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.4 5 5.6.8-4 3.9.9 5.6L12 15.6l-4.9 2.7.9-5.6-4-3.9 5.6-.8z"/></svg>',
 'heartline':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7.5-4.6-9.6-9.2C.9 8.4 3 4.5 6.7 4.5c2.1 0 3.6 1.2 5.3 3.1 1.7-1.9 3.2-3.1 5.3-3.1 3.7 0 5.8 3.9 4.3 7.3C19.5 16.4 12 21 12 21z"/></svg>',
 'cap':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c0 1.5 3 3 6 3s6-1.5 6-3v-5M22 9v6"/></svg>',
 'whisk':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M14 10 21 3M4.5 19.5c-2-2-1.2-7.8 2.5-11.5s7-3 7-3 .7 3.3-3 7-9.5 4.5-6.5 7.5zM9 7c-1 2-1.3 5 0 8"/></svg>',
 'clock':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 'truck':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M1 5h13v11H1zM14 9h4l4 4v3h-8z"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="18" cy="18.5" r="2"/></svg>',
 'bag':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M5 8h14l-1 13H6zM9 8V6a3 3 0 0 1 6 0v2"/></svg>',
 'card':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M10 18h4"/></svg>',
 'cal':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/></svg>',
 'cash':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 9v.01M18 15v.01"/></svg>',
 'lock':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
 'gift':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="8" width="18" height="4"/><path d="M5 12v9h14v-9M12 8v13M12 8S10.5 3 8 4s0 4 4 4zm0 0s1.5-5 4-4-0 4-4 4z"/></svg>',
}
C='<span class="cedi">GH₵</span>'
def wa_item(cat, item, price):
    msg = f"Hello Mystery Bakebite! 🍩 I'd like to order:\n\n• {item} ({cat}): GH₵{price}{" (plain / with toppings. Please specify topping: Oreo, chocolate or raisin)" if "/" in price else ""}\n\nQuantity: \nDate needed: \nPickup or delivery (area in Tamale): \nName: "
    return "https://wa.me/233554520532?text=" + urllib.parse.quote(msg)
def wa_cat(cat):
    msg = f"Hello Mystery Bakebite! 🍩 I'm interested in your {cat}. Could you help me with an order?\n\nDate needed: \nPickup or delivery: "
    return "https://wa.me/233554520532?text=" + urllib.parse.quote(msg)
NAV_LINKS=[('index.html#menu','Menu'),('index.html#order','How to Order'),('index.html#payment','Payment'),('index.html#classes','Classes'),('index.html#gallery','Gallery'),('index.html#reviews','Reviews'),('index.html#story','Our Story')]
def header():
    nav=''.join(f'<a href="{h}">{t}</a>' for h,t in NAV_LINKS)
    return f'''<header class="site-header"><div class="wrap header-inner">
<a class="brand" href="index.html"><img class="brand-logo" src="assets/logo.jpg" alt="Mystery Bakebite logo"><span class="brand-name"><span class="brand-mystery">Mystery</span><span class="brand-bakebite">Bakebite</span></span></a>
<nav class="main-nav" aria-label="Main">{nav}</nav>
<a class="btn btn-wa header-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']}<span class="wa-label">Order on WhatsApp</span></a>
<button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
</div></header>'''
SOC=[('tt','TikTok','https://www.tiktok.com/@mysterybakebite'),('ig','Instagram','https://www.instagram.com/mysterybakebite'),('fb','Facebook','https://www.facebook.com/mysterybakebite'),('yt','YouTube','https://www.youtube.com/@mysterybakebite')]
def footer():
    s=''.join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{IC[k]}</a>' for k,n,u in SOC)
    cats=[('milky','Milky Doughnuts'),('slices','Cake Slices'),('cupcakes','Cupcakes'),('parfait','Cake Parfait'),('cookies','Cookies'),('loaves','Cake Loaves')]
    ml=''.join(f'<li><a href="menu.html#{a}">{b}</a></li>' for a,b in cats)
    return f'''<footer class="footer" id="contact">
<div class="f-cta"><div class="wrap f-cta-inner"><div><p class="f-cta-script">Craving something sweet?</p><p class="f-cta-sub">Send us a message and we'll bake it fresh for you.</p></div>
<a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Chat on WhatsApp</a></div></div>
<div class="wrap"><div class="footer-grid">
<div class="f-brand"><a class="brand" href="index.html"><img class="f-logo" src="assets/logo.jpg" alt="Mystery Bakebite logo"><span class="brand-name"><span class="brand-mystery">Mystery</span><span class="brand-bakebite">Bakebite</span></span></a>
<p class="f-tag">Unveiling The Uniqueness of A Recipe</p>
<p>Every batch starts in Amara's kitchen in Tamale: small, handmade and never rushed. Baking, training and creative custom orders.</p>
<div class="socials">{s}</div></div>
<div><h3 class="f-h">The Menu</h3><ul class="f-links">{ml}<li><a href="menu.html" class="f-more">Full price list →</a></li></ul></div>
<div><h3 class="f-h">Bakery</h3><ul class="f-links"><li><a href="index.html#order">How to Order</a></li><li><a href="index.html#info">Ordering Info</a></li><li><a href="index.html#payment">Payment Options</a></li><li><a href="index.html#gallery">Gallery</a></li><li><a href="index.html#reviews">Reviews</a></li><li><a href="index.html#classes">Baking Classes</a></li><li><a href="index.html#custom">Custom Orders</a></li><li><a href="index.html#story">Our Story</a></li><li><a href="assets/price-list.png" download="Mystery-Bakebite-Menu-Sept-2026.png">Download Menu</a></li></ul></div>
<div><h3 class="f-h">Visit &amp; Contact</h3><ul class="f-list">
<li>{IC['wa']}<a href="{WA}" target="_blank" rel="noopener">+233 55 452 0532</a></li>
<li>{IC['mail']}<a href="mailto:mysterybakebite@gmail.com">mysterybakebite@gmail.com</a></li>
<li>{IC['pin']}<span>Tamale, Northern Ghana</span></li>
<li>{IC['clock']}<span>Mon to Sun, 8am to 7pm</span></li></ul>
<div class="f-qr"><img src="assets/qr.jpg" alt="WhatsApp QR code"><span>Scan to<br>order</span></div></div>
</div></div>
<div class="f-bottom"><div class="wrap f-bottom-inner">
<p class="small">© 2026 Mystery Bakebite. Made in Tamale.</p>
<p class="love">{IC['heart']} Baked with Love, Especially for You</p>
<a class="to-top" href="#top">Back to top ↑</a></div></div></footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{IC['wa']}</a>
<script src="js/main.js"></script></body></html>'''
def head(title,desc):
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="icon" href="assets/logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css"></head><body id="top">'''
DIV=f'<div class="divider">{IC["heart"]}</div>'


INFO_ITEMS=[('clock','Order notice','Doughnuts, cookies &amp; chips: <b>order 24 hrs ahead</b>. Custom &amp; celebration cakes: <b>3 to 5 days</b>.'),
 ('truck','Delivery in Tamale','Delivery across Tamale. The fee depends on your area and is <b>confirmed on WhatsApp</b> with your order total.'),
 ('bag','Pickup','Free pickup in Tamale at an agreed time. The exact location is shared when your order is confirmed.'),
 ('card','Payment','<b>Cash on delivery or pickup</b>, or <b>full payment upfront via Mobile Money</b>. See payment options below.'),
 ('cal','Opening hours','Open <b>every day, Monday to Sunday, 8am to 7pm</b>. Messages sent after hours are answered the next morning.'),
 ('gift','Custom &amp; bulk','Parties, weddings, office treats and gift boxes. Tell us your theme, guest count and budget.')]
def info_block(extra_cls=''):
    cards=''.join(f'<div class="info-card reveal"><div class="info-ic">{IC[i]}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in INFO_ITEMS)
    return f'''<section class="info {extra_cls}" id="info"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Good to know</span><h2 class="sec-title">Ordering info</h2><p class="sec-sub">Everything you need before you message us.</p>{DIV}</div>
<div class="info-grid">{cards}</div></div></section>'''


def payment_block():
    return f"""<section class="payment" id="payment"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Payment</span><h2 class="sec-title">Two simple ways to pay</h2><p class="sec-sub">Choose what suits you when you place your order on WhatsApp.</p>{DIV}</div>
<div class="pay-grid">
<article class="pay-card reveal"><span class="pay-num">Option 1</span><div class="pay-ic">{IC['cash']}</div><h3>Cash on Delivery or Pickup</h3>
<p>Pay in cash when your order arrives or when you collect it. No payment needed before we bake.</p>
<ul class="ticks"><li>Pay the rider on delivery, or pay at pickup</li><li>Please have the exact amount ready</li><li>Delivery fee confirmed on WhatsApp</li></ul></article>
<article class="pay-card featured reveal"><span class="pay-num">Option 2</span><div class="pay-ic">{IC['card']}</div><h3>Full Payment Upfront</h3>
<p>Pay the full amount in advance through <b>Mobile Money (MoMo)</b>. Your order is confirmed as soon as payment is received.</p>
<ol class="pay-steps"><li>Send your order on WhatsApp</li><li>We reply with your total and our MoMo details</li><li>Send the payment and share the screenshot or reference</li><li>We confirm and start baking</li></ol>
<div class="momo-row"><span class="momo">MTN MoMo</span><span class="momo">Telecel Cash</span><span class="momo">AT Money</span></div></article>
</div>
<p class="pay-note">{IC['lock']} For your safety, only send MoMo payments to the number and name we confirm in our WhatsApp chat.</p>
</div></section>"""

# NOTE: SAMPLE testimonials. Replace with real customer words (with permission) before launch.
TESTIMONIALS=[
 ("The milky donuts are unreal. Soft, fresh and so much cream inside. My whole office now asks me to order every Friday.","Abena","Tamale","milky"),
 ("Ordered a custom birthday cake for my daughter and it was exactly what I pictured. Amara was patient with every detail.","Fuseini","Tamale","slices"),
 ("I joined a baking class as a complete beginner. Now I bake cupcakes for my family and even take small orders.","Rahinatu","Class student","cupcakes"),
 ("Ordering on WhatsApp was so easy. Paid with MoMo, got my parfaits on time and they were beautifully packed.","Kwame","Tamale","parfait"),
]
def testimonials_block():
    cards=''.join(f"""<figure class="t-card reveal"><div class="t-stars">★★★★★</div><blockquote>“{q}”</blockquote><figcaption><img src="assets/{img}.jpg" alt="" loading="lazy"><span><b>{n}</b><small>{w}</small></span></figcaption></figure>""" for q,n,w,img in TESTIMONIALS)
    return f"""<section class="testimonials on-dark" id="reviews"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Kind words</span><h2 class="sec-title">What our customers say</h2>{DIV}</div>
<div class="t-grid">{cards}</div>
<p class="t-cta">Tried our bakes? <a href="{WA_REVIEW}" target="_blank" rel="noopener">Send us your review on WhatsApp</a></p></div></section>"""

GALLERY=[('milky','Milky doughnuts','wide'),('founder','Amara at work','tall'),('parfait','Cake parfaits',''),('cupcakes','Cupcake box',''),
 ('slices','Signature cake slices','wide'),('thank-you','Our thank-you card','tall'),('balls','Doughnut balls',''),('cookies','Chocolate chip cookies',''),
 ('loaves','Banana &amp; vanilla loaves','wide'),('chips','Fried &amp; baked chips','')]
def gallery_block():
    items=''.join(f"""<button class="g-item {c} reveal" data-src="assets/{sl}.jpg" data-cap="{cap}"><img src="assets/{sl}.jpg" alt="{cap}" loading="lazy"><span class="g-cap">{cap}</span></button>""" for sl,cap,c in GALLERY)
    return f"""<section class="gallery" id="gallery"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Gallery</span><h2 class="sec-title">Fresh from the kitchen</h2><p class="sec-sub">A peek at recent bakes. Tap any photo to view it larger. More every day on <a href="https://www.instagram.com/mysterybakebite" target="_blank" rel="noopener">@mysterybakebite</a>.</p>{DIV}</div>
<div class="g-grid">{items}</div></div></section>
<div class="lightbox" id="lightbox" hidden><button class="lb-close" aria-label="Close">×</button><button class="lb-prev" aria-label="Previous">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="lb-next" aria-label="Next">›</button></div>"""

# ---- menu data (from price list, Sept 2026)
MENU=[
 ('milky','Milky Doughnuts',None,30,True,[('Milky donuts, 2 pcs','30'),('Milky donuts, 3 pcs','42'),('Milky donuts, 6 pcs','75'),('Milky donuts, 12 pcs','140',1)]),
 ('balls','Doughnut Balls &amp; Mini Doughnuts',None,30,True,[('Mini donuts, pack of 10','35'),('Donut balls, pack of 12','30'),('Donut balls, party pack of 25','55',1)]),
 ('slices','Cake Slices',None,35,False,[('Classic slice (vanilla or banana)','35'),('Signature slice (chocolate, red velvet, carrot or lemon)','40'),('Tasting box, 4 half-slices, all flavours','70'),('Full flavour box, 4 full slices, one of each','130')]),
 ('loaves','Cake Loaves','Plain / with toppings: Oreo, chocolate or raisin',35,False,[('Banana loaf, big','70 / GH₵85'),('Vanilla loaf, big','65 / GH₵80'),('Banana loaf, small','35 / GH₵45'),('Vanilla loaf, small','35 / GH₵45')]),
 ('chips','Fried &amp; Baked Chips',None,30,False,[('Fried and baked chips','30'),('Large (500g)','70')]),
 ('parfait','Cake Parfait',None,35,False,[('Cake parfait (cup)','35')]),
 ('cookies','Cookies',None,30,True,[('Chocolate chip, pack of 6','40'),('Butter cookies, pack of 6','30'),('Mixed cookie box, 12 pcs','65',1)]),
 ('cupcakes','Cupcakes',None,75,False,[('6 pieces (box)','75'),('12 pieces (box)','140')]),
]
cards=''
for slug,name,note,frm,new,items in MENU:
    b='<span class="badge-new">NEW</span>' if new else ''
    cards+=f'''<div class="mcard reveal">{b}<a href="menu.html#{slug}" class="mcard-link" aria-label="{name} prices"></a><figure><img src="assets/{slug}.jpg" alt="{name}" loading="lazy"></figure>
<div class="mcard-body"><h3>{name}</h3><span class="from">from <span class="price">{C}{frm}</span></span><div class="mcard-actions"><span class="more">See prices {IC['arrow']}</span><a class="order-btn" href="{wa_cat(name.replace('&amp;','&'))}" target="_blank" rel="noopener">{IC['wa']}<span>Order</span></a></div></div></div>'''

VAL=[('bulb','Quality'),('brush','Creativity'),('heartline','Passion'),('cap','Education')]
vals=''.join(f'<span class="vbadge">{IC[i]}{t}</span>' for i,t in VAL)
TILES=[('milky','Cream-filled milky donuts'),('parfait','Layered cake parfaits'),('cupcakes','Swirled cupcakes'),('slices','Signature cake slices')]
tiles=''.join(f'<a class="tile reveal" href="https://www.instagram.com/mysterybakebite" target="_blank" rel="noopener"><img src="assets/{s}.jpg" alt="{a}" loading="lazy"><div class="ov">{IC["ig"]}<b>{a}</b></div></a>' for s,a in TILES)
def wa_msg(m): return "https://wa.me/233554520532?text=" + urllib.parse.quote(m)
WA_CLASS = wa_msg("Hello Mystery Bakebite! 👩🏾‍🍳 I'd like to book a baking class.\n\nName: \nClass I'm interested in: \nExperience level (beginner / some experience): \nPreferred dates: ")
WA_CUSTOM = wa_msg("Hello Mystery Bakebite! 🎂 I'd like to request a custom order.\n\nOccasion: \nDate needed: \nNumber of guests / servings: \nTheme or colours: \nBudget (GH₵): \nPickup or delivery: ")
WA_REVIEW = wa_msg("Hello Mystery Bakebite! 💬 I'd like to share a review.\n\nWhat I ordered: \nMy review: \nName (as you'd like it shown): ")
info_cards=''.join(f'<div class="info-card reveal"><div class="info-ic">{IC[i]}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in INFO_ITEMS)

index=head('Mystery Bakebite | Home Bakery in Tamale, Northern Ghana','Milky doughnuts, cakes, cupcakes, cookies, baking classes and custom orders from Mystery Bakebite in Tamale. Order on WhatsApp.')+header()+f"""
<main>
<section class="hero"><div class="wrap hero-grid">
<div><img class="hero-logo" src="assets/logo.jpg" alt="Mystery Bakebite circular logo">
<p class="hero-kicker">Baking · Training · Creative</p>
<h1 class="hero-title"><span class="t-m">Mystery</span><span class="t-b">Bakebite</span></h1>
<p class="hero-tagline">Unveiling The Uniqueness of A Recipe</p>
<p class="hero-lede">Soft milky doughnuts, dripping cakes, parfaits and cookies, baked fresh at home in Tamale and made just for you. Message us, tell us what you're craving, and we'll take it from there.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Order on WhatsApp</a><a class="btn btn-ghost" href="#menu">See the menu</a></div>
<div class="hero-chips"><span class="chip">{IC['pin']} Tamale, Northern Ghana</span><span class="chip">{IC['whisk']} Baked to order</span></div></div>
<div class="hero-art"><span class="hero-badge">Fresh daily</span><div class="glass-tag"><small>Milky donuts</small><b>from <span>GH₵30</span></b></div>
<div class="hero-frame"><img src="assets/milky.jpg" alt="Milky donuts cut open showing vanilla and strawberry cream filling"></div>
<div class="hero-frame2"><img src="assets/founder.jpg" alt="Amara Johnson with a pink chocolate-drip cake" style="object-position:top"></div></div>
</div></section>
<div class="marquee" aria-hidden="true"><div class="marquee-track">MQ</div></div>

<section class="menu-sec" id="menu"><div class="wrap"><div class="sec-head reveal"><span class="kicker">The menu</span><h2 class="sec-title">Something sweet for every moment</h2><p class="sec-sub">Eight favourites, baked to order. Tap a card for prices, or order straight from it.</p>{DIV}</div>
<div class="menu-grid">{cards}</div>
<div class="menu-ctas"><a class="btn btn-brown" href="menu.html">Full price list {IC['arrow']}</a><a class="btn btn-ghost-dark" href="assets/price-list.png" download="Mystery-Bakebite-Menu-Sept-2026.png">Download menu card</a></div>
<p class="menu-note">Prices effective September 2026 · All prices in GH₵</p></div></section>

<section class="order on-dark" id="order"><div class="wrap"><div class="sec-head reveal"><span class="kicker">How to order</span><h2 class="sec-title">Three easy steps</h2><p class="sec-sub">No app, no account. Just a chat.</p>{DIV}</div>
<div class="steps">
<div class="step reveal"><div class="num">01</div><h3>Pick your treats</h3><p>Choose from the <a href="menu.html">full price list</a>, or come with an idea for a custom order.</p></div>
<div class="step reveal"><div class="num">02</div><h3>Message on WhatsApp</h3><p>Tap any Order button or scan the code. We'll confirm availability, your total and payment.</p></div>
<div class="step reveal"><div class="num">03</div><h3>Pickup or delivery</h3><p>Collect your treats, or have them delivered within Tamale. Fresh, boxed and ready to enjoy.</p></div></div>
<div class="order-bottom">
<div class="qr-panel reveal"><div class="qr-card"><img src="assets/qr.jpg" alt="WhatsApp QR code for Mystery Bakebite"></div>
<div class="qr-copy"><h3>Scan to chat</h3><p class="wa-num">+233 55 452 0532</p><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Order on WhatsApp</a></div></div>
<div id="info" class="info-wrap"><h3 class="info-title">Good to know</h3><div class="info-grid dark">{info_cards}</div></div>
</div></div></section>

"""+payment_block()+f"""<section class="services" id="classes"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Beyond the bakes</span><h2 class="sec-title">Learn with us, or dream it up with us</h2>{DIV}</div>
<div class="svc-grid">
<article class="svc reveal"><figure><img src="assets/cupcakes.jpg" alt="Cupcakes from a baking class" loading="lazy"><span class="svc-tag">{IC['cap']} Training</span></figure>
<div class="svc-body"><h3>Baking Classes</h3><p>Hands-on classes in Amara's kitchen for beginners and budding bakers. Small groups, real recipes, and everything you need to bake with confidence.</p>
<ul class="ticks"><li>Doughnuts, cakes, cupcakes and cookies</li><li>Frosting, decorating and finishing</li><li>Pricing and starting a home baking business</li><li>Recipes to take home</li></ul>
<a class="btn btn-wa" href="{WA_CLASS}" target="_blank" rel="noopener">{IC['wa']} Book a class</a></div></article>
<article class="svc reveal" id="custom"><figure><img src="assets/slices.jpg" alt="Layered celebration cake slices" loading="lazy"><span class="svc-tag">{IC['gift']} Creative</span></figure>
<div class="svc-body"><h3>Custom Orders</h3><p>Birthdays, weddings, naming ceremonies, office treats and gift boxes. Tell us your theme and we'll design something that's truly yours.</p>
<ul class="ticks"><li>Celebration and themed cakes</li><li>Dessert tables and party packs</li><li>Branded gift boxes and bulk orders</li><li>Order 3 to 5 days ahead</li></ul>
<a class="btn btn-wa" href="{WA_CUSTOM}" target="_blank" rel="noopener">{IC['wa']} Request a custom order</a></div></article>
</div></div></section>

<section class="story on-dark" id="story"><div class="wrap story-grid">
<div class="story-photo reveal"><img src="assets/founder.jpg" alt="Amara Johnson, Founder and Head Baker of Mystery Bakebite"><div class="story-cap"><b>Amara Johnson</b><span>Founder &amp; Head Baker</span></div></div>
<div class="reveal"><span class="kicker">Our story</span><h2 class="sec-title">A recipe is never just a recipe</h2>
<p class="lead-in">Mystery Bakebite started in a home kitchen in Tamale with one simple belief: every recipe has something unique waiting to be discovered. The "mystery" is that little twist: the extra cream in a milky donut, the flavour pairing you didn't expect, that turns a good bake into your favourite one.</p>
<p>Everything is still made by hand, in small batches, by Amara herself. No factory, no shortcuts, just good ingredients and a lot of love. Alongside the bakes, she teaches classes and creates custom pieces for Tamale's celebrations.</p>
<div class="vbadges">{vals}</div>
<p class="story-sign">With love, Amara</p></div></div></section>

"""+testimonials_block()+gallery_block()+f"""
</main>"""+footer()

# ---- menu page
pl=''
for slug,name,note,frm,new,items in MENU:
    lis=''
    for it in items:
        n='<span class="mini-new">NEW</span>' if len(it)>2 else ''
        plain = name.replace('&amp;','&')
        lis+=f'<li><span class="item">{it[0]}{n}</span><span class="dots"></span><span class="price">{C}{it[1]}</span><a class="order-btn" href="{wa_item(plain,it[0],it[1])}" target="_blank" rel="noopener" aria-label="Order {it[0]} on WhatsApp">{IC["wa"]}<span>Order</span></a></li>'
    nt=f'<p class="note">{note}</p>' if note else ''
    pl+=f'<article class="pl-card reveal" id="{slug}"><figure><img src="assets/{slug}.jpg" alt="{name}" loading="lazy"></figure><div class="pl-body"><h2>{name}</h2>{nt}<ul class="pl">{lis}</ul></div></article>'
menu=head('Menu & Prices | Mystery Bakebite','Full price list for Mystery Bakebite, Tamale. Effective September 2026.')+header()+f'''
<main><section class="page-hero"><div class="wrap"><img class="ph-logo" src="assets/logo.jpg" alt="Mystery Bakebite logo"><h1>Menu &amp; Prices</h1><p class="script">Unveiling The Uniqueness of A Recipe</p>
<p class="ph-meta">Effective September 2026<i>♥</i>Tamale<i>♥</i>All prices in GH₵</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Order on WhatsApp</a><a class="btn btn-ghost" href="assets/price-list.png" download="Mystery-Bakebite-Menu-Sept-2026.png">Download menu card</a></div></div></section>
<section class="pricelist"><div class="wrap"><div class="pl-grid">{pl}</div></div></section>
'''+info_block()+payment_block()+f'''<section class="order-strip"><div class="wrap"><p class="script">Ready to order?</p><p>Send us your picks on WhatsApp with your preferred date and pickup or delivery in Tamale. Custom cakes and class bookings? Just ask!</p><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Message +233 55 452 0532</a></div></section></main>'''+footer()
MQ=''.join(f'<span>{i} {IC["heart"]} <em>freshly baked</em> {IC["heart"]}</span>' for i in ['Milky Doughnuts', 'Cake Slices', 'Cupcakes', 'Cake Parfaits', 'Donut Balls', 'Cookies', 'Cake Loaves', 'Baking Classes', 'Custom Orders'])
index=index.replace('MQ',MQ*2)
open('index.html','w').write(index); open('menu.html','w').write(menu)
