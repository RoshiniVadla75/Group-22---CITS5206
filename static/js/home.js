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
        <a href="/topic-detail/${topic.slug}" class="museum-card paradigm-card">
          <span class="paradigm-year">${topic.year_range}</span>
          <h3>${topic.title}</h3>
          <p>${topic.short_summary || "Explore this AI paradigm shift in detail."}</p>
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

// Initialize the page
renderNav();
renderParadigmShifts();
setupMobileMenu();