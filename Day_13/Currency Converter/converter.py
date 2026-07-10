from data import rates


def show_currencies():
    """Display available currencies."""

    print("\nAvailable currencies:")

    for currency in rates:
        print(currency)


def convert_currency(amount, currency):
    """
    Convert INR to selected currency.
    """

    return amount * rates[currency]


def get_amount():
    """
    Get amount from user.
    """

    while True:
        try:
            amount = float(
                input("\nEnter amount in INR: ₹")
            )

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid amount.")


def get_currency():
    """
    Get target currency.
    """

    while True:

        currency = input(
            "Convert to: "
        ).upper()

        if currency in rates:
            return currency

        print("Invalid currency code.")


def play_again():

    while True:

        choice = input(
            "\nConvert again? (Y/N): "
        ).strip().lower()

        if choice in ["y", "yes"]:
            return True

        if choice in ["n", "no"]:
            return False

        print("Please enter Y or N.")