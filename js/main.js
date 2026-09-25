// Mystery Bakebite: tiny progressive-enhancement script
document.documentElement.classList.add('js');

// Navigation v2: dropdowns, drawer, current page
(function () {
  var items = document.querySelectorAll('.has-dd');
  function closeAll(except) { items.forEach(function (i) { if (i !== except) { i.classList.remove('open'); i.querySelector('.dd-btn').setAttribute('aria-expanded', 'false'); } }); }
  items.forEach(function (it) {
    var b = it.querySelector('.dd-btn');
    b.addEventListener('click', function (e) {
      e.stopPropagation(); var o = !it.classList.contains('open'); closeAll(it);
      it.classList.toggle('open', o); b.setAttribute('aria-expanded', o ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.has-dd')) closeAll(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeAll(); closeDrawer(); } });
  document.querySelectorAll('.dd-link, .dd-foot').forEach(function (a) { a.addEventListener('click', function () { closeAll(); }); });

  var toggle = document.querySelector('.nav-toggle');
  function openDrawer() { document.body.classList.add('drawer-open'); toggle.setAttribute('aria-expanded', 'true'); document.getElementById('drawer').setAttribute('aria-hidden', 'false'); }
  function closeDrawer() { document.body.classList.remove('drawer-open'); if (toggle) toggle.setAttribute('aria-expanded', 'false'); var d = document.getElementById('drawer'); if (d) d.setAttribute('aria-hidden', 'true'); }
  if (toggle) toggle.addEventListener('click', openDrawer);
  document.querySelectorAll('[data-close], .dr-panel a').forEach(function (el) { el.addEventListener('click', closeDrawer); });

  // current page highlight
  var page = location.pathname.split('/').pop() || 'index.html';
  var key = page === 'menu.html' ? 'menu' : /^class/.test(page) ? 'classes' : page === 'index.html' ? 'home' : null;
  if (key) { var el = document.querySelector('.main-nav [data-key="' + key + '"]'); if (el) el.classList.add('current'); }
  document.querySelectorAll('.dr-main').forEach(function (a) { if (a.getAttribute('href') === page || (key === 'classes' && a.getAttribute('href') === 'classes.html')) a.classList.add('current'); });
  document.querySelectorAll('.dd-link').forEach(function (a) { if (a.getAttribute('href') === page) a.style.background = 'rgba(212,164,55,.14)'; });
})();

// Reveal-on-scroll
if ('IntersectionObserver' in window) {
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
} else {
  document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('visible'); });
}

var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// Stagger reveals among siblings + directional variants
document.querySelectorAll('.menu-grid, .insta-grid, .steps, .pl-grid, .svc-grid, .info-grid, .pay-grid, .g-grid, .stage-grid, .guide-grid, .cd-facts, .bundle-grid, .level-list, .rgrid, .sgrid, .dgrid').forEach(function (g) {
  Array.prototype.forEach.call(g.querySelectorAll('.reveal'), function (el, i) {
    el.style.setProperty('--d', (i % 4) * 0.1 + 's');
  });
});
document.querySelectorAll('.insta-grid .reveal').forEach(function (el) { el.classList.add('zoom'); });
var sp = document.querySelector('.story-photo'); if (sp) sp.classList.add('from-left');
var sc = document.querySelector('.story-grid > div:last-child'); if (sc) sc.classList.add('from-right');

// Scroll progress + header state + hero parallax
var bar = document.createElement('div'); bar.className = 'progress'; document.body.appendChild(bar);
var header = document.querySelector('.site-header');
var frame = document.querySelector('.hero-frame');
function onScroll() {
  var y = window.scrollY, h = document.documentElement.scrollHeight - innerHeight;
  bar.style.transform = 'scaleX(' + (h > 0 ? y / h : 0) + ')';
  if (header) header.classList.toggle('scrolled', y > 30);
  if (frame && !reduce && y < 900) frame.style.transform = 'rotate(-1.6deg) translateY(' + (y * -0.08) + 'px)';
}
addEventListener('scroll', onScroll, { passive: true }); onScroll();

var desktop = window.matchMedia('(min-width: 769px)').matches;
if (!reduce && desktop) {
  // Cursor sheen on menu cards (no tilt)
  document.querySelectorAll('.mcard').forEach(function (c) {
    c.addEventListener('mousemove', function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) / r.width * 100 + '%');
      c.style.setProperty('--my', (e.clientY - r.top) / r.height * 100 + '%');
    });
  });
  // A few sprinkles, homepage hero only
  var hero = document.querySelector('.hero');
  if (hero) {
    var box = document.createElement('div'); box.className = 'sprinkles';
    var cols = ['#F7B7C8', '#D4A437', '#F5E6D6'];
    for (var i = 0; i < 10; i++) {
      var s = document.createElement('i');
      s.style.left = Math.random() * 100 + '%';
      s.style.background = cols[i % cols.length];
      s.style.animationDuration = 14 + Math.random() * 10 + 's';
      s.style.animationDelay = -Math.random() * 20 + 's';
      box.appendChild(s);
    }
    hero.insertBefore(box, hero.firstChild);
  }
}

