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
        pass

    def process_payment(self, cost):
        # TODO
        pass

    def make_coffee(self, drink_name, ingredients):
        # TODO
        pass