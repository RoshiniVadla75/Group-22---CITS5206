function setupMobileMenu() {
  const mobileToggle = document.getElementById('mobileToggle');
  const mobileNav = document.getElementById('mobileNav');

  if (!mobileToggle || !mobileNav) return;

  mobileToggle.addEventListener('click', () => {
    mobileNav.classList.toggle('open');
    mobileToggle.textContent = mobileNav.classList.contains('open')
      ? '✕'
      : '☰';
  });
}

function highlightCurrentNav() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('#desktopNav a, #mobileNav a');

  navLinks.forEach((link) => {
    const href = link.getAttribute('href');

    if (
      href === currentPath ||
      (currentPath.startsWith('/topic/') && href === '/timeline')
    ) {
      link.classList.add('active');
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  setupMobileMenu();
  highlightCurrentNav();
});
