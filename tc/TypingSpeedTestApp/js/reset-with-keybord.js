import { resetButton } from "./input.js";

// Function to restart the test
function restartTest() {
  // Trigger a click event on the reset button
  resetButton.click();
}

// Function to reset the test
function resetTest() {
  // Reset the input field and other relevant data
  // (You can implement your reset logic here)
  console.log("Test reset");
}

// Add event listener for the "Enter" key
document.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    restartTest();
  }
});

// Add event listener for the "Esc" key
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    resetTest();
  }
});
