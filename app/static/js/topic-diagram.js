document.addEventListener("DOMContentLoaded", function () {
  const container = document.getElementById("interactive-diagram");
  if (!container) return;

  const slug = container.dataset.slug;
  const flowContainer = document.getElementById("diagram-flow");
  const titleBox = document.getElementById("diagram-title");
  const descriptionBox = document.getElementById("diagram-description");

  if (!flowContainer || !titleBox || !descriptionBox) return;

  const diagrams = {
    "learning-machines": [
      {
        label: "1. Current Parameters",
        title: "Current Parameters",
        description:
          "The system starts with adjustable parameters, such as weights assigned to board features like piece count and positional strength.",
      },
      {
        label: "2. Generate Action",
        title: "Generate Action",
        description:
          "The learning machine chooses an action based on its current parameters. In Samuel’s checkers program, this means selecting a move.",
      },
      {
        label: "3. Evaluate Outcome",
        title: "Evaluate Outcome",
        description:
          "The outcome is evaluated using a scoring or utility function, such as whether the move improved the board position or contributed to a win.",
      },
      {
        label: "4. Compare Feedback",
        title: "Compare Feedback",
        description:
          "The system compares the result with the expected outcome and identifies whether its current strategy performed well or poorly.",
      },
      {
        label: "5. Update Parameters",
        title: "Update Parameters",
        description:
          "The system adjusts feature weights or parameters to favour actions linked with better outcomes in future games.",
      },
      {
        label: "6. Repeat Through Self-Play",
        title: "Repeat Through Self-Play",
        description:
          "The cycle repeats through many games. Over time, performance improves through repeated evaluation and adjustment.",
      },
    ],

    "game-playing-ai": [
      {
        label: "1. Current Game State",
        title: "Current Game State",
        description:
          "The AI observes the current board configuration, including all pieces, positions, and possible legal moves.",
      },
      {
        label: "2. Generate Possible Moves",
        title: "Move Generation",
        description:
          "The system generates all possible legal moves available from the current state.",
      },
      {
        label: "3. Expand Game Tree",
        title: "Game Tree Expansion",
        description:
          "Each move leads to a new game state. The AI builds a tree of future possibilities by exploring sequences of moves.",
      },
      {
        label: "4. Depth-Limited Search",
        title: "Depth-Limited Search",
        description:
          "Because the full game tree is too large, the AI explores only a limited number of moves ahead.",
      },
      {
        label: "5. Evaluate Positions",
        title: "Evaluation Function",
        description:
          "Each resulting state is scored using a heuristic evaluation function, based on factors like material advantage and position strength.",
      },
      {
        label: "6. Minimax Decision",
        title: "Minimax Algorithm",
        description:
          "The AI assumes the opponent plays optimally. It maximises its own score while minimising the opponent’s best possible response.",
      },
      {
        label: "7. Alpha-Beta Pruning",
        title: "Alpha-Beta Pruning",
        description:
          "Branches that cannot influence the final decision are removed early, reducing computation while preserving accuracy.",
      },
      {
        label: "8. Select Best Move",
        title: "Best Move Selection",
        description:
          "The AI selects the move with the highest evaluated outcome after considering all relevant possibilities.",
      },
    ],

    "large-language-models": [
      {
        label: "1. Input Prompt",
        title: "Input Prompt",
        description:
          "The user enters a prompt such as a question, instruction, or request for writing, explanation, or code.",
      },
      {
        label: "2. Tokenisation",
        title: "Tokenisation",
        description:
          "The text is split into smaller units called tokens so the model can process language numerically.",
      },
      {
        label: "3. Pattern Processing",
        title: "Pattern Processing",
        description:
          "The Transformer model examines relationships between tokens using patterns learned from massive training data.",
      },
      {
        label: "4. Prediction",
        title: "Next-Token Prediction",
        description:
          "The model predicts the most likely next token based on previous context and repeats this step many times.",
      },
      {
        label: "5. Generated Output",
        title: "Generated Output",
        description:
          "The final result is produced as natural-language output such as an answer, summary, response, or generated text.",
      },
    ],

    "synthetic-media-technology-deep-fakes": [
      {
        label: "1. Training Data",
        title: "Training Data",
        description:
          "The system is trained on many images, videos, or audio clips to learn the appearance, voice, or movement of a person.",
      },
      {
        label: "2. Feature Learning",
        title: "Feature Learning",
        description:
          "The model learns patterns such as facial structure, expressions, voice characteristics, timing, and style.",
      },
      {
        label: "3. Media Synthesis",
        title: "Media Synthesis",
        description:
          "Using those learned patterns, the model generates synthetic image, video, or audio content.",
      },
      {
        label: "4. Manipulated Output",
        title: "Manipulated Output",
        description:
          "The output can look highly realistic, making fake content appear authentic to viewers.",
      },
      {
        label: "5. Detection & Ethics",
        title: "Detection and Ethical Risk",
        description:
          "Deepfakes raise concerns about misinformation, consent, fraud, and trust, so detection tools and ethical safeguards are essential.",
      },
    ],

    "artificial-neural-nets": [
      {
        label: "1. Input Data",
        title: "Input Data",
        description:
          "The neural network receives numerical input, such as image pixels, sound features, or other data values.",
      },
      {
        label: "2. Weighted Connections",
        title: "Weighted Connections",
        description:
          "Information passes through connections between neurons. Each connection has a weight that affects how strongly information is passed forward.",
      },
      {
        label: "3. Hidden Layers",
        title: "Hidden Layers",
        description:
          "Hidden layers process the data and detect patterns such as edges, shapes, colours, or more complex relationships.",
      },
      {
        label: "4. Output Prediction",
        title: "Output Prediction",
        description:
          "The output layer produces a prediction, such as whether an image is more likely to be a cat, a dog, or another category.",
      },
      {
        label: "5. Error Check",
        title: "Error Check",
        description:
          "During training, the network compares its prediction with the correct answer and measures the error.",
      },
      {
        label: "6. Weight Update",
        title: "Weight Update",
        description:
          "The network adjusts its weights to reduce the error. Repeating this process allows the system to learn and improve over time.",
      },
    ],

    "natural-language-processing": [
      {
        label: "1. Input Text",
        title: "Input Text",
        description:
          "The system receives human language input, such as a sentence, question, search query, or instruction.",
      },
      {
        label: "2. Tokenisation",
        title: "Tokenisation",
        description:
          "The text is split into smaller units called tokens, such as words or subwords, so the computer can process it.",
      },
      {
        label: "3. Vector Representation",
        title: "Vector Representation",
        description:
          "Tokens are converted into numerical vectors. These vectors help the model capture relationships between words.",
      },
      {
        label: "4. Context Processing",
        title: "Context Processing",
        description:
          "Modern NLP models use attention mechanisms to focus on important words and understand how words relate to each other in context.",
      },
      {
        label: "5. Pattern-Based Decision",
        title: "Pattern-Based Decision",
        description:
          "The system identifies learned language patterns, such as intent, meaning, or sentiment, based on statistical relationships in data.",
      },
      {
        label: "6. Output",
        title: "Output",
        description:
          "The model produces an output, such as a response, translation, summary, search result, or prediction.",
      },
    ],
  };

  const steps = diagrams[slug];
  if (!steps) {
    container.style.display = "none";
    return;
  }

  const isVertical = flowContainer.classList.contains("vertical");
  flowContainer.innerHTML = "";
  if (isVertical) {
    flowContainer.classList.add("vertical");
  }

  function setActiveStep(button, step) {
    flowContainer.querySelectorAll(".diagram-step").forEach((item) => {
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