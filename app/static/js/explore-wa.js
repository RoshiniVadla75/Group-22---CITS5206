const WA_MAP_LOCATIONS = [
  {
    id: "uwa",
    mapLabel: "U",
    cardLabel: "UWA",
    name: "The University of Western Australia",
    type: "University",
    location: "Crawley, Perth",
    coords: [-31.9809, 115.8179],
    image: "",
    slugs: [
      "turing-thoughts-on-ai",
      "learning-machines",
      "game-playing-ai",
      "evolutionary-computing-genetic-algorithms",
      "large-language-models",
    ],
    summary:
      "UWA connects early AI foundations, learning machines, game-playing search, optimisation, and modern LLM research to teaching and research in Western Australia.",
    mapNote: "Campus-level marker. Coordinates are approximate.",
  },
  {
    id: "curtin",
    mapLabel: "C",
    cardLabel: "CUR",
    name: "Curtin University",
    type: "University",
    location: "Bentley, Perth",
    coords: [-32.0064, 115.8944],
    image: "",
    slugs: [
      "artificial-neural-nets",
      "natural-language-processing",
      "large-language-models",
    ],
    summary:
      "Curtin is a useful local connection for applied AI, autonomous systems, computer vision, NLP, and newer agentic AI research directions.",
    mapNote: "Campus-level marker. Coordinates are approximate.",
  },
  {
    id: "pawsey",
    mapLabel: "P",
    cardLabel: "PAW",
    name: "Pawsey Supercomputing Research Centre",
    type: "Research Infrastructure",
    location: "Kensington, Perth",
    coords: [-31.9927, 115.8857],
    image: "/static/images/pawsey-supercomputing-centre.png",
    slugs: [
      "learning-machines",
      "artificial-neural-nets",
      "natural-language-processing",
      "large-language-models",
    ],
    summary:
      "Pawsey represents the computing power behind modern AI: large datasets, model training, scientific computing, and data-intensive discovery.",
    mapNote: "Facility-level marker. Coordinates are approximate.",
  },
  {
    id: "ska",
    mapLabel: "S",
    cardLabel: "SKA",
    name: "SKA-Low and Murchison Radio-astronomy Observatory",
    type: "Scientific Project",
    location: "Murchison region",
    coords: [-26.7033, 116.631],
    image: "",
    slugs: [
      "artificial-neural-nets",
      "natural-language-processing",
      "large-language-models",
    ],
    summary:
      "The SKA context shows why WA needs high-performance data processing: huge scientific datasets create demand for pattern recognition, metadata analysis, automation, and scalable AI methods.",
    mapNote: "Regional project marker. Coordinates are approximate.",
  },
  {
    id: "rio-tinto",
    mapLabel: "R",
    cardLabel: "RIO",
    name: "Rio Tinto Remote Operations Centre",
    type: "Industry",
    location: "Perth Airport precinct",
    coords: [-31.9399, 115.967],
    image: "",
    slugs: [
      "learning-machines",
      "internet-driven-ai-ibm-watson",
      "large-language-models",
    ],
    summary:
      "Remote operations make WA's geography part of the AI story: connected systems, predictive analytics, automation, and data platforms coordinate activity across distant Pilbara sites.",
    mapNote: "Precinct-level marker. Coordinates are approximate.",
  },
  {
    id: "bhp",
    mapLabel: "B",
    cardLabel: "BHP",
    name: "BHP Perth Operations and Technology Context",
    type: "Industry",
    location: "Perth CBD",
    coords: [-31.9546, 115.8573],
    image: "",
    slugs: [
      "internet-driven-ai-ibm-watson",
      "natural-language-processing",
      "large-language-models",
    ],
    summary:
      "BHP's WA operations connect internet-driven AI to enterprise data, operational analytics, decision support, and newer language-based interfaces for knowledge work.",
    mapNote: "CBD context marker. Coordinates are approximate.",
  },
  {
    id: "wagerup",
    mapLabel: "A",
    cardLabel: "ALC",
    name: "Alcoa Wagerup Alumina Refinery",
    type: "Industry",
    location: "Wagerup, Peel region",
    coords: [-32.917, 115.897],
    image: "",
    slugs: ["expert-systems"],
    summary:
      "Wagerup gives a practical local way to understand expert systems: complex industrial processes often use codified specialist knowledge, diagnostics, scheduling, and operating rules.",
    mapNote: "Industrial-area marker. Coordinates are approximate.",
  },
  {
    id: "main-roads",
    mapLabel: "M",
    cardLabel: "RD",
    name: "Main Roads WA and Transport Planning Context",
    type: "Government",
    location: "East Perth",
    coords: [-31.9587, 115.8781],
    image: "",
    slugs: [
      "evolutionary-computing-genetic-algorithms",
      "internet-driven-ai-ibm-watson",
    ],
    summary:
      "Transport planning helps explain optimisation: roadworks, scheduling, network planning, and competing priorities are natural fits for evolutionary and data-driven methods.",
    mapNote: "Agency context marker. Coordinates are approximate.",
  },
  {
    id: "wa-government",
    mapLabel: "G",
    cardLabel: "GOV",
    name: "WA Government Digital Policy Context",
    type: "Government",
    location: "Perth CBD",
    coords: [-31.9505, 115.8605],
    image: "",
    slugs: [
      "synthetic-media-technology-deep-fakes",
      "large-language-models",
    ],
    summary:
      "Public-sector guidance connects the newest AI shifts to responsible use, privacy, misinformation risk, synthetic media, and public trust.",
    mapNote: "CBD context marker. Coordinates are approximate.",
  },
];

