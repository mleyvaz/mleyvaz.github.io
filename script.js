// ============================================
// Sitio personal — Dr. Maikel Leyva Vázquez
// Interacciones: navbar, menú móvil, fade-in
// ============================================

// --- Navbar: añadir clase .scrolled al hacer scroll
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 30) navbar.classList.add('scrolled');
  else navbar.classList.remove('scrolled');
});

// --- Toggle menú móvil
const navToggle = document.getElementById('navToggle');
const navMenu = document.querySelector('.nav-menu');
navToggle.addEventListener('click', () => {
  navMenu.classList.toggle('open');
  navToggle.classList.toggle('open');
});
// Cerrar menú móvil al clicar un link
document.querySelectorAll('.nav-menu a').forEach(link => {
  link.addEventListener('click', () => {
    navMenu.classList.remove('open');
    navToggle.classList.remove('open');
  });
});

// --- Fade-in de secciones al entrar en viewport
const sections = document.querySelectorAll('.section, .hero-meta');
sections.forEach(s => s.classList.add('fade-in'));

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -80px 0px' });

sections.forEach(s => observer.observe(s));

// --- Scroll activo (resalta la sección actual en navbar)
const navLinks = document.querySelectorAll('.nav-menu a');
const sectionTargets = document.querySelectorAll('section[id]');

window.addEventListener('scroll', () => {
  const scrollPos = window.scrollY + 120;
  sectionTargets.forEach(section => {
    const top = section.offsetTop;
    const bottom = top + section.offsetHeight;
    const id = section.getAttribute('id');
    const link = document.querySelector(`.nav-menu a[href="#${id}"]`);
    if (link) {
      if (scrollPos >= top && scrollPos < bottom) link.classList.add('active');
      else link.classList.remove('active');
    }
  });
});
