document.addEventListener("DOMContentLoaded", () => {
  const lightbox = document.getElementById("imageLightbox");
  const lightboxImage = document.getElementById("lightboxImage");
  const lightboxCaption = document.getElementById("lightboxCaption");
  const closeButton = document.querySelector(".lightbox-close");
  const mediaImages = document.querySelectorAll(".media-image");

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
});