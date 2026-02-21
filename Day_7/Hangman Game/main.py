import random

from asciiart import hangman_logo, stages
from hangman_words import words

# Number of lives the player has
life = 6


# Randomly choose a word and convert to lowercase
chosen_word = random.choice(words).lower()
print("Welcome to Hangman!")
print(hangman_logo)
# For debugging: Show the answer (comment out for real play)
print(f"(DEBUG) The chosen word is: {chosen_word}")

# Underscores for each letter in the chosen word
display = ["_" for _ in chosen_word]

# To control the game loop
game_running = True

while game_running:
    print("\n" + stages[life])    # Show the current hangman
    print("Current word: " + " ".join(display))
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in display:
        print(f"You already revealed the letter '{guess_letter}'. Try another letter!")
    elif guess_letter in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if letter == guess_letter:
                display[idx] = guess_letter
        print(f"Good job! '{guess_letter}' is in the word.")

        if "_" not in display:
            print("\nCongratulations! You guessed the word:", chosen_word)
            game_running = False
    else:
        print(f"Sorry, the letter '{guess_letter}' is not in the word.")
        life -= 1
        print(f"Lives remaining: {life}/6")
        if life == 0:
            print(stages[0])
            print("\nYou've run out of lives. Game Over!")
            print(f"The word was: {chosen_word}")
            game_running = False
