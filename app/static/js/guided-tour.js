let topics = [];
let currentStep = -1;
let visited = new Set();

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

function escapeHtml(value) {
  if (value === null || value === undefined) return "";
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function renderEmptyState() {
  const app = document.getElementById("guidedTourApp");
  if (!app) return;

  app.innerHTML = `
    <section class="tour-intro fade-in">
      <div class="intro-icon">🧭</div>
      <span class="exhibit-label">Museum Route</span>
      <h1 class="page-title brass-text">Guided Tour</h1>
      <p class="intro-text">
        The guided tour content is not available right now. Please try again later.
      </p>
      <div class="complete-actions">
        <a href="/timeline" class="primary-btn">Go to Timeline</a>
      </div>
    </section>
  `;
}

function renderIntro() {
  const app = document.getElementById("guidedTourApp");
  if (!app) return;

  app.innerHTML = `
    <section class="tour-intro fade-in">
      <div class="intro-icon">🧭</div>
      <span class="exhibit-label">Museum Route</span>
      <h1 class="page-title brass-text">Guided Tour</h1>
      <p class="intro-text">
        Follow a structured journey through the history of artificial intelligence.
        This guided tour will take you through the major paradigm shifts in sequence,
        while helping you understand their key ideas and Western Australia connections.
      </p>
      <p class="intro-meta">
        ${topics.length} exhibits · Interactive museum walkthrough
      </p>
      <button id="beginJourneyBtn" class="primary-btn large-btn">Begin Journey</button>
    </section>
  `;

  const beginBtn = document.getElementById("beginJourneyBtn");
  if (beginBtn) {
    beginBtn.addEventListener("click", () => {
      currentStep = 0;
      visited = new Set([0]);
      renderStep();
    });
  }
}

function renderProgress() {
  const total = topics.length;
  const currentNumber = currentStep + 1;
  const percent = total > 0 ? Math.round((currentNumber / total) * 100) : 0;

  return `
    <section class="progress-section fade-in">
      <div class="progress-top">
        <span class="exhibit-label">Tour Progress</span>
        <span class="progress-percent">Stop ${currentNumber} of ${total} · ${percent}%</span>
      </div>

      <div class="progress-bar-shell">
        <div class="progress-bar-fill" style="width: ${percent}%;"></div>
      </div>

      <div class="progress-dots">
        ${topics
          .map((_, index) => {
            const classes = [
              "progress-dot",
              visited.has(index) ? "visited" : "",
              index === currentStep ? "current" : "",
            ]
              .filter(Boolean)
              .join(" ");

            return `<button class="${classes}" data-step="${index}" aria-label="Go to stop ${index + 1}"></button>`;
          })
          .join("")}
      </div>
    </section>
  `;
}

function renderSections(topic) {
  const sections = [
    { label: "How It Works", content: topic.howItWorks },
    { label: "Simple Example", content: topic.simpleExample },
    { label: "Where Most Effective", content: topic.effectiveUse },
    { label: "Real-World Examples", content: topic.realWorldExamples },
    { label: "Advantages", content: topic.advantages },
    { label: "Limitations", content: topic.limitations },
    { label: "Possible Misuse", content: topic.misuse },
    { label: "Ethical Concerns", content: topic.ethics },
    { label: "Western Australia Context", content: topic.waContext },
  ];

  return sections
    .filter((section) => section.content && String(section.content).trim() !== "")
    .map(
      (section) => `
        <div class="museum-card topic-section">
          <span class="exhibit-label block-label">${escapeHtml(section.label)}</span>
          <p>${escapeHtml(section.content)}</p>
        </div>
      `
    )
    .join("");
}

function renderMedia(topic) {
  if (!topic.media || !topic.media.length) return "";

  return `
    <div class="museum-card topic-section">
      <span class="exhibit-label block-label">Media & Visual Materials</span>
      <div class="guided-media-list">
        ${topic.media
          .map(
            (item) => `
              <div class="guided-media-item" style="margin-bottom: 1.5rem;">
                ${
                  item.url
                    ? `<img src="${escapeHtml(item.url)}" alt="${escapeHtml(item.title || topic.title)}" style="width: 100%; max-width: 520px; border-radius: 6px; display: block; margin-bottom: 0.75rem;" />`
                    : ""
                }
                ${
                  item.title
                    ? `<h3 style="margin: 0 0 0.4rem 0;">${escapeHtml(item.title)}</h3>`
                    : ""
                }
                ${
                  item.caption
                    ? `<p style="margin: 0; color: var(--muted-foreground);">${escapeHtml(item.caption)}</p>`
                    : ""
                }
              </div>
            `
          )
          .join("")}
      </div>
    </div>
  `;
}

function renderReferences(topic) {
  if (!topic.references || !topic.references.length) return "";

  return `
    <div class="museum-card topic-section">
      <span class="exhibit-label block-label">References</span>
      <div class="guided-reference-list">
        ${topic.references
          .map(
            (ref) => `
              <div class="guided-reference-item" style="margin-bottom: 1rem;">
                <p style="margin: 0 0 0.35rem 0;">
                  ${
                    ref.url
                      ? `<a href="${escapeHtml(ref.url)}" target="_blank" rel="noopener noreferrer" style="color: var(--primary);">${escapeHtml(ref.title || ref.url)}</a>`
                      : escapeHtml(ref.title || "Reference")
                  }
                </p>
                ${
                  ref.sourceType
                    ? `<p style="margin: 0; color: var(--muted-foreground); font-size: 0.95rem;">Type: ${escapeHtml(ref.sourceType)}</p>`
                    : ""
                }
                ${
                  ref.accessedDate
                    ? `<p style="margin: 0; color: var(--muted-foreground); font-size: 0.95rem;">${escapeHtml(ref.accessedDate)}</p>`
                    : ""
                }
                ${
                  ref.notes
                    ? `<p style="margin: 0.25rem 0 0 0; color: var(--muted-foreground);">${escapeHtml(ref.notes)}</p>`
                    : ""
                }
              </div>
            `
          )
          .join("")}
      </div>
    </div>
  `;
}

function renderStep() {
  const app = document.getElementById("guidedTourApp");
  if (!app) return;

  if (!topics.length) {
    renderEmptyState();
    return;
  }

  if (currentStep >= topics.length) {
    renderComplete();
    return;
  }

  const topic = topics[currentStep];
  const total = topics.length;

  app.innerHTML = `
    ${renderProgress()}

    <section class="topic-step fade-in">
      <article class="museum-card topic-card">
        <div class="topic-meta">
          <span class="exhibit-label">Stop ${currentStep + 1}</span>
          ${topic.yearRange ? `<span class="topic-year">${escapeHtml(topic.yearRange)}</span>` : ""}
        </div>

        <h2 class="topic-title brass-text">${escapeHtml(topic.title)}</h2>

        <p class="topic-intro">
          ${escapeHtml(topic.shortSummary || topic.introText || "Discover this exhibit in the guided tour.")}
        </p>

        <div class="archival-divider"></div>

        <div class="topic-sections">
          ${renderSections(topic)}
          ${renderMedia(topic)}
          ${renderReferences(topic)}
        </div>

        <div class="archival-divider"></div>

        <div class="topic-link-row">
          <a href="/topic/${encodeURIComponent(topic.slug)}" class="topic-link">Open full exhibit</a>
        </div>
      </article>

      <div class="tour-navigation">
        <button id="prevBtn" class="secondary-btn" ${currentStep === 0 ? "disabled" : ""}>
          ← Previous
        </button>

        <button id="nextBtn" class="primary-btn">
          ${currentStep === total - 1 ? "Finish Tour" : "Next Stop →"}
        </button>
      </div>
    </section>
  `;

  document.querySelectorAll(".progress-dot").forEach((dot) => {
    dot.addEventListener("click", () => {
      const step = Number(dot.dataset.step);
      currentStep = step;
      visited.add(step);
      renderStep();
    });
  });

  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");

  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      if (currentStep > 0) {
        currentStep -= 1;
        visited.add(currentStep);
        renderStep();
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener("click", () => {
      currentStep += 1;
      if (currentStep < topics.length) {
        visited.add(currentStep);
      }
      renderStep();
    });
  }
}

function renderComplete() {
  const app = document.getElementById("guidedTourApp");
  if (!app) return;

  app.innerHTML = `
    <section class="tour-complete fade-in">
      <div class="complete-icon">🏛️</div>
      <span class="exhibit-label">Tour Complete</span>
      <h1 class="page-title brass-text">You’ve finished the Guided Tour</h1>
      <p class="complete-text">
        You’ve now explored the major paradigm shifts in the history of artificial intelligence.
        You can revisit any exhibit, continue browsing the timeline, or explore Western Australia’s place in this story.
      </p>

      <div class="complete-actions">
        <button id="restartTourBtn" class="primary-btn">Restart Tour</button>
        <a href="/timeline" class="secondary-btn">View Timeline</a>
        <a href="/explore-wa" class="secondary-btn">Explore WA</a>
      </div>
    </section>
  `;

  const restartBtn = document.getElementById("restartTourBtn");
  if (restartBtn) {
    restartBtn.addEventListener("click", () => {
      currentStep = -1;
      visited = new Set();
      renderIntro();
    });
  }
}

async function initGuidedTourPage() {
  topics = await fetchTopics();

  if (!topics.length) {
    renderEmptyState();
    return;
  }

  renderIntro();
}

document.addEventListener("DOMContentLoaded", () => {
  initGuidedTourPage();
});