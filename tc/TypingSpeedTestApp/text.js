export async function fetchAndDisplayPoem() {
  try {
    const response = await fetch("https://poetrydb.org/random/1");
    if (!response.ok) {
      throw new Error("Failed to fetch data from PoetryDB");
    }

    const data = await response.json();

    if (data.length === 0) {
      throw new Error("No poems found in the response");
    }

    const poem = data[0];

    const poemText = poem.lines.join(" "); // Join lines into a single text
    const words = poemText.split(/\s+/); // Split text into words
    const first50Words = words.slice(0, 50); // Get the first 50 words

    const combinedWords = first50Words.join(" "); // Combine the words into a single string

    // Update the content of the <p> element with id "text-to-type"
    const textToTypeElement = document.getElementById("text-to-type");
    if (textToTypeElement) {
      // Clear the previous text content
      textToTypeElement.textContent = "";

      // Set the new text content
      textToTypeElement.textContent = combinedWords;
    }
  } catch (error) {
    console.error("Error:", error.message);
  }
}

window.fetchAndDisplayPoem = fetchAndDisplayPoem;
