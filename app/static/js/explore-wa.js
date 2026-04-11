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

async function renderTopics() {
  const topicsList = document.getElementById("topicsList");
  if (!topicsList) return;

  const topics = await fetchTopics();

  if (!topics.length) {
    topicsList.innerHTML = `
      <p class="small-muted">
        WA-related topic content will appear here once loaded from the database.
      </p>
    `;
    return;
  }

  topicsList.innerHTML = topics
    .map((topic) => {
      const description =
        topic.waContext ||
        topic.shortSummary ||
        topic.introText ||
        "Explore this topic and its connection to Western Australia.";

      return `
        <a href="/topic/${encodeURIComponent(topic.slug)}" class="museum-card topic-link-card">
          <div class="topic-pin">📍</div>
          <div class="topic-content">
            <div class="topic-header">
              <span class="topic-title">${escapeHtml(topic.title)}</span>
              ${
                topic.yearRange
                  ? `<span class="topic-year">${escapeHtml(topic.yearRange)}</span>`
                  : ""
              }
            </div>
            <p class="topic-desc">${escapeHtml(description)}</p>
          </div>
          <div class="topic-arrow">→</div>
        </a>
      `;
    })
    .join("");
}

document.addEventListener("DOMContentLoaded", () => {
  renderTopics();
});