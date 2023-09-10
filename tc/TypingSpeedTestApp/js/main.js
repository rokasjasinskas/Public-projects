import { fetchAndDisplayPoem } from "./text.js";
import { countdown, resetTimer } from "./timer.js";
import {
  setActiveLetter,
  updateFocusLine,
  resetInputField,
  resetButton,
} from "./input.js";
import { calculateTypingMetrics, resetResultsDisplay } from "./metrics.js";
import { restartTest } from "./reset-with-keyboard.js";

//Metrics
// Call the function to start tracking typing metrics
calculateTypingMetrics();
// Add a click event listener to the reset button
resetButton.addEventListener("click", () => {
  // Call the function to reset the results display
  resetResultsDisplay();
});

//Text------------------------------------------------------------
// Call the fetchAndDisplayPoem function when the page loads
window.onload = fetchAndDisplayPoem;
// Add event listener to the button
document
  .getElementById("reset-button")
  .addEventListener("click", fetchAndDisplayPoem);

//Timer------------------------------------------------------------
// Add event listener to the input field
document.getElementById("user-input").addEventListener("input", countdown);
// Add event listener to the "Reset" button
document.getElementById("reset-button").addEventListener("click", function () {
  resetTimer(); // Call the resetTimer function to reset the timer
});

//Input------------------------------------------------------------
// Initial call to set the active letter and focus line
// This function hangles input tracking
setActiveLetter();
updateFocusLine();
// Add an event listener to the reset button
resetButton.addEventListener("click", resetInputField);

//Reset with keybord

// Add event listener for the "Enter" key
document.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    restartTest();
    console.log("enter");
  }
});

// Add event listener for the "Esc" key
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    event.preventDefault();
    restartTest();
    console.log("esc");
  }
});
