const navItems = [
  { path: "home.html", label: "Home" },
  { path: "timeline.html", label: "Timeline" },
  { path: "explore_WA.html", label: "Explore WA" },
  { path: "guided_tour.html", label: "Guided Tour" },
  { path: "search.html", label: "Search" }
];

function renderNav() {
  const desktopNav = document.getElementById("desktopNav");
  const mobileNav = document.getElementById("mobileNav");
  const currentPage = "explore_WA.html";

  const html = navItems.map(item => {
    const activeClass = item.path === currentPage ? "active" : "";
    return `<a href="${item.path}" class="${activeClass}">${item.label}</a>`;
  }).join("");

  desktopNav.innerHTML = html;
  mobileNav.innerHTML = html;
}

function renderTopics() {
  const topicsList = document.getElementById("topicsList");

  topicsList.innerHTML = topics.map(topic => {
    return `
      <a href="topic_detail.html?slug=${topic.slug}" class="museum-card topic-link-card">
        <div class="topic-pin">📍</div>
        <div class="topic-content">
          <div class="topic-header">
            <span class="topic-title">${topic.title}</span>
            <span class="topic-year">${topic.yearRange}</span>
          </div>
          <p class="topic-desc">${topic.waContext}</p>
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

renderNav();
renderTopics();
setupMobileMenu();