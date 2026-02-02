from random import choice, shuffle

# Tuple of alphabetic characters (lowercase and uppercase)
alphabet = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
)

# Tuple of number characters
numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

# Tuple of symbol characters
symbols = (
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{',
    '|', '}', '~'
)

password = ""   # Initialize an empty string to build the password

# Ask user for the number of alphabet characters to use in the password
count_of_alphabet = int(input("How many alphabet character needed in password?\nCount of Alphabet = "))

# Ask user for the number of number characters to use in the password
count_of_number = int(input("How many number character needed in password?\nCount of Number = "))

# Ask user for the number of symbol characters to use in the password
count_of_symbol = int(input("How many symbol character needed in password?\nCount of Symbol = "))

# Select random alphabetic characters and add to password
for n in range(count_of_alphabet):
    character = choice(alphabet)    # Pick a random alphabet character
    password += character           # Add it to the password string

# Select random number characters and add to password
for n in range(count_of_number):
    character = choice(numbers)     # Pick a random number character
    password += character           # Add it to the password string

# Select random symbol characters and add to password
for n in range(count_of_symbol):
    character = choice(symbols)     # Pick a random symbol character
    password += character           # Add it to the password string

password = list(password)           # Convert the password string into a list for shuffling

shuffle(password)                   # Shuffle the list to mix up the character order

# Combine the shuffled list back into a string and display the password
print(f"Your password may be like : {''.join(password)}")
