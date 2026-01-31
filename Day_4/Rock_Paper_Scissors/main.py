import random  # Import the random module to let the computer make a random choice

# ASCII art for Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# ASCII art for Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# ASCII art for Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Put all the choices into a list so we can access them by index
game_images = [rock, paper, scissors]

# Ask the user for their choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# Check if the user's Input is valid
if user_choice < 0 or user_choice >= 3:
    print("You chose an invalid number. You lose.")
else:
    # Show the user's choice
    print("You chose:")
    print(game_images[user_choice])

    # Computer makes a random choice between 0 and 2
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Decide who wins using the game rules
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")  # Rock beats Scissors
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")  # Paper beats Rock
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")  # Scissors beats Paper
    else:
        print("Computer wins!")
