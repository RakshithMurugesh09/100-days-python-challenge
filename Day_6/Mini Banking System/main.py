# Initial account balance
account_balance = 1000.0
account_password = 1234  # Example password


# Function for password protection
def password_protection():
    print("Welcome to the Banking System")
    attempts = 3
    while attempts > 0:
        try:
            password = int(input("Enter your password: "))
            if password == account_password:
                print("✅ Password correct! Access granted.")
                return True
            else:
                attempts -= 1
                print(f"❌ Wrong password! Attempts left: {attempts}")
        except ValueError:
            print("Please enter numbers only!")
    print("🚫 Too many wrong attempts! Exiting...")
    return False


# Menu options
def menu_option():
    print("\n--- Banking Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please choose between 1-4.")
        except ValueError:
            print("Invalid Input! Enter a number between 1-4.")


# Check balance
def check_balance():
    print(f"💰 Your account balance is: ₹{account_balance:.2f}")


# Deposit money
def deposit_money():
    global account_balance
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            account_balance += amount
            print(f"✅ Deposited ₹{amount:.2f}. New balance: ₹{account_balance:.2f}")
        else:
            print("❌ Amount must be greater than 0.")
    except ValueError:
        print("Invalid amount! Please enter a number.")


# Withdraw money
def withdraw_money():
    global account_balance
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount > account_balance:
            print("❌ Insufficient balance!")
        elif amount > 0:
            account_balance -= amount
            print(f"✅ Withdrawn ₹{amount:.2f}. New balance: ₹{account_balance:.2f}")
        else:
            print("❌ Amount must be greater than 0.")
    except ValueError:
        print("Invalid amount! Please enter a number.")


# Main program
if password_protection():
    while True:
        choice = menu_option()
        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            print("👋 Thank you for using the Banking System!")
            break
