import { totalSeconds } from "./timer.js";
import { userInput, resetButton } from "./input.js";

// Function to calculate typing metrics
function calculateTypingMetrics() {
  // Get the expected text to type from the HTML
  const textToTypeElement = document.getElementById("text-to-type");
  let textToType = textToTypeElement.textContent;
  const startTime = new Date(); // Record the start time
  let lastCharacterCount = 0;
  let lastTime = startTime;

  function inputEventListener() {
    const currentTime = new Date();

    // Calculate elapsed time (in seconds)
    const elapsedTime = (currentTime - startTime) / 1000;

    // Calculate typing speed (characters per minute) based on correct characters
    const characterCount = userInput.value.length;
    let correctCharacterCount = 0;

    // Compare each character entered by the user with the expected text
    for (let i = 0; i < characterCount; i++) {
      if (i < textToType.length) {
        if (userInput.value[i] === textToType[i]) {
          correctCharacterCount++;
        }
      }
    }

    const typingSpeed = (correctCharacterCount / elapsedTime) * 60;

    // Calculate typing accuracy (error rate)
    const expectedCharacterCount = textToType.length;
    const typingAccuracy =
      (correctCharacterCount / expectedCharacterCount) * 100;

    // Ensure accuracy is never more than 100%
    const finalAccuracy = Math.min(typingAccuracy, 100);

    // Store typing speed and accuracy in local storage
    const typingMetrics = {
      speed: typingSpeed,
      accuracy: finalAccuracy,
    };

    localStorage.setItem("typingMetrics", JSON.stringify(typingMetrics));

    // Display typing speed and accuracy in the HTML
    document.getElementById("speed").textContent = typingSpeed.toFixed(2); // Display speed with two decimal places
    document.getElementById("accuracy").textContent = finalAccuracy.toFixed(2); // Display accuracy with two decimal places

    // Update the last character count and time
    lastCharacterCount = characterCount;
    lastTime = currentTime;
  }

  // Add event listener to the input field using the defined function
  userInput.addEventListener("input", inputEventListener);

  // Add focus event listener to the input field
  userInput.addEventListener("focus", () => {
    textToType = textToTypeElement.textContent; // Update expected text when the input is in focus
  });
}

// Call the function to start tracking typing metrics
calculateTypingMetrics();

// Function to reset the results display
function resetResultsDisplay() {
  // Get the HTML elements for speed and accuracy
  const speedElement = document.getElementById("speed");
  const accuracyElement = document.getElementById("accuracy");

  // Reset their values to the initial values (0)
  speedElement.textContent = "0";
  accuracyElement.textContent = "0"; // Set accuracy to 0% initially
}

// Add a click event listener to the reset button
resetButton.addEventListener("click", () => {
  // Call the function to reset the results display
  resetResultsDisplay();
});
