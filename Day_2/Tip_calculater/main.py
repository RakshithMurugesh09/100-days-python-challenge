# Welcome message
print("Welcome to the Project Tip Calculator!")

""" Collect necessary inputs from the user """

# To Do 1: Ask the user to enter the total bill amount before tip.
#          Ensure it's a numerical value for accurate calculations.
bill_amount = float(input("What was the total bill?\nBill Amount: "))

# To Do 2: Ask the user what percentage tip they would like to give.
#          You can suggest common options like 10%, 12%, or 15% for convenience.
tip_percent = int(input("What % tip would you like to give? (e.g. 10, 12, 15):\nTip %: "))

# To Do 3: Ask how many people will be splitting the bill.
#          This helps calculate how much each person needs to contribute.
no_of_people = int(input("How many people to split the bill?\nNo. of People: "))

""" Perform the required calculations """

# To Do 4: Calculate the tip amount
tip_amount = (tip_percent / 100) * bill_amount

# Add tip to an original bill to get the total amount
total_amount = bill_amount + tip_amount

# Divide the total amount by number of people
per_person_share = total_amount / no_of_people

""" Display the result """

# To Do 5: Present the final amount each person needs to pay.
#          Format output to 2 decimal places for currency.
print("\n----- Final Summary -----")
print(f"Total Bill: {bill_amount:.2f} Rs")
print(f"Tip ({tip_percent}%): {tip_amount:.2f} Rs")
print(f"Total Amount (with Tip): {total_amount:.2f} Rs")
print(f"Number of People: {no_of_people}")
print(f"Each Person Should Pay: {per_person_share:.2f} Rs")
