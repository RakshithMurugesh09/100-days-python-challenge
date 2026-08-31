import math


# ============================================
# DAY 31 PROJECT
# FLEXIBLE FUNCTION CALCULATOR
# ============================================


# ============================================
# GLOBAL VARIABLES
# ============================================

history = []


# ============================================
# MENU
# ============================================

def display_menu():
    """Display the main menu and return the user's choice."""

    print("\n========== FLEXIBLE CALCULATOR ==========")
    print("1. Add Numbers")
    print("2. Multiply Numbers")
    print("3. Calculate Average")
    print("4. Calculation Information")
    print("5. View History")
    print("6. Exit")

    user_choice = input("Enter your choice (1-6): ").strip()

    return user_choice


# ============================================
# INPUT FUNCTIONS
# ============================================

def get_numbers():
    """Get at least two valid numbers from the user."""

    numbers = []

    # Get the first two required numbers
    while len(numbers) < 2:
        try:
            number = float(input(f"Enter number {len(numbers) + 1}: "))
            numbers.append(number)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Ask whether the user wants to enter more numbers
    while True:
        choice = input("Do you want to add another number? (y/n): ").strip().lower()

        if choice == "n":
            return numbers

        elif choice == "y":
            while True:
                try:
                    number = float(input(f"Enter number {len(numbers) + 1}: "))
                    numbers.append(number)
                    break

                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        else:
            print("Invalid choice. Please enter 'y' or 'n'.")


# ============================================
# CALCULATION FUNCTIONS
# ============================================

def add_numbers(*numbers):
    """Add any number of numbers."""

    total = sum(numbers)

    return total


def multiply_numbers(*numbers):
    """Multiply any number of numbers."""

    product = math.prod(numbers)

    return product


def calculate_average(*numbers):
    """Calculate the average of any number of numbers."""

    if not numbers:
        return None

    average = sum(numbers) / len(numbers)

    return average


# ============================================
# NUMBER FORMATTING
# ============================================

def format_number(number):
    """Remove unnecessary decimal zeros from a number."""

    if isinstance(number, float) and number.is_integer():
        return int(number)

    return round(number, 2)


def format_numbers(numbers):
    """Convert a list of numbers into a readable string."""

    formatted_numbers = []

    for number in numbers:
        formatted_numbers.append(str(format_number(number)))

    return ", ".join(formatted_numbers)


# ============================================
# DISPLAY RESULT
# ============================================

def display_result(title, numbers, result):
    """Display the numbers and calculation result."""

    print(f"\n========== {title.upper()} ==========")
    print(f"Numbers : {format_numbers(numbers)}")
    print(f"Result  : {format_number(result)}")


# ============================================
# KWARGS FUNCTION
# ============================================

def calculation_info(**details):
    """Display calculation information using keyword arguments."""

    print("\n========== CALCULATION INFORMATION ==========")

    for key, value in details.items():
        label = key.replace("_", " ").title()

        if key == "numbers":
            value = format_numbers(value)

        elif key == "result":
            value = format_number(value)

        print(f"{label:<13}: {value}")


# ============================================
# SAVE CALCULATION TO HISTORY
# ============================================

def save_to_history(operation, numbers, result):
    """Store a completed calculation in history."""

    calculation = {
        "operation": operation,
        "numbers": numbers.copy(),
        "result": result
    }

    history.append(calculation)


# ============================================
# DISPLAY HISTORY
# ============================================

def display_history():
    """Display all previous calculations."""

    print("\n========== CALCULATION HISTORY ==========")

    if not history:
        print("No calculation history.")
        return

    for number, calculation in enumerate(history, start=1):
        print(f"\nCalculation #{number}")
        print(f"Operation : {calculation['operation']}")
        print(f"Numbers   : "
            f"{format_numbers(calculation['numbers'])}")
        print(f"Result    : "
            f"{format_number(calculation['result'])}")


# ============================================
# MAIN PROGRAM
# ============================================

def main():
    """Run the Flexible Calculator."""

    while True:
        choice = display_menu()

        # ====================================
        # ADDITION
        # ====================================

        if choice == "1":
            numbers = get_numbers()
            # *numbers unpacks the list
            result = add_numbers(*numbers)

            display_result(
                title="Add Numbers",
                numbers=numbers,
                result=result
            )

            save_to_history(
                operation="Addition",
                numbers=numbers,
                result=result
            )

        # ====================================
        # MULTIPLICATION
        # ====================================

        elif choice == "2":
            numbers = get_numbers()

            # *numbers unpacks the list
            result = multiply_numbers(*numbers)

            display_result(
                title="Multiply Numbers",
                numbers=numbers,
                result=result
            )

            save_to_history(
                operation="Multiplication",
                numbers=numbers,
                result=result
            )

        # ====================================
        # AVERAGE
        # ====================================

        elif choice == "3":
            numbers = get_numbers()

            # *numbers unpacks the list
            result = calculate_average(*numbers)

            display_result(
                title="Calculate Average",
                numbers=numbers,
                result=result
            )

            save_to_history(
                operation="Average",
                numbers=numbers,
                result=result
            )

        # ====================================
        # CALCULATION INFORMATION
        # ====================================

        elif choice == "4":
            if not history:
                print(
                    "\nNo calculation information available."
                )
                print("Please perform a calculation first.")

            else:
                latest_calculation = history[-1]

                calculation_info(
                    operation=latest_calculation["operation"],
                    numbers=latest_calculation["numbers"],
                    number_count=len(
                        latest_calculation["numbers"]
                    ),
                    result=latest_calculation["result"]
                )

        # ====================================
        # HISTORY
        # ====================================

        elif choice == "5":
            display_history()

        # ====================================
        # EXIT
        # ====================================

        elif choice == "6":
            print(
                "\nThank you for using "
                "Flexible Calculator!"
            )
            break

        # ====================================
        # INVALID CHOICE
        # ====================================

        else:
            print(
                "\nInvalid choice. "
                "Please select a number from 1 to 6."
            )


# ============================================
# PROGRAM START
# ============================================

if __name__ == "__main__":
    main()