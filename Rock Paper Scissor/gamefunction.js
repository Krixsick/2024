"use strict";

const playerOneRock = document.querySelector(".rock");
const playerOnePaper = document.querySelector(".paper");
const playerOneScissor = document.querySelector(".scissor");
const playerOneConfirm = document.querySelector(".confirm");
const playerOneChoiceImg = document.getElementById("playerOneChoiceImg");
const playerOneScore = document.getElementById("playerOneScore");

const playerTwoChoiceImg = document.querySelector("#playerTwoChoiceImg");
const playerTwoScore = document.querySelector("#playerTwoScore");

const winScreen = document.querySelector("#winScreen");
const loseScreen = document.querySelector("#loseScreen");

const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const btnCloseModal = document.querySelector(".close-modal");
const btnOpenModal = document.querySelector(".show-modal");

let attempts = 10;
let botChoice;
let playerOneWins = 0;
let playerTwoWins = 0;
let playerOneChoice = null; //We let playerchoice be one of the options

const openModal = function () {
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};

const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

function imageReplacement(player, choice) {
  if (player === "Player One") {
    if (choice === "paper") {
      playerOneChoiceImg.src = "images/paper.png";
    } else if (choice === "rock") {
      playerOneChoiceImg.src = "images/rock.png";
    } else if (choice === "scissor") {
      playerOneChoiceImg.src = "images/scissors.png";
    }
  } else if (player == "Player Two") {
    if (choice === "paper") {
      playerTwoChoiceImg.src = "images/paper.png";
    } else if (choice === "rock") {
      playerTwoChoiceImg.src = "images/rock.png";
    } else if (choice === "scissor") {
      playerTwoChoiceImg.src = "images/scissors.png";
    }
  }
}

function botMoveChoice() {
  const options = ["paper", "rock", "scissor"];
  const randomNum = Math.trunc(Math.random() * 3);
  botChoice = options[randomNum];
  return botChoice;
}

function whoWins() {
  if (playerOneWins === 20) {
    winScreen.classList.remove("hidden");
  } else if (playerTwoWins === 20) {
    loseScreen.classList.remove("hidden");
  }
}

function gameLogic(playerOneMove, BotMove) {
  if (playerOneMove === "scissor" && BotMove === "rock") {
    return "Loss";
  } else if (playerOneMove === "scissor" && BotMove === "paper") {
    return "Win";
  } else if (playerOneMove === "scissor" && BotMove === "scissor") {
    return "Tie";
  } else if (playerOneMove === "paper" && BotMove === "rock") {
    return "Win";
  } else if (playerOneMove === "paper" && BotMove === "paper") {
    return "Tie";
  } else if (playerOneMove === "paper" && BotMove === "scissor") {
    return "Loss";
  } else if (playerOneMove === "rock" && BotMove === "rock") {
    return "Tie";
  } else if (playerOneMove === "rock" && BotMove === "paper") {
    return "Loss";
  } else if (playerOneMove === "rock" && BotMove === "scissor") {
    return "Win";
  }
}

//The Options for the User
playerOnePaper.addEventListener("click", function () {
  imageReplacement("Player One", "paper");
  playerOneChoice = "paper";
});
playerOneRock.addEventListener("click", function () {
  imageReplacement("Player One", "rock");
  playerOneChoice = "rock";
});
playerOneScissor.addEventListener("click", function () {
  imageReplacement("Player One", "scissor");
  playerOneChoice = "scissor";
});

playerOneConfirm.addEventListener("click", function () {
  if (playerOneChoice === null) {
    alert("Please choose Rock, Paper, or Scissor.");
  } else if (playerOneChoice !== null) {
    if (playerOneScore.textContent < 20 && playerTwoScore.textContent < 20) {
      botChoice = botMoveChoice();
      imageReplacement("Player Two", botChoice);
      let result = gameLogic(playerOneChoice, botChoice);
      if (result === "Loss") {
        playerTwoWins += 1;
        playerTwoScore.textContent = playerTwoWins;
      } else if (result === "Win") {
        playerOneWins += 1;
        playerOneScore.textContent = playerOneWins;
      } else if (result === "Tie") {
        playerOneWins += 1;
        playerTwoWins += 1;
        playerOneScore.textContent = playerOneWins;
        playerTwoScore.textContent = playerTwoWins;
      }
      whoWins();
    }
  }
});

//If we just have one modal to be opened we use the line below
btnOpenModal.addEventListener("click", openModal);
/*BUt let's say we have multiple buttons and we all want them to do the same thing, then we do:
btnsOpenModal.forEach(btn => {
  btn.addEventListener('click', openModal);
});

We use the line above for multiple as it loops through and then goes to each of the button element
separately to give it its own function when it gets clicked so it displays information
relevant to their button
*/
btnCloseModal.addEventListener("click", closeModal);
overlay.addEventListener("click", closeModal);
