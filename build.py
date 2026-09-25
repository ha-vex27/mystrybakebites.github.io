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
def acc(v): return f'GH₵ {float(v):,.2f}'
def wa_item(cat, item, price):
    msg = f"Hello Mystery Bakebite! 🍩 I'd like to order:\n\n• {item} ({cat}): GH₵{price}{" (plain / with toppings. Please specify topping: Oreo, chocolate or raisin)" if "/" in price else ""}\n\nQuantity: \nDate needed: \nPickup or delivery (area in Tamale): \nName: "
    return "https://wa.me/233554520532?text=" + urllib.parse.quote(msg)
def wa_cat(cat):
    msg = f"Hello Mystery Bakebite! 🍩 I'm interested in your {cat}. Could you help me with an order?\n\nDate needed: \nPickup or delivery: "
    return "https://wa.me/233554520532?text=" + urllib.parse.quote(msg)
def header():
    def dd(label, key, items, foot=''):
        li=''.join(f'<a class="dd-link" href="{h}"><span class="dd-ic">{ic}</span><span><b>{t}</b><small>{d}</small></span></a>' for h,ic,t,d in items)
        return f"""<div class="nav-item has-dd" data-key="{key}"><button class="nav-link dd-btn" aria-expanded="false" aria-haspopup="true">{label}<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></button>
<div class="dd-panel"><div class="dd-inner">{li}</div>{foot}</div></div>"""
    def mega():
        cards=''.join(f'<a class="mg-card s-{c["slug"]}" href="class-{c["slug"]}.html"><span class="mg-num">{c["num"]}</span><span class="mg-lvl">{c["level"]}</span><b>{c["title"]}</b><span class="mg-meta">1 week · 6 recipes</span><span class="mg-fee">{acc(c["fee"])}</span></a>' for c in CLASSES)
        return f"""<div class="nav-item has-dd" data-key="classes"><button class="nav-link dd-btn" aria-expanded="false" aria-haspopup="true">Classes<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></button>
<div class="dd-panel dd-mega"><div class="mg-head"><div><p class="mg-kicker">Baking classes</p><p class="mg-script">Learn. Bake. Create.</p></div><a class="mg-all" href="classes.html">All classes →</a></div>
<div class="mg-grid">{cards}</div><a class="dd-foot" href="classes.html#{CLASSES[0]['slug']}">Bundle &amp; save: {BUNDLE[2]}% off 2 classes · {BUNDLE[3]}% off all 3 →</a></div></div>"""
    cls_items=[(f'class-{c["slug"]}.html', f'<b class="dd-n">{c["num"]}</b>', f'{c["level"]}', f'{c["title"]} · {acc(c["fee"])}') for c in CLASSES]
    cls_foot=f'<a class="dd-foot" href="classes.html">View all classes &amp; bundles (save up to {BUNDLE[3]}%) →</a>'
    ord_items=[('index.html#order',IC['whisk'],'How to Order','Three easy steps on WhatsApp'),('index.html#payment',IC['card'],'Payment','Cash, or full MoMo payment upfront'),('index.html#info',IC['clock'],'Ordering Info','Notice, delivery &amp; hours'),('index.html#custom',IC['gift'],'Custom Orders','Cakes and party packs')]
    about_items=[('index.html#story',IC['heartline'],'Our Story','Meet Emmanuella'),('index.html#gallery',IC['ig'],'Gallery','Fresh from the kitchen'),('index.html#reviews',IC['heart'],'Reviews','What customers say')]
    nav=(f'<a class="nav-link" href="menu.html" data-key="menu">Menu</a>'
         + mega()
         + dd('Order','order',ord_items)
         + dd('About','about',about_items))
    # mobile drawer
    def group(title, items): return f'<div class="dr-group"><p class="dr-h">{title}</p>'+''.join(f'<a href="{h}">{t}</a>' for h,_,t,_d in items)+'</div>'
    soc=''.join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{IC[k]}</a>' for k,n,u in SOC)
    lv=''.join(f'<a class="dr-lv" href="class-{c["slug"]}.html"><b>{c["num"]}</b>{c["level"]}</a>' for c in CLASSES)
    drawer=f"""<div class="drawer" id="drawer" aria-hidden="true"><div class="dr-backdrop" data-close></div>
<aside class="dr-panel" role="dialog" aria-label="Menu"><div class="dr-top"><a class="brand" href="index.html"><img class="brand-logo" src="assets/logo.jpg" alt=""><span class="brand-name"><span class="brand-mystery">Mystery</span><span class="brand-bakebite">Bakebite</span></span></a><button class="dr-close" data-close aria-label="Close menu">×</button></div>
<p class="dr-slogan">Unveiling The Uniqueness of A Recipe</p>
<nav class="dr-nav"><a class="dr-main" href="index.html"><i>01</i>Home</a><a class="dr-main" href="menu.html"><i>02</i>Menu &amp; Prices</a><a class="dr-main" href="classes.html"><i>03</i>Baking Classes</a>
<div class="dr-levels">{lv}</div>
{group('Order', ord_items)}{group('About', about_items)}</nav>
<div class="dr-bottom"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Order on WhatsApp</a><div class="dr-soc">{soc}</div><p>Open daily · 8am to 7pm · Tamale</p></div>
</aside></div>"""
    flat=[('index.html','Home','home'),('menu.html','Menu','menu'),('classes.html','Classes','classes'),('index.html#order','How to Order','order'),('index.html#gallery','Gallery','gallery'),('index.html#story','Our Story','story')]
    links=''.join(f'<a class="nav-link" href="{h}" data-key="{k}">{t}</a>' for h,t,k in flat)
    return f"""<header class="site-header nav5 nav6"><div class="wrap nav5-inner">
<a class="brand" href="index.html"><img class="brand-logo" src="assets/logo.jpg" alt="Mystery Bakebite logo"><span class="brand-name"><span class="brand-mystery">Mystery</span><span class="brand-bakebite">Bakebite</span></span></a>
<nav class="main-nav" aria-label="Main">{links}</nav>
<a class="btn btn-wa header-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']}<span class="wa-label">Order on WhatsApp</span></a>
<button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="drawer"><span></span><span></span><span></span></button>
</div></header>{drawer}"""

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
<p>Every batch starts in Emmanuella's kitchen in Tamale: small, handmade and never rushed. Baking, training and creative custom orders.</p>
<div class="socials">{s}</div></div>
<div><h3 class="f-h">The Menu</h3><ul class="f-links">{ml}<li><a href="menu.html" class="f-more">Full price list →</a></li></ul></div>
<div><h3 class="f-h">Bakery</h3><ul class="f-links"><li><a href="index.html#order">How to Order</a></li><li><a href="index.html#info">Ordering Info</a></li><li><a href="index.html#payment">Payment Options</a></li><li><a href="index.html#gallery">Gallery</a></li><li><a href="index.html#reviews">Reviews</a></li><li><a href="classes.html">Baking Classes</a></li><li><a href="index.html#custom">Custom Orders</a></li><li><a href="index.html#story">Our Story</a></li><li><a href="assets/price-list.png" download="Mystery-Bakebite-Menu-Sept-2026.png">Download Menu</a></li></ul></div>
<div><h3 class="f-h">Visit &amp; Contact</h3><ul class="f-list">
<li>{IC['wa']}<a href="{WA}" target="_blank" rel="noopener">+233 55 452 0532</a></li>
<li>{IC['mail']}<a href="mailto:mysterybakebite@gmail.com">mysterybakebite@gmail.com</a></li>
<li>{IC['pin']}<span>Tamale, Northern Ghana</span></li>
<li>{IC['clock']}<span>Mon to Sun, 8am to 7pm</span></li></ul>
<div class="f-qr"><img src="assets/qr.jpg" alt="WhatsApp QR code"><span>Scan to<br>order</span></div></div>
</div></div>
<div class="f-bottom"><div class="wrap f-bottom-inner">
<p class="small">© 2026 Mystery Bakebite. All rights reserved.</p>
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
 ("Ordered a custom birthday cake for my daughter and it was exactly what I pictured. Emmanuella was patient with every detail.","Fuseini","Tamale","slices"),
 ("I joined a baking class as a complete beginner. Now I bake cupcakes for my family and even take small orders.","Rahinatu","Class student","cupcakes"),
 ("Ordering on WhatsApp was so easy. Paid with MoMo, got my parfaits on time and they were beautifully packed.","Kwame","Tamale","parfait"),
]

