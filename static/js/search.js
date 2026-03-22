const navItems = [
    { href: "home.html", label: "Home" },
    { href: "timeline.html", label: "Timeline" },
    { href: "explore_WA.html", label: "Explore WA" },
    { href: "guided_tour.html", label: "Guided Tour" },
    { href: "search.html", label: "Search" }
  ];
  
  const currentPage = "search.html";
  
  function renderNavigation() {
    const desktopNav = document.getElementById("desktopNav");
    const mobileNav = document.getElementById("mobileNav");
    const mobileToggle = document.getElementById("mobileToggle");
  
    if (!desktopNav || !mobileNav || !mobileToggle) return;
  
    desktopNav.innerHTML = navItems.map((item) => `
      <a href="${item.href}" class="${item.href === currentPage ? "active" : ""}">
        ${item.label}
      </a>
    `).join("");
  
    mobileNav.innerHTML = navItems.map((item) => `
      <a href="${item.href}" class="${item.href === currentPage ? "active" : ""}">
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
  
  function getSearchableText(topic) {
    const referenceTitles = (topic.references || []).map((r) => r.title).join(" ");
    const mediaTitles = (topic.media || []).map((m) => m.title).join(" ");
  
    return [
      topic.title,
      topic.category,
      topic.yearRange,
      topic.shortSummary,
      topic.introText,
      topic.howItWorks,
      topic.simpleExample,
      topic.effectiveUse,
      topic.waContext,
      topic.advantages,
      topic.limitations,
      topic.misuse,
      topic.ethics,
      referenceTitles,
      mediaTitles
    ].join(" ").toLowerCase();
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
      <a href="topic_detail.html?slug=${topic.slug}" class="museum-card result-card fade-in" style="animation-delay:${index * 0.05}s">
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
  
    searchInput.addEventListener("input", (event) => {
      const query = event.target.value.trim().toLowerCase();
  
      if (!query) {
        renderResults([], "");
        return;
      }
  
      const results = topics.filter((topic) => {
        const searchableText = getSearchableText(topic);
        return searchableText.includes(query);
      });
  
      renderResults(results, query);
    });
  
    renderResults([], "");
  }
  
  document.addEventListener("DOMContentLoaded", () => {
    renderNavigation();
    initSearch();
  });