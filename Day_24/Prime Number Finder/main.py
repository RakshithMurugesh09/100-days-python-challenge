def display_menu():
    """Display the main menu."""
    print("\n========== PRIME NUMBER FINDER ==========")
    print("1. Check Prime Number")
    print("2. Find Primes in Range")
    print("3. Exit")

    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("\n❌ Invalid choice. Please enter a number.")


def get_number():
    """Get a valid positive integer from the user."""
    while True:
        try:
            user_number = int(input("Enter a number: "))

            if user_number > 0:
                return user_number

            print("\n❌ Please enter a positive integer.")

        except ValueError:
            print("\n❌ Invalid input. Please enter a valid integer.")


def get_range():
    """Get a valid start and end range."""
    print("\nEnter Range:")

    start_number = get_number()

    while True:
        print("Enter ending number:")
        end_number = get_number()

        if end_number >= start_number:
            return start_number, end_number

        print("\n❌ End range should be greater than or equal to start range.")


def is_prime(number):
    """Return True if number is prime, otherwise False."""

    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


def check_single_prime():
    """Check whether one number is prime."""

    number = get_number()

    if is_prime(number):
        print(f"\n✅ {number} is a Prime Number.")
    else:
        print(f"\n❌ {number} is NOT a Prime Number.")


def find_primes():
    """Find all prime numbers in a range."""

    start, end = get_range()

    prime_numbers = [
        number
        for number in range(start, end + 1)
        if is_prime(number)
    ]

    if not prime_numbers:
        print("\n❌ No prime numbers found in the given range.")
        return

    print("\n✅ Prime Numbers:")
    print(*prime_numbers, sep=", ")

    display_statistics(prime_numbers)


def display_statistics(prime_numbers):
    """Display statistics about prime numbers."""

    print("\n========== STATISTICS ==========")
    print(f"Total Primes   : {len(prime_numbers)}")
    print(f"Smallest Prime : {min(prime_numbers)}")
    print(f"Largest Prime  : {max(prime_numbers)}")
    print(f"Sum            : {sum(prime_numbers)}")
    print(f"Average        : {sum(prime_numbers) / len(prime_numbers):.2f}")


def main():
    """Main program."""

    while True:

        choice = display_menu()

        if choice == 1:
            check_single_prime()

        elif choice == 2:
            find_primes()

        elif choice == 3:
            print("\n👋 Thank you for using Prime Number Finder.")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")




main()