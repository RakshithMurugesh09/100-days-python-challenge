from coffee_data import resources


def print_report(profit):
    """
    Print machine resources.
    """

    print(f"Water : {resources['water']}ml")
    print(f"Milk  : {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money : ${profit}")


def check_resources(ingredients):
    """
    Check if resources are sufficient.
    """

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False

    return True


def process_coins():
    """
    Ask user for coins and calculate total.
    """

    print("\nPlease insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (
        quarters * 0.25
        + dimes * 0.10
        + nickles * 0.05
        + pennies * 0.01
    )

    return total


def check_transaction(payment, cost):
    """
    Check payment and return status.
    """

    if payment >= cost:

        change = round(payment - cost, 2)

        if change > 0:
            print(f"Here is ${change} in change.")

        return True

    print("Sorry that's not enough money. Money refunded. $", payment)
    return False


def make_coffee(drink_name, ingredients):
    """
    Deduct resources and serve drink.
    """

    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"\nHere is your {drink_name} ☕ Enjoy!")