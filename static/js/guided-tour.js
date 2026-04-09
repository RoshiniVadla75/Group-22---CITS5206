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
  const currentPage = window.location.pathname;

  if (!desktopNav || !mobileNav || !mobileToggle) return;

  desktopNav.innerHTML = navItems.map((item) => `
    <a href="${item.path}" class="nav-link ${item.path === currentPage ? "active" : ""}">
      ${item.label}
    </a>
  `).join("");

  mobileNav.innerHTML = navItems.map((item) => `
    <a href="${item.path}" class="mobile-nav-link ${item.path === currentPage ? "active" : ""}">
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

function setupJourneyButtons() {
  const beginJourneyBtn = document.getElementById("beginJourneyBtn");
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");

  if (beginJourneyBtn) {
    beginJourneyBtn.addEventListener("click", () => {
      const firstStep = document.querySelector(".tour-step");
      if (firstStep) {
        firstStep.scrollIntoView({ behavior: "smooth" });
      }
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      const currentStep = document.querySelector(".tour-step.current");
      if (currentStep) {
        const prevStep = currentStep.previousElementSibling;
        if (prevStep && prevStep.classList.contains("tour-step")) {
          currentStep.classList.remove("current");
          prevStep.classList.add("current");
          prevStep.scrollIntoView({ behavior: "smooth" });
        }
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener("click", () => {
      const currentStep = document.querySelector(".tour-step.current");
      if (currentStep) {
        const nextStep = currentStep.nextElementSibling;
        if (nextStep && nextStep.classList.contains("tour-step")) {
          currentStep.classList.remove("current");
          nextStep.classList.add("current");
          nextStep.scrollIntoView({ behavior: "smooth" });
        }
      }
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  renderNavigation();
  setupJourneyButtons();
});