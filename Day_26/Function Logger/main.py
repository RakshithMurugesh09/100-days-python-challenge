from functools import wraps


def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("\n========== LOGGER ==========")
        print(f"Function : {function.__name__.title()}")
        print("Status   : Started")

        result = function(*args, **kwargs)

        print("Status   : Finished")
        print("============================\n")

        return result

    return wrapper


@logger
def add(first_number, second_number):
    return first_number + second_number


@logger
def subtract(first_number, second_number):
    return first_number - second_number


@logger
def multiply(first_number, second_number):
    return first_number * second_number


@logger
def divide(first_number, second_number):
    if second_number == 0:
        print("❌ Cannot divide by zero.")
        return None

    return first_number / second_number


def display_menu():
    print("\n========== FUNCTION LOGGER ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        return int(input("\nEnter your choice: "))
    except ValueError:
        return 0


def get_numbers():
    while True:
        try:
            first_number = float(input("Enter First Number : "))
            second_number = float(input("Enter Second Number: "))
            return first_number, second_number

        except ValueError:
            print("❌ Please enter valid numbers.")


def main():

    while True:

        choice = display_menu()

        if choice == 5:
            print("\nThank you for using Function Logger.")
            break

        if choice not in [1, 2, 3, 4]:
            print("❌ Invalid choice.")
            continue

        first_number, second_number = get_numbers()

        if choice == 1:
            result = add(first_number, second_number)

        elif choice == 2:
            result = subtract(first_number, second_number)

        elif choice == 3:
            result = multiply(first_number, second_number)

        elif choice == 4:
            result = divide(first_number, second_number)

        if result is not None:
            print(f"Result : {result}")


main()