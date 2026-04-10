const decades = [
  "All",
  "1950s",
  "1960s",
  "1970s",
  "1980s",
  "1990s",
  "2000s",
  "2010s",
  "2020s",
];

const statuses = ["All", "Active", "Legacy"];

let selectedDecade = "All";
let selectedCategory = "All";
let selectedStatus = "All";
let allTopics = [];

async function fetchTopics() {
  try {
    const response = await fetch("/api/topics");

    if (!response.ok) {
      throw new Error(`Failed to fetch topics: ${response.status}`);
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

function extractStartYear(yearRange) {
  if (!yearRange) return null;

  const match = String(yearRange).match(/\d{4}|\d{3}/);
  if (!match) return null;

  return parseInt(match[0], 10);
}

function getTopicDecade(topic) {
  const year = extractStartYear(topic.yearRange);
  if (!year) return null;

  return `${Math.floor(year / 10) * 10}s`;
}

function getCategories() {
  const categories = allTopics
    .map((topic) => topic.category)
    .filter((category) => category && category.trim() !== "");

  return ["All", ...new Set(categories)];
}

function buildFilterButtons(containerId, values, selectedValue, onClickHandler) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = values
    .map((value) => {
      const activeClass = value === selectedValue ? "active" : "";
      return `
        <button
          type="button"
          class="filter-btn ${activeClass}"
          data-value="${escapeHtml(value)}"
        >
          ${escapeHtml(value)}
        </button>
      `;
    })
    .join("");

  container.querySelectorAll(".filter-btn").forEach((button) => {
    button.addEventListener("click", () => {
      onClickHandler(button.dataset.value);
    });
  });
}

function renderFilters() {
  buildFilterButtons("decadeFilters", decades, selectedDecade, (value) => {
    selectedDecade = value;
    renderFilters();
    renderTimeline();
  });

  buildFilterButtons(
    "categoryFilters",
    getCategories(),
    selectedCategory,
    (value) => {
      selectedCategory = value;
      renderFilters();
      renderTimeline();
    }
  );

  buildFilterButtons("statusFilters", statuses, selectedStatus, (value) => {
    selectedStatus = value;
    renderFilters();
    renderTimeline();
  });
}

function getFilteredTopics() {
  return allTopics.filter((topic) => {
    const matchesDecade =
      selectedDecade === "All" || getTopicDecade(topic) === selectedDecade;

    const matchesCategory =
      selectedCategory === "All" || topic.category === selectedCategory;

    const matchesStatus =
      selectedStatus === "All" || topic.status === selectedStatus;

    return matchesDecade && matchesCategory && matchesStatus;
  });
}

function renderMediaPreview(topic) {
  if (!topic.media || !topic.media.length) return "";

  const imageItem = topic.media.find((item) => item.type === "image" && item.url);

  if (!imageItem) return "";

  return `
    <div class="timeline-media">
      <img
        src="${escapeHtml(imageItem.url)}"
        alt="${escapeHtml(imageItem.title || topic.title)}"
        class="timeline-media-image"
      />
      ${
        imageItem.caption
          ? `<p class="timeline-media-caption">${escapeHtml(imageItem.caption)}</p>`
          : ""
      }
    </div>
  `;
}

function renderReferenceMeta(topic) {
  const refCount = topic.references ? topic.references.length : 0;
  const mediaCount = topic.media ? topic.media.length : 0;

  if (!refCount && !mediaCount) return "";

  return `
    <div class="timeline-meta-row">
      ${
        mediaCount
          ? `<span class="timeline-meta-chip">${mediaCount} media item${mediaCount > 1 ? "s" : ""}</span>`
          : ""
      }
      ${
        refCount
          ? `<span class="timeline-meta-chip">${refCount} reference${refCount > 1 ? "s" : ""}</span>`
          : ""
      }
    </div>
  `;
}

function renderTimeline() {
  const timelineList = document.getElementById("timelineList");
  const emptyState = document.getElementById("emptyState");

  if (!timelineList || !emptyState) return;

  const filteredTopics = getFilteredTopics();

  if (filteredTopics.length === 0) {
    timelineList.innerHTML = "";
    emptyState.classList.remove("hidden");
    return;
  }

  emptyState.classList.add("hidden");

  timelineList.innerHTML = filteredTopics
    .map((topic, index) => {
      const isActive = String(topic.status || "").toLowerCase() === "active";
      const rowClass =
        index % 2 === 0 ? "timeline-item-row" : "timeline-item-row reverse";
      const dotClass = isActive ? "timeline-dot active" : "timeline-dot legacy";
      const badgeClass = isActive
        ? "timeline-status status-active"
        : "timeline-status status-legacy";

      const description =
        topic.shortSummary ||
        topic.introText ||
        "Explore this exhibit in the AI Museum timeline.";

      return `
        <div class="${rowClass}">
          <div class="${dotClass}"></div>

          <div class="timeline-spacer"></div>

          <div class="timeline-card-shell">
            <a href="/topic/${encodeURIComponent(topic.slug)}" class="museum-card timeline-card">
              <div class="timeline-card-header">
                <div class="timeline-topline">
                  <span class="exhibit-label timeline-category">
                    ${escapeHtml(topic.category || "")}
                  </span>
                  <span class="${badgeClass}">
                    ${escapeHtml(topic.status || "Legacy")}
                  </span>
                </div>
                <span class="timeline-year">
                  ${escapeHtml(topic.yearRange || "")}
                </span>
              </div>

              <h3 class="timeline-title">
                ${escapeHtml(topic.title || "")}
              </h3>

              ${renderMediaPreview(topic)}

              <p class="timeline-desc">
                ${escapeHtml(description)}
              </p>

              ${topic.waContext ? `<p class="timeline-wa">${escapeHtml(topic.waContext)}</p>` : ""}

              ${renderReferenceMeta(topic)}

              <div class="timeline-link">
                <span>Open Exhibit</span>
                <span class="timeline-arrow">→</span>
              </div>
            </a>
          </div>
        </div>
      `;
    })
    .join("");
}

async function initTimelinePage() {
  allTopics = await fetchTopics();

  renderFilters();
  renderTimeline();
}

document.addEventListener("DOMContentLoaded", () => {
  initTimelinePage();
});