class BankAccount:
    """Represents a bank account."""

    def __init__(self):
        print()

        self.account_holder = input("Enter Account Holder Name: ")
        self.account_number = input("Enter Account Number: ")

        while True:
            try:
                balance = float(input("Enter Initial Balance: ₹"))

                if balance < 0:
                    print("❌ Initial balance cannot be negative.")
                    continue

                self.balance = balance
                break

            except ValueError:
                print("❌ Please enter a valid amount.")

    def deposit(self):
        """Deposit money into the account."""

        while True:
            try:
                amount = float(input("\nEnter amount to deposit: ₹"))

                if amount <= 0:
                    print("❌ Deposit amount must be greater than zero.")
                    return

                self.balance += amount

                print(f"\n✅ ₹{amount:.2f} deposited successfully.")
                print(f"Current Balance: ₹{self.balance:.2f}")
                return

            except ValueError:
                print("❌ Please enter a valid amount.")

    def withdraw(self):
        """Withdraw money from the account."""

        while True:
            try:
                amount = float(input("\nEnter amount to withdraw: ₹"))

                if amount <= 0:
                    print("❌ Withdrawal amount must be greater than zero.")
                    return

                if amount > self.balance:
                    print("❌ Insufficient balance.")
                    return

                self.balance -= amount

                print(f"\n✅ ₹{amount:.2f} withdrawn successfully.")
                print(f"Current Balance: ₹{self.balance:.2f}")
                return

            except ValueError:
                print("❌ Please enter a valid amount.")

    def check_balance(self):
        """Display current balance."""

        print(f"\nCurrent Balance: ₹{self.balance:.2f}")

    def display_details(self):
        """Display account details."""

        print("\n========== ACCOUNT DETAILS ==========")

        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance         : ₹{self.balance:.2f}")

        print("=====================================")