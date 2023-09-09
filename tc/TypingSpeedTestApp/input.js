// Select the text element and input element
const textToTypeElement = document.getElementById("text-to-type");
const userInputElement = document.getElementById("user-input");

// Event listener for user input
userInputElement.addEventListener("input", () => {
  const textToType = textToTypeElement.textContent;
  const userInput = userInputElement.value;

  // Loop through each character in the text and compare it with the user's input
  for (let i = 0; i < textToType.length; i++) {
    const char = textToType[i];
    const userChar = userInput[i];

    // Create a span element for each character
    const charSpan = document.createElement("span");
    charSpan.textContent = char;

    // Check correctness and apply CSS styles
    if (userChar === undefined) {
      // User hasn't typed this character yet
      charSpan.style.color = "black";
    } else if (char === userChar) {
      // Correctly typed character
      charSpan.style.color = "green";
    } else {
      // Incorrectly typed character
      charSpan.style.color = "red";
    }

    // Append the span element to the text element
    textToTypeElement.appendChild(charSpan);
  }
});
