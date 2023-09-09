// Constants
const textToTypeElement = document.getElementById("text-to-type");
const userInputElement = document.getElementById("user-input");
const timerElement = document.getElementById("timer");
const speedElement = document.getElementById("speed");
const accuracyElement = document.getElementById("accuracy");
const resetButton = document.getElementById("reset-button");

let textToType = "";
let timer;
let startTime;
let wordsTyped = 0;
let errors = 0;

// Function to fetch random text from the API
async function fetchText() {
  try {
    const response = await fetch("https://api.example.com/random-text"); // Replace with the actual API endpoint
    const data = await response.json();
    textToType = data.text;
    textToTypeElement.textContent = textToType;
  } catch (error) {
    console.error("Error fetching text:", error);
  }
}

// Function to start the typing test
function startTypingTest() {
  userInputElement.value = ""; // Clear the input field
  userInputElement.focus();
  startTime = Date.now();
  timer = setInterval(updateTimer, 1000);
}

// Function to update the timer
function updateTimer() {
  const currentTime = Date.now();
  const elapsedSeconds = Math.floor((currentTime - startTime) / 1000);
  const remainingSeconds = Math.max(0, 60 - elapsedSeconds);

  timerElement.textContent = remainingSeconds;

  if (remainingSeconds === 0) {
    clearInterval(timer);
    endTypingTest();
  }
}

// Function to end the typing test
function endTypingTest() {
  const elapsedTime = (Date.now() - startTime) / 1000;
  const wordsPerMinute = Math.round((wordsTyped / elapsedTime) * 60);
  const accuracy = ((textToType.length - errors) / textToType.length) * 100;

  speedElement.textContent = wordsPerMinute;
  accuracyElement.textContent = accuracy.toFixed(2);

  // Store user metrics (you can use local storage)
  const previousMetrics =
    JSON.parse(localStorage.getItem("typingMetrics")) || [];
  const newMetric = { speed: wordsPerMinute, accuracy: accuracy };
  previousMetrics.push(newMetric);
  localStorage.setItem("typingMetrics", JSON.stringify(previousMetrics));
}

// Event listeners
userInputElement.addEventListener("input", checkInput);
resetButton.addEventListener("click", fetchText);

// Function to check user input
function checkInput() {
  const inputText = userInputElement.value;
  const inputWords = inputText.split(" ");
  const expectedWords = textToType.split(" ");

  wordsTyped = inputWords.length;

  for (let i = 0; i < inputWords.length; i++) {
    if (inputWords[i] !== expectedWords[i]) {
      errors++;
    }
  }

  // Update text highlighting based on correct/incorrect input
  // You can use CSS to apply highlighting styles

  if (inputText === textToType) {
    endTypingTest();
  }
}

// Initial fetch of text
fetchText();
