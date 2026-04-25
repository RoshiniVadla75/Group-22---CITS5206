document.addEventListener("DOMContentLoaded", function () {
  const container = document.getElementById("interactive-diagram");
  if (!container) return;

  const slug = container.dataset.slug;
  const flowContainer = document.getElementById("diagram-flow");
  const titleBox = document.getElementById("diagram-title");
  const descriptionBox = document.getElementById("diagram-description");

  if (!flowContainer || !titleBox || !descriptionBox) return;

  const diagrams = {
    "large-language-models": [
      {
        label: "1. Input Prompt",
        title: "Input Prompt",
        description: "The user enters a prompt such as a question, instruction, or request for writing, explanation, or code."
      },
      {
        label: "2. Tokenisation",
        title: "Tokenisation",
        description: "The text is split into smaller units called tokens so the model can process language numerically."
      },
      {
        label: "3. Pattern Processing",
        title: "Pattern Processing",
        description: "The Transformer model examines relationships between tokens using patterns learned from massive training data."
      },
      {
        label: "4. Prediction",
        title: "Next-Token Prediction",
        description: "The model predicts the most likely next token based on previous context and repeats this step many times."
      },
      {
        label: "5. Generated Output",
        title: "Generated Output",
        description: "The final result is produced as natural-language output such as an answer, summary, response, or generated text."
      }
    ],
    "synthetic-media-technology-deep-fakes": [
      {
        label: "1. Training Data",
        title: "Training Data",
        description: "The system is trained on many images, videos, or audio clips to learn the appearance, voice, or movement of a person."
      },
      {
        label: "2. Feature Learning",
        title: "Feature Learning",
        description: "The model learns patterns such as facial structure, expressions, voice characteristics, timing, and style."
      },
      {
        label: "3. Media Synthesis",
        title: "Media Synthesis",
        description: "Using those learned patterns, the model generates synthetic image, video, or audio content."
      },
      {
        label: "4. Manipulated Output",
        title: "Manipulated Output",
        description: "The output can look highly realistic, making fake content appear authentic to viewers."
      },
      {
        label: "5. Detection & Ethics",
        title: "Detection and Ethical Risk",
        description: "Deepfakes raise concerns about misinformation, consent, fraud, and trust, so detection tools and ethical safeguards are essential."
      }
    ]
  };

  const steps = diagrams[slug];
  if (!steps) {
    container.style.display = "none";
    return;
  }

  // Preserve the vertical class when clearing
  const isVertical = flowContainer.classList.contains('vertical');
  flowContainer.innerHTML = "";
  if (isVertical) {
    flowContainer.classList.add('vertical');
  }

  function setActiveStep(button, step) {
    flowContainer.querySelectorAll(".diagram-step").forEach(item => {
      item.classList.remove("active");
      item.setAttribute("aria-pressed", "false");
    });

    button.classList.add("active");
    button.setAttribute("aria-pressed", "true");
    titleBox.textContent = step.title;
    descriptionBox.textContent = step.description;
  }

  steps.forEach((step, index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "diagram-step";
    button.textContent = step.label;
    button.setAttribute("aria-pressed", "false");

    button.addEventListener("click", function () {
      setActiveStep(button, step);
    });

    flowContainer.appendChild(button);

    if (index < steps.length - 1) {
      const arrow = document.createElement("div");
      arrow.className = "diagram-arrow";
      arrow.textContent = "↓";
      flowContainer.appendChild(arrow);
    }
  });

  const firstButton = flowContainer.querySelector(".diagram-step");
  if (firstButton) {
    setActiveStep(firstButton, steps[0]);
  }
});