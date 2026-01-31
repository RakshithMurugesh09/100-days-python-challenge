import random  # Importing the random module to use random number generation

# List of guest names
guest = ["Keerthi", "Rakshith", "Rachu", "Manu", "Teju"]

# Get the total number of guests
length_guest = len(guest)

# Generate a random index from 0 to (number of guests - 1)
bill_paying = random.randint(0, length_guest - 1)

# Print the name of the person who will pay the bill, with a message
print(f"{guest[bill_paying]} is going to pay the bill today!")