// Ambient glass blobs in each section
(function () {
  if (!window.matchMedia('(min-width: 769px)').matches) return;
  var sets = [['pink', 'gold'], ['gold', 'warm'], ['pink', 'warm']];
  document.querySelectorAll('section, .footer').forEach(function (sec, i) {
    sets[i % 3].concat(['pink']).forEach(function (c, j) {
      var b = document.createElement('span');
      b.className = 'blob ' + c;
      var size = 260 + Math.random() * 220;
      b.style.width = b.style.height = size + 'px';
      b.style.left = (j === 0 ? -8 : j === 1 ? 62 : 30) + Math.random() * 12 + '%';
      b.style.top = (j === 1 ? -10 : 45) + Math.random() * 25 + '%';
      b.style.animationDelay = -Math.random() * 18 + 's';
      b.style.animationDuration = 16 + Math.random() * 10 + 's';
      sec.insertBefore(b, sec.firstChild);
    });
  });
})();

// Gallery lightbox
(function () {
  var lb = document.getElementById('lightbox'); if (!lb) return;
  var items = Array.prototype.slice.call(document.querySelectorAll('.g-item'));
  var img = lb.querySelector('img'), cap = lb.querySelector('figcaption'), idx = 0;
  function show(i) { idx = (i + items.length) % items.length; img.src = items[idx].dataset.src; img.alt = items[idx].dataset.cap; cap.innerHTML = items[idx].dataset.cap; }
  function open(i) { show(i); lb.hidden = false; document.body.style.overflow = 'hidden'; }
  function close() { lb.hidden = true; document.body.style.overflow = ''; }
  items.forEach(function (it, i) { it.addEventListener('click', function () { open(i); }); });
  lb.querySelector('.lb-close').onclick = close;
  lb.querySelector('.lb-prev').onclick = function (e) { e.stopPropagation(); show(idx - 1); };
  lb.querySelector('.lb-next').onclick = function (e) { e.stopPropagation(); show(idx + 1); };
  lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  document.addEventListener('keydown', function (e) {
    if (lb.hidden) return;
    if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(idx - 1); if (e.key === 'ArrowRight') show(idx + 1);
  });
})();

// Class booking form -> WhatsApp (multi-class bundles)
document.querySelectorAll('.book-form').forEach(function (f) {
  var fmt = function (n) { return n.toLocaleString('en-GH', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); };
  var d2 = +f.dataset.d2, d3 = +f.dataset.d3;
  var boxes = Array.prototype.slice.call(f.querySelectorAll('[name=cls]'));
  var seats = f.querySelector('[name=seats]');
  var q = f.querySelector.bind(f);
  // preselect from ?add=slug or ?add=all
  var add = new URLSearchParams(location.search).get('add');
  if (add) boxes.forEach(function (b) { if (add === 'all' || add.split(',').indexOf(b.value) > -1) b.checked = true; });
  var state = {};
  function calc() {
    var chosen = boxes.filter(function (b) { return b.checked; });
    if (!chosen.length) { chosen = [boxes.filter(function (b) { return b.defaultChecked; })[0] || boxes[0]]; chosen[0].checked = true; }
    var sub = chosen.reduce(function (t, b) { return t + (+b.dataset.fee); }, 0);
    var pct = chosen.length >= 3 ? d3 : chosen.length === 2 ? d2 : 0;
    var n = +seats.value, disc = sub * pct / 100, tot = (sub - disc) * n;
    q('.sub').textContent = fmt(sub); q('.disc').textContent = fmt(disc); q('.disc-pct').textContent = pct;
    q('.disc-row').hidden = !pct; q('.n').textContent = n; q('.tot').textContent = fmt(tot);
    state = { chosen: chosen, sub: sub, pct: pct, disc: disc, n: n, tot: tot };
  }
  boxes.forEach(function (b) { b.addEventListener('change', calc); });
  seats.addEventListener('change', calc); calc();
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var g = function (n) { var el = f.querySelector('[name=' + n + ']'); return el ? el.value.trim() : ''; };
    var sch = f.querySelector('[name=schedule]:checked');
    var list = state.chosen.map(function (b) { return '   - ' + b.dataset.name + ' (GH₵ ' + fmt(+b.dataset.fee) + ')'; }).join('\n');
    var msg = "Hello Mystery Bakebite! 👩🏾‍🍳 I'd like to book baking class" + (state.chosen.length > 1 ? 'es' : '') + ".\n\n" +
      '• Class' + (state.chosen.length > 1 ? 'es' : '') + ' (1 week each):\n' + list + '\n' +
      (state.pct ? '• Bundle discount: ' + state.pct + '% (− GH₵ ' + fmt(state.disc) + ' per student)\n' : '') +
      '• Preferred schedule: ' + (sch ? sch.value : '') + '\n' +
      '• Preferred start date: ' + (g('date') || 'Flexible') + '\n' +
      '• Number of students: ' + state.n + '\n' +
      '• Estimated total: GH₵ ' + fmt(state.tot) + '\n\n' +
      'Name: ' + g('name') + '\nPhone: ' + g('phone');
    window.open('https://wa.me/233554520532?text=' + encodeURIComponent(msg), '_blank', 'noopener');
  });
});

