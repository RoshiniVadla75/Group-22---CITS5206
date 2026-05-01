document.addEventListener("DOMContentLoaded", () => {
  const lightbox = document.getElementById("imageLightbox");
  const lightboxImage = document.getElementById("lightboxImage");
  const lightboxCaption = document.getElementById("lightboxCaption");
  const closeButton = document.querySelector(".lightbox-close");
  const mediaImages = document.querySelectorAll(".media-image");
  const narrationCard = document.getElementById("audioNarrationCard");
  const playNarration = document.getElementById("playNarration");
  const pauseNarration = document.getElementById("pauseNarration");
  const stopNarration = document.getElementById("stopNarration");
  const narrationStatus = document.getElementById("narrationStatus");
  const narrationSource = document.getElementById("narrationSource");
  let currentUtterance = null;
  let narrationQueue = [];
  let narrationIndex = 0;
  let narrationActive = false;

  const openLightbox = (img) => {
    const mediaItem = img.closest(".media-item");
    const title = mediaItem?.querySelector(".media-title")?.textContent || "";
    const caption = mediaItem?.querySelector(".media-caption")?.textContent || "";

    lightboxImage.src = img.src;
    lightboxImage.alt = img.alt || title;
    lightboxCaption.textContent = caption || title || "Image preview";
    lightboxCaption.style.display = caption || title ? "block" : "none";
    lightbox.classList.add("visible");
    lightbox.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  };

  const closeLightbox = () => {
    lightbox.classList.remove("visible");
    lightbox.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    lightboxImage.src = "";
  };

  mediaImages.forEach((img) => {
    img.addEventListener("click", () => openLightbox(img));
  });

  closeButton?.addEventListener("click", closeLightbox);

  lightbox?.addEventListener("click", (event) => {
    if (event.target === lightbox || event.target.classList.contains("lightbox-backdrop")) {
      closeLightbox();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && lightbox.classList.contains("visible")) {
      closeLightbox();
    }
  });

  const setNarrationStatus = (message) => {
    if (narrationStatus) {
      narrationStatus.textContent = message;
    }
  };

  const normalizeText = (value) => {
    return String(value || "").replace(/\s+/g, " ").trim();
  };

  const getNarrationText = () => {
    const sourceText = narrationSource?.innerText || narrationSource?.textContent || "";
    const fallbackText = [
      narrationCard?.dataset.narrationTitle || "Topic",
      narrationCard?.dataset.narrationText || "",
    ].join(". ");

    return normalizeText(sourceText || fallbackText);
  };

  const splitNarrationText = (text) => {
    const normalizedText = normalizeText(text);
    if (!normalizedText) return [];

    const sentences = normalizedText.match(/[^.!?]+[.!?]+|[^.!?]+$/g) || [
      normalizedText,
    ];
    const chunks = [];
    let chunk = "";

    sentences.forEach((sentence) => {
      const nextSentence = sentence.trim();
      if (!nextSentence) return;

      const combined = `${chunk} ${nextSentence}`.trim();
      if (combined.length > 280 && chunk) {
        chunks.push(chunk);
        chunk = nextSentence;
      } else {
        chunk = combined;
      }
    });

    if (chunk) {
      chunks.push(chunk);
    }

    return chunks;
  };

  const stopSpeech = (message = "Narration is stopped.") => {
    narrationActive = false;
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }
    currentUtterance = null;
    narrationQueue = [];
    narrationIndex = 0;
    if (message) {
      setNarrationStatus(message);
    }
  };

  const speakCurrentChunk = () => {
    if (!narrationActive || narrationIndex >= narrationQueue.length) {
      narrationActive = false;
      currentUtterance = null;
      setNarrationStatus("Narration finished.");
      return;
    }

    currentUtterance = new SpeechSynthesisUtterance(
      narrationQueue[narrationIndex]
    );
    currentUtterance.rate = 0.95;
    currentUtterance.pitch = 1;
    currentUtterance.onend = () => {
      if (!narrationActive) return;
      narrationIndex += 1;
      speakCurrentChunk();
    };
    currentUtterance.onerror = () => {
      narrationActive = false;
      setNarrationStatus("Narration could not be played.");
    };

    window.speechSynthesis.speak(currentUtterance);
    setNarrationStatus(
      `Narration is playing (${narrationIndex + 1} of ${narrationQueue.length}).`
    );
  };

  if (!("speechSynthesis" in window)) {
    setNarrationStatus("Audio narration is not supported in this browser.");
    playNarration?.setAttribute("disabled", "true");
    pauseNarration?.setAttribute("disabled", "true");
    stopNarration?.setAttribute("disabled", "true");
    return;
  }

  playNarration?.addEventListener("click", () => {
    if (window.speechSynthesis.paused && currentUtterance) {
      window.speechSynthesis.resume();
      setNarrationStatus(
        `Narration is playing (${narrationIndex + 1} of ${narrationQueue.length}).`
      );
      return;
    }

    if (window.speechSynthesis.speaking && narrationActive) {
      setNarrationStatus(
        `Narration is already playing (${narrationIndex + 1} of ${narrationQueue.length}).`
      );
      return;
    }

    const narrationText = getNarrationText();

    if (!narrationText) {
      setNarrationStatus("No narration text is available for this exhibit.");
      return;
    }

    stopSpeech("");
    narrationQueue = splitNarrationText(narrationText);
    narrationIndex = 0;
    narrationActive = true;
    speakCurrentChunk();
  });

  pauseNarration?.addEventListener("click", () => {
    if (window.speechSynthesis.speaking) {
      window.speechSynthesis.pause();
      setNarrationStatus("Narration is paused.");
    }
  });

  stopNarration?.addEventListener("click", stopSpeech);

  window.addEventListener("beforeunload", () => {
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }
  });
});
