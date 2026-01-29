user_age = int(input("Enter your age: "))
is_citizen_of_india = input("Are you an Indian Citizen? (yes/no): ").lower()

if user_age >= 18 and is_citizen_of_india == 'yes':
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")