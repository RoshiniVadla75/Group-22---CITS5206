const navItems = [
  { path: 'home.html', label: 'Home' },
  { path: 'timeline.html', label: 'Timeline' },
  { path: 'explore_WA.html', label: 'Explore WA' },
  { path: 'guided_tour.html', label: 'Guided Tour' },
  { path: 'search.html', label: 'Search' },
];

const topicPreviews = {
  turing: {
    title: "Turing’s AI Foundations",
    year: "1950",
    text: "This exhibit introduces Alan Turing’s foundational ideas about machine intelligence, the Turing Test, and early thinking about whether machines could imitate human reasoning.",
    link: "topic_turing.html"
  },
  "learning-machines": {
    title: "Learning Machines",
    year: "1960s",
    text: "This exhibit explores how early systems began adapting from experience, forming the basis of machine learning concepts that later became central to AI.",
    link: "topic_learning_machines.html"
  },
  "game-playing": {
    title: "Game Playing Systems",
    year: "1960–1970",
    text: "This exhibit shows how games became controlled environments for testing strategy, rule-based decision making, and computational search.",
    link: "topic_game_playing.html"
  },
  "expert-systems": {
    title: "Expert Systems",
    year: "1980s",
    text: "This exhibit examines knowledge-based AI systems that used rules and inference engines to replicate expert human decision-making.",
    link: "topic_expert_systems.html"
  },
  "neural-networks": {
    title: "Artificial Neural Networks",
    year: "1980–2000",
    text: "This exhibit presents the rise of neural computation, pattern recognition, and the foundations that later enabled deep learning.",
    link: "topic_neural_networks.html"
  },
  "internet-ai": {
    title: "Internet-Driven AI",
    year: "2010",
    text: "This exhibit explores how internet-scale data transformed AI, enabling more connected knowledge systems and broader information retrieval.",
    link: "topic_internet_ai.html"
  },
  "evolutionary-computing": {
    title: "Evolutionary Computing",
    year: "2010",
    text: "This exhibit focuses on optimisation methods inspired by biological evolution, including mutation, selection, and adaptation.",
    link: "topic_evolutionary_computing.html"
  },
  "synthetic-media": {
    title: "Synthetic Media Generation",
    year: "2015",
    text: "This exhibit examines AI-generated media, including realistic video and image synthesis, and the ethical issues surrounding authenticity and trust.",
    link: "topic_synthetic_media.html"
  },
  nlp: {
    title: "Natural Language Processing",
    year: "2010–2020",
    text: "This exhibit presents the methods used to interpret, classify, and generate human language, preparing the path for modern language models.",
    link: "topic_nlp.html"
  },
  llms: {
    title: "Large Language Models",
    year: "2020–Present",
    text: "This exhibit explains how transformer-based language systems generate, summarise, and respond to text across many knowledge domains.",
    link: "topic_llms.html"
  }
};

function renderNav() {
  const desktopNav = document.getElementById('desktopNav');
  const mobileNav = document.getElementById('mobileNav');
  const currentPage = 'home.html';

  const html = navItems
    .map((item) => {
      const activeClass = item.path === currentPage ? 'active' : '';
      return `<a href="${item.path}" class="${activeClass}">${item.label}</a>`;
    })
    .join('');

  desktopNav.innerHTML = html;
  mobileNav.innerHTML = html;
}

function setupMobileMenu() {
  const mobileToggle = document.getElementById('mobileToggle');
  const mobileNav = document.getElementById('mobileNav');

  if (!mobileToggle || !mobileNav) return;

  mobileToggle.addEventListener('click', () => {
    mobileNav.classList.toggle('open');
    mobileToggle.textContent = mobileNav.classList.contains('open')
      ? '✕'
      : '☰';
  });
}

function setupParadigmModal() {
  const cards = document.querySelectorAll('.paradigm-card');
  const modal = document.getElementById('topicModal');
  const closeBtn = document.getElementById('modalClose');
  const modalTitle = document.getElementById('modalTitle');
  const modalYear = document.getElementById('modalYear');
  const modalText = document.getElementById('modalText');
  const modalLink = document.getElementById('modalLink');

  if (!cards.length || !modal) return;

  cards.forEach((card) => {
    card.addEventListener('click', () => {
      const key = card.dataset.topic;
      const topic = topicPreviews[key];
      if (!topic) return;

      modalTitle.textContent = topic.title;
      modalYear.textContent = topic.year;
      modalText.textContent = topic.text;
      modalLink.href = topic.link;

      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    });
  });

  closeBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.add('hidden');
      document.body.style.overflow = '';
    }
  });
}

renderNav();
setupMobileMenu();
setupParadigmModal();