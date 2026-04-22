// ============================================================
// APNI PEHCHAN — main.js
// ============================================================

// ── Theme Toggle ──
const themeToggle = document.getElementById('themeToggle');
const html = document.documentElement;

function applyTheme(dark) {
    html.setAttribute('data-theme', dark ? 'dark' : 'light');
    if (themeToggle) themeToggle.querySelector('.theme-icon').textContent = dark ? '☀' : '🌙';
    localStorage.setItem('ap-theme', dark ? 'dark' : 'light');
}

let isDark = localStorage.getItem('ap-theme') !== 'light';
applyTheme(isDark);
if (themeToggle) {
    themeToggle.addEventListener('click', () => { isDark = !isDark; applyTheme(isDark); });
}

// ── Mobile Hamburger ──
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');
if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => mobileMenu.classList.toggle('open'));
}

// ── Navbar scroll shrink ──
const navbar = document.getElementById('navbar');
if (navbar) {
    window.addEventListener('scroll', () => {
        navbar.style.height = window.scrollY > 60 ? '56px' : '';
    });
}

// ── Scroll Reveal ──
document.querySelectorAll('.reveal').forEach(el => {
    new IntersectionObserver(([entry]) => {
        if (entry.isIntersecting) { el.classList.add('visible'); }
    }, { threshold: 0.1 }).observe(el);
});

// ── Flash messages auto-dismiss ──
document.querySelectorAll('.alert').forEach(el => {
    setTimeout(() => el.style.opacity = '0', 4000);
});

// ── Jinja2 filter for from_json (handled server-side, but also needed client-side) ──
// Profile page: avatar drag and drop
const dropZone = document.querySelector('.upload-zone');
if (dropZone) {
    ['dragenter','dragover'].forEach(e => dropZone.addEventListener(e, ev => {
        ev.preventDefault(); dropZone.style.borderColor = 'var(--accent)';
    }));
    dropZone.addEventListener('dragleave', () => dropZone.style.borderColor = '');
    dropZone.addEventListener('drop', ev => {
        ev.preventDefault();
        const file = ev.dataTransfer.files[0];
        const input = document.getElementById('avatarInput');
        if (input && file) {
            const dt = new DataTransfer();
            dt.items.add(file);
            input.files = dt.files;
            input.dispatchEvent(new Event('change'));
        }
    });
}