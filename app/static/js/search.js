function setupSearch() {
  const input = document.getElementById("searchInput");
  const results = document.getElementById("resultsContainer");
  const emptyState = document.getElementById("emptyState");
  const resultCount = document.getElementById("resultCount");

  if (!input || !results || !emptyState || !resultCount) return;

  const cards = Array.from(results.querySelectorAll(".result-card"));

  function resetEmptyState() {
    const title = emptyState.querySelector(".empty-title");
    const text = emptyState.querySelector(".empty-text");

    if (title) {
      title.textContent = "Enter a search term to explore the collection";
    }
    if (text) {
      text.textContent =
        "Search across titles, topics, categories, years, and content";
    }
  }

  function showNoResultsState() {
    const title = emptyState.querySelector(".empty-title");
    const text = emptyState.querySelector(".empty-text");

    if (title) {
      title.textContent = "No results found";
    }
    if (text) {
      text.textContent =
        "Try another keyword, title, category, or year.";
    }
  }

  function filterResults(query) {
    let visibleCount = 0;

    cards.forEach((card) => {
      const text = card.innerText.toLowerCase();

      if (text.includes(query)) {
        card.style.display = "block";
        visibleCount++;
      } else {
        card.style.display = "none";
      }
    });

    if (query === "") {
      resetEmptyState();
      emptyState.classList.remove("hidden");
      resultCount.classList.add("hidden");
      cards.forEach((card) => {
        card.style.display = "block";
      });
      return;
    }

    if (visibleCount === 0) {
      showNoResultsState();
      emptyState.classList.remove("hidden");
    } else {
      emptyState.classList.add("hidden");
    }

    resultCount.classList.remove("hidden");
    resultCount.textContent = `${visibleCount} result(s) found`;
  }

  input.addEventListener("input", (e) => {
    const query = e.target.value.trim().toLowerCase();
    filterResults(query);
  });

  resetEmptyState();
  emptyState.classList.remove("hidden");
  resultCount.classList.add("hidden");
}

document.addEventListener("DOMContentLoaded", () => {
  setupSearch();
});