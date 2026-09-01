from pathlib import Path

LOG_DIRECTORY = Path("logs")


def display_menu():
    print("""
========== FILE & LOG MANAGER ==========

1. Create Logs Directory
2. Create Sample Log Files
3. List Log Files
4. Search Logs Recursively
5. File Information
6. Search Keyword in Logs
7. Log Summary
8. Exit
""")
    return input("Enter your choice: ").strip()


def create_logs_directory():
    LOG_DIRECTORY.mkdir(exist_ok=True)
    print("✅ Logs Directory Created")


def create_sample_logs():
    LOG_DIRECTORY.mkdir(exist_ok=True)

    sample_logs = {
        "app.log": """INFO: Application started
ERROR: Database connection failed
INFO: User login successful
WARNING: Memory usage high
""",
        "server.log": """INFO: Server started
INFO: Request received
ERROR: Timeout occurred
INFO: Request completed
""",
        "security.log": """WARNING: Multiple login attempts
INFO: User authenticated
ERROR: Unauthorized access detected
"""
    }

    for file_name, content in sample_logs.items():
        file_path = LOG_DIRECTORY / file_name
        file_path.write_text(content)

    print("✅ Sample log files created successfully")


def list_log_files():
    if not LOG_DIRECTORY.exists():
        print("❌ Logs directory not found")
        return

    log_files = list(LOG_DIRECTORY.glob("*.log"))

    if not log_files:
        print("No log files found")
        return

    print("\n========== LOG FILES ==========")
    for index, file in enumerate(log_files, start=1):
        print(f"{index}. {file.name}")


def search_logs_recursively():
    if not LOG_DIRECTORY.exists():
        print("❌ Logs directory not found")
        return

    log_files = list(LOG_DIRECTORY.rglob("*.log"))

    if not log_files:
        print("No log files found")
        return

    print("\n========== RECURSIVE SEARCH ==========")
    for file in log_files:
        print(file)


def display_file_information():
    if not LOG_DIRECTORY.exists():
        print("❌ Logs directory not found")
        return

    filename = input("Enter log file name: ").strip()
    file_path = LOG_DIRECTORY / filename

    if not file_path.exists():
        print("❌ File not found")
        return

    print("\n========== FILE INFORMATION ==========")
    print(f"Name          : {file_path.name}")
    print(f"Path          : {file_path.resolve()}")
    print(f"Size          : {file_path.stat().st_size} bytes")
    print(f"Extension     : {file_path.suffix}")


def search_keyword():
    if not LOG_DIRECTORY.exists():
        print("❌ Logs directory not found")
        return

    keyword = input("Enter keyword to search: ").strip()

    found = False

    print(f"\n========== SEARCH RESULTS FOR '{keyword}' ==========")

    for file in LOG_DIRECTORY.rglob("*.log"):
        lines = file.read_text().splitlines()

        for line_number, line in enumerate(lines, start=1):
            if keyword.lower() in line.lower():
                found = True
                print(f"{file.name} | Line {line_number}: {line}")

    if not found:
        print("No matches found")


def log_summary():
    if not LOG_DIRECTORY.exists():
        print("❌ Logs directory not found")
        return

    log_files = list(LOG_DIRECTORY.rglob("*.log"))

    if not log_files:
        print("No log files found")
        return

    total_files = len(log_files)
    total_lines = 0
    error_count = 0
    warning_count = 0
    info_count = 0

    for file in log_files:
        lines = file.read_text().splitlines()

        total_lines += len(lines)

        for line in lines:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    print("\n========== LOG SUMMARY ==========")
    print(f"Total Log Files : {total_files}")
    print(f"Total Lines     : {total_lines}")
    print(f"INFO Entries    : {info_count}")
    print(f"WARNING Entries : {warning_count}")
    print(f"ERROR Entries   : {error_count}")


def main():

    while True:

        choice = display_menu()

        if choice == "1":
            create_logs_directory()

        elif choice == "2":
            create_sample_logs()

        elif choice == "3":
            list_log_files()

        elif choice == "4":
            search_logs_recursively()

        elif choice == "5":
            display_file_information()

        elif choice == "6":
            search_keyword()

        elif choice == "7":
            log_summary()

        elif choice == "8":
            print("Thank you for using File & Log Manager!")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()