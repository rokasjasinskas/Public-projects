var countdownStarted = false; // Flag to track if countdown has started
var countdownInterval; // Store the countdown interval ID

export function countdown() {
  if (!countdownStarted) {
    countdownStarted = true; // Set the flag to true so that the countdown starts only once

    var minutesElement = document.getElementById("minutes");
    var secondsElement = document.getElementById("seconds");

    var totalSeconds = 60;

    countdownInterval = setInterval(function () {
      var minutes = Math.floor(totalSeconds / 60);
      var seconds = totalSeconds % 60;

      // Update the HTML elements with the current countdown values
      minutesElement.textContent = minutes.toString().padStart(2, "0");
      secondsElement.textContent = seconds.toString().padStart(2, "0");

      totalSeconds--;

      if (totalSeconds < 0) {
        clearInterval(countdownInterval); // Stop the countdown when it reaches zero
      }
    }, 1000); // Update every 1 second
  }
}
