const navItems = [
  { path: 'home.html', label: 'Home' },
  { path: 'timeline.html', label: 'Timeline' },
  { path: 'explore_WA.html', label: 'Explore WA' },
  { path: 'guided_tour.html', label: 'Guided Tour' },
  { path: 'search.html', label: 'Search' },
];

function renderNav() {
  const desktopNav = document.getElementById('desktopNav');
  const mobileNav = document.getElementById('mobileNav');
  const currentPage = 'home.html';

  const html = navItems
    .map((item) => {
      const activeClass = item.path === currentPage ? 'active' : '';
      return `<a href="${item.path}" class="${activeClass}">${item.label}</a>`;
    })
    .join('');

  desktopNav.innerHTML = html;
  mobileNav.innerHTML = html;
}

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

renderNav();
setupMobileMenu();