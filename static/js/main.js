/**
 * AI Platform Hub - Main JavaScript
 * Handles navigation toggle, smooth interactions, and shared UI behaviors.
 */

(function () {
    "use strict";

    // Mobile navigation toggle
    const navToggle = document.getElementById("navToggle");
    const navLinks = document.getElementById("navLinks");

    if (navToggle && navLinks) {
        navToggle.addEventListener("click", function () {
            navLinks.classList.toggle("open");
            navToggle.classList.toggle("active");
        });

        // Close menu when a link is clicked (mobile)
        navLinks.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", function () {
                navLinks.classList.remove("open");
                navToggle.classList.remove("active");
            });
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener("click", function (e) {
            const targetId = this.getAttribute("href");
            if (targetId === "#") return;
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: "smooth", block: "start" });
            }
        });
    });

    // Auto-dismiss alerts after 5 seconds
    document.querySelectorAll(".alert").forEach(function (alert) {
        setTimeout(function () {
            alert.style.transition = "opacity 0.4s";
            alert.style.opacity = "0";
            setTimeout(function () {
                alert.remove();
            }, 400);
        }, 5000);
    });

    // Highlight current nav item based on path (fallback)
    const path = window.location.pathname;
    document.querySelectorAll(".nav-links a").forEach(function (link) {
        const href = link.getAttribute("href");
        if (href && href !== "/" && path.startsWith(href)) {
            link.classList.add("active");
        }
    });

    // Simple fade-in for cards on scroll (optional enhancement)
    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = "1";
                        entry.target.style.transform = "translateY(0)";
                    }
                });
            },
            { threshold: 0.08 }
        );

        document.querySelectorAll(".feature-card, .model-card, .testimonial-card, .pricing-card, .blog-card, .team-card").forEach(function (el) {
            el.style.opacity = "0";
            el.style.transform = "translateY(12px)";
            el.style.transition = "opacity 0.4s ease, transform 0.4s ease";
            observer.observe(el);
        });
    }

    // Utility: copy text to clipboard
    window.copyToClipboard = function (text) {
        if (navigator.clipboard) {
            navigator.clipboard.writeText(text).then(function () {
                console.log("Copied to clipboard");
            });
        }
    };

    // Console branding
    console.log("%c AI Platform Hub ", "background:#6366f1;color:#fff;padding:4px 8px;border-radius:4px;font-weight:bold;");
    console.log("Welcome to the AI Platform Hub demo application.");
})();
