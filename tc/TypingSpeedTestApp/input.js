function checkUserInput() {
  // Get the text from the HTML element with id "text-to-type"
  const textToTypeElement = document.getElementById("text-to-type");
  const textToType = textToTypeElement.textContent.trim(); // Remove leading/trailing white spaces

  // Get the user's input from the input field
  const userInput = document.getElementById("user-input");
  const userInputValue = userInput.value.trim(); // Remove leading/trailing white spaces

  // Create a new HTML element to display the text with color-coded letters
  const textWithColors = document.createElement("span");

  // Check each letter of the user's input
  for (let i = 0; i < textToType.length; i++) {
    const userLetter = userInputValue[i];
    const expectedLetter = textToType[i];

    // Create a new span element for each letter
    const letterSpan = document.createElement("span");

    if (userLetter === expectedLetter) {
      // User entered the correct letter, apply green color
      console.log("Correct letter:", userLetter);

      letterSpan.textContent = userLetter;
      letterSpan.classList.add("correct-letter");
    } else {
      console.log("Incorrect letter:", userLetter);

      // User entered an incorrect letter, apply red color
      letterSpan.textContent = expectedLetter; // Show the expected letter in red
      letterSpan.classList.add("incorrect-letter");
    }

    // Append the letter span to the textWithColors element
    textWithColors.appendChild(letterSpan);
  }

  // Replace the content of the "text-to-type" element with the colored letters
  textToTypeElement.innerText = textWithColors.innerText;
}

// Add an event listener to trigger the check when the user types
document.getElementById("user-input").addEventListener("input", checkUserInput);
