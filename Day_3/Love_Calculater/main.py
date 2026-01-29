# Simple Love Calculator
print("Welcome to the Project Love Calculator 💘")

# This program asks for two names and calculates a "love score"
# based on a playful formula. It's purely for fun and not based on real science!

# Request the user for partners' names
partner_one = input("Enter first name: ").lower()
partner_two = input("Enter second name: ").lower()

# Combine both names
combined_names = partner_one + partner_two

# Count letters for "TRUE"
t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')

# Count letters for "LOVE"
l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')

# Calculate the total scores
true_score = t + r + u + e
love_score = l + o + v + e

# Combine the scores into a single number
love_percentage = int(str(true_score) + str(love_score))

# Output the result
print(f"Your love score is: {love_percentage}%")

# Interpret the love score with fun messages
if love_percentage < 10 or love_percentage > 90:
    print("Not made for each other 💔, You like Oil and Water ")
elif 40 <= love_percentage <= 80:
    print("You are made for each other 💖")
else: #
    print("This might be a chaotic love story! Proceed with caution 😬")

