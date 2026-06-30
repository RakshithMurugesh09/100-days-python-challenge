import random
from art import logo

# -----------------------------
# BLACKJACK GAME
# -----------------------------

# Card values
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


# ----------------------------------------
# Draw a random card
# ----------------------------------------
def deal_card():
    """
    Returns one random card from the deck.
    11 represents an Ace.
    """
    return random.choice(cards)


# ----------------------------------------
# Calculate score
# ----------------------------------------
def calculate_score(hand):
    """
    Calculates the score of a hand.

    Blackjack:
    Ace + 10 = 21 using only two cards.
    Returns 0 to represent Blackjack.
    """

    score = sum(hand)

    # Blackjack
    if score == 21 and len(hand) == 2:
        return 0

    # Convert Ace from 11 to 1 if needed
    while 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score


# ----------------------------------------
# Display cards
# ----------------------------------------
def show_cards(player_cards,
               computer_cards,
               player_score,
               computer_score,
               reveal_computer=False):
    """
    Prints the current game status.
    """

    print("\n----------------------------")

    print(f"Your cards: {player_cards}")
    print(f"Your score: {player_score}")

    if reveal_computer:
        print(f"Computer cards: {computer_cards}")
        print(f"Computer score: {computer_score}")
    else:
        print(f"Computer first card: {computer_cards[0]}")

    print("----------------------------")


# ----------------------------------------
# Decide winner
# ----------------------------------------
def compare(player_score, computer_score):

    if player_score == computer_score:
        return "It's a Draw!"

    if player_score == 0:
        return "Blackjack! You Win!"

    if computer_score == 0:
        return "Computer has Blackjack. You Lose."

    if player_score > 21:
        return "You went over 21. You Lose."

    if computer_score > 21:
        return "Computer went over 21. You Win!"

    if player_score > computer_score:
        return "You Win!"

    return "Computer Wins."


# ----------------------------------------
# Start one game
# ----------------------------------------
def play_blackjack():

    # Give two cards each
    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        show_cards(
            player_cards,
            computer_cards,
            player_score,
            computer_score,
            False,
        )

        # End conditions
        if (
            player_score == 0
            or computer_score == 0
            or player_score > 21
        ):
            game_over = True
            break

        choice = input("Type 'h' to Hit or 's' to Stand: ").lower()

        if choice == "h":
            player_cards.append(deal_card())
        else:
            game_over = True

    # Dealer plays only if player hasn't busted
    if player_score <= 21 and player_score != 0:

        computer_score = calculate_score(computer_cards)

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    # Final scores
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    show_cards(
        player_cards,
        computer_cards,
        player_score,
        computer_score,
        True,
    )

    print(compare(player_score, computer_score))


# ----------------------------------------
# Main Program
# ----------------------------------------

print(logo)
while True:

    start = input("\nPlay Blackjack? (y/n): ").lower()

    if start != "y":
        print("Thanks for playing!")
        break

    play_blackjack()