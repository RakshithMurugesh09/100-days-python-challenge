# Custom Exception
class InvalidNumberError(Exception):
    """Raised when the user enters an invalid number."""
    print("Error alert")
    pass


def get_numbers():
    """
    Get two numbers from the user.
    Validate the input.
    Raise custom exception if needed.
    Return both numbers.
    """
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        return number1, number2

    except ValueError as e:
        raise InvalidNumberError("Please enter valid numbers.") from e


def add(n1, n2):
    """
    Perform addition.
    Handle exceptions.
    """
    return n1 + n2



def subtract(n1, n2):
    """
    Perform subtraction.
    Handle exceptions.
    """
    return n1 - n2



def multiply(n1, n2):
    """
    Perform multiplication.
    Handle exceptions.
    """
    return n1 * n2



def divide(n1, n2):
    """
    Perform division.
    Handle division by zero.
    Handle other exceptions.
    """
    try:
        return n1 / n2

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except Exception as e:
        print(f"Error during division: {e}")


def display_menu():
    """
    Print the calculator menu.
    """
    print("\n===== ROBUST CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")


def main():
    """
    Display the menu in a loop.
    Get the user's choice.
    Call the appropriate function.
    Handle invalid menu choices.
    Exit when requested.
    """

    while True:
        display_menu()

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator. Goodbye!")
            break

        try:
            n1, n2 = get_numbers()

            if choice == "1":
                result = add(n1, n2)

            elif choice == "2":
                result = subtract(n1, n2)

            elif choice == "3":
                result = multiply(n1, n2)

            elif choice == "4":
                result = divide(n1, n2)

            else:
                print("Invalid menu choice.")
                continue

        except InvalidNumberError as e:
            print(f"Error: {e}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")

        else:
            print(f"Result: {result}")

        finally:
            print("-" * 35)
            print("Operation completed.\n")


if __name__ == "__main__":
    main()