class BankAccount:
    """
    Represents a bank account.
    """

    def __init__(self):
        print()

        self.account_holder = input("Enter Account Holder Name: ")
        self.account_number = input("Enter Account Number: ")
        self.balance = float(input("Enter Initial Balance: "))

    def deposit(self):
        amount = float(input("\nEnter amount to deposit: "))

        if amount <= 0:
            print("\n❌ Deposit amount must be greater than 0.")
            return

        self.balance += amount

        print(f"\n₹{amount:.0f} deposited successfully.")
        print(f"\nCurrent Balance: ₹{self.balance:.0f}")

    def withdraw(self):
        amount = float(input("\nEnter amount to withdraw: "))

        if amount <= 0:
            print("\n❌ Withdrawal amount must be greater than 0.")
            return

        if amount > self.balance:
            print("\n❌ Insufficient Funds!")
            return

        self.balance -= amount

        print(f"\n₹{amount:.0f} withdrawn successfully.")
        print(f"\nCurrent Balance: ₹{self.balance:.0f}")

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance:.0f}")

    def display_details(self):
        print("\n========== ACCOUNT DETAILS ==========\n")

        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance         : ₹{self.balance:.0f}")