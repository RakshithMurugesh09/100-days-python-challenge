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
    """Display the main menu and return user's choice."""

    print("\n========== FLEXIBLE CALCULATOR ==========")
    print("1. Add Numbers")
    print("2. Multiply Numbers")
    print("3. Calculate Average")
    print("4. Calculation Information")
    print("5. View History")
    print("6. Exit")

    # TODO:
    # Get the user's choice
    # Handle invalid input
    # Return the choice

    pass


# ============================================
# INPUT FUNCTIONS
# ============================================

def get_numbers():
    """Get multiple numbers from the user."""

    # TODO:
    # Ask the user to enter multiple numbers
    #
    # Example:
    # Enter numbers: 10 20 30 40
    #
    # Convert each value into a number.
    #
    # If the user enters invalid data,
    # display an error and ask again.
    #
    # Return the numbers as a list.

    pass


# ============================================
# CALCULATION FUNCTIONS
# ============================================

def add_numbers(*numbers):
    """Add any number of numbers."""

    # TODO:
    # Use *numbers
    # Calculate the total
    # Return the result

    pass


def multiply_numbers(*numbers):
    """Multiply any number of numbers."""

    # TODO:
    # Use *numbers
    # Multiply all values
    # Return the result

    pass


def calculate_average(*numbers):
    """Calculate the average of any number of numbers."""

    # TODO:
    # Calculate the average
    # Make sure you don't divide by zero
    # Return the result

    pass


# ============================================
# KWARGS FUNCTION
# ============================================

def calculation_info(**details):
    """Display calculation information."""

    print("\n========== CALCULATION INFORMATION ==========")

    # TODO:
    # Use details.items()
    # Display every key and value
    #
    # Example:
    #
    # Operation : Addition
    # Numbers   : 3
    # Result    : 60

    pass


# ============================================
# HISTORY
# ============================================

def display_history():
    """Display all previous calculations."""

    # TODO:
    # Check whether history is empty.
    #
    # If empty:
    #     Display "No calculation history."
    #
    # Otherwise:
    #     Loop through history
    #     Display operation
    #     Display numbers
    #     Display result

    pass


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

            # TODO:
            # Get numbers
            # Call add_numbers(*numbers)
            # Display result
            # Store calculation in history

            pass


        # ====================================
        # MULTIPLICATION
        # ====================================

        elif choice == "2":

            # TODO:
            # Get numbers
            # Call multiply_numbers(*numbers)
            # Display result
            # Store calculation in history

            pass


        # ====================================
        # AVERAGE
        # ====================================

        elif choice == "3":

            # TODO:
            # Get numbers
            # Call calculate_average(*numbers)
            # Display result
            # Store calculation in history

            pass


        # ====================================
        # CALCULATION INFORMATION
        # ====================================

        elif choice == "4":

            # TODO:
            # Ask the user for the information
            # OR use information from the latest
            # calculation.
            #
            # Call:
            #
            # calculation_info(
            #     operation=...,
            #     numbers=...,
            #     result=...
            # )

            pass


        # ====================================
        # HISTORY
        # ====================================

        elif choice == "5":

            display_history()


        # ====================================
        # EXIT
        # ====================================

        elif choice == "6":

            print("\n👋 Thank you for using Flexible Calculator!")
            break


        # ====================================
        # INVALID CHOICE
        # ====================================

        else:

            print("\n❌ Invalid choice. Please select 1-6.")


# ============================================
# PROGRAM START
# ============================================

if __name__ == "__main__":
    main()