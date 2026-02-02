target = 10 # Set the upper limit for the numbers to check (0 to 100)

# Loop through numbers from 0 to target (inclusive)
for numbers in range(0, target + 1):
    # Check if the number is divisible by both 3 and 5
    if numbers % 5 == 0 and numbers % 3 == 0:
        print("Fizz Bizz")  # Print "Fizz Bizz" if divisible by both 3 and 5

    # Check if the number is divisible by 3 only
    elif numbers % 3 == 0:
        print("Fizz")  # Print "Fizz" if divisible by 3

    # Check if the number is divisible by 5 only
    elif numbers % 5 == 0:
        print("Bizz")  # Print "Bizz" if divisible by 5

    # If number is not divisible by 3 or 5, just print the number
    else:
        print(numbers)
