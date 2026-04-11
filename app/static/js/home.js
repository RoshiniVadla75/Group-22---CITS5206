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

async function renderParadigmGrid() {
  const paradigmGrid = document.getElementById("paradigmGrid");
  if (!paradigmGrid) return;

  const topics = await fetchTopics();

  if (!topics.length) {
    paradigmGrid.innerHTML = `
      <p class="section-text">
        Topic previews will appear here once data is loaded from the backend.
      </p>
    `;
    return;
  }

  paradigmGrid.innerHTML = topics
    .map((topic) => {
      const description =
        topic.shortSummary ||
        topic.introText ||
        "Discover this exhibit in the virtual museum.";

      return `
        <a href="/topic/${encodeURIComponent(topic.slug)}" class="museum-card paradigm-card">
          ${
            topic.yearRange
              ? `<span class="paradigm-year">${escapeHtml(topic.yearRange)}</span>`
              : ""
          }
          <h3>${escapeHtml(topic.title)}</h3>
          <p>${escapeHtml(description)}</p>
          <span class="topic-arrow">→</span>
        </a>
      `;
    })
    .join("");
}

document.addEventListener("DOMContentLoaded", () => {
  renderParadigmGrid();
});