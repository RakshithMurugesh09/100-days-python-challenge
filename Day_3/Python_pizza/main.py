# 🍕 Python Pizza Order Program

# Step 1: Welcome Message
print("Welcome to Python Pizza 🍕!")

# Step 2: Ask for pizza size
size = input("What size pizza do you want? (S - Small, M - Medium, L - Large): ").lower()

# Step 3: Ask if they want pepperoni
add_pepperoni = input("Do you want pepperoni? (Y/N): ").lower()

# Step 4: Ask if they want extra cheese
add_cheese = input("Do you want extra cheese? (Y/N): ").lower()

# Step 5: Set base price depending on size
bill = 0

if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25
else:
    print("Invalid size selected. Defaulting to Small.")
    bill += 15

# Step 6: Add pepperoni cost
if add_pepperoni == 'y':
    if size == 's':
        bill += 2
    else:  # m or l
        bill += 3

# Step 7: Add extra cheese cost
if add_cheese == 'y':
    bill += 1

# Step 8: Print final bill
print(f"Your total bill is: ${bill}")
