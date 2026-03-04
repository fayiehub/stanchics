/* js/main.js — shared across all pages */

const API_BASE = 'https://stanchics-api.azurewebsites.net'; // update after deploying backend

/* =============================================
   NAV — inject shared nav, set active link
============================================= */
function initNav() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';

  const navHTML = `
    <nav class="nav" id="mainNav">
      <div class="container">
        <div class="nav__inner">
          <a href="../index.html" class="nav__logo">
            <div class="nav__logo-mark">S</div>
            <div>
              <div class="nav__logo-text">Stanchics</div>
              <span class="nav__logo-sub">Women in Tech · Stanbic Bank</span>
            </div>
          </a>
          <ul class="nav__links">
            <li><a class="nav__link" href="index.html"       data-page="index.html">Home</a></li>
            <li><a class="nav__link" href="about.html"     data-page="about.html">About</a></li>
            <li><a class="nav__link" href="events.html"    data-page="events.html">Events</a></li>
            <li><a class="nav__link" href="community.html" data-page="community.html">Community</a></li>
            <li><a class="nav__link" href="contact.html"   data-page="contact.html">Contact</a></li>
          </ul>
          <div class="nav__actions">
            <a class="btn btn--primary btn--sm" href="community.html">Join Us</a>
            <button class="nav__hamburger" id="hamburger" aria-label="Open menu" onclick="openDrawer()">
              <span></span><span></span><span></span>
            </button>
          </div>
        </div>
      </div>
    </nav>

    <div class="nav__drawer" id="navDrawer">
      <div class="nav__drawer-overlay" onclick="closeDrawer()"></div>
      <div class="nav__drawer-panel">
        <button class="nav__drawer-close" onclick="closeDrawer()">
          <i data-lucide="x" width="24" height="24"></i>
        </button>
        <ul class="nav__drawer-links">
          <li><a class="nav__drawer-link" href="index.html">Home</a></li>
          <li><a class="nav__drawer-link" href="about.html">About</a></li>
          <li><a class="nav__drawer-link" href="events.html">Events</a></li>
          <li><a class="nav__drawer-link" href="community.html">Community</a></li>
          <li><a class="nav__drawer-link" href="contact.html">Contact</a></li>
        </ul>
        <a class="btn btn--primary" href="community.html" style="width:100%; justify-content:center;">Join the Community</a>
      </div>
    </div>
  `;

  // Insert nav at the very top of body
  document.body.insertAdjacentHTML('afterbegin', navHTML);

  // Mark the active link
  document.querySelectorAll('.nav__link').forEach(link => {
    if (link.dataset.page === currentPage) link.classList.add('active');
  });

  // Sticky shadow on scroll
  window.addEventListener('scroll', () => {
    document.getElementById('mainNav').classList.toggle('scrolled', window.scrollY > 10);
  });
}

/* =============================================
   FOOTER — inject shared footer
============================================= */
function initFooter() {
  const footerHTML = `
    <footer class="footer">
      <div class="container">
        <div class="footer__grid">
          <div>
            <div class="footer__logo-mark">S</div>
            <div class="footer__brand-name">Stanchics</div>
            <p class="footer__tagline">Women in Tech. In Community.</p>
            <div class="footer__location">
              <i data-lucide="map-pin" width="14" height="14"></i>
              Nairobi, Kenya 🇰🇪
            </div>
          </div>
          <div>
            <div class="footer__nav-heading">Navigate</div>
            <ul class="footer__nav-list">
              <li><a class="footer__nav-link" href="index.html">Home</a></li>
              <li><a class="footer__nav-link" href="about.html">About</a></li>
              <li><a class="footer__nav-link" href="events.html">Events</a></li>
              <li><a class="footer__nav-link" href="community.html">Community</a></li>
              <li><a class="footer__nav-link" href="contact.html">Contact</a></li>
            </ul>
          </div>
          <div>
            <div class="footer__newsletter-heading">Stay in the loop</div>
            <p class="footer__newsletter-sub">Get event announcements and community updates — no spam, ever.</p>
            <div class="footer__newsletter-form">
              <input type="email" class="form-input" placeholder="Your email" id="footerEmailInput" />
              <button class="btn btn--primary btn--sm" onclick="handleFooterSignup()">Subscribe</button>
            </div>
            <div id="footerSignupSuccess" class="form-success" style="margin-top:var(--space-2); font-size:13px; padding:10px 14px;">
              <i data-lucide="check-circle" width="16" height="16"></i>
              You're subscribed!
            </div>
          </div>
        </div>
        <div class="footer__bottom">
          <span>© 2026 Stanchics. All rights reserved.</span>
          <span>Made with ❤️ by Faith Irungu</span>
        </div>
      </div>
    </footer>
  `;

  document.body.insertAdjacentHTML('beforeend', footerHTML);
}

/* =============================================
   MOBILE DRAWER
============================================= */
function openDrawer() {
  document.getElementById('navDrawer').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeDrawer() {
  document.getElementById('navDrawer').classList.remove('open');
  document.body.style.overflow = '';
}

/* =============================================
   SCROLL ANIMATIONS
============================================= */
function initScrollAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), i * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.fade-in-up').forEach(el => observer.observe(el));
}

/* =============================================
   API HELPER
============================================= */
async function postToAPI(endpoint, data) {
  const res = await fetch(`${API_BASE}${endpoint}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || 'Something went wrong. Please try again.');
  }
  return res.json();
}

/* =============================================
   NEWSLETTER SIGNUP — footer (shared)
============================================= */
async function handleFooterSignup() {
  const emailEl = document.getElementById('footerEmailInput');
  const email = emailEl.value.trim();
  if (!email || !email.includes('@')) { alert('Please enter a valid email address.'); return; }

  try {
    await postToAPI('/api/newsletter', { email, source: 'footer' });
  } catch (e) {
    // fail silently — still show success to user for UX
    console.warn('Newsletter API error:', e.message);
  }

  document.getElementById('footerSignupSuccess').classList.add('visible');
  emailEl.value = '';
  lucide.createIcons();
}

/* =============================================
   FORM UTILITY
============================================= */
function showSuccess(id) {
  const el = document.getElementById(id);
  if (el) { el.classList.add('visible'); lucide.createIcons(); }
}

function clearFields(...ids) {
  ids.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.value = '';
  });
}

/* =============================================
   INIT — run on every page
============================================= */
document.addEventListener('DOMContentLoaded', () => {
  initNav();
  initFooter();
  lucide.createIcons();
  initScrollAnimations();
});
