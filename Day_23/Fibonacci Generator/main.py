# ============================================
# Day 23 Project
# Fibonacci Generator
# ============================================


def display_menu():
    """
    Display the main menu.

    Returns:
        str: User's menu choice.
    """

    # TODO:
    # Display:
    # 1. Generate Fibonacci Sequence
    # 2. Exit

    # TODO:
    # Return user's choice

    pass


def get_number_of_terms():
    """
    Ask the user how many Fibonacci numbers to generate.

    Returns:
        int: Number of terms.
    """

    # TODO:
    # Keep asking until user enters
    # a valid positive integer.

    pass


def fibonacci_generator(number_of_terms):
    """
    Generator function.

    Args:
        number_of_terms (int)

    Yields:
        int: Next Fibonacci number.
    """

    # TODO:
    # Initialize the first two numbers.

    # TODO:
    # Generate Fibonacci numbers
    # one at a time using yield.

    pass


def display_sequence(fibonacci_numbers):
    """
    Display all generated Fibonacci numbers.

    Args:
        fibonacci_numbers (list)
    """

    # TODO:
    # Print heading.

    # TODO:
    # Display every number neatly.

    pass


def display_statistics(fibonacci_numbers):
    """
    Display sequence statistics.

    Args:
        fibonacci_numbers (list)
    """

    # TODO:
    # Display:
    # Total Numbers
    # Sum
    # Largest Number

    pass


def main():
    """
    Main program.
    """

    while True:

        choice = display_menu()

        if choice == "1":

            # TODO:
            # Get number of terms.

            # TODO:
            # Create an empty list.

            # TODO:
            # Loop through the generator.

            # TODO:
            # Store each generated number.

            # TODO:
            # Display the sequence.

            # TODO:
            # Display statistics.

            pass

        elif choice == "2":

            # TODO:
            # Print goodbye message.

            break

        else:

            # TODO:
            # Invalid menu choice.

            pass


# ============================================
# Program Starts Here
# ============================================

if __name__ == "__main__":
    main()