# Day 14 - Higher Lower Game

import random

from art import logo, vs
from game_data import data

print(logo)
print("Welcome to the Higher Lower Game!")

score = 0


def display_player(player):
    """Display player information."""
    print(
        f"{player['name']}, "
        f"a {player['description']}, "
        f"from {player['country']}"
    )


def compare(player1, player2):
    """Return True if player1 has more followers."""
    return player1["follower_count"] > player2["follower_count"]


# Select the first player
player_a = random.choice(data)

while True:

    # Select a different player
    player_b = random.choice(data)

    while player_a == player_b:
        player_b = random.choice(data)

    print("\nCompare A:")
    display_player(player_a)

    print(vs)

    print("Against B:")
    display_player(player_b)

    user_input = input(
        "\nWho has more followers? Type 'A' or 'B': "
    ).upper()

    # User chose A
    if user_input == "A" and compare(player_a, player_b):
        score += 1
        print(f"\n✅ Correct! Current score: {score}")

    # User chose B
    elif user_input == "B" and compare(player_b, player_a):
        score += 1
        player_a = player_b
        print(f"\n✅ Correct! Current score: {score}")

    else:
        print(f"\n❌ Wrong! Final score: {score}")
        break