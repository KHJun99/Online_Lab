// Element selection
const player1Img = document.querySelector('#player1-img');
const player2Img = document.querySelector('#player2-img');
const countA = document.querySelector('.countA');
const countB = document.querySelector('.countB');
const scissorsButton = document.querySelector('#scissors-button');
const rockButton = document.querySelector('#rock-button');
const paperButton = document.querySelector('#paper-button');
const modal = document.querySelector('.modal');
const modalContent = document.querySelector('.modal-content');

// Initialize counts
let count1 = 0;
let count2 = 0;

// Image path mapping
const imgMap = {
  'scissors': './img/scissors.png',
  'rock': './img/rock.png',
  'paper': './img/paper.png'
};

// playGame function: receives player1 and player2 choices and returns the game result
function playGame(player1, player2) {
  // Rock, Paper, Scissors win/lose determination
  if (player1 === player2) {
    return 0; // Draw
  }

  // When player1 chooses scissors
  if (player1 === 'scissors') {
    if (player2 === 'rock') {
      count2++;
      return 2; // player2 wins
    } else if (player2 === 'paper') {
      count1++;
      return 1; // player1 wins
    }
  }

  // When player1 chooses rock
  if (player1 === 'rock') {
    if (player2 === 'scissors') {
      count1++;
      return 1; // player1 wins
    } else if (player2 === 'paper') {
      count2++;
      return 2; // player2 wins
    }
  }

  // When player1 chooses paper
  if (player1 === 'paper') {
    if (player2 === 'rock') {
      count1++;
      return 1; // player1 wins
    } else if (player2 === 'scissors') {
      count2++;
      return 2; // player2 wins
    }
  }

  return 0; // Draw for other cases
}

// buttonClickHandler function: handles the action when the button is clicked
function buttonClickHandler(choice) {
  // Disable scissors, rock, paper buttons
  scissorsButton.disabled = true;
  rockButton.disabled = true;
  paperButton.disabled = true;

  // Set player1 image
  player1Img.src = imgMap[choice];

  // Store possible choices in an array
  const choices = ['scissors', 'rock', 'paper'];

  // Randomly select an index to determine opponent's choice
  const randomIndex = Math.floor(Math.random() * choices.length);
  const player2Choice = choices[randomIndex];

  // Use setInterval function to periodically change the image on screen
  let currentIndex = 0;
  const interval = setInterval(() => {
    player2Img.src = imgMap[choices[currentIndex % 3]];
    currentIndex++;
  }, 100); // Change image every 100ms

  // Use setTimeout function to display result after 3 seconds
  setTimeout(() => {
    // Stop setInterval
    clearInterval(interval);

    // Set player2's final choice image
    player2Img.src = imgMap[player2Choice];

    // Call playGame function to get game result
    const result = playGame(choice, player2Choice);

    // Update counts
    countA.textContent = count1;
    countB.textContent = count2;

    // Display result message
    let resultMessage = '';
    if (result === 1) {
      resultMessage = 'Player 1 Wins!';
    } else if (result === 2) {
      resultMessage = 'Player 2 Wins!';
    } else {
      resultMessage = "It's a tie!";
    }

    // Display modal
    modalContent.textContent = resultMessage;
    modal.style.display = 'flex';

    // Re-enable buttons
    scissorsButton.disabled = false;
    rockButton.disabled = false;
    paperButton.disabled = false;
  }, 3000); // Execute after 3 seconds
}

// Register click event handlers for scissors, rock, paper buttons
scissorsButton.addEventListener('click', () => {
  buttonClickHandler('scissors');
});

rockButton.addEventListener('click', () => {
  buttonClickHandler('rock');
});

paperButton.addEventListener('click', () => {
  buttonClickHandler('paper');
});

// Close modal when clicked
modal.addEventListener('click', () => {
  modal.style.display = 'none';
});
