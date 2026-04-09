const navItems = [
  { path: "/", label: "Home" },
  { path: "/timeline", label: "Timeline" },
  { path: "/guided-tour", label: "Guided Tour" },
  { path: "/explore-wa", label: "Explore WA" },
  { path: "/search", label: "Search" }
];

function renderNav() {
  const desktopNav = document.getElementById("desktopNav");
  const mobileNav = document.getElementById("mobileNav");
  const currentPage = window.location.pathname;

  if (!desktopNav || !mobileNav) return;

  const html = navItems.map(item => {
    const activeClass = item.path === currentPage ? "active" : "";
    return `<a href="${item.path}" class="${activeClass}">${item.label}</a>`;
  }).join("");

  desktopNav.innerHTML = html;
  mobileNav.innerHTML = html;
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

// Initialize navigation and mobile menu
renderNav();
setupMobileMenu();