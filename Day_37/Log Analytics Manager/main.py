from collections import Counter, defaultdict, deque
import os

LOG_FILE = (r"C:\Users\Rakshith.Murugesh\PycharmProjects"
            r"\100-days-python-challenge\Day_36\Application Log Manager\app.log")


# =========================
# FILE OPERATIONS
# =========================

def log_file_exists():
    """Check whether the log file exists and contains data."""

    if not os.path.exists(LOG_FILE):
        print("❌ Log file does not exist.")
        return False

    if os.path.getsize(LOG_FILE) == 0:
        print("❌ Log file is empty.")
        return False

    return True


def read_logs():
    """Read all logs from the log file."""

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        return file.readlines()


# =========================
# LOG ANALYSIS
# =========================

def view_log_statistics():
    """Display overall log statistics."""

    logs = read_logs()

    print("\n===== LOG STATISTICS =====")

    print(f"Total Logs: {len(logs)}")

    level_counter = Counter(
        line.split("|")[2].strip()
        for line in logs
        if len(line.split("|")) >= 3
    )

    for level, count in level_counter.items():
        print(f"{level:<10}: {count}")


def count_log_levels():
    """Count INFO, WARNING, ERROR, CRITICAL, etc."""

    levels = [
        line.split("|")[2].strip()
        for line in read_logs()
        if len(line.split("|")) >= 3
    ]

    counter = Counter(levels)

    print("\n===== LOG LEVEL STATISTICS =====")

    for level, count in counter.items():
        print(f"{level:<10}: {count}")


def show_most_common_errors():
    """Display the most common ERROR messages."""

    error_counter = Counter(
        line.split("|")[3].strip()
        for line in read_logs()
        if len(line.split("|")) >= 4
        and line.split("|")[2].strip() == "ERROR"
    )

    if not error_counter:
        print("No ERROR logs found.")
        return

    print("\n===== MOST COMMON ERRORS =====")

    for error, count in error_counter.most_common():
        print(f"{count}x | {error}")

    print(f"\nTotal Errors: {sum(error_counter.values())}")


def group_logs_by_level():
    """Group log messages using defaultdict."""

    grouped_logs = defaultdict(list)

    for line in read_logs():

        parts = line.strip().split("|")

        if len(parts) >= 4:
            level = parts[2].strip()
            message = parts[3].strip()

            grouped_logs[level].append(message)

    print("\n===== GROUPED LOGS =====")

    for level, messages in grouped_logs.items():

        print(f"\n[{level}]")

        for message in messages:
            print(f" - {message}")


def show_last_n_logs():
    """Display the most recent N logs using deque."""

    try:

        n = int(input("How many recent logs would you like to see? "))

        if n <= 0:
            print("Please enter a number greater than 0.")
            return

    except ValueError:
        print("Invalid number.")
        return

    recent_logs = deque(maxlen=n)

    for line in read_logs():
        recent_logs.append(line)

    print(f"\n===== LAST {len(recent_logs)} LOGS =====")

    for log in recent_logs:
        print(log.strip())


def search_logs():
    """Search the log file for a keyword."""

    keyword = input("Enter a keyword: ").strip().lower()

    matches = []

    for log in read_logs():

        if keyword in log.lower():
            matches.append(log.strip())

    print(f"\nFound {len(matches)} matching log(s).\n")

    if not matches:
        print("No matching logs found.")
        return

    for match in matches:
        print(f"> {match}")


# =========================
# MENU
# =========================

def display_menu():

    print("""
===== LOG ANALYTICS MANAGER =====

1. View Log Statistics
2. Count Log Levels
3. Show Most Common Errors
4. Group Logs By Level
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

    if not log_file_exists():
        return

    while True:

        choice = display_menu()

        if choice == 1:
            view_log_statistics()

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