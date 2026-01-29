# Welcome message
print("Welcome to BMI Check Project")

""" Collect necessary inputs from the user """

# TODO: Prompt the user to enter their weight in kilograms
user_weight = float(input("Weight in kg = "))
# TODO: Prompt the user to enter their height in meters
user_height = float(input("Height in meter = "))
# TODO: Calculate BMI using the formula: BMI = weight / (height ** 2)
bmi = round(user_weight/(user_height * user_height), 2)
# TODO: Display the calculated BMI value, formatted to two decimal places
print(f"\nYour BMI is {bmi} kg/m²")
# TODO: Check the BMI category based on standard ranges:
#   - If BMI is less than 18.5, categorize as underweight
if bmi < 18.5:
    print(f'As your BMI is below 18.5 so your categorize as "underweight".')
#   - If BMI is between 18.5 and 24.9, categorize as normal weight
elif bmi < 24.9:
    print(f'As your BMI is perfect so your categorize as "normal weight".')
#   - If BMI is between 25 and 29.9, categorize as overweight
elif bmi < 29.9:
    print(f'As your BMI is Little then average so your categorize as "overweight".')
#   - If BMI is 30 or above, categorize as obese
else:
    print(f'As your BMI is more then average so your categorize as "obese".')
