const navItems = [
  { path: "/", label: "Home" },
  { path: "/timeline", label: "Timeline" },
  { path: "/explore-wa", label: "Explore WA" },
  { path: "/guided-tour", label: "Guided Tour" },
  { path: "/search", label: "Search" }
];

function renderNavigation() {
  const desktopNav = document.getElementById("desktopNav");
  const mobileNav = document.getElementById("mobileNav");
  const mobileToggle = document.getElementById("mobileToggle");

  if (!desktopNav || !mobileNav || !mobileToggle) return;

  const currentPage = window.location.pathname;

  desktopNav.innerHTML = navItems.map((item) => `
    <a href="${item.path}" class="${item.path === currentPage ? "active" : ""}">
      ${item.label}
    </a>
  `).join("");

  mobileNav.innerHTML = navItems.map((item) => `
    <a href="${item.path}" class="${item.path === currentPage ? "active" : ""}">
      ${item.label}
    </a>
  `).join("");

  mobileToggle.addEventListener("click", () => {
    mobileNav.classList.toggle("open");
  });

  mobileNav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      mobileNav.classList.remove("open");
    });
  });
}

function escapeRegExp(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function highlightText(text, query) {
  if (!query.trim()) return text;

  const regex = new RegExp(`(${escapeRegExp(query)})`, "gi");
  return text.replace(regex, '<mark class="search-highlight">$1</mark>');
}

async function fetchTopics() {
  try {
    const response = await fetch("/api/topics");
    if (!response.ok) {
      throw new Error("Failed to fetch topics");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching topics:", error);
    return [];
  }
}

function renderResults(results, query) {
  const resultsContainer = document.getElementById("resultsContainer");
  const emptyState = document.getElementById("emptyState");
  const resultCount = document.getElementById("resultCount");

  if (!resultsContainer || !emptyState || !resultCount) return;

  if (!query.trim()) {
    resultsContainer.innerHTML = "";
    resultCount.classList.add("hidden");
    emptyState.classList.remove("hidden");
    return;
  }

  resultCount.textContent = `${results.length} exhibit${results.length !== 1 ? "s" : ""} found`;
  resultCount.classList.remove("hidden");

  if (results.length === 0) {
    emptyState.classList.remove("hidden");
    emptyState.innerHTML = `
      <div class="empty-icon">🔎</div>
      <p class="empty-title">No exhibits found</p>
      <p class="empty-text">Try searching with another keyword, category, or year.</p>
    `;
    resultsContainer.innerHTML = "";
    return;
  }

  emptyState.classList.add("hidden");

  resultsContainer.innerHTML = results.map((topic, index) => `
    <a href="/topic/${topic.slug}" class="museum-card result-card fade-in" style="animation-delay:${index * 0.05}s">
      <div class="result-meta">
        <span class="exhibit-label">${topic.category}</span>
        <span class="result-year">${topic.yearRange}</span>
      </div>
      <h3 class="result-title">${highlightText(topic.title, query)}</h3>
      <p class="result-summary">${highlightText(topic.shortSummary, query)}</p>
      <div class="result-link">
        <span>Open exhibit</span>
        <span class="result-link-arrow">→</span>
      </div>
    </a>
  `).join("");
}

function initSearch() {
  const searchInput = document.getElementById("searchInput");
  if (!searchInput) return;

  let topics = [];

  // Fetch topics once and filter them locally
  fetchTopics().then((fetchedTopics) => {
    topics = fetchedTopics;

    searchInput.addEventListener("input", (event) => {
      const query = event.target.value.trim().toLowerCase();

      if (!query) {
        renderResults([], "");
        return;
      }

      const results = topics.filter((topic) => {
        const searchableText = [
          topic.title,
          topic.category,
          topic.yearRange,
          topic.shortSummary,
          topic.waContext
        ].join(" ").toLowerCase();
        return searchableText.includes(query);
      });

      renderResults(results, query);
    });

    // Render empty results initially
    renderResults([], "");
  });
}

document.addEventListener("DOMContentLoaded", () => {
  renderNavigation();
  initSearch();
});