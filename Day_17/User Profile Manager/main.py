from profile_manager import *

def menu():
    print("\n========== USER PROFILE MANAGER ==========\n"
          "1. Create Profile\n"
          "2. View Profile\n"
          "3. Update City\n"
          "4. Add Skill\n"
          "5. Delete Profile\n"
          "6. Exit\n")
    return int(input("Please enter your choice: "))


def main():
    while True:
        choice = menu()

        if choice == 1:
            add_profile()
        elif choice == 2:
            view_profile()
        elif choice == 3:
            update_city()
        elif choice == 4:
            add_new_skill()
        elif choice == 5:
            delete_profile()
        elif choice == 6:
            print("Thank you for using this program")
            break
        else:
            print("Please enter a valid choice")


if __name__ == "__main__":
    main()
