// Function to calculate typing speed and accuracy
function calculateTypingMetrics() {
  const textToType = document.getElementById("text-to-type").textContent;

  // Add event listener to the input field to record when typing ends
  userInput.addEventListener("input", () => {
    const currentTime = new Date();

    // Check if the countdown timer has ended
    if (currentTime >= endTime) {
      const userTypedText = userInput.value;
      const totalCharacters = textToType.length;

      // Calculate typing speed (characters per minute)
      const typingSpeed = (totalCharacters / 60) * 60; // Assuming 60 seconds is the measurement period

      // Calculate typing accuracy (error rate)
      let errorCount = 0;
      for (let i = 0; i < totalCharacters; i++) {
        if (userTypedText[i] !== textToType[i]) {
          errorCount++;
        }
      }
      const typingAccuracy =
        ((totalCharacters - errorCount) / totalCharacters) * 100;

      // Store typing speed and accuracy in local storage
      const typingMetrics = {
        speed: typingSpeed,
        accuracy: typingAccuracy,
      };

      localStorage.setItem("typingMetrics", JSON.stringify(typingMetrics));

      // Remove the input event listener
      userInput.removeEventListener("input");
    }
  });
}

// Call the function to start tracking typing metrics
calculateTypingMetrics();
