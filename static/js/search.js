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
    if (href === currentPath) {
      link.classList.add('active');
    }
  });
}

function setupSearch() {
  const input = document.getElementById('searchInput');
  const results = document.getElementById('resultsContainer');
  const emptyState = document.getElementById('emptyState');
  const resultCount = document.getElementById('resultCount');

  if (!input || !results) return;

  const cards = Array.from(results.querySelectorAll('.result-card'));

  function filterResults(query) {
    let visibleCount = 0;

    cards.forEach((card) => {
      const text = card.innerText.toLowerCase();

      if (text.includes(query)) {
        card.style.display = 'block';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    if (query === '') {
      emptyState.classList.remove('hidden');
      resultCount.classList.add('hidden');
      cards.forEach((c) => (c.style.display = 'block'));
      return;
    }

    emptyState.classList.add('hidden');

    resultCount.classList.remove('hidden');
    resultCount.textContent = `${visibleCount} result(s) found`;

    if (visibleCount === 0) {
      emptyState.classList.remove('hidden');
      emptyState.querySelector('.empty-title').textContent =
        'No results found';
    }
  }

  input.addEventListener('input', (e) => {
    const query = e.target.value.trim().toLowerCase();
    filterResults(query);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  setupMobileMenu();
  highlightCurrentNav();
  setupSearch();
});