const FALLBACK_TOPIC_TITLES = {
  "turing-thoughts-on-ai": "Alan Turing & The Turing Test",
  "learning-machines": "Learning Machines",
  "game-playing-ai": "Board Game Playing",
  "expert-systems": "Expert Systems",
  "artificial-neural-nets": "Artificial Neural Nets",
  "internet-driven-ai-ibm-watson": "Internet-Driven AI Systems",
  "evolutionary-computing-genetic-algorithms":
    "Evolutionary Computing & Genetic Algorithms",
  "synthetic-media-technology-deep-fakes": "Synthetic Media Technology / Deep Fakes",
  "natural-language-processing": "Natural Language Processing",
  "large-language-models": "Large Language Models",
};

let allTopics = [];
let activeTopicSlug = "all";
let selectedLocationId = WA_MAP_LOCATIONS[0].id;
let waMap = null;
let markerLayer = null;
const locationMarkers = new Map();

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

function getTopicBySlug(slug) {
  return allTopics.find((topic) => topic.slug === slug);
}

function getTopicTitle(slug) {
  return getTopicBySlug(slug)?.title || FALLBACK_TOPIC_TITLES[slug] || slug;
}

function getLocationById(id) {
  return WA_MAP_LOCATIONS.find((location) => location.id === id);
}

function getVisibleLocations() {
  if (activeTopicSlug === "all") return WA_MAP_LOCATIONS;
  return WA_MAP_LOCATIONS.filter((location) =>
    location.slugs.includes(activeTopicSlug)
  );
}

function getUsedTopicSlugs() {
  const slugs = new Set();
  WA_MAP_LOCATIONS.forEach((location) => {
    location.slugs.forEach((slug) => slugs.add(slug));
  });

  const apiOrder = allTopics
    .map((topic) => topic.slug)
    .filter((slug) => slugs.has(slug));

  const fallbackOrder = Object.keys(FALLBACK_TOPIC_TITLES).filter((slug) =>
    slugs.has(slug)
  );

  return apiOrder.length ? apiOrder : fallbackOrder;
}

