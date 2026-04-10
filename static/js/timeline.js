const navItems = [
  { path: '/', label: 'Home' },
  { path: '/timeline', label: 'Timeline' },
  { path: '/explore-wa', label: 'Explore WA' },
  { path: '/guided-tour', label: 'Guided Tour' },
  { path: '/search', label: 'Search' },
];

const decades = [
  'All',
  '1950s',
  '1960s',
  '1970s',
  '1980s',
  '1990s',
  '2000s',
  '2010s',
  '2020s',
];

const statuses = ['All', 'Active', 'Legacy'];

let selectedDecade = 'All';
let selectedCategory = 'All';
let selectedStatus = 'All';
let allTopics = [];

function renderNav() {
  const desktopNav = document.getElementById('desktopNav');
  const mobileNav = document.getElementById('mobileNav');
  const currentPage = window.location.pathname;

  if (!desktopNav || !mobileNav) return;

  const html = navItems
    .map((item) => {
      const activeClass = item.path === currentPage ? 'active' : '';
      return `<a href="${item.path}" class="${activeClass}">${item.label}</a>`;
    })
    .join('');

  desktopNav.innerHTML = html;
  mobileNav.innerHTML = html;
}

async function fetchTopics() {
  try {
    const response = await fetch('/api/topics');
    if (!response.ok) {
      throw new Error('Failed to fetch topics');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching topics:', error);
    return [];
  }
}

function extractStartYear(yearRange) {
  if (!yearRange) return null;
  const match = String(yearRange).match(/\d{4}|\d{3}/);
  if (!match) return null;
  return parseInt(match[0], 10);
}

function getTopicDecade(topic) {
  const year = extractStartYear(topic.yearRange);
  if (!year) return null;
  return `${Math.floor(year / 10) * 10}s`;
}

function getCategories() {
  const categories = allTopics
    .map((topic) => topic.category)
    .filter((category) => category && category.trim() !== '');
  return ['All', ...new Set(categories)];
}

function buildFilterButtons(
  containerId,
  values,
  selectedValue,
  onClickHandler,
) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = values
    .map((value) => {
      const activeClass = value === selectedValue ? 'active' : '';
      return `<button class="filter-btn ${activeClass}" data-value="${value}">${value}</button>`;
    })
    .join('');

  container.querySelectorAll('.filter-btn').forEach((button) => {
    button.addEventListener('click', () => {
      onClickHandler(button.dataset.value);
    });
  });
}

function renderFilters() {
  buildFilterButtons('decadeFilters', decades, selectedDecade, (value) => {
    selectedDecade = value;
    renderFilters();
    renderTimeline();
  });

  buildFilterButtons(
    'categoryFilters',
    getCategories(),
    selectedCategory,
    (value) => {
      selectedCategory = value;
      renderFilters();
      renderTimeline();
    },
  );

  buildFilterButtons('statusFilters', statuses, selectedStatus, (value) => {
    selectedStatus = value;
    renderFilters();
    renderTimeline();
  });
}

function getFilteredTopics() {
  return allTopics.filter((topic) => {
    const matchesDecade =
      selectedDecade === 'All' || getTopicDecade(topic) === selectedDecade;

    const matchesCategory =
      selectedCategory === 'All' || topic.category === selectedCategory;

    const matchesStatus =
      selectedStatus === 'All' || topic.status === selectedStatus;

    return matchesDecade && matchesCategory && matchesStatus;
  });
}

function renderTimeline() {
  const timelineList = document.getElementById('timelineList');
  const emptyState = document.getElementById('emptyState');

  if (!timelineList || !emptyState) return;

  const filteredTopics = getFilteredTopics();

  if (filteredTopics.length === 0) {
    timelineList.innerHTML = '';
    emptyState.classList.remove('hidden');
    return;
  }

  emptyState.classList.add('hidden');

  timelineList.innerHTML = filteredTopics
    .map((topic, index) => {
      const sideClass = index % 2 === 0 ? 'right' : 'left';
      const isActive = topic.status === 'Active';
      const statusClass = isActive ? 'status-active' : 'status-legacy';
      const dotClass = isActive ? 'timeline-dot active' : 'timeline-dot legacy';

      return `
        <div class="timeline-row">
          <div class="timeline-card-wrap ${sideClass}">
            <a href="/topic/${topic.slug}" class="museum-card timeline-card">
              <div class="timeline-card-header">
                <div class="timeline-topline">
                  <span class="exhibit-label timeline-category">${topic.category || ''}</span>
                  <span class="timeline-status ${statusClass}">${topic.status || 'Legacy'}</span>
                </div>

                <span class="timeline-year">${topic.yearRange || ''}</span>
              </div>

              <h3 class="timeline-title">${topic.title}</h3>

              <p class="timeline-desc">
                ${topic.shortSummary || 'Explore this exhibit in the AI Museum timeline.'}
              </p>

              <div class="timeline-link">
                <span>Open Exhibit</span>
                <span class="timeline-arrow">→</span>
              </div>
            </a>
          </div>

          <div class="timeline-middle">
            <div class="${dotClass}"></div>
          </div>
        </div>
      `;
    })
    .join('');
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

async function initTimelinePage() {
  renderNav();
  setupMobileMenu();

  allTopics = await fetchTopics();

  renderFilters();
  renderTimeline();
}

initTimelinePage();
