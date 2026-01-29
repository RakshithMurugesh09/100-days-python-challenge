# Welcome message for the Odd or Even Number Calculator
print("Welcome to the Odd or Even Number Calculator!")

# Ask the user to enter a whole number (integer)
# Convert the Input to an integer using int()
user_number = int(input("Please enter an integer number: "))

# Check if the number is even and positive
if user_number % 2 == 0 and user_number >= 0:
    # If the number is divisible by 2 and greater than or equal to 0, it's a positive even number
    print(f"\nThe number '{user_number}' is a Positive even number.")

# Check if the number is even and negative
elif user_number % 2 == 0 and user_number < 0:
    # If the number is divisible by 2 and less than 0, it's a negative even number
    print(f"\nThe number '{user_number}' is a Negative even number.")

# Check if the number is odd and positive
elif (user_number % 2) != 0 and user_number > 0:
    # If the number is not divisible by 2 and greater than 0, it's a positive odd number
    print(f"\nThe number '{user_number}' is a Positive odd number.")

# If none of the above conditions are met, the number must be odd and negative
else:
    # The number is not divisible by 2 and less than 0, so it's a negative odd number
    print(f"\nThe number '{user_number}' is a Negative odd number.")
