import logging
import time
import os

# =========================
# LOGGING CONFIGURATION
# =========================

logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="%(asctime)s GMT | %(name)s | %(levelname)s | %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
    level=logging.DEBUG
)

# Use GMT / UTC
logging.Formatter.converter = time.gmtime


# =========================
# MENU
# =========================

def display_menu():
    print("""
===== APPLICATION LOG MANAGER =====

1. Start Application
2. Generate INFO Log
3. Generate WARNING Log
4. Generate ERROR Log
5. Generate Exception Log
6. View Log File
7. Search Logs
8. View Last N Logs
9. Clear Log File
10. Exit
""")

    try:
        return int(input("Enter your choice: "))
    except ValueError:
        return -1


# =========================
# LOG FUNCTIONS
# =========================

def start_app():
    logging.info("Application Started Successfully")
    print("Application started.")


def generate_info_log():
    message = input("Enter INFO message: ").strip()
    logging.info(message)
    print("INFO log created.")


def generate_warning_log():
    message = input("Enter WARNING message: ").strip()
    logging.warning(message)
    print("WARNING log created.")


def generate_error_log():
    message = input("Enter ERROR message: ").strip()
    logging.error(message)
    print("ERROR log created.")


def generate_exception_log():
    try:
        int("abc")
    except ValueError:
        logging.exception("ValueError occurred while converting string to integer")
        print("Exception logged.")


# =========================
# FILE OPERATIONS
# =========================

def log_file_exists():
    if not os.path.exists("app.log"):
        print("Log file does not exist.")
        return False

    if os.path.getsize("app.log") == 0:
        print("Log file is empty.")
        return False

    return True


def view_log_file():
    if not log_file_exists():
        return

    print("\n===== LOG FILE CONTENT =====\n")

    with open("app.log", "r") as file:
        for line in file:
            print(line.strip())


def search_logs():
    if not log_file_exists():
        return

    keyword = input("Enter keyword to search: ").strip().lower()

    matches = 0

    print("\n===== SEARCH RESULTS =====\n")

    with open("app.log", "r") as file:
        for line in file:
            if keyword in line.lower():
                print(line.strip())
                matches += 1

    if matches == 0:
        print(f"No logs found containing '{keyword}'")
    else:
        print(f"\nTotal Matches Found: {matches}")


def view_last_n_logs():
    if not log_file_exists():
        return

    try:
        n = int(input("How many recent logs do you want to see? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if n < 0:
        print("Please enter a valid number.")
        return

    with open("app.log", "r") as file:
        logs = file.readlines()

    total_logs = len(logs)

    if n > total_logs:
        print(f"Only {total_logs} logs available. Displaying all logs.\n")
    else:
        print(f"\n===== LAST {n} LOGS =====\n")

    for log in logs[-n:]:
        print(log.strip())


def clear_log_file():
    confirmation = input("Are you sure you want to clear all logs? (yes/no): ").lower()

    if confirmation == "yes":
        open("app.log", "w").close()
        print("Log file cleared.")
        logging.info("Log file was cleared")
    else:
        print("Operation cancelled.")


# =========================
# MAIN PROGRAM
# =========================

def main():

    while True:

        choice = display_menu()

        if choice == 1:
            start_app()

        elif choice == 2:
            generate_info_log()

        elif choice == 3:
            generate_warning_log()

        elif choice == 4:
            generate_error_log()

        elif choice == 5:
            generate_exception_log()

        elif choice == 6:
            view_log_file()

        elif choice == 7:
            search_logs()

        elif choice == 8:
            view_last_n_logs()

        elif choice == 9:
            clear_log_file()

        elif choice == 10:
            logging.info("Application Exited")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()