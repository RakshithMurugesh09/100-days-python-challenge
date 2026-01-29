# 🏰 Amusement Park Ticket Booth 🎟️

# Step 1: Print a welcome message
print("Welcome to 🏰 Amusement Park Ticket Booth 🎟️")

# Step 2: Ask the user to Input their height in cm
user_height = int(input("Please provide your height in CM = "))

# Step 3: Use an if-statement to check if the height is above or equal to 120 cm
# If yes, allow the user to proceed
# If not, print a message that they cannot ride
if user_height < 120:
    print("\nSorry your height is lower than 120cm, you can't have ride" )
    pass
else:
    bill = 0

    # Step 4: If they are tall enough, ask their age
    user_age = int(input("What is your age = "))

    # Step 5: Use if-elif-else to set different prices based on age:
    # - Below 12: $5
    # - 12 to 18: $7
    # - Above 18: $12
    if user_age < 12:
        bill += 5
    elif user_age <= 18:
        bill += 7
    else:
        bill += 12

    print(f"Ticket price = ${bill}")

    # Step 6: Ask if the user wants a photo taken (Y/N)
    photo_needed = input("Do u need photo (Y/N): ").lower()

    # Step 7: If yes, add $3 to the bill
    if photo_needed == 'y':
        bill += 3
        print("Photo added: +$3")

    # Step 8: Print the final bill total with a thank-you message
    print(f"\nThe final total is {bill} $")
    print("Thank you! Enjoy your ride 🎢")
