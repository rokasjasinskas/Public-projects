const initialTotalSeconds = 60; // Set the initial totalSeconds value

let countdownStarted = false; // Flag to track if countdown has started
let countdownInterval; // Store the countdown interval ID
export let totalSeconds = initialTotalSeconds;

// Create a custom event for timer ending
export const timerEndedEvent = new Event("timerEnded");

export function countdown() {
  if (!countdownStarted) {
    countdownStarted = true; // Set the flag to true so that the countdown starts only once

    var minutesElement = document.getElementById("minutes");
    var secondsElement = document.getElementById("seconds");

    countdownInterval = setInterval(function () {
      const minutes = Math.floor(totalSeconds / 60);
      const seconds = totalSeconds % 60;

      // Update the HTML elements with the current countdown values
      minutesElement.textContent = minutes.toString().padStart(2, "0");
      secondsElement.textContent = seconds.toString().padStart(2, "0");

      totalSeconds--;

      if (totalSeconds < 0) {
        clearInterval(countdownInterval); // Stop the countdown when it reaches zero
        const timerEndedEvent = new Event("timerEnded");
        document.dispatchEvent(timerEndedEvent); // Dispatch the custom "timerEnded" event
      }
    }, 1000); // Update every 1 second
  }
}

export function resetTimer() {
  clearInterval(countdownInterval); // Stop the countdown if running
  countdownStarted = false; // Reset the countdownStarted flag
  totalSeconds = initialTotalSeconds;
  document.getElementById("minutes").textContent = "00"; // Reset the minutes display
  document.getElementById("seconds").textContent = "00"; // Reset the seconds display
}
