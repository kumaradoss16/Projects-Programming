// Function to randomly select and return "Rock", "Paper", and "Scissors" (Computer Choice)
function getRandomComputerResult() {
    const options = ["Rock", "Paper", "Scissors"];
    // Generate a Random index between 0 and options.length - 1
    // Math.random() return a decimal between 0 (inclusive) and 1 (exclusive)
    const randomIndex = Math.floor(options.length * Math.random());
    return options[randomIndex];
};

// Function has to determine if the player has won or lost round.
function hasPlayerWonTheRound(player, computer) {
    return (
    (player === "Rock" && computer === "Scissors") ||
    (player === "Scissors" && computer === "Paper") ||
    (player === "Paper" && computer === "Rock")
    );
};

let playerScore = 0;
let computerScore = 0;
// Function to get the results of the round
function getRoundResults(userOption) {
    const computerResult = getRandomComputerResult();
    if (hasPlayerWonTheRound(userOption, computerResult)) {
        playerScore++;
        return `<span style="color: #578FCA;">Player wins!</span> ${userOption} beats ${computerResult}`;
    } else if (userOption === computerResult){
        return `It's a tie! Both chose ${userOption}`;
    } else {
        computerScore++;
        return `<span style="color: #DA6C6C;">Computer wins!</span> ${computerResult} beats ${userOption}`;
    }
};

const playerScoreSpanElement = document.getElementById("player-score");
const computerScoreSpanElement = document.getElementById("computer-score");
const roundResultsMsg = document.getElementById("results-msg");
const winnerMsgElement = document.getElementById("winner-msg");
const optionsContainer = document.querySelector(".options-container");
const resetGameBtn = document.getElementById("reset-game-btn");
// Function to update the scores and round results message
function showResults(userOption) {
    roundResultsMsg.innerHTML = getRoundResults(userOption);
    computerScoreSpanElement.innerText = computerScore;
    playerScoreSpanElement.innerText = playerScore;
    // Check if the player or computer has reached three points
    if (playerScore === 3 || computerScore ===3) {
        winnerMsgElement.innerHTML = `<span class="${playerScore === 3 ? 'player-winner' : 'computer-winner'}">${playerScore === 3 ? "Player" : "Computer"}</span> has won the game!`;
        // Show reset button and hide options container regardless of who wins
        resetGameBtn.style.display = "block";
        optionsContainer.style.display = "none";
    }
};

// Function to reset the game and play again
function resetGame() {
    playerScore = 0;
    computerScore = 0;
    playerScoreSpanElement.innerText = playerScore;
    computerScoreSpanElement.innerText = computerScore;
    roundResultsMsg.innerText = "";
    winnerMsgElement.innerText = "";
    resetGameBtn.style.display = "none";
    optionsContainer.style.display = "block";
};

resetGameBtn.addEventListener("click", resetGame);

const rockBtn = document.getElementById("rock-btn");
const paperBtn = document.getElementById("paper-btn");
const scissorsBtn = document.getElementById("scissors-btn");

rockBtn.addEventListener("click", function() {
    showResults("Rock");
});

paperBtn.addEventListener("click", function() {
    showResults("Paper");
});

scissorsBtn.addEventListener("click", function() {
    showResults("Scissors");
});
