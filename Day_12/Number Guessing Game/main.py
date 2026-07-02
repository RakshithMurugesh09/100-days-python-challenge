# Import the random module to generate a random number and import logo
import random
from art import logo

# Constants for the number of attempts allowed
EASY_TURNS = 10
HARD_TURNS = 5

# Logo
print(logo)

# Welcome message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number between 1 and 100
answer = random.randint(1, 100)

# Ask the user to choose a difficulty level
difficulty = input("Choose difficulty (easy/hard): ")

# Set the number of turns based on the chosen difficulty
if difficulty == "easy":
    turns = EASY_TURNS
else:
    turns = HARD_TURNS

# Continue the game while the player still has turns left
while turns > 0:

    # Display remaining attempts
    print(f"Attempts left: {turns}")

    # Get the user's guess
    guess = int(input("Make a guess: "))

    # Check if the guess is correct
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        break

    # Tell the user if the guess is too high
    elif guess > answer:
        print("Too high.")

    # Tell the user if the guess is too low
    else:
        print("Too low.")

    # Reduce the remaining turns by 1
    turns -= 1

# If the player runs out of attempts, reveal the answer
if turns == 0:
    print(f"You lose. The answer was {answer}.")