# NOTE: SAMPLE reviews below. Replace with real customer words (with permission) before launch.
TESTIMONIALS += [
 ("Best bofrot I've had outside my grandmother's kitchen. Soft, light and not oily at all.","Adwoa","Tamale","balls"),
 ("The red velvet slice was so moist. I came back the next day for the tasting box.","Yakubu","Tamale","slices"),
 ("Ordered 12 cupcakes for my son's party and every child wanted a second one.","Mariam","Tamale","cupcakes"),
 ("The banana loaf with chocolate topping is my weekend treat now. Always fresh.","Kofi","Tamale","loaves"),
 ("Cookies arrived warm and perfectly packed. The mixed box is great for sharing.","Esi","Tamale","cookies"),
 ("I took the Beginner class and finally understand how to knead dough properly.","Zainab","Class student","balls"),
 ("Her parfaits are beautiful and taste even better. Perfect for our church event.","Ama","Tamale","parfait"),
 ("Chips are crunchy and well seasoned. My kids finish the 500g pack in a day.","Iddrisu","Tamale","chips"),
 ("Delivery was right on time and the rider was very polite. Will order again.","Akosua","Tamale","milky"),
 ("The custom cake for our anniversary looked exactly like the picture I sent.","Sulemana","Tamale","slices"),
 ("Milky donuts with strawberry cream are my absolute favourite. So generous!","Efua","Tamale","milky"),
 ("Paid upfront with MoMo and got a confirmation straight away. Very professional.","Abdul-Rahman","Tamale","parfait"),
 ("The Intermediate class taught me butter bread. My family can't stop eating it.","Grace","Class student","loaves"),
 ("We ordered party packs of donut balls for our office. Gone in ten minutes.","Mohammed","Tamale","balls"),
 ("Emmanuella answers every question patiently. You can tell she loves what she does.","Linda","Tamale","cupcakes"),
 ("The chocolate chip cookies are chewy in the middle and crisp at the edges. Perfect.","Nana","Tamale","cookies"),
 ("I ordered a tasting box to try all the flavours. Lemon surprised me the most!","Awal","Tamale","slices"),
 ("Clean kitchen, small group and lots of hands-on time. Worth every cedi.","Salamatu","Class student","cupcakes"),
 ("The vanilla loaf is soft and not too sweet. Great with tea in the morning.","Yaw","Tamale","loaves"),
 ("My naming ceremony guests kept asking where the cupcakes came from.","Hawa","Tamale","cupcakes"),
 ("Fast replies on WhatsApp and the pickup was easy to arrange. Five stars.","Kwabena","Tamale","milky"),
 ("The Advanced class sourdough session changed how I bake. Loved it.","Patience","Class student","loaves"),
 ("The thank-you card in the box was such a sweet personal touch.","Rashida","Tamale","parfait"),
 ("Butter cookies taste homemade in the best way. My mum loves them.","Emmanuel","Tamale","cookies"),
 ("Consistent quality every single time I order. That is rare.","Fatima","Tamale","milky"),
 ("Our office Friday treats are now always from Mystery Bakebite.","Kojo","Tamale","balls"),
 ("I gifted a cupcake box to a friend and she ordered her own the next week.","Adjoa","Tamale","cupcakes"),
 ("Cake parfaits are the perfect size for a sweet craving after lunch.","Alhassan","Tamale","parfait"),
 ("Great value for the quality. The 12 piece milky donut box is a steal.","Selina","Tamale","milky"),
 ("From ordering to the last bite, everything felt personal and made with love.","Issah","Tamale","slices"),
]

