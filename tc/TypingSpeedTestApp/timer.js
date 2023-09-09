document
  .getElementById("fetch-text-button")
  .addEventListener("click", async () => {
    function startTimer(durationInSeconds) {
      let timerElement = document.getElementById("timer"); // Assuming you have an element with id "timer" to display the timer
      let secondsRemaining = durationInSeconds;

      // Function to update the timer
      function updateTimer() {
        if (secondsRemaining <= 0) {
          clearInterval(timerInterval); // Stop the timer when it reaches zero
          timerElement.textContent = "Time's up!";
          logTimerResults(durationInSeconds); // Log timer results when it's done
        } else {
          const minutes = Math.floor(secondsRemaining / 60);
          const seconds = secondsRemaining % 60;
          timerElement.textContent = `${minutes
            .toString()
            .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
          secondsRemaining--;
        }
      }

      // Initial update
      updateTimer();

      // Start the timer and update it every 1000 milliseconds (1 second)
      const timerInterval = setInterval(updateTimer, 1000);
    }

    // Function to log timer results
    function logTimerResults(durationInSeconds) {
      console.log(`Timer completed after ${durationInSeconds} seconds`);
    }

    // Example: Start a timer for 60 seconds
    startTimer(2);
  });