function categoryClass(value) {
  return String(value || "place")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

function renderTopicSelect() {
  const select = document.getElementById("topicPlaceSelect");
  if (!select) return;

  const options = [
    `<option value="all">All topics and places</option>`,
    ...getUsedTopicSlugs().map(
      (slug) =>
        `<option value="${escapeHtml(slug)}">${escapeHtml(getTopicTitle(slug))}</option>`
    ),
  ];

  select.innerHTML = options.join("");
  select.value = activeTopicSlug;

  select.addEventListener("change", () => {
    activeTopicSlug = select.value;
    refreshMapActivity(true);
  });
}

function renderSelectionHint() {
  const hint = document.getElementById("mapSelectionHint");
  if (!hint) return;

  const visibleLocations = getVisibleLocations();
  if (activeTopicSlug === "all") {
    hint.textContent =
      "Showing all mapped WA places. Select a topic to narrow the list.";
    return;
  }

  hint.textContent = `${visibleLocations.length} WA place${
    visibleLocations.length === 1 ? "" : "s"
  } connected to ${getTopicTitle(activeTopicSlug)}.`;
}

function renderTopicLinks(location) {
  return location.slugs
    .map((slug) => {
      const activeClass = slug === activeTopicSlug ? "active" : "";
      return `
        <a href="/topic/${encodeURIComponent(slug)}" class="map-topic-link ${activeClass}">
          ${escapeHtml(getTopicTitle(slug))}
        </a>
      `;
    })
    .join("");
}

function renderDetailPanel(location) {
  const panel = document.getElementById("mapDetailPanel");
  if (!panel || !location) return;

  const imageBlock = location.image
    ? `
      <img
        src="${escapeHtml(location.image)}"
        alt="${escapeHtml(location.name)}"
        class="map-detail-image"
      />
    `
    : `
      <div class="map-detail-placeholder">
        <span>${escapeHtml(location.type)}</span>
      </div>
    `;

  panel.innerHTML = `
    ${imageBlock}
    <div class="map-detail-content">
      <div class="map-detail-meta">
        <span class="exhibit-label">${escapeHtml(location.type)}</span>
        <span>${escapeHtml(location.location)}</span>
      </div>
      <h3>${escapeHtml(location.name)}</h3>
      <p>${escapeHtml(location.summary)}</p>
      <p class="map-note">${escapeHtml(location.mapNote)}</p>

      <div class="map-topic-links">
        <span class="detail-subtitle">Topic places linked here</span>
        ${renderTopicLinks(location)}
      </div>
    </div>
  `;
}

function bringMapIntoView() {
  const mapShell = document.querySelector(".map-shell");
  if (!mapShell) return;

  mapShell.scrollIntoView({
    behavior: "smooth",
    block: "center",
  });
}

function bringPlaceCardIntoView(locationId) {
  const card = document.getElementById(`place-card-${locationId}`);
  if (!card) return;

  card.scrollIntoView({
    behavior: "smooth",
    block: "center",
  });

  card.classList.remove("detail-attention");
  window.setTimeout(() => {
    card.classList.add("detail-attention");
    card.focus({ preventScroll: true });
  }, 50);

  window.setTimeout(() => {
    card.classList.remove("detail-attention");
  }, 1400);
}

function renderLocationList() {
  const list = document.getElementById("mapLocationList");
  if (!list) return;

  const visibleLocations = getVisibleLocations();

  if (!visibleLocations.length) {
    list.innerHTML = `
      <div class="map-list-header">
        <span class="exhibit-label">WA Topic Places</span>
      </div>
      <p class="small-muted">No mapped WA places match this topic yet.</p>
    `;
    return;
  }

  list.innerHTML = `
    <div class="map-list-header">
      <span class="exhibit-label">WA Topic Places</span>
      <span>${visibleLocations.length} place${visibleLocations.length === 1 ? "" : "s"}</span>
    </div>
    <div class="map-list-items">
      ${visibleLocations
        .map((location) => {
          const activeClass = location.id === selectedLocationId ? "active" : "";
          const linkedTopics = location.slugs
            .slice(0, 3)
            .map((slug) => getTopicTitle(slug))
            .join(", ");

          return `
            <article
              id="place-card-${escapeHtml(location.id)}"
              class="map-location-card ${activeClass}"
              data-location-id="${escapeHtml(location.id)}"
              tabindex="-1"
            >
              <span class="location-index">${escapeHtml(location.cardLabel)}</span>
              <span class="location-card-copy">
                <strong>${escapeHtml(location.name)}</strong>
                <small>${escapeHtml(location.location)} - ${escapeHtml(location.type)}</small>
                <em>${escapeHtml(linkedTopics)}${location.slugs.length > 3 ? "..." : ""}</em>
                <p class="place-summary">${escapeHtml(location.summary)}</p>
                <p class="place-note">${escapeHtml(location.mapNote)}</p>
                <span class="detail-subtitle">Linked exhibits</span>
                <span class="place-topic-links">
                  ${renderTopicLinks(location)}
                </span>
                <button type="button" class="card-action show-on-map-btn" data-location-id="${escapeHtml(location.id)}">
                  Show on map
                </button>
              </span>
            </article>
          `;
        })
        .join("")}
    </div>
  `;

  list.querySelectorAll(".show-on-map-btn").forEach((button) => {
    button.addEventListener("click", () => {
      selectLocation(button.dataset.locationId, true);
      bringMapIntoView();
    });
  });
}

function makeMarkerIcon(location) {
  const typeClass = categoryClass(location.type);
  return L.divIcon({
    className: `wa-marker-icon ${typeClass}`,
    html: `<span>${escapeHtml(location.mapLabel)}</span>`,
    iconSize: [28, 28],
    iconAnchor: [14, 14],
    popupAnchor: [0, -14],
  });
}

function fitMapToVisibleLocations(visibleLocations) {
  if (!waMap || !visibleLocations.length) return;

  if (visibleLocations.length === 1) {
    waMap.setView(visibleLocations[0].coords, 12);
    return;
  }

  const bounds = L.latLngBounds(visibleLocations.map((location) => location.coords));
  waMap.fitBounds(bounds.pad(0.2), {
    maxZoom: activeTopicSlug === "all" ? 7 : 11,
  });
}

function renderMarkers() {
  if (!waMap || !markerLayer) return;

  markerLayer.clearLayers();
  locationMarkers.clear();

  const visibleLocations = getVisibleLocations();

  visibleLocations.forEach((location) => {
    const marker = L.marker(location.coords, {
      icon: makeMarkerIcon(location),
      title: location.name,
      keyboard: true,
    });

    marker.bindPopup(`
      <strong>${escapeHtml(location.name)}</strong><br />
      ${escapeHtml(location.location)}<br />
      <button type="button" class="popup-select-btn" data-location-id="${escapeHtml(location.id)}">Show place card below</button>
    `);

    marker.on("click", () => selectLocation(location.id, false));
    marker.on("popupopen", (event) => {
      const button = event.popup
        .getElement()
        ?.querySelector(".popup-select-btn");
      button?.addEventListener("click", () => {
        selectLocation(location.id, false);
        bringPlaceCardIntoView(location.id);
      });
    });

    marker.addTo(markerLayer);
    locationMarkers.set(location.id, marker);
  });

  fitMapToVisibleLocations(visibleLocations);
}

function selectLocation(locationId, panMap) {
  const location = getLocationById(locationId);
  if (!location) return;

  selectedLocationId = location.id;
  renderDetailPanel(location);
  renderLocationList();

  if (waMap && panMap) {
    waMap.flyTo(location.coords, Math.max(waMap.getZoom(), 10), {
      duration: 0.65,
    });
    locationMarkers.get(location.id)?.openPopup();
  }
}

function refreshMapActivity(resetSelection) {
  const visibleLocations = getVisibleLocations();
  if (resetSelection || !visibleLocations.some((location) => location.id === selectedLocationId)) {
    selectedLocationId = visibleLocations[0]?.id || WA_MAP_LOCATIONS[0].id;
  }

  renderSelectionHint();
  renderMarkers();
  renderDetailPanel(getLocationById(selectedLocationId));
  renderLocationList();
}

function initMap() {
  const mapElement = document.getElementById("waMap");
  const fallback = document.getElementById("mapFallback");
  if (!mapElement) return;

  if (!window.L) {
    fallback?.classList.remove("hidden");
    mapElement.classList.add("map-unavailable");
    return;
  }

  waMap = L.map(mapElement, {
    scrollWheelZoom: false,
    zoomControl: true,
  }).setView([-27.8, 121.6], 5);

  const tileLayer = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution: "&copy; OpenStreetMap contributors",
  });

  tileLayer.on("tileerror", () => {
    fallback?.classList.remove("hidden");
  });

  tileLayer.addTo(waMap);
  markerLayer = L.layerGroup().addTo(waMap);

  setTimeout(() => {
    waMap.invalidateSize();
    refreshMapActivity(false);
  }, 100);
}

function initWaMapActivity() {
  const mapRoot = document.getElementById("waMap");
  if (!mapRoot) return;

  renderTopicSelect();
  renderSelectionHint();
  renderDetailPanel(getLocationById(selectedLocationId));
  renderLocationList();
  initMap();
}

async function renderTopics() {
  const topicsList = document.getElementById("topicsList");
  if (!topicsList) return;

  if (!allTopics.length) {
    allTopics = await fetchTopics();
  }

  if (!allTopics.length) {
    topicsList.innerHTML = `
      <p class="small-muted">
        WA-related topic content will appear here once loaded from the database.
      </p>
    `;
    return;
  }

  topicsList.innerHTML = allTopics
    .map((topic) => {
      const description =
        topic.waContext ||
        topic.shortSummary ||
        topic.introText ||
        "Explore this topic and its connection to Western Australia.";

      return `
        <a href="/topic/${encodeURIComponent(topic.slug)}" class="museum-card topic-link-card">
          <div class="topic-pin">Map</div>
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
          <div class="topic-arrow">-&gt;</div>
        </a>
      `;
    })
    .join("");
}

document.addEventListener("DOMContentLoaded", async () => {
  allTopics = await fetchTopics();
  initWaMapActivity();
  renderTopics();
});
