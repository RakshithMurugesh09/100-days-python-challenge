shopping_list = []

while True:
    print("\nShopping list Menu:"
          "\n1. Add an item"
          "\n2. Remove an item"
          "\n3. View list"
          "\n4. Exit")
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid Choice Please Try again!!!")
        continue

    if choice == 1:
        shopping_list.append(input("Enter item to add: ").strip().title())
        print(f"{shopping_list[-1]} has been added to the list")
    elif choice == 2:
        item = input("Enter the item to remove: ").strip().title()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from list")
        else:
            print(f'{item} not in list')
    elif choice == 3:
        if shopping_list:
            print("\nShopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f'{i}. {item}')
        else:
            print("List is empty")
    elif choice == 4:
        print("Exiting the program. Good Bye!!!")
        break
    else:
        print("Invalid Choice Please Try again!!!")