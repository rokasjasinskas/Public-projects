export let userInput = document.getElementById("user-input");
export let activeLetterIndex = 0; // To keep track of the currently active letter
export const resetButton = document.getElementById("reset-button");

// Flag to track whether the timer has ended
let timerEnded = false;

// Event listener to handle the custom timer ended event
document.addEventListener("timerEnded", () => {
  timerEnded = true;
  userInput.readOnly = true;
  setActiveLetter();
});

// Function to add blue shadow to the active letter
export function setActiveLetter() {
  // Get the text from the HTML element with id "text-to-type"
  const textToTypeElement = document.getElementById("text-to-type");
  const textToType = textToTypeElement.textContent.trim(); // Remove leading/trailing white spaces

  // Create a new HTML element to display the text with color-coded letters and blue shadow
  const textWithColors = document.createElement("span");

  // Check each letter of the user's input
  for (let i = 0; i < textToType.length; i++) {
    const userLetter = textToType[i];
    // Create a new span element for each letter
    const letterSpan = document.createElement("span");

    // If the letter is the currently active letter, add a blue shadow
    if (i === activeLetterIndex) {
      letterSpan.classList.add("user-input-letter");
    }

    // Check if the user has entered a letter at this position
    if (i < userInput.value.length) {
      const enteredLetter = userInput.value[i];
      // If the entered letter matches the expected letter, apply green color
      if (enteredLetter === userLetter) {
        letterSpan.classList.add("correct-letter");
      } else {
        // If the entered letter is incorrect, apply red color
        letterSpan.classList.add("incorrect-letter");
      }
    }

    letterSpan.textContent = userLetter;

    // Append the letter span to the textWithColors element
    textWithColors.appendChild(letterSpan);
  }

  // Replace the content of the "text-to-type" element with the colored letters
  textToTypeElement.innerHTML = textWithColors.innerHTML;
}

// Function to update the focus line
export function updateFocusLine() {
  const inputText = userInput.value;
  if (inputText.length === 0) {
    activeLetterIndex = 0; // Reset the active letter index if the input is empty
  } else {
    activeLetterIndex = Math.min(activeLetterIndex, inputText.length - 1);
  }
  setActiveLetter();
}

// Function to reset the input field
export function resetInputField() {
  userInput.value = ""; // Set the value to an empty string
  activeLetterIndex = 0; // Reset the active letter index
  userInput.readOnly = false; // Make the input field active again
  setActiveLetter();
}

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
