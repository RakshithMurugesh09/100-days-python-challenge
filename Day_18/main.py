import re

def display_menu():
    return input("1. Validate Email\n2. Validate Phone Number\n3. Exit\nEnter your choice: ")

def validate_email():
    user_email = input("Enter your email: ")
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|in)$"
    match = re.fullmatch(pattern, user_email)
    if match:
        print("Valid Email")
    else:
        print("Invalid Email")

def validate_phone_number():
    user_input = input("Enter your phone number: ")
    pattern = r"^[6-9]\d{9}$"
    match = re.fullmatch(pattern, user_input)
    if match:
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")

def main():

    while True:
        user_choice = display_menu()
        if user_choice == "1":
            validate_email()
        elif user_choice == "2":
            validate_phone_number()
        elif user_choice == "3":
            print("Thank you for your time. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")




if __name__ == "__main__":
    main()

