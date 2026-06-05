print("Welcome to the Odd or Even Number Calculator!")

user_number = int(input("Please enter an integer number:"))

party = "even" if user_number % 2 == 0 else "odd"
sign = "positive" if user_number >= 0 else "negative"

match(party, sign):
    case ("even", "positive"):
        print(f"\nThe number '{user_number}' is a Positive even number.")
    case ("even", "negative"):
        print(f"\nThe number '{user_number}' is a Negative even number.")
    case ("odd", "positive"):
        print(f"\nThe number '{user_number}' is a Positive Odd number.")
    case ("odd", "negative"):
        print(f"\nThe number '{user_number}' is a Negative Odd number.")
