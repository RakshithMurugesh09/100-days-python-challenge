from data import DataManager

print("Welcome to Rakshith's Flight Club!")
print("We find the best flight deals and email them to you.\n")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

email = input("What is your email?\n")
confirm_email = input("Type your email again.\n")

if email == confirm_email:

    data_manager = DataManager()

    data_manager.add_user(
        first_name=first_name,
        last_name=last_name,
        email=email
    )

    print("✅ You are in the club!")

else:
    print("❌ Emails do not match.")