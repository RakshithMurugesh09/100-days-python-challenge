from art import logo
from bankaccount import BankAccount


def display_menu():
    print("\n========== MENU ==========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    try:
        return int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid number.")


def main():
    print(logo)

    bank = BankAccount()

    while True:
        user_choice = display_menu()

        if user_choice == 1:
            bank.deposit()

        elif user_choice == 2:
            bank.withdraw()

        elif user_choice == 3:
            bank.check_balance()

        elif user_choice == 4:
            bank.display_details()

        elif user_choice == 5:
            print("\nThank you for using Bank Account System!")
            break

        else:
            print("\n❌ Invalid Choice. Please try again.")


if __name__ == "__main__":
    main()