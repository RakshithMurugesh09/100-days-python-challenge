# ============================================
# Day 24 Project
# Prime Number Finder
# ============================================


def display_menu():
    """Display the main menu."""

    print("\n========== PRIME NUMBER FINDER ==========")
    print("1. Check Prime Number")
    print("2. Find Primes in Range")
    print("3. Exit")

    # TODO:
    # Get the user's menu choice.
    # Return the choice.



def get_number():
    """Get a valid integer from the user."""

    # TODO:
    # Ask the user to enter a number.
    # Use try/except to handle invalid input.
    # Return the valid integer.


def get_range():
    """Get a valid start and end range."""

    # TODO:
    # Ask for start number.
    # Ask for end number.
    # Validate:
    # - Both are integers.
    # - Start <= End.
    # Return start and end.


def is_prime(number):
    """Return True if number is prime, otherwise False."""

    # TODO:
    # If number is less than 2,
    # return False.

    # TODO:
    # Check divisibility.

    # TODO:
    # Return True if prime.


def check_single_prime():
    """Check whether one number is prime."""

    # TODO:
    # Get a number.
    # Call is_prime().
    # Display whether it is prime.


def find_primes():
    """Find all prime numbers in a range."""

    # TODO:
    # Get start and end.

    # TODO:
    # Create a list comprehension
    # that stores every prime number.

    # Example structure only:
    #
    # prime_numbers = [
    #     ...
    # ]

    # TODO:
    # If no prime numbers exist,
    # display a message.

    # TODO:
    # Otherwise:
    # Print every prime number.

    # TODO:
    # Call display_statistics().


def display_statistics(prime_numbers):
    """Display statistics about prime numbers."""

    # TODO:
    # Display:
    # Total primes
    # Smallest prime
    # Largest prime

    # BONUS:
    # Sum
    # Average


def main():
    """Main program."""

    while True:

        choice = display_menu()

        if choice == "1":

            # TODO:
            # Check a single prime number.
            pass

        elif choice == "2":

            # TODO:
            # Find primes in a range.
            pass

        elif choice == "3":

            print("\n👋 Thank you for using Prime Number Finder.")
            break

        else:

            print("\n❌ Invalid choice. Please try again.")


# ============================================
# Program Starts Here
# ============================================

main()