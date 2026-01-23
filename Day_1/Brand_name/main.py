# Welcome message for the user
print("Welcome to the Brand Name Generator Project!")

# -----------------------------
# Step 1: Get user Input
# -----------------------------

# Ask the user for their birthplace
birth_place = input("What is your birth place?\nAnswer: ").title()

# Ask the user for their pet's name and convert it to title case
# (first letter capitalized, rest lowercase)
pet_name = input("What is your pet's name?\nAnswer: ").title()

# -----------------------------
# Step 2: Generate brand name
# -----------------------------

# Combine the birthplace and pet name to create a brand name
# Convert the birthplace to title case to match the pet name style
brand_name = birth_place.title() + " " +pet_name

# -----------------------------
# Step 3: Show the result
# -----------------------------

# Display the generated brand name to the user
print(f'Your brand name may be like "{brand_name}"')