def testimonials_block():
    cards=''.join(f"""<figure class="t-card"><div class="t-stars">★★★★★</div><blockquote>“{q}”</blockquote><figcaption><img src="assets/{img}.jpg" alt="" loading="lazy"><span><b>{n}</b><small>{w}</small></span></figcaption></figure>""" for q,n,w,img in TESTIMONIALS)
    cards_dup=cards.replace('<figure class="t-card">','<figure class="t-card" aria-hidden="true">')
    return f"""<section class="testimonials on-dark" id="reviews"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Kind words</span><h2 class="sec-title">What our customers say</h2>{DIV}</div>
<div class="t-carousel"><div class="t-track">{cards}{cards_dup}</div></div>
<p class="t-cta">Tried our bakes? <a href="{WA_REVIEW}" target="_blank" rel="noopener">Send us your review on WhatsApp</a></p></div></section>"""

GALLERY=[('milky','Milky doughnuts','wide'),('founder','Emmanuella at work','tall'),('parfait','Cake parfaits',''),('cupcakes','Cupcake box',''),
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


# ============================================================
# CLASSES  (fees, durations, spaces are PLACEHOLDERS: edit here)
# ============================================================
CLASSES=[
 dict(slug='beginner', num='01', level='Beginner', cat='Basic', title='Local Ghanaian Bread-Making', img='balls',
  short='Master the Ghanaian classics and the fundamentals of dough.',
  purpose='Introduce beginners to fundamental Ghanaian bread-making techniques, basic dough preparation, shaping, frying, baking, and ingredient handling.',
  recipes=['Ghanaian Sugar Bread','Ghanaian Tea Bread','Bofrot (Togbei / Ghanaian Puff Puff)','Ghanaian Coconut Bread','Ghanaian Rock Buns','Atwemo (Twisted Fried Dough)'],
  learn=['Measuring and handling flour, yeast, sugar and fats','Mixing and kneading by hand','Proofing: how to tell when dough is ready','Shaping loaves, buns and twists','Deep-frying safely for bofrot and atwemo','Baking temperatures and checking doneness'],
  skill='No experience needed. Perfect if you have never baked bread before.',
  duration='1 week · Mon to Fri', time='9:00am to 1:00pm', hours='4 hours a day', fee='750', spaces='Small group, up to 8 students'),
 dict(slug='intermediate', num='02', level='Intermediate', cat='Intermediate', title='Butter Bread &amp; Wheat Bread', img='loaves',
  short='Richer doughs, wheat flours and neater shaping.',
  purpose='Build on basic baking skills by introducing richer doughs, wheat-based breads, enriched breads, shaping techniques, and more advanced preparation methods.',
  recipes=['Rich Butter Bread','Whole Meal Wheat Bread','Soft Buttermilk Rolls','Wheat Sandwich Baguettes','Cinnamon Swirl Butter Loaf','Wholewheat Burger Buns'],
  learn=['Working with enriched doughs (butter, milk, eggs)','Baking with whole meal and wholewheat flour','Windowpane test and dough strength','Rolling, filling and swirling loaves','Uniform rolls, buns and baguette shaping','Getting soft crumbs and golden crusts'],
  skill='Completed our Beginner class, or comfortable making a basic yeast dough.',
  duration='1 week · Mon to Fri', time='9:00am to 2:00pm', hours='5 hours a day', fee='950', spaces='Small group, up to 6 students'),
 dict(slug='advanced', num='03', level='Advanced', cat='Advanced', title='International Bread Varieties', img='slices',
  short='Artisan fermentation and breads from around the world.',
  purpose='Introduce advanced bread-making techniques and internationally recognized bread varieties, including fermentation, artisan shaping, specialty dough preparation, and different baking methods.',
  recipes=['Artisan Sourdough Boule','Classic French Baguette','Rosemary Focaccia','Braided Challah','Skillet Naan','New York-Style Bagels'],
  learn=['Building and feeding a sourdough starter','Long and cold fermentation','High-hydration dough handling','Artisan scoring, braiding and shaping','Boiling, skillet and steam baking methods','Planning a bakery-style production schedule'],
  skill='Completed our Intermediate class, or confident with enriched and wheat doughs.',
  duration='1 week · Mon to Fri', time='9:00am to 3:00pm', hours='6 hours a day', fee='1150', spaces='Small group, up to 6 students'),
]
BUNDLE={2:15,3:25}  # number of classes : discount %
CLASS_INCLUDED=['All ingredients and equipment','Printed recipe booklet for all 6 recipes','Apron to use during class','Take home everything you bake','Light refreshments','Certificate of completion']
CLASS_BRING=['A notebook and pen','Containers or a bag to carry your bakes home','Hair tie or cap, and closed shoes','An appetite to learn!']
CLASS_SCHEDULES=['Weekday mornings (8am to 1pm)','Weekday afternoons (1pm to 7pm)','Weekends (Saturday and Sunday)']

def stage_path(active=None):
    out=''
    for i,c in enumerate(CLASSES):
        cls='on' if active==c['slug'] else ''
        out+=f'<a class="path-step {cls}" href="class-{c["slug"]}.html"><span class="ps-num">{c["num"]}</span><span class="ps-lvl">{c["level"]}</span></a>'
        if i<2: out+='<span class="path-arrow" aria-hidden="true">→</span>'
    return f'<nav class="pathway" aria-label="Learning pathway">{out}</nav>'

def classes_teaser():
    tiles=''.join(f"""<a class="stage-tile s-{c['slug']} reveal" href="classes.html#{c['slug']}"><span class="st-num">{c['num']}</span><span class="st-lvl">{c['level']}</span><h3>{c['title']}</h3><p>{c['short']}</p><span class="st-meta">1 week · {c['time']}<br>6 recipes · {acc(c['fee'])}</span><span class="more">View class {IC['arrow']}</span></a>""" for c in CLASSES)
    return f"""<section class="classes-teaser on-dark" id="classes"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Baking classes</span><h2 class="sec-title">Learn. Bake. Create.</h2><p class="sec-script">Unveiling The Uniqueness of A Recipe</p><p class="sec-sub">Hands-on, in-person bread-making classes in Tamale. Three stages, one pathway from your first dough to artisan loaves.</p>{DIV}</div>
{stage_path()}
<div class="stage-grid">{tiles}</div>
<div class="menu-ctas"><a class="btn btn-wa" href="classes.html">{IC['cap']} Explore all classes</a></div></div></section>"""

def class_card(c):
    rec=''.join(f'<li>{r}</li>' for r in c['recipes'])
    return f"""<article class="level-card s-{c['slug']} reveal" id="{c['slug']}">
<div class="lc-side"><span class="lc-num">{c['num']}</span><span class="lc-lvl">{c['level']}</span><figure><img src="assets/{c['img']}.jpg" alt="" loading="lazy"></figure></div>
<div class="lc-body"><span class="lc-cat">{c['cat']} · {c['title']}</span><h2>{c['title']}</h2><p class="lc-short">{c['purpose']}</p>
<div class="lc-meta"><span>{IC['whisk']} <b>6 Recipes</b></span><span>{IC['cal']} {c['duration']}</span><span>{IC['clock']} {c['time']}</span><span class="lc-fee">{acc(c['fee'])}</span></div>
<ol class="recipes">{rec}</ol>
<div class="lc-ctas"><a class="btn btn-brown" href="class-{c['slug']}.html">View Class {IC['arrow']}</a><a class="btn btn-wa" href="class-{c['slug']}.html#book">Book {c['level']} Class</a></div></div></article>"""

def bundle_block():
    fees=[float(c['fee']) for c in CLASSES]
    b2=[(CLASSES[0],CLASSES[1]),(CLASSES[1],CLASSES[2])]
    rows=''
    for a,b in b2:
        full=float(a['fee'])+float(b['fee']); rows+=f"""<div class="bundle reveal"><span class="b-off">Save {BUNDLE[2]}%</span><h3>{a['level']} + {b['level']}</h3><p class="b-was">{acc(full)}</p><p class="b-now">{acc(full*(1-BUNDLE[2]/100))}</p><a class="btn btn-brown" href="class-{a['slug']}.html?add={b['slug']}#book">Book this bundle</a></div>"""
    full=sum(fees)
    rows+=f"""<div class="bundle best reveal"><span class="b-off">Save {BUNDLE[3]}%</span><h3>Full Pathway<small>Beginner + Intermediate + Advanced</small></h3><p class="b-was">{acc(full)}</p><p class="b-now">{acc(full*(1-BUNDLE[3]/100))}</p><a class="btn btn-wa" href="class-beginner.html?add=all#book">{IC['cap']} Book the full pathway</a></div>"""
    return f"""<div class="bundles"><div class="sec-head reveal"><span class="kicker">Bundle &amp; save</span><h2 class="sec-title">Take more than one class</h2><p class="sec-sub">Book any <b>2 classes</b> and get <b>{BUNDLE[2]}% off</b>, or all <b>3 classes</b> for <b>{BUNDLE[3]}% off</b>. Any combination works; you can pick your classes on the booking form.</p>{DIV}</div>
<div class="bundle-grid">{rows}</div></div>"""

def classes_page():
    cards=''.join(class_card(c)+('<div class="lc-connector" aria-hidden="true"><span>then</span></div>' if i<2 else '') for i,c in enumerate(CLASSES))
    guide=''.join(f'<div class="guide reveal"><span class="g-num">{c["num"]}</span><div><b>{c["level"]}</b><p>{c["skill"]}</p></div></div>' for c in CLASSES)
    return head('Baking Classes | Mystery Bakebite | Unveiling The Uniqueness of A Recipe','Unveiling The Uniqueness of A Recipe. Hands-on bread-making classes in Tamale: Beginner, Intermediate and Advanced.')+header()+f"""
<main><section class="page-hero"><div class="wrap"><img class="ph-logo" src="assets/logo.jpg" alt="Mystery Bakebite logo"><h1>Classes</h1><p class="script">Unveiling The Uniqueness of A Recipe</p><p class="ph-sub">Learn. Bake. Create.</p>
<p class="ph-meta">In person<i>♥</i>Tamale<i>♥</i>Small groups</p>{stage_path()}</div></section>
<section class="levels"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Choose your level</span><h2 class="sec-title">A pathway, one stage at a time</h2><p class="sec-sub">Each stage builds on the one before. Start where you're comfortable and progress from Ghanaian classics to international artisan breads.</p>{DIV}</div>
<div class="guide-grid">{guide}</div>
<div class="level-list">{cards}</div>
{bundle_block()}
<p class="menu-note">Fees include all ingredients. Dates are arranged with you on WhatsApp.</p></div></section></main>"""+footer()

FOR_WHOM={
 'beginner':['You have never baked bread, or only a little','You want to master Ghanaian favourites at home','You are thinking about selling bread or snacks'],
 'intermediate':['You have done our Beginner class or bake basic doughs','You want softer, richer and healthier wheat breads','You want neater shaping for home or small business'],
 'advanced':['You have done our Intermediate class or bake confidently','You want to learn artisan and international breads','You are ready for sourdough and long fermentation'],
}
def class_detail(i):
    c=CLASSES[i]; SL='Unveiling The Uniqueness of A Recipe'
    ttl=c['title'].replace('&amp;','&')
    rec=''.join(f'<div class="rcard reveal"><span class="r-num">{j+1:02d}</span><h3>{r}</h3><span class="r-tag">{c["level"]}</span></div>' for j,r in enumerate(c['recipes']))
    learn=''.join(f'<div class="skill reveal"><span class="sk-ic">{IC["whisk"] if j%3==0 else IC["clock"] if j%3==1 else IC["brush"]}</span><p>{r}</p></div>' for j,r in enumerate(c['learn']))
    inc=''.join(f'<li>{r}</li>' for r in CLASS_INCLUDED)
    bring=''.join(f'<li>{r}</li>' for r in CLASS_BRING)
    who=''.join(f'<li>{r}</li>' for r in FOR_WHOM[c['slug']])
    opts=''.join(f'<label class="opt"><input type="radio" name="schedule" value="{o}" {"checked" if j==0 else ""}><span>{o}</span></label>' for j,o in enumerate(CLASS_SCHEDULES))
    picks=''.join(f'<label class="opt pk"><input type="checkbox" name="cls" value="{x["slug"]}" data-fee="{x["fee"]}" data-name="{x["num"]} {x["level"]}: {x["title"].replace("&amp;","&")}" {"checked" if x is c else ""}><span><b>{x["num"]} {x["level"]}</b><small>{x["title"]}</small></span><em>{acc(x["fee"])}</em></label>' for x in CLASSES)
    # where it fits
    fit=''
    for x in CLASSES:
        st='now' if x is c else ('done' if CLASSES.index(x)<i else 'next')
        lab={'now':'You are here','done':'Before this','next':'Up next'}[st]
        fit+=f'<a class="fit {st}" href="class-{x["slug"]}.html"><span class="fit-n">{x["num"]}</span><b>{x["level"]}</b><small>{lab}</small></a>'
    faqs=[
     ('How do I pay?', 'You can pay in cash when the class starts, or make full payment upfront through Mobile Money. We share the MoMo details in the WhatsApp chat when your booking is confirmed.'),
     ('Can I book more than one class?', f'Yes. Book any 2 classes and get {BUNDLE[2]}% off, or all 3 for {BUNDLE[3]}% off. Just tick the classes you want in the booking form.'),
     ('Is this the right level for me?', c['skill']+' Not sure? Message us on WhatsApp and we will help you choose.'),
     ('When does the next class start?', 'Classes run for one week, Monday to Friday. Choose your preferred schedule and start date in the form and we will confirm the date with you on WhatsApp.'),
     ('Do I need to bring ingredients or equipment?', 'No. All ingredients and equipment are included. You only need the few items listed under What to bring.'),
    ]
    faq=''.join(f'<details class="faq reveal"{" open" if j==0 else ""}><summary>{q}<span class="fq-ic" aria-hidden="true">+</span></summary><p>{ans}</p></details>' for j,(q,ans) in enumerate(faqs))
    if i<2:
        n=CLASSES[i+1]; nxt=f'<section class="next-band"><div class="wrap nb-inner reveal"><div><span class="kicker">Keep progressing</span><h2>Next stage: {n["num"]} {n["level"]}</h2><p>{n["title"]} · 6 recipes · {acc(n["fee"])}</p></div><div class="nb-ctas"><a class="btn btn-ghost" href="class-{n["slug"]}.html">View {n["level"]} {IC["arrow"]}</a><a class="btn btn-wa" href="class-{c["slug"]}.html?add={n["slug"]}#book">Book both, save {BUNDLE[2]}%</a></div></div></section>'
    else:
        nxt=f'<section class="next-band"><div class="wrap nb-inner reveal"><div><span class="kicker">The full pathway</span><h2>Beginner → Intermediate → Advanced</h2><p>Book all three classes together and save {BUNDLE[3]}%.</p></div><div class="nb-ctas"><a class="btn btn-ghost" href="classes.html">All classes {IC["arrow"]}</a><a class="btn btn-wa" href="class-advanced.html?add=all#book">Book full pathway</a></div></div></section>'
    return head(f'{c["level"]} Class: {ttl} | Mystery Bakebite | {SL}',f'{SL}. '+c['purpose'])+header()+f"""
<main>
<section class="page-hero cx-hero s-{c['slug']}"><div class="wrap">
<p class="crumbs"><a href="index.html">Home</a> / <a href="classes.html">Classes</a> / {c['level']}</p>
<div class="cx-grid">
<div class="cx-intro"><span class="cx-chip">Stage {c['num']} · {c['level']}</span>
<h1><span class="cx-num">{c['num']}</span>{c['title']}</h1>
<p class="ph-lede">{c['purpose']}</p>
<p class="script cd-slogan">{SL}</p>
<div class="hero-ctas"><a class="btn btn-wa" href="#book">{IC['wa']} Book {c['level']} Class</a><a class="btn btn-ghost" href="#recipes">See the 6 recipes</a></div></div>
<aside class="glance"><h2>At a glance</h2><ul>
<li>{IC['cal']}<span><small>Duration</small>{c['duration']}</span></li>
<li>{IC['clock']}<span><small>Recommended time</small>{c['time']} · {c['hours']}</span></li>
<li>{IC['whisk']}<span><small>Recipes</small>6 recipes</span></li>
<li>{IC['pin']}<span><small>Location</small>In person, Tamale</span></li>
<li>{IC['heartline']}<span><small>Available spaces</small>{c['spaces']}</span></li></ul>
<div class="gl-fee"><small>Class fee</small><b>{acc(c['fee'])}</b><span>per student · ingredients included</span></div></aside>
</div>{stage_path(c['slug'])}</div></section>

<nav class="subnav" aria-label="Class sections"><div class="wrap sn-inner">
<a href="#overview">Overview</a><a href="#recipes">Recipes</a><a href="#skills">Skills</a><a href="#details">Details</a><a href="#faq">FAQ</a><a href="#book" class="sn-book">Book now</a></div></nav>

<section class="cx-sec" id="overview"><div class="wrap ov-grid">
<div class="reveal"><span class="kicker">Overview</span><h2 class="sec-title left">About this class</h2><p class="ov-lead">{c['purpose']}</p><p class="ov-p">{c['short']} Over one week in a small group, you'll bake all six recipes with your own hands, guided step by step by Emmanuella.</p></div>
<div class="who reveal"><h3>Is this class for you?</h3><ul class="ticks">{who}</ul><p class="who-skill"><b>Required skill level:</b> {c['skill']}</p></div>
</div>
<div class="wrap"><div class="fit-row reveal">{fit}</div></div></section>

<section class="cx-sec alt" id="recipes"><div class="wrap"><div class="sec-head reveal"><span class="kicker">What you'll bake</span><h2 class="sec-title">The 6 recipes</h2><p class="sec-sub">{c['cat']} · {c['title']}</p>{DIV}</div>
<div class="rgrid">{rec}</div></div></section>

<section class="cx-sec" id="skills"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Skills</span><h2 class="sec-title">What you'll learn</h2>{DIV}</div>
<div class="sgrid">{learn}</div></div></section>

<section class="cx-sec alt" id="details"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Class details</span><h2 class="sec-title">Everything you need to know</h2>{DIV}</div>
<div class="dgrid">
<div class="dcard reveal"><h3>{IC['cal']} Schedule &amp; place</h3><dl>
<dt>Duration</dt><dd>{c['duration']}</dd><dt>Recommended time</dt><dd>{c['time']} ({c['hours']})</dd>
<dt>Location</dt><dd>In person, Tamale</dd><dt>Spaces</dt><dd>{c['spaces']}</dd><dt>Fee</dt><dd class="dd-fee">{acc(c['fee'])}</dd></dl></div>
<div class="dcard reveal"><h3>{IC['gift']} What's included</h3><ul class="ticks">{inc}</ul></div>
<div class="dcard reveal"><h3>{IC['bag']} What to bring</h3><ul class="ticks">{bring}</ul></div>
</div></div></section>

<section class="book-band on-dark" id="book"><div class="wrap bb-grid">
<div class="bb-intro reveal"><span class="kicker">Book your place</span><h2 class="sec-title left">Reserve your spot</h2><p class="bk-slogan">{SL}</p>
<p class="bb-p">Fill in the form and tap Book Now. WhatsApp opens with your booking details, and we confirm your date and space in the chat.</p>
<div class="bb-price"><small>Stage {c['num']} · {c['level']}</small><b>{acc(c['fee'])}</b><span>per student · {c['duration']} · {c['time']}</span></div>
<ul class="bb-deals"><li><b>{BUNDLE[2]}% off</b> when you book any 2 classes</li><li><b>{BUNDLE[3]}% off</b> when you book all 3 classes</li><li>Pay cash, or full payment upfront via MoMo</li></ul></div>
<form class="book-form bb-form reveal" data-d2="{BUNDLE[2]}" data-d3="{BUNDLE[3]}" data-level="{c['num']} {c['level']}" data-title="{ttl}" data-fee="{c['fee']}">
<fieldset class="pick"><legend>1 · Choose your class(es)</legend>{picks}<p class="pick-hint">Add a 2nd class for <b>{BUNDLE[2]}% off</b>, or all 3 for <b>{BUNDLE[3]}% off</b>.</p></fieldset>
<fieldset><legend>2 · Preferred schedule</legend>{opts}</fieldset>
<fieldset><legend>3 · Your details</legend><div class="fld-grid">
<label class="fld">Preferred start date<input type="date" name="date"></label>
<label class="fld">Number of students<select name="seats"><option>1</option><option>2</option><option>3</option><option>4</option></select></label>
<label class="fld">Your name<input type="text" name="name" placeholder="Full name" required></label>
<label class="fld">Phone number<input type="tel" name="phone" placeholder="e.g. 024 000 0000"></label></div></fieldset>
<div class="bk-sum">
<p><span>Classes subtotal</span><span>GH₵ <span class="sub">{float(c['fee']):,.2f}</span></span></p>
<p class="disc-row" hidden><span>Bundle discount (<span class="disc-pct">0</span>%)</span><span>− GH₵ <span class="disc">0.00</span></span></p>
<p><span>Students</span><span>× <span class="n">1</span></span></p>
<p class="bk-total"><span>Estimated total</span><b>GH₵ <span class="tot">{float(c['fee']):,.2f}</span></b></p></div>
<button class="btn btn-wa bk-btn" type="submit">{IC['wa']} Book Now</button>
<p class="bk-note">Your date and space are confirmed in the WhatsApp chat.</p>
</form></div></section>

<section class="cx-sec" id="faq"><div class="wrap faq-wrap"><div class="sec-head reveal"><span class="kicker">Questions</span><h2 class="sec-title">Frequently asked</h2>{DIV}</div>{faq}</div></section>
{nxt}
</main>"""+footer()


index=head('Mystery Bakebite | Unveiling The Uniqueness of A Recipe','Unveiling The Uniqueness of A Recipe. Home bakery in Tamale, Northern Ghana. Milky doughnuts, cakes, cupcakes, cookies, baking classes and custom orders from Mystery Bakebite in Tamale. Order on WhatsApp.')+header()+f"""
<main>
<section class="hero hero-story"><div class="wrap hs-grid">
<div class="hs-photo"><div class="hs-frame"><img src="assets/founder.jpg" alt="Emmanuella N. Awini, Founder and Head Baker, with a pink chocolate-drip cake"></div>
<div class="hs-note"><span class="hs-note-k">Founder &amp; Head Baker</span><b>Emmanuella N. Awini</b></div>
<div class="hs-float"><img src="assets/milky.jpg" alt="Milky donuts with cream filling"><span>Milky donuts from <b>GH₵30</b></span></div></div>
<div class="hs-copy"><p class="hero-kicker">Baking · Training · Creative</p>
<h1 class="hs-title">Hi, I'm Emmanuella.<span>Welcome to my kitchen.</span></h1>
<p class="hero-tagline">Unveiling The Uniqueness of A Recipe</p>
<p class="hero-lede">Mystery Bakebite began in my home kitchen in Tamale with one belief: every recipe hides something special. I bake soft milky doughnuts, dripping cakes and parfaits for your everyday moments, teach others to bake, and create custom treats for your celebrations.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Order on WhatsApp</a><a class="btn btn-ghost" href="#story">Read my story</a></div>
<p class="hs-sign">With love, Emmanuella</p></div>
</div></section>
<div class="marquee" aria-hidden="true"><div class="marquee-track">MQ</div></div>

<section class="story2" id="story"><div class="wrap">
<div class="sec-head reveal"><span class="kicker">Our story</span><h2 class="sec-title">A recipe is never just a recipe</h2><p class="sec-script">Unveiling The Uniqueness of A Recipe</p>{DIV}</div>
<div class="chapters">
<article class="chapter reveal"><span class="ch-n">01</span><div class="ch-ic">{IC['whisk']}</div><h3>It started at home</h3><p>A small kitchen in Tamale, a few trusted recipes, and family and friends who kept asking for more. Every batch is still made by hand, in small batches, by Emmanuella herself.</p></article>
<article class="chapter reveal"><span class="ch-n">02</span><div class="ch-ic">{IC['brush']}</div><h3>The mystery twist</h3><p>The "mystery" is that little something extra: more cream in a milky donut, a flavour pairing you didn't expect. It's what turns a good bake into your favourite one.</p></article>
<article class="chapter reveal"><span class="ch-n">03</span><div class="ch-ic">{IC['cap']}</div><h3>Sharing the craft</h3><p>Today, Mystery Bakebite also teaches hands-on baking classes and designs custom pieces for Tamale's birthdays, weddings and naming ceremonies.</p></article>
</div>
<blockquote class="pull reveal"><p>“I want every box that leaves my kitchen to feel like it was made just for you, because it was.”</p><cite>Emmanuella N. Awini, Founder &amp; Head Baker</cite></blockquote>
<div class="vbadges center reveal">{vals}</div>
</div></section>
<section class="menu-sec" id="menu"><div class="wrap"><div class="sec-head reveal"><span class="kicker">From my kitchen to your table</span><h2 class="sec-title">Something sweet for every moment</h2><p class="sec-sub">Eight favourites, baked to order. Tap a card for prices, or order straight from it.</p>{DIV}</div>
<div class="menu-grid">{cards}</div>
<div class="menu-ctas"><a class="btn btn-brown" href="menu.html">Full price list {IC['arrow']}</a><a class="btn btn-ghost-dark" href="assets/price-list.png" download="Mystery-Bakebite-Menu-Sept-2026.png">Download menu card</a></div>
<p class="menu-note">Prices effective September 2026 · All prices in GH₵</p></div></section>

"""+classes_teaser()+f"""
<section class="services custom-sec" id="custom"><div class="wrap">
<article class="svc svc-wide reveal"><figure><img src="assets/slices.jpg" alt="Layered celebration cake slices" loading="lazy"><span class="svc-tag">{IC['gift']} Creative</span></figure>
<div class="svc-body"><span class="kicker">Custom orders</span><h3>Dream it up with us</h3><p>Birthdays, weddings, naming ceremonies, office treats and gift boxes. Tell us your theme and we'll design something that's truly yours.</p>
<ul class="ticks two"><li>Celebration and themed cakes</li><li>Dessert tables and party packs</li><li>Branded gift boxes and bulk orders</li><li>Order 3 to 5 days ahead</li></ul>
<a class="btn btn-wa" href="{WA_CUSTOM}" target="_blank" rel="noopener">{IC['wa']} Request a custom order</a></div></article>
</div></section>

"""+testimonials_block()+gallery_block()+f"""
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

"""+payment_block()+f"""
<section class="closing on-dark"><div class="wrap cl-inner reveal"><img class="cl-logo" src="assets/logo.jpg" alt="">
<p class="cl-script">Baked with Love, Especially for You</p><p class="cl-p">Thank you for supporting a small, home-grown Tamale business. Whatever you're craving, let's make it together.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Order on WhatsApp</a><a class="btn btn-ghost" href="classes.html">Explore classes</a></div></div></section>
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
menu=head('Menu & Prices | Mystery Bakebite | Unveiling The Uniqueness of A Recipe','Unveiling The Uniqueness of A Recipe. Full price list for Mystery Bakebite, Tamale. Effective September 2026.')+header()+f'''
<main><section class="page-hero"><div class="wrap"><img class="ph-logo" src="assets/logo.jpg" alt="Mystery Bakebite logo"><h1>Menu &amp; Prices</h1><p class="script">Unveiling The Uniqueness of A Recipe</p>
<p class="ph-meta">Effective September 2026<i>♥</i>Tamale<i>♥</i>All prices in GH₵</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Order on WhatsApp</a><a class="btn btn-ghost" href="assets/price-list.png" download="Mystery-Bakebite-Menu-Sept-2026.png">Download menu card</a></div></div></section>
<section class="pricelist"><div class="wrap"><div class="pl-grid">{pl}</div></div></section>
'''+info_block()+payment_block()+f'''<section class="order-strip"><div class="wrap"><p class="script">Ready to order?</p><p>Send us your picks on WhatsApp with your preferred date and pickup or delivery in Tamale. Custom cakes and class bookings? Just ask!</p><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Message +233 55 452 0532</a></div></section></main>'''+footer()
MQ=''.join(f'<span>{i} {IC["heart"]} <em>freshly baked</em> {IC["heart"]}</span>' for i in ['Milky Doughnuts', 'Cake Slices', 'Cupcakes', 'Cake Parfaits', 'Donut Balls', 'Cookies', 'Cake Loaves', 'Baking Classes', 'Custom Orders'])
index=index.replace('MQ',MQ*2)
open('index.html','w').write(index); open('menu.html','w').write(menu)
open('classes.html','w').write(classes_page())
for _i,_c in enumerate(CLASSES): open(f'class-{_c["slug"]}.html','w').write(class_detail(_i))
