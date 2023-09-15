const cells = document.querySelectorAll("[data-cell]");
const restartButton = document.getElementById("restart-btn");
const winnerMessage = document.getElementById("winner-message");
const aiButton = document.getElementById("ai-btn");

let isAITurn = false;
let isHumanVsAI = false; // Added to track the game mode

let currentPlayer = "X";
let gameBoard = [
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
];
let gameEnded = false;

// Function to simulate AI's random move
function makeAIMove() {
  // Find all available empty cells
  const emptyCells = [...cells].filter(
    (cell, index) => gameBoard[index] === ""
  );

  // If there are empty cells, pick a random one
  if (emptyCells.length > 0) {
    const randomIndex = Math.floor(Math.random() * emptyCells.length);
    const cellIndex = [...cells].indexOf(emptyCells[randomIndex]);

    setTimeout(() => {
      // Simulate AI's move after a 500ms delay
      gameBoard[cellIndex] = currentPlayer;
      cells[cellIndex].textContent = currentPlayer;

      // Check for a winner or draw
      const winner = checkWinner();
      if (winner === "draw") {
        winnerMessage.textContent = "It's a draw!";
        gameEnded = true;
      } else if (winner) {
        winnerMessage.textContent = `Player ${winner} wins!`;
        gameEnded = true;
      } else {
        // Switch back to human player's turn
        currentPlayer = currentPlayer === "X" ? "O" : "X";
        winnerMessage.textContent = `Player ${currentPlayer}'s turn`;
        isAITurn = false; // AI's turn is over
      }
    }, 500);
  }
}

function checkWinner() {
  const winningCombinations = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15],
    [0, 4, 8, 12],
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15],
    [0, 5, 10, 15],
    [3, 6, 9, 12],
  ];

  for (const combination of winningCombinations) {
    const [a, b, c, d] = combination;
    if (
      gameBoard[a] &&
      gameBoard[a] === gameBoard[b] &&
      gameBoard[a] === gameBoard[c] &&
      gameBoard[a] === gameBoard[d]
    ) {
      highlightWinner(combination);
      return gameBoard[a];
    }
  }

  if (!gameBoard.includes("")) {
    return "draw";
  }

  return null;
}

function highlightWinner(combination) {
  for (const index of combination) {
    cells[index].style.backgroundColor = "green";
  }
}

function handleClick(event) {
  const cellIndex = [...cells].indexOf(event.target);

  if (gameEnded || gameBoard[cellIndex] !== "") {
    return;
  }

  if (!isHumanVsAI) {
    gameBoard[cellIndex] = currentPlayer;
    cells[cellIndex].textContent = currentPlayer;

    const winner = checkWinner();
    if (winner === "draw") {
      winnerMessage.textContent = "It's a draw!";
      gameEnded = true;
    } else if (winner) {
      winnerMessage.textContent = `Player ${winner} wins!`;
      gameEnded = true;
    } else {
      currentPlayer = currentPlayer === "X" ? "O" : "X";
      winnerMessage.textContent = `Player ${currentPlayer}'s turn`;
    }
  } else if (currentPlayer === "X") {
    // Only allow human player X to make a move in human vs AI mode
    gameBoard[cellIndex] = currentPlayer;
    cells[cellIndex].textContent = currentPlayer;

    const winner = checkWinner();
    if (winner === "draw") {
      winnerMessage.textContent = "It's a draw!";
      gameEnded = true;
    } else if (winner) {
      winnerMessage.textContent = `Player ${winner} wins!`;
      gameEnded = true;
    } else {
      currentPlayer = "O"; // Switch to AI's turn
      winnerMessage.textContent = "AI's turn";
      isAITurn = true;
      makeAIMove();
    }
  }
}

function restartGame() {
  gameBoard = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""];
  gameEnded = false;
  winnerMessage.textContent = "";
  cells.forEach((cell) => {
    cell.textContent = "";
    cell.style.backgroundColor = "#eee";
  });
  currentPlayer = "X";
}

cells.forEach((cell) => cell.addEventListener("click", handleClick));
restartButton.addEventListener("click", restartGame);
aiButton.addEventListener("click", toggleGameMode);

function toggleGameMode() {
  isHumanVsAI = !isHumanVsAI; // Toggle the game mode
  restartGame(); // Reset the game
  if (isHumanVsAI) {
    aiButton.textContent = "Switch to Human vs. Human?";
    isAITurn = false; // Reset isAITurn when switching to human vs. human mode
  } else {
    aiButton.textContent = "Switch to Player vs. AI?";
  }
}