// Soft fade-out when moving between pages
if (!reduce) {
  document.querySelectorAll('a[href]').forEach(function (a) {
    var h = a.getAttribute('href');
    if (!h || h.charAt(0) === '#' || a.target === '_blank' || a.hasAttribute('download') || /^(https?:|mailto:|tel:)/.test(h) || h.indexOf('#') > 0 && h.split('#')[0] === location.pathname.split('/').pop()) return;
    a.addEventListener('click', function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey) return;
      e.preventDefault(); document.body.classList.add('leaving');
      setTimeout(function () { location.href = h; }, 220);
    });
  });
  window.addEventListener('pageshow', function () { document.body.classList.remove('leaving'); });
}
// Flash the total when it changes
document.querySelectorAll('.book-form').forEach(function (f) {
  var t = f.querySelector('.bk-total b');
  f.addEventListener('change', function () { t.classList.remove('bump'); void t.offsetWidth; t.classList.add('bump'); });
});

// Class page sub-nav: highlight current section
(function () {
  var links = document.querySelectorAll('.subnav a:not(.sn-book)'); if (!links.length || !('IntersectionObserver' in window)) return;
  var map = {}; links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { links.forEach(function (l) { l.classList.remove('active'); }); var l = map[e.target.id]; if (l) { l.classList.add('active'); l.scrollIntoView({ block: 'nearest', inline: 'center' }); } } });
  }, { rootMargin: '-45% 0px -50% 0px' });
  Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
})();

// Sliding glow pill behind hovered nav item
(function () {
  var nav = document.querySelector('.nav2 .main-nav'), glow = nav && nav.querySelector('.nav-glow'); if (!glow) return;
  var links = nav.querySelectorAll(':scope > .nav-link, :scope > .nav-item > .nav-link');
  function move(el) { var r = el.getBoundingClientRect(), n = nav.getBoundingClientRect(); glow.style.left = (r.left - n.left) + 'px'; glow.style.width = r.width + 'px'; glow.style.opacity = 1; }
  function rest() { var cur = nav.querySelector('.current > .nav-link, .nav-link.current'); if (cur) move(cur); else glow.style.opacity = 0; }
  links.forEach(function (l) { (l.closest('.nav-item') || l).addEventListener('mouseenter', function () { move(l); }); l.addEventListener('focus', function () { move(l); }); });
  nav.addEventListener('mouseleave', function () { if (!nav.querySelector('.has-dd.open')) rest(); });
  setTimeout(rest, 50); addEventListener('resize', rest);
})();

// Homepage: highlight nav link for the section in view
(function () {
  var page = location.pathname.split('/').pop() || 'index.html'; if (page !== 'index.html' || !('IntersectionObserver' in window)) return;
  var map = { order: 'order', payment: 'order', gallery: 'gallery', story: 'story' };
  var home = document.querySelector('.nav6 [data-key="home"]');
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      var k = map[e.target.id]; if (!k) return;
      var l = document.querySelector('.nav6 [data-key="' + k + '"]');
      if (e.isIntersecting) { document.querySelectorAll('.nav6 .nav-link').forEach(function (x) { x.classList.remove('current'); }); l.classList.add('current'); }
      else if (l.classList.contains('current')) { l.classList.remove('current'); if (home) home.classList.add('current'); }
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
})();
