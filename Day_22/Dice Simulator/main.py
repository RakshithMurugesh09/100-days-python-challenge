import random

all_rolls = []


def display_menu():
    """Display menu and return user's choice."""

    print("\n========== DICE SIMULATOR ==========")
    print("1. Roll One Die")
    print("2. Roll Multiple Dice")
    print("3. View Statistics")
    print("4. Exit")

    try:
        return int(input("Enter your choice: "))
    except ValueError:
        return 0


def roll_one_die():
    """Roll a single die."""

    roll = random.randint(1, 6)

    print(f"\n🎲 You rolled: {roll}")

    all_rolls.append(roll)


def roll_multiple_dice():
    """Roll multiple dice."""

    try:
        number_of_rolls = int(input("How many dice would you like to roll? "))

        if number_of_rolls <= 0:
            print("❌ Number of rolls must be greater than 0.")
            return

        rolls = []

        for _ in range(number_of_rolls):
            roll = random.randint(1, 6)

            rolls.append(roll)
            all_rolls.append(roll)

        print(f"\n🎲 You rolled: {rolls}")
        print(f"📊 Total Value: {sum(rolls)}")

    except ValueError:
        print("❌ Please enter a valid number.")


def view_statistics():
    """Display roll statistics."""

    if not all_rolls:
        print("📭 No rolls have been made yet.")
        return

    print("\n========== STATISTICS ==========")
    print(f"🎲 Total Rolls   : {len(all_rolls)}")
    print(f"🎯 Last Roll     : {all_rolls[-1]}")
    print(f"🔺 Highest Roll  : {max(all_rolls)}")
    print(f"🔻 Lowest Roll   : {min(all_rolls)}")
    print(f"📈 Average Roll  : {sum(all_rolls) / len(all_rolls):.2f}")


def main():
    """Main program."""

    while True:

        choice = display_menu()

        if choice == 1:
            roll_one_die()

        elif choice == 2:
            roll_multiple_dice()

        elif choice == 3:
            view_statistics()

        elif choice == 4:
            print("👋 Thank you for playing!")
            break

        else:
            print("❌ Please enter a number between 1 and 4.")


main()