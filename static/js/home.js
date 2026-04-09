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
setupMobileMenu();