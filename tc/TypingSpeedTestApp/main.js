import { fetchAndDisplayPoem } from "./text.js";
import { countdown, resetTimer } from "./timer.js";
import {
  setActiveLetter,
  updateFocusLine,
  resetInputField,
  userInput,
  activeLetterIndex,
} from "./input.js";

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
// Add an event listener to update the active letter when the input field is focused
userInput.addEventListener("focus", () => {
  activeLetterIndex = Math.min(activeLetterIndex, userInput.value.length - 1);
  setActiveLetter();
});
// Add an event listener to trigger the check when the user types
userInput.addEventListener("input", () => {
  // Increment the active letter index when the user types
  activeLetterIndex++;
  updateFocusLine();
});
// Add an event listener to handle the backspace key
userInput.addEventListener("keydown", (event) => {
  if (event.key === "Backspace") {
    // If the active letter index is greater than 0, decrement it
    if (activeLetterIndex > 0) {
      activeLetterIndex--;
    } else {
      userInput.focus(); // Set the focus back to the input field
    }
    updateFocusLine();
  }
});
// Add an event listener to the reset button
const resetButton = document.getElementById("reset-button");
resetButton.addEventListener("click", resetInputField);
// Initial call to set the active letter and focus line
setActiveLetter();
updateFocusLine();
