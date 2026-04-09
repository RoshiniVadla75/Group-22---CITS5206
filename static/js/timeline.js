const navItems = [
  { path: "/", label: "Home" },
  { path: "/timeline", label: "Timeline" },
  { path: "/explore-wa", label: "Explore WA" },
  { path: "/guided-tour", label: "Guided Tour" },
  { path: "/search", label: "Search" },
];

const decades = [
  "All",
  "1950s",
  "1960s",
  "1970s",
  "1980s",
  "1990s",
  "2000s",
  "2010s",
  "2020s",
];

let selectedDecade = "All";
let selectedCategory = "All";

function renderNav() {
  const desktopNav = document.getElementById("desktopNav");
  const mobileNav = document.getElementById("mobileNav");
  const currentPage = window.location.pathname;

  const html = navItems
    .map((item) => {
      const activeClass = item.path === currentPage ? "active" : "";
      return `<a href="${item.path}" class="${activeClass}">${item.label}</a>`;
    })
    .join("");

  desktopNav.innerHTML = html;
  mobileNav.innerHTML = html;
}

function extractStartYear(yearRange) {
  const match = yearRange.match(/\d{4}|\d{3}/);
  if (!match) return null;
  return parseInt(match[0], 10);
}

function getTopicDecade(topic) {
  const year = extractStartYear(topic.year_range);
  if (!year) return null;
  return `${Math.floor(year / 10) * 10}s`;
}

function getCategories() {
  return ["All", ...new Set(topics.map((topic) => topic.category))];
}

function buildFilterButtons(containerId, values, selectedValue, onClickHandler) {
  const container = document.getElementById(containerId);

  container.innerHTML = values
    .map((value) => {
      const activeClass = value === selectedValue ? "active" : "";
      return `<button class="filter-btn ${activeClass}" data-value="${value}">${value}</button>`;
    })
    .join("");

  container.querySelectorAll(".filter-btn").forEach((button) => {
    button.addEventListener("click", () => {
      onClickHandler(button.dataset.value);
    });
  });
}

function renderFilters() {
  buildFilterButtons("decadeFilters", decades, selectedDecade, (value) => {
    selectedDecade = value;
    renderFilters();
    renderTimeline();
  });

  buildFilterButtons(
    "categoryFilters",
    getCategories(),
    selectedCategory,
    (value) => {
      selectedCategory = value;
      renderFilters();
      renderTimeline();
    }
  );
}

function getFilteredTopics() {
  return topics.filter((topic) => {
    const matchesDecade =
      selectedDecade === "All" || getTopicDecade(topic) === selectedDecade;

    const matchesCategory =
      selectedCategory === "All" || topic.category === selectedCategory;

    return matchesDecade && matchesCategory;
  });
}

function renderTimeline() {
  const timelineList = document.getElementById("timelineList");
  const emptyState = document.getElementById("emptyState");
  const filteredTopics = getFilteredTopics();

  if (filteredTopics.length === 0) {
    timelineList.innerHTML = "";
    emptyState.classList.remove("hidden");
    return;
  }

  emptyState.classList.add("hidden");

  timelineList.innerHTML = filteredTopics
    .map((topic, index) => {
      const sideClass = index % 2 === 0 ? "right" : "left";

      return `
      <div class="timeline-row">
        <div class="timeline-card-wrap ${sideClass}">
          <a href="/topic-detail/${topic.slug}" class="museum-card timeline-card">
            <div class="timeline-card-header">
              <span class="exhibit-label timeline-category">${topic.category}</span>
              <span class="timeline-year">${topic.year_range}</span>
            </div>

            <h3 class="timeline-title">${topic.title}</h3>

            <p class="timeline-desc">${topic.short_summary}</p>

            <div class="timeline-link">
              <span>Open Exhibit</span>
              <span class="timeline-arrow">→</span>
            </div>
          </a>
        </div>

        <div class="timeline-middle">
          <div class="timeline-dot"></div>
        </div>
      </div>
    `;
    })
    .join("");
}

function setupMobileMenu() {
  const mobileToggle = document.getElementById("mobileToggle");
  const mobileNav = document.getElementById("mobileNav");

  if (!mobileToggle || !mobileNav) return;

  mobileToggle.addEventListener("click", () => {
    mobileNav.classList.toggle("open");
    mobileToggle.textContent = mobileNav.classList.contains("open")
      ? "✕"
      : "☰";
  });
}

renderNav();
renderFilters();
renderTimeline();
setupMobileMenu();