let topics = [];

// Fetch topics dynamically from the backend
async function fetchTopics() {
  try {
    const response = await fetch("/api/topics");
    if (!response.ok) {
      throw new Error("Failed to fetch topics");
    }
    topics = await response.json();
  } catch (error) {
    console.error("Error fetching topics:", error);
  }
}

// Get a topic by its slug
function getTopicBySlug(slug) {
  return topics.find((topic) => topic.slug === slug);
}

// Get adjacent topics (previous and next) based on the topic ID
function getAdjacentTopics(id) {
  const index = topics.findIndex((topic) => topic.id === id);
  return {
    prev: index > 0 ? topics[index - 1] : null,
    next: index < topics.length - 1 ? topics[index + 1] : null,
  };
}

// Initialize topics by fetching them from the backend
document.addEventListener("DOMContentLoaded", async () => {
  await fetchTopics();
});