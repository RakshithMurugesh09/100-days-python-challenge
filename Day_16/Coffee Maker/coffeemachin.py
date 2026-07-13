from data import MENU


class CoffeeMachine:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
        self.money = 0

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.money}")

    def get_menu(self):
        return "/".join(MENU.keys())

    def find_drink(self, drink_name):
        return MENU.get(drink_name)

    def is_resource_sufficient(self, ingredients):
        # TODO
        for item in ingredients:
            if ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False

        return True

    def process_payment(self, cost):
        # TODO

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

        if total < cost:
            print("\nSorry, you don't have enough money.\n Here is you refund")
            return False

        change = round(total - cost, 2)

        if change > 0:
            print(f"Here is ${change} in change.")

        self.money += cost
        return True

    def make_coffee(self, drink_name, ingredients):
        # TODO
        for item in ingredients:
            self.resources[item] -= ingredients[item]

        print(f"\nHere is your {drink_name} ☕ Enjoy!")