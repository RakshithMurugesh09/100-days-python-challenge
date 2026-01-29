# Welcome message for the player
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

# First decision prompt: Choose a direction (left or right)
direction_choice = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n= ')

# Check if player chooses 'left'
if direction_choice.lower() == 'left':
    # Second decision prompt: Choose an action (wait or swim)
    lake_action = input(
        'You come to a lake. There is an island in the middle of the lake.\n'
        'Type "wait" to wait for a boat. Type "swim" to swim across.\n= '
    )

    # Check if player chooses 'wait'
    if lake_action.lower() == "wait":
        # Third decision prompt: Choose a door color (red, yellow, or blue)
        door_color_choice = input(
            "You arrive at the island unharmed. There are 3 doors: one red, one yellow, and one blue.\n"
            "Which colour do you choose?\n= "
        )

        # Check if player chooses 'red'
        if door_color_choice.lower() == "red":
            # Player loses — game over a message for red door
            print("Game over! You entered the red door and were burned by fire.")

        # Check if player chooses 'yellow'
        elif door_color_choice.lower() == "yellow":
            # Player wins — treasure found message
            print("Congratulations! You found the treasure and won the game!")

        # Check if player chooses 'blue'
        elif door_color_choice.lower() == "blue":
            # Player loses — game over a message for blue door
            print("Game over! You entered the blue door and were eaten by beasts.")

        # If a player chooses any other door color
        else:
            # Invalid option — game over a message
            print("Invalid option — game over.")

    # Check if player chooses 'swim'
    elif lake_action.lower() == "swim":
        # Player loses — attacked by trout game over a message
        print("Game over! You were attacked by trout while swimming.")

    # If a player chooses anything other than 'wait' or 'swim'
    else:
        # Invalid option — game over a message
        print("Invalid option — game over.")

# Check if player chooses 'right'
elif direction_choice.lower() == "right":
    # Player loses — falls into a hole game over a message
    print("Game over! You fell into a hole.")

# If a player chooses anything other than 'left' or 'right'
else:
    # Invalid option — game over a message
    print("Invalid option — game over.")
