const navItems = [
  { path: "home.html", label: "Home" },
  { path: "timeline.html", label: "Timeline" },
  { path: "explore_WA.html", label: "Explore WA" },
  { path: "guided_tour.html", label: "Guided Tour" },
  { path: "search.html", label: "Search" }
];


function getQueryParam(name) {
  const url = new URL(window.location.href);
  return url.searchParams.get(name);
}

function renderNav() {
  const desktopNav = document.getElementById("desktopNav");
  const mobileNav = document.getElementById("mobileNav");

  const html = navItems.map(item => {
    const activeClass = item.label === "Explore WA" ? "active" : "";
    return `<a href="${item.path}" class="${activeClass}">${item.label}</a>`;
  }).join("");

  desktopNav.innerHTML = html;
  mobileNav.innerHTML = html;
}

function renderTopicPage() {
  const slug = getQueryParam("slug");
  const topic = getTopicBySlug(slug);

  if (!topic) {
    document.querySelector(".page-section").innerHTML = `
      <div style="text-align:center; padding:80px 20px;">
        <h1 class="page-title brass-text">Exhibit Not Found</h1>
        <p style="margin-top:16px;">
          <a href="explore_WA.html" style="color:#d4a017;">Return to Explore WA</a>
        </p>
      </div>
    `;
    return;
  }

  const { prev, next } = getAdjacentTopics(topic.id);

  document.getElementById("breadcrumb").innerHTML = `
    <a href="home.html">Timeline</a>
    <span>›</span>
    <span>${topic.title}</span>
  `;

  document.getElementById("topicHeader").innerHTML = `
    <div class="header-block">
      <div class="header-meta">
        <span class="exhibit-label">${topic.category}</span>
        <span class="meta-muted">Exhibit #${topic.id}</span>
      </div>
      <h1 class="page-title brass-text">${topic.title}</h1>
      <p class="year-text">${topic.yearRange}</p>
      <div class="archival-divider"></div>
    </div>
  `;

  document.getElementById("introCard").innerHTML = `
    <div class="museum-card">
      <span class="exhibit-label block-label">Introduction</span>
      <p class="intro-text">${topic.introText}</p>
    </div>
  `;

  document.getElementById("summaryCard").innerHTML = `
    <div class="museum-card summary-card">
      <span class="exhibit-label block-label">Key Takeaways</span>
      <p class="summary-text">${topic.shortSummary}</p>
    </div>
  `;

  const sections = [
    { title: "How It Works", content: topic.howItWorks, icon: "⚙️" },
    { title: "Simple Example", content: topic.simpleExample, icon: "💡" },
    { title: "Where Most Effective", content: topic.effectiveUse, icon: "⚡" },
    { title: "Real-World Examples", content: topic.realWorldExamples, icon: "👁️" },
    { title: "Advantages", content: topic.advantages, icon: "👍" },
    { title: "Limitations", content: topic.limitations, icon: "⛔" },
    { title: "Possible Misuse", content: topic.misuse, icon: "⚠️" },
    { title: "Ethical Concerns", content: topic.ethics, icon: "🛡️" },
    { title: "WA Connection", content: topic.waContext, icon: "📍" }
  ];

  document.getElementById("sectionsContainer").innerHTML = sections.map(section => `
    <div class="museum-card section-card">
      <div class="section-title-row">
        <span class="section-emoji">${section.icon}</span>
        <span class="exhibit-label">${section.title}</span>
      </div>
      <p class="section-text">${section.content}</p>
    </div>
  `).join("");

  document.getElementById("mediaCard").innerHTML = `
    <div class="museum-card">
      <span class="exhibit-label block-label">Media Gallery</span>
      <div class="sidebar-stack">
        ${topic.media.map(item => `
          <div class="media-item">
            <img src="${item.url}" alt="${item.caption}" class="media-image" />
            <div class="media-caption-box">
              <p class="media-title">${item.title}</p>
              <p class="media-caption">${item.caption}</p>
            </div>
          </div>
        `).join("")}
      </div>
    </div>
  `;

  document.getElementById("referencesCard").innerHTML = `
    <div class="museum-card">
      <span class="exhibit-label block-label">References & Sources</span>
      <div class="sidebar-stack">
        ${topic.references.map(ref => `
          <div class="reference-item">
            <a href="${ref.url}" target="_blank" rel="noopener noreferrer" class="reference-link">${ref.title}</a>
            <p class="reference-meta">${ref.sourceType} · ${ref.accessedDate}</p>
            <p class="reference-notes">${ref.notes}</p>
          </div>
        `).join("")}
      </div>
    </div>
  `;

  document.getElementById("relatedCard").innerHTML = `
    <div class="museum-card">
      <span class="exhibit-label block-label">Related Exhibits</span>
      <div class="sidebar-stack">
        ${topics.filter(t => t.id !== topic.id).slice(0, 3).map(t => `
          <a href="topic_detail.html?slug=${t.slug}" class="related-link">
            <span class="related-id">#${t.id}</span>
            <span>${t.title}</span>
          </a>
        `).join("")}
      </div>
    </div>
  `;

  document.getElementById("bottomNav").innerHTML = `
    <div>
      ${prev ? `
        <a href="topic_detail.html?slug=${prev.slug}" class="museum-card nav-card">
          <div class="nav-direction">Previous</div>
          <div class="nav-title">← ${prev.title}</div>
        </a>
      ` : ""}
    </div>
    <div>
      ${next ? `
        <a href="topic_detail.html?slug=${next.slug}" class="museum-card nav-card nav-card-right">
          <div class="nav-direction">Next Discovery</div>
          <div class="nav-title">${next.title} →</div>
        </a>
      ` : ""}
    </div>
  `;
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

renderNav();
renderTopicPage();
setupMobileMenu();