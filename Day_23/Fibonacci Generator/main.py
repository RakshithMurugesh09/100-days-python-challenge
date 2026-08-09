# ============================================
# Day 23 Project
# Fibonacci Generator
# ============================================

def display_menu():
    print("\n========== Fibonacci Generator ==========")
    print("1. Generate Fibonacci Sequence")
    print("2. Exit")

    return input("Enter your choice: ").strip()


def get_number_of_terms():
    while True:
        try:
            number_of_terms = int(input("Enter number of terms: "))

            if number_of_terms > 0:
                return number_of_terms

            print("Please enter a positive number.")

        except ValueError:
            print("Invalid input. Enter a valid number.")


def fibonacci_generator(number_of_terms):

    first_number = 0
    second_number = 1

    for _ in range(number_of_terms):
        yield first_number
        first_number, second_number = (second_number, first_number + second_number)


def display_sequence(fibonacci_numbers):

    print("\n========== Fibonacci Sequence ==========")

    for number in fibonacci_numbers:
        print(number)


def display_statistics(fibonacci_numbers):

    print("\n========== Statistics ==========")
    print(f"Total Numbers : {len(fibonacci_numbers)}")
    print(f"Sum           : {sum(fibonacci_numbers)}")
    print(f"Largest Number: {max(fibonacci_numbers)}")


def main():

    while True:

        choice = display_menu()

        if choice == "1":

            number_of_terms = get_number_of_terms()

            fibonacci_numbers = []

            for number in fibonacci_generator(number_of_terms):
                fibonacci_numbers.append(number)

            display_sequence(fibonacci_numbers)

            display_statistics(fibonacci_numbers)

        elif choice == "2":

            print("\nThank you for using Fibonacci Generator. Goodbye!")
            break

        else:

            print("\nInvalid choice. Please select 1 or 2.")


# ============================================
# Program Starts Here
# ============================================

main()