from art import logo
from coffee_data import MENU, profit
from coffee_utils import (print_report,check_resources,process_coins,check_transaction,make_coffee)

print(logo)

machine_on = True

while machine_on:

    choice = input(
        "\nWhat would you like? "
        "(espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print_report(profit)

    elif choice in MENU:

        drink = MENU[choice]

        if check_resources(drink["ingredients"]):

            payment = process_coins()

            if check_transaction(payment,drink["cost"]):
                profit += drink["cost"]
                make_coffee(choice,drink["ingredients"])

    else:
        print("Invalid choice.")