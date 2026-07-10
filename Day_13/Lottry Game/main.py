import random


def display_logo():
    """Display game logo."""
    print("=" * 40)
    print("         SIMPLE LOTTERY GAME")
    print("=" * 40)


def is_valid(number, numbers_list):
    """
    Validate user input.
    Returns True if invalid, False if valid.
    """
    if number < 1 or number > 50:
        print("❌ Enter a number between 1 and 50.")
        return True

    if number in numbers_list:
        print("❌ Number already entered.")
        return True

    return False


def get_user_numbers():
    """
    Get 6 unique numbers from the user.
    """
    user_numbers = []

    print("\nEnter 6 unique numbers between 1 and 50:\n")

    while len(user_numbers) < 6:
        try:
            number = int(input(f"Enter number {len(user_numbers) + 1}: "))

            if is_valid(number, user_numbers):
                continue

            user_numbers.append(number)

        except ValueError:
            print("❌ Please enter a valid integer.")

    return sorted(user_numbers)


def generate_lottery_numbers():
    """
    Generate 6 unique lottery numbers.
    """
    return sorted(random.sample(range(1, 51), 6))


def find_matches(user_numbers, lottery_numbers):
    """
    Find matching numbers.
    """
    return sorted(set(user_numbers) & set(lottery_numbers))


def display_results(user_numbers, lottery_numbers, matched_numbers):
    """
    Display game results.
    """
    print("\n========== RESULTS ==========")
    print(f"Your Numbers    : {user_numbers}")
    print(f"Lottery Numbers : {lottery_numbers}")
    print(f"Matched Numbers : {matched_numbers}")
    print(f"Total Matches   : {len(matched_numbers)}")
    print("=============================\n")

    return len(matched_numbers)


def check_prize(match_count):
    """
    Display prize based on number of matches.
    """
    prizes = {
        3: "🎉 Consolation Prize",
        4: "🥉 Third Prize",
        5: "🥈 Second Prize",
        6: "🥇 JACKPOT!"
    }

    print(prizes.get(match_count, "❌ Better luck next time!"))


def play_again():
    """
    Ask whether the user wants to play again.
    """
    while True:
        choice = input("\nPlay again? (Y/N): ").strip().lower()

        if choice in ["y", "yes"]:
            return True

        if choice in ["n", "no"]:
            return False

        print("Please enter Y or N.")


def main():
    """
    Main game loop.
    """
    display_logo()

    while True:
        user_numbers = get_user_numbers()
        lottery_numbers = generate_lottery_numbers()

        matched_numbers = find_matches(
            user_numbers,
            lottery_numbers
        )

        match_count = display_results(
            user_numbers,
            lottery_numbers,
            matched_numbers
        )

        check_prize(match_count)

        if not play_again():
            print("\n👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()