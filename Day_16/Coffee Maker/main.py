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
            # TODO:
            # Check resources
            # Process payment
            # Make coffee

        else:
            print("Invalid choice.")
