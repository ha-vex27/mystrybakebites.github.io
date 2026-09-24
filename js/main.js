// Mystery Bakebite: tiny progressive-enhancement script
document.documentElement.classList.add('js');

// Mobile navigation toggle
var toggle = document.querySelector('.nav-toggle');
if (toggle) {
  toggle.addEventListener('click', function () {
    var open = document.body.classList.toggle('nav-open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  // close after choosing a link
  document.querySelectorAll('.main-nav a').forEach(function (a) {
    a.addEventListener('click', function () {
      document.body.classList.remove('nav-open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}

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
document.querySelectorAll('.menu-grid, .insta-grid, .steps, .pl-grid, .svc-grid, .info-grid, .pay-grid, .t-grid, .g-grid').forEach(function (g) {
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
