const navItems = [
  { path: "/", label: "Home" },
  { path: "/timeline", label: "Timeline" },
  { path: "/explore-wa", label: "Explore WA" },
  { path: "/guided-tour", label: "Guided Tour" },
  { path: "/search", label: "Search" }
];

function renderNav() {
  const desktopNav = document.getElementById("desktopNav");
  const mobileNav = document.getElementById("mobileNav");
  const currentPage = window.location.pathname;

  const html = navItems.map(item => {
    const activeClass = item.path === currentPage ? "active" : "";
    return `<a href="${item.path}" class="${activeClass}">${item.label}</a>`;
  }).join("");

  desktopNav.innerHTML = html;
  mobileNav.innerHTML = html;
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

async function renderTopics() {
  const topicsList = document.getElementById("topicsList");
  const topics = await fetchTopics();

  if (topics.length === 0) {
    topicsList.innerHTML = `<p class="small-muted">No topics available at the moment.</p>`;
    return;
  }

  topicsList.innerHTML = topics.map(topic => {
    return `
      <a href="/topic-detail/${topic.slug}" class="museum-card topic-link-card">
        <div class="topic-pin">📍</div>
        <div class="topic-content">
          <div class="topic-header">
            <span class="topic-title">${topic.title}</span>
            <span class="topic-year">${topic.year_range}</span>
          </div>
          <p class="topic-desc">${topic.wa_context || "Explore this topic in detail."}</p>
        </div>
        <div class="topic-arrow">→</div>
      </a>
    `;
  }).join("");
}

function setupMobileMenu() {
  const mobileToggle = document.getElementById("mobileToggle");
  const mobileNav = document.getElementById("mobileNav");

  if (!mobileToggle || !mobileNav) return;

  mobileToggle.addEventListener("click", () => {
    mobileNav.classList.toggle("open");
    mobileToggle.textContent = mobileNav.classList.contains("open") ? "✕" : "☰";
  });
}

// Initialize the page
renderNav();
renderTopics();
setupMobileMenu();