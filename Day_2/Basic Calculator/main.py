# Basic Calculator in Python
# Demonstrates data types, type casting, and operators

# Ask user for the first number
num1 = input("Enter the first number: ")  # input() returns a string

# Convert the input string to a float (type casting)
num1 = float(num1)

# Ask user for the second number
num2 = input("Enter the second number: ")
num2 = float(num2)  # type casting to float

# Ask user for the operation
operation = input("Enter operation (+, -, *, /, %): ")

# Perform calculation based on the chosen operator
if operation == '+':
    result = num1 + num2  # addition operator
elif operation == '-':
    result = num1 - num2  # subtraction operator
elif operation == '*':
    result = num1 * num2  # multiplication operator
elif operation == '/':
    if num2 != 0:
        result = num1 / num2  # division operator
    else:
        result = "Error! Division by zero."
elif operation == '%':
    if num2 != 0:
        result = num1 % num2  # modulus operator
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Display the result
print("Result:", result)
