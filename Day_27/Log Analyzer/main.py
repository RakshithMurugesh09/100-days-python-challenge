FILENAME = "system.log"


def display_menu():
    print("\n========== LOG ANALYZER ==========")
    print("1. View All Logs")
    print("2. Count Log Levels")
    print("3. Search Keyword")
    print("4. Show ERROR Logs")
    print("5. Summary Report")
    print("6. Exit")

    return int(input("Enter your choice: "))


def read_file():
    try:
        with open(FILENAME, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return None


def view_logs():
    logs = read_file()

    if logs is None:
        print("File not found!")
        return

    if not logs:
        print("No logs found in the file!")
        return

    print("\n========== ALL LOGS ==========")
    for log in logs:
        print(log.strip())


def count_log_levels():
    logs = read_file()

    if logs is None:
        print("File not found!")
        return

    if not logs:
        print("No logs found in the file!")
        return

    levels = {
        "INFO": 0,
        "DEBUG": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in logs:
        upper_line = line.upper()

        for level in levels:
            if level in upper_line:
                levels[level] += 1

    print("\n========== LOG COUNTS ==========")
    for level, count in levels.items():
        print(f"{level}: {count}")


def search_logs():
    logs = read_file()

    if logs is None:
        print("File not found!")
        return

    if not logs:
        print("No logs found in the file!")
        return

    keyword = input("Enter keyword to search: ").upper()

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for line in logs:
        if keyword in line.upper():
            print(line.strip())
            found = True

    if not found:
        print(f"Keyword '{keyword}' not found.")


def show_error_logs():
    logs = read_file()

    if logs is None:
        print("File not found!")
        return

    if not logs:
        print("No logs found in the file!")
        return

    found = False

    print("\n========== ERROR LOGS ==========")

    for line in logs:
        if "ERROR" in line.upper():
            print(line.strip())
            found = True

    if not found:
        print("No ERROR logs found.")


def display_summary():
    logs = read_file()

    if logs is None:
        print("File not found!")
        return

    if not logs:
        print("No logs found in the file!")
        return

    total_logs = len(logs)
    error_logs = sum(1 for log in logs if "ERROR" in log.upper())
    warning_logs = sum(1 for log in logs if "WARNING" in log.upper())

    print("\n========== SUMMARY REPORT ==========")
    print(f"Total Logs   : {total_logs}")
    print(f"ERROR Logs   : {error_logs}")
    print(f"WARNING Logs : {warning_logs}")


def main():
    while True:
        try:
            choice = display_menu()

            if choice == 1:
                view_logs()

            elif choice == 2:
                count_log_levels()

            elif choice == 3:
                search_logs()

            elif choice == 4:
                show_error_logs()

            elif choice == 5:
                display_summary()

            elif choice == 6:
                print("Thank you for using Log Analyzer!")
                break

            else:
                print("Please enter a valid choice (1-6).")

        except ValueError:
            print("Please enter a number only!")


main()