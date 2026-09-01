import os
import platform


def show_current_directory():
    print("\n===== CURRENT DIRECTORY =====")
    print(os.getcwd())


def list_files():
    print("\n===== FILES & FOLDERS =====")
    for item in os.listdir():
        print(item)


def show_python_environment():
    print("\n===== PYTHON ENVIRONMENT =====")
    print(f"OS          : {platform.system()}")
    print(f"OS Version  : {platform.release()}")
    print(f"Machine     : {platform.machine()}")


def show_environment_variable():
    print("\n===== ENVIRONMENT VARIABLES =====")

    env_vars = [
        "USERNAME",
        "COMPUTERNAME",
        "USERPROFILE",
        "PATH",
        "PYTHONPATH"
    ]

    for var in env_vars:
        print(f"{var} : {os.environ.get(var, 'Not Found')}")

def show_application_configuration():
    print("\n===== APPLICATION CONFIGURATION =====")
    print(f"Python Version : {platform.python_version()}")
    print(f"Python Compiler: {platform.python_compiler()}")
    print(f"Platform       : {platform.system()}")


def display_menu():
    print("\n========== ENVIRONMENT & SYSTEM INFORMATION MANAGER ==========")
    print("1. Show Current Directory")
    print("2. List Files")
    print("3. Show Python Environment")
    print("4. Show Environment Variables")
    print("5. Show Application Configuration")
    print("6. Exit")


def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            show_current_directory()

        elif choice == "2":
            list_files()

        elif choice == "3":
            show_python_environment()

        elif choice == "4":
            show_environment_variable()

        elif choice == "5":
            show_application_configuration()

        elif choice == "6":
            print("\nThank you for using Environment & System Information Manager.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()