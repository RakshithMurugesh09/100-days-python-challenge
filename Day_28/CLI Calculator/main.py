import sys


def validate_arguments():
    """
    Validate command-line arguments.

    Expected format:
    python calculator.py <number1> <operator> <number2>
    """
    if len(sys.argv) != 4:
        sys.exit("Usage: python calculator.py <num1> <operator> <num2>")


def convert_numbers():
    """
    Convert command-line arguments to numbers.
    """
    try:
        first_number = float(sys.argv[1])
        second_number = float(sys.argv[3])
        return first_number, second_number
    except ValueError:
        sys.exit("Error: Numbers must be valid.")


def calculate(first_number, operator, second_number):
    """
    Perform calculation based on operator.
    """
    if operator == "+":
        return first_number + second_number

    elif operator == "-":
        return first_number - second_number

    elif operator == "*":
        return first_number * second_number

    elif operator == "/":
        if second_number == 0:
            sys.exit("Error: Cannot divide by zero.")
        return first_number / second_number

    else:
        sys.exit("Error: Invalid operator. Use +, -, *, /")


def display_result(result):
    """
    Display result.
    """
    print(f"Result: {result}")


def main():
    validate_arguments()

    first_number, second_number = convert_numbers()

    operator = sys.argv[2]

    result = calculate(first_number,operator,second_number)

    display_result(result)


if __name__ == "__main__":
    main()