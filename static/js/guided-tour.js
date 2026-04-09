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

let currentStep = -1; // -1 = intro
let visited = new Set();

function markVisited(step) {
  visited.add(step);
}

function goNext() {
  if (currentStep >= 0) {
    markVisited(currentStep);
  }
  currentStep = Math.min(currentStep + 1, topics.length);
  renderGuidedTour();
}

function goPrev() {
  currentStep = Math.max(currentStep - 1, -1);
  renderGuidedTour();
}

function goToStep(step) {
  currentStep = step;
  renderGuidedTour();
}

function renderIntro(container) {
  container.innerHTML = `
    <section class="tour-intro fade-in">
      <div class="intro-icon">🧭</div>
      <span class="exhibit-label">Guided Museum Journey</span>
      <h1 class="page-title brass-text">Start Your Discovery</h1>
      <p class="intro-text">
        Step through 10 groundbreaking moments in AI history, presented in chronological order.
        Each stop reveals a paradigm shift that changed how humans and machines interact.
      </p>
      <p class="intro-meta">Estimated time: 15–20 minutes · 10 exhibits</p>
      <button id="beginJourneyBtn" class="primary-btn large-btn" type="button">
        🧭 Begin Journey
      </button>
    </section>
  `;

  const beginBtn = document.getElementById("beginJourneyBtn");
  if (beginBtn) {
    beginBtn.addEventListener("click", goNext);
  }
}

function renderCompleted(container) {
  container.innerHTML = `
    <section class="tour-complete fade-in">
      <div class="complete-icon">✅</div>
      <h1 class="page-title brass-text">Journey Complete</h1>
      <p class="complete-text">
        You've explored all 10 paradigm shifts in AI history. You now have a broad understanding
        of how artificial intelligence evolved from theoretical concepts to the powerful systems
        shaping our world today.
      </p>
      <div class="complete-actions">
        <button id="restartJourneyBtn" class="secondary-btn" type="button">Restart Journey</button>
        <a href="/explore-wa" class="primary-btn">Explore WA Context</a>
      </div>
    </section>
  `;

  const restartBtn = document.getElementById("restartJourneyBtn");
  if (restartBtn) {
    restartBtn.addEventListener("click", () => {
      currentStep = -1;
      visited = new Set();
      renderGuidedTour();
    });
  }
}

function renderProgress(step, total) {
  const progressPercent = Math.round(((step + 1) / total) * 100);

  return `
    <section class="progress-section fade-in">
      <div class="progress-top">
        <span class="exhibit-label">Discovery ${step + 1} of ${total}</span>
        <span class="progress-percent">${progressPercent}% Complete</span>
      </div>

      <div class="progress-bar-shell">
        <div class="progress-bar-fill" style="width: ${progressPercent}%"></div>
      </div>

      <div class="progress-dots">
        ${topics.map((_, i) => `
          <button
            class="progress-dot ${i === step ? "current" : visited.has(i) ? "visited" : ""}"
            data-step="${i}"
            aria-label="Go to discovery ${i + 1}"
            type="button"
          ></button>
        `).join("")}
      </div>
    </section>
  `;
}

function renderTopicStep(container, topic, step) {
  container.innerHTML = `
    ${renderProgress(step, topics.length)}

    <section class="topic-step fade-in">
      <div class="museum-card topic-card">
        <div class="topic-meta">
          <span class="exhibit-label">${topic.category}</span>
          <span class="topic-year">${topic.year_range}</span>
        </div>

        <h2 class="topic-title brass-text">${topic.title}</h2>

        <p class="topic-intro">${topic.intro_text}</p>

        <div class="archival-divider"></div>

        <div class="topic-sections">
          <div class="topic-section">
            <span class="exhibit-label block-label">How It Works</span>
            <p>${topic.how_it_works}</p>
          </div>

          <div class="topic-section">
            <span class="exhibit-label block-label">Simple Example</span>
            <p>${topic.simple_example}</p>
          </div>

          <div class="topic-section">
            <span class="exhibit-label block-label">WA Connection</span>
            <p>${topic.wa_context}</p>
          </div>
        </div>

        <div class="archival-divider"></div>

        <div class="topic-link-row">
          <a href="/topic-detail/${topic.slug}" class="topic-link">
            View full exhibit →
          </a>
        </div>
      </div>
    </section>

    <section class="tour-navigation fade-in">
      <button id="prevBtn" class="secondary-btn" type="button" ${step <= 0 ? "disabled" : ""}>
        ← Previous
      </button>

      <button id="nextBtn" class="primary-btn" type="button">
        ${step < topics.length - 1 ? "Next Discovery →" : "Complete Journey →"}
      </button>
    </section>
  `;

  document.querySelectorAll(".progress-dot").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const targetStep = parseInt(e.currentTarget.dataset.step, 10);
      if (!Number.isNaN(targetStep)) {
        goToStep(targetStep);
      }
    });
  });

  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");

  if (prevBtn) {
    prevBtn.addEventListener("click", goPrev);
  }

  if (nextBtn) {
    nextBtn.addEventListener("click", goNext);
  }
}

function renderGuidedTour() {
  const container = document.getElementById("guidedTourApp");
  if (!container) return;

  if (currentStep === -1) {
    renderIntro(container);
    return;
  }

  if (currentStep >= topics.length) {
    renderCompleted(container);
    return;
  }

  const topic = topics[currentStep];
  if (!topic) return;

  renderTopicStep(container, topic, currentStep);
}

document.addEventListener("DOMContentLoaded", () => {
  renderNavigation();
  renderGuidedTour();
});