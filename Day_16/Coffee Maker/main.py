from coffeemachin import CoffeeMachine


machine = CoffeeMachine()

is_on = True

while is_on:

    choice = input(
        f"What would you like? ({machine.get_menu()}): "
    ).lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        machine.report()

    else:
        drink = machine.find_drink(choice)

        if drink:
            print(f"You selected {choice}")
            if (machine.is_resource_sufficient(drink["ingredients"])
                    and machine.process_payment(drink["cost"])):
                machine.make_coffee(choice, drink["ingredients"])


        else:
            print("Invalid choice.")
