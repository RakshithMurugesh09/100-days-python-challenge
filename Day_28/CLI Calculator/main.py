import sys


def validate_arguments():
    """
    Validate the number of command-line arguments.

    Expected format:
    python calculator.py <number1> <operator> <number2>
    """

    # TODO:
    # Check whether the user provided exactly 3 arguments
    # apart from the program name.

    # Hint:
    # len(sys.argv) should be ______


def convert_numbers():
    """
    Convert the first and third command-line arguments
    from strings into numbers.
    """

    # TODO:
    # Get the first number from sys.argv
    # Get the second number from sys.argv

    # TODO:
    # Convert both values using float()

    # TODO:
    # Handle ValueError

    pass


def calculate(first_number, operator, second_number):
    """
    Perform calculation based on the operator.
    """

    # TODO:
    # Check the operator.

    # if operator == "+":
    #     ...

    # elif operator == "-":
    #     ...

    # elif operator == "*":
    #     ...

    # elif operator == "/":
    #     ...

    # TODO:
    # Before division, check whether second_number is 0.

    # TODO:
    # If operator is unsupported, display an error.

    pass


def display_result(result):
    """
    Display the calculation result.
    """

    # TODO:
    # Print the result in a user-friendly format.

    pass


def main():
    """
    Main program.
    """

    # Step 1:
    # Validate command-line arguments

    # Step 2:
    # Convert numbers

    # Step 3:
    # Get operator from sys.argv

    # Step 4:
    # Calculate result

    # Step 5:
    # Display result

    pass


if __name__ == "__main__":
    main()