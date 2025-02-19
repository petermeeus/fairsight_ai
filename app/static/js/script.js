document.addEventListener("DOMContentLoaded", function () {
    // Sidebar Toggle
    const sidebar = document.getElementById("sidebar");
    const openBtn = document.getElementById("openSidebar");
    const closeBtn = document.getElementById("closeSidebar");
  
    if (sidebar && openBtn && closeBtn) {
      openBtn.addEventListener("click", () => {
        sidebar.classList.add("sidebar-open");
      });
      closeBtn.addEventListener("click", () => {
        sidebar.classList.remove("sidebar-open");
      });
    }
  
    // Scroll Animations
    const animatedElements = document.querySelectorAll(".animate-up, .animate-fadein");
    function handleScrollAnimations() {
      const triggerBottom = window.innerHeight * 0.85;
      animatedElements.forEach((el) => {
        const rect = el.getBoundingClientRect();
        if (rect.top < triggerBottom) {
          el.classList.add("visible");
        }
      });
    }
    window.addEventListener("scroll", handleScrollAnimations);
    handleScrollAnimations();
  
    // Toggle Password Visibility (for auth pages)
    const toggleIcons = document.querySelectorAll(".toggle-password");
    toggleIcons.forEach(function (icon) {
      icon.addEventListener("click", function () {
        const targetSelector = icon.getAttribute("data-target");
        const passwordField = document.querySelector(targetSelector);
        if (passwordField) {
          const currentType = passwordField.getAttribute("type");
          passwordField.setAttribute("type", currentType === "password" ? "text" : "password");
        }
      });
    });
  
    // Carousel Logic with Dot Indicators
    const carousel = document.getElementById("statsCarousel");
    const dotsContainer = document.getElementById("carouselDots");
    const prevBtn = document.querySelector(".left-arrow");
    const nextBtn = document.querySelector(".right-arrow");
    if (carousel) {
      const slides = carousel.querySelectorAll(".carousel-slide");
      let currentIndex = 0;
  
      // Create dot indicators if container exists
      if (dotsContainer) {
        slides.forEach((slide, i) => {
          const dot = document.createElement("div");
          dot.className = "carousel-dot";
          dot.addEventListener("click", () => {
            currentIndex = i;
            showSlide(currentIndex);
          });
          dotsContainer.appendChild(dot);
        });
      }
      const dots = dotsContainer ? dotsContainer.querySelectorAll(".carousel-dot") : [];
  
      function showSlide(index) {
        carousel.style.transform = `translateX(-${index * 100}%)`;
        updateDots(index);
      }
  
      function updateDots(index) {
        dots.forEach((dot, i) => {
          dot.classList.toggle("active", i === index);
        });
      }
  
      // Initialize
      showSlide(currentIndex);
  
      if (prevBtn) {
        prevBtn.addEventListener("click", () => {
          currentIndex = currentIndex === 0 ? slides.length - 1 : currentIndex - 1;
          showSlide(currentIndex);
        });
      }
      if (nextBtn) {
        nextBtn.addEventListener("click", () => {
          currentIndex = currentIndex === slides.length - 1 ? 0 : currentIndex + 1;
          showSlide(currentIndex);
        });
      }
    }
  });
  