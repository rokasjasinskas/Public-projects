// Initialize attemptCount to 0 and a variable to store the previous accuracy
let attemptCount = 0;
let previousAccuracy = 0;

// Function to handle the "timerEnded" event
function handleTimerEnded() {
  // Increment the attempt count
  attemptCount++;

  // Get the final typing speed and accuracy values from the HTML
  const speedElement = document.getElementById("speed");
  const accuracyElement = document.getElementById("accuracy");

  const finalSpeed = parseFloat(speedElement.textContent);
  const finalAccuracy = parseFloat(accuracyElement.textContent);

  // Create an object to store the results
  const results = {
    speed: finalSpeed,
    accuracy: finalAccuracy,
  };

  // Store the results in local storage
  localStorage.setItem("previousResults", JSON.stringify(results));

  // Log the results to the console
  console.log("Attempt #" + attemptCount);
  console.log("WPM:", finalSpeed);

  // Compare accuracy with the previous attempt and log the result
  let accuracyComparison = 0;
  if (attemptCount > 1) {
    accuracyComparison = finalAccuracy - previousAccuracy;
    console.log("Accuracy Change:", accuracyComparison.toFixed(2), "%");
  } else {
    console.log("Accuracy Change: N/A");
  }

  // Update the previous accuracy for the next comparison
  previousAccuracy = finalAccuracy;

  // Add the results to the table in the HTML
  const previousResultsTableBody = document.getElementById(
    "previous-results-table-body"
  );
  const newRow = previousResultsTableBody.insertRow(0);
  const attemptCell = newRow.insertCell(0);
  const speedCell = newRow.insertCell(1);
  const accuracyCell = newRow.insertCell(2);
  const improvementCell = newRow.insertCell(3);

  attemptCell.textContent = attemptCount;
  speedCell.textContent = finalSpeed.toFixed(2);
  accuracyCell.textContent = finalAccuracy.toFixed(2);
  improvementCell.textContent = accuracyComparison.toFixed(2) + "%"; // Display the improvement
}

// Add an event listener to listen for the "timerEnded" event
document.addEventListener("timerEnded", handleTimerEnded);
