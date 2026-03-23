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
  const currentPage = "home.html";

  const html = navItems
    .map((item) => {
      const activeClass = item.path === currentPage ? "active" : "";
      return `<a href="${item.path}" class="${activeClass}">${item.label}</a>`;
    })
    .join("");

  if (desktopNav) desktopNav.innerHTML = html;
  if (mobileNav) mobileNav.innerHTML = html;
}

function renderParadigmShifts() {
  const paradigmGrid = document.getElementById("paradigmGrid");
  if (!paradigmGrid || typeof topics === "undefined") return;

  paradigmGrid.innerHTML = topics
    .map((topic) => {
      return `
        <a href="topic_detail.html?slug=${topic.slug}" class="museum-card paradigm-card">
          <span class="paradigm-year">${topic.yearRange}</span>
          <h3>${topic.title}</h3>
          <p>${topic.shortSummary || "Explore this AI paradigm shift in detail."}</p>
          <div class="topic-arrow">→</div>
        </a>
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
    mobileToggle.textContent = mobileNav.classList.contains("open") ? "✕" : "☰";
  });
}

renderNav();
renderParadigmShifts();
setupMobileMenu();