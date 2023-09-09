import { fetchAndDisplayPoem } from "./text.js";
import { countdown } from "./timer.js";

//Text
// Call the fetchAndDisplayPoem function when the page loads
window.onload = fetchAndDisplayPoem;
// Add event listener to the button
document
  .getElementById("reset-button")
  .addEventListener("click", fetchAndDisplayPoem);

//Timer
// Add event listener to the input field
document.getElementById("user-input").addEventListener("input", countdown);
// Add event listener to the "Reset" button
document.getElementById("reset-button").addEventListener("click", function () {
  clearInterval(countdownInterval); // Stop the countdown if running
  countdownStarted = false; // Reset the countdownStarted flag
  document.getElementById("minutes").textContent = "00"; // Reset the minutes display
  document.getElementById("seconds").textContent = "00"; // Reset the seconds display
});
