
# 📘 Assignment: Games in Python

## 🎯 Objetivo

Create a classic Hangman word-guessing game where players try to discover a hidden word by guessing letters one at a time. You'll practice string manipulation, loops, conditionals, and user input while building an engaging interactive game.

## 📝 Tarefas

### 🛠️ Setup & Word List

#### Description

Create a word list and set up the basic game structure with proper initialization and user instructions.

#### Requirements

Completed program should:

- Define a list of at least 5 different words for the game
- Randomly select a word for the player to guess using `random.choice()`
- Display clear game instructions and rules to the user
- Initialize game variables (attempts remaining, guessed letters, etc.)

### 🛠️ Implement Game Logic

#### Description

Build the core Hangman gameplay mechanics with proper input validation and game state tracking.

#### Requirements

Completed program should:

- Display word progress using underscores (_) for unguessed letters
- Accept and validate single letter guesses from the user
- Provide feedback whether each guess is correct or incorrect
- Track and display the number of incorrect attempts remaining
- End the game with appropriate win/lose messages and reveal the word
