// Your scrollToSection function remains the same
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
  }

// script.js
const startButton = document.getElementById("homeButton");
const animatedBox = document.querySelector(".headerDescription");

let animationRunning = false;

// Function to start the animation
function startAnimationAndScroll() {
    // Execute scrollToSection function before starting the animation
    scrollToSection("home"); // Replace "scroll-target" with the actual section ID you want to scroll to
    
    animatedBox.classList.add("run-animation");
    animationRunning = true;
    startButton.disabled = false;
    setTimeout(() => {
        stopAnimation();
    }, 2000); // Change 5000 to the desired duration in milliseconds

}

// Function to stop the animation
function stopAnimation() {
    animatedBox.classList.remove("run-animation");
    animationRunning = false;
    startButton.disabled = false;
}

// Event listener for button click
startButton.addEventListener("click", function () {
    if (!animationRunning) {
        startAnimationAndScroll();
    }
});

// Start the animation when the page loads
window.addEventListener("load", function () {
    startButton.disabled = true;
    startAnimationAndScroll();

});



document.addEventListener("DOMContentLoaded", function () {
    const imageButtons = document.querySelectorAll(".btn.btn-outline-secondary");
    const scrollContent = document.querySelector(".scroll-content");
  
    imageButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const imageNumber = button.getAttribute("data-image");
            const images = scrollContent.querySelectorAll("img");
            
            // Ocultar todas las imágenes
            images.forEach((image) => {
                image.style.display = "none";
            });
  
            // Mostrar la imagen seleccionada
            const selectedImage = scrollContent.querySelector(`[alt="Imagen ${imageNumber}"]`);
            if (selectedImage) {
                selectedImage.style.display = "block";
            }
        });
    });
  });