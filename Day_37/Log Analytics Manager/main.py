from collections import Counter, defaultdict, deque
import os


LOG_FILE = "app.log"


# =========================
# FILE OPERATIONS
# =========================

def log_file_exists():
    """Check whether the log file exists and contains data."""
    if not os.path.exists(LOG_FILE):
        print("Log file does not exist.")
        return False

    if os.path.getsize(LOG_FILE) == 0:
        print("Log file is empty.")
        return False

    return True


def read_logs():
    """Read all logs from the log file."""
    pass


# =========================
# LOG ANALYSIS
# =========================

def count_log_levels():
    """Count INFO, WARNING, ERROR, CRITICAL, etc."""
    pass


def show_most_common_errors():
    """Find the most frequently occurring ERROR messages."""
    pass


def group_logs_by_level():
    """Group log messages using defaultdict."""
    pass


def show_last_n_logs():
    """Display the most recent N logs using deque."""
    pass


def search_logs():
    """Search the log file for a keyword."""
    pass


# =========================
# MENU
# =========================

def display_menu():
    print("""
===== LOG ANALYTICS MANAGER =====

1. View Log Statistics
2. Count Log Levels
3. Show Most Common Errors
4. Group Logs by Level
5. Show Last N Logs
6. Search Logs
7. Exit
""")

    try:
        return int(input("Enter your choice: "))
    except ValueError:
        return -1


# =========================
# MAIN PROGRAM
# =========================

def main():

    while True:

        choice = display_menu()

        if choice == 1:
            pass

        elif choice == 2:
            count_log_levels()

        elif choice == 3:
            show_most_common_errors()

        elif choice == 4:
            group_logs_by_level()

        elif choice == 5:
            show_last_n_logs()

        elif choice == 6:
            search_logs()

        elif choice == 7:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()