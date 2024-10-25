document.addEventListener("DOMContentLoaded", function() {
    // Toggle mobile menu
    const mobileMenuLink = document.getElementById("mobileMenuLink");
    const nav = document.querySelector("nav");

    if (mobileMenuLink && nav) {
        mobileMenuLink.addEventListener("click", function() {
            nav.classList.toggle("open");
        });
    }

    // Basic script for responsive images or other future interactivity can go here
    console.log("JavaScript loaded successfully");
});
