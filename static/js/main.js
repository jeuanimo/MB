// Main JavaScript file for Django Project

document.addEventListener("DOMContentLoaded", function () {
  // Initialize all components when DOM is ready
  initializeComponents();
  setupEventListeners();
  animateElements();
});

// Initialize various components
function initializeComponents() {
  // Initialize tooltips if using Bootstrap
  const tooltipTriggerList = Array.from(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  const tooltips = [];
  for (const tooltipTriggerEl of tooltipTriggerList) {
    tooltips.push(new bootstrap.Tooltip(tooltipTriggerEl));
  }

  // Initialize popovers if using Bootstrap
  const popoverTriggerList = Array.from(
    document.querySelectorAll('[data-bs-toggle="popover"]')
  );
  const popovers = [];
  for (const popoverTriggerEl of popoverTriggerList) {
    popovers.push(new bootstrap.Popover(popoverTriggerEl));
  }

  console.log("Components initialized successfully");
  return { tooltips, popovers };
}

// Setup event listeners
function setupEventListeners() {
  // Smooth scrolling for anchor links
  for (const anchor of document.querySelectorAll('a[href^="#"]')) {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    });
  }

  // Form validation
  const forms = document.querySelectorAll(".needs-validation");
  for (const form of forms) {
    form.addEventListener("submit", function (event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add("was-validated");
    });
  }

  // Loading states for buttons
  for (const button of document.querySelectorAll(".btn-loading")) {
    button.addEventListener("click", function () {
      showLoading(this);
    });
  }
}

// Animate elements on scroll or load
function animateElements() {
  // Add fade-in animation to cards
  const cards = document.querySelectorAll(".card");
  for (const [index, card] of cards.entries()) {
    setTimeout(() => {
      card.classList.add("fade-in");
    }, index * 100);
  }

  // Intersection Observer for scroll animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.add("fade-in");
      }
    }
  }, observerOptions);

  // Observe elements with the animate class
  for (const el of document.querySelectorAll(".animate")) {
    observer.observe(el);
  }
}

// Utility functions
function showLoading(button) {
  const originalText = button.innerHTML;
  button.innerHTML =
    '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';
  button.disabled = true;

  // Simulate loading time (remove this in real implementation)
  setTimeout(() => {
    button.innerHTML = originalText;
    button.disabled = false;
  }, 2000);
}

function showAlert(message, type = "info") {
  const alertDiv = document.createElement("div");
  alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
  alertDiv.role = "alert";
  alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;

  // Insert at the top of the main content area
  const container = document.querySelector("main.container");
  if (container) {
    container.insertBefore(alertDiv, container.firstChild);
  }

  // Auto-remove after 5 seconds
  setTimeout(() => {
    alertDiv.remove();
  }, 5000);
}

// AJAX helper function
function makeRequest(url, method = "GET", data = null) {
  const options = {
    method: method,
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
  };

  if (data) {
    options.body = JSON.stringify(data);
  }

  return fetch(url, options)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .catch((error) => {
      console.error("Request failed:", error);
      showAlert("An error occurred. Please try again.", "danger");
      throw error;
    });
}

// Get CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (const cookie of cookies) {
      const cleanCookie = cookie.trim();
      if (cleanCookie.substring(0, name.length + 1) === `${name}=`) {
        cookieValue = decodeURIComponent(
          cleanCookie.substring(name.length + 1)
        );
        break;
      }
    }
  }
  return cookieValue;
}

// Debounce function for search inputs
function debounce(func, wait, immediate) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      timeout = null;
      if (!immediate) func.apply(this, args);
    };
    const callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(this, args);
  };
}

// Form serialization helper
function serializeForm(form) {
  const formData = new FormData(form);
  const object = {};
  for (const [key, value] of formData) {
    if (object[key]) {
      if (Array.isArray(object[key])) {
        object[key].push(value);
      } else {
        object[key] = [object[key], value];
      }
    } else {
      object[key] = value;
    }
  }
  return object;
}
