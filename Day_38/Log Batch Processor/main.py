from itertools import count, cycle, repeat, chain, islice, groupby

# =========================
# LOG DATA
# =========================

application_logs = [
    ("INFO", "Application Started"),
    ("INFO", "User Logged In")
]

system_logs = [
    ("WARNING", "Disk Space Low"),
    ("WARNING", "Memory Usage High")
]

security_logs = [
    ("ERROR", "Failed Login Attempt"),
    ("ERROR", "Unauthorized Access")
]

# =========================
# LOG GENERATION
# =========================

def generate_log_records():
    """Generate log records with sequential IDs using itertools.count()."""

    records = []

    counter = count(1)

    for n in counter:
        records.append(f"LOG-{n}")

        if n == 100:
            break

    return records


# =========================
# BATCH PROCESSING
# =========================

def process_logs_in_batches():
    """Process logs in batches using itertools.islice()."""

    batch_size = int(input("Enter batch size: "))

    logs = generate_log_records()

    iterator = iter(logs)

    batch_number = 1

    while True:

        batch = list(
            islice(iterator, batch_size)
        )

        if not batch:
            print("\nAll logs processed!")
            break

        print(f"\nBatch {batch_number}")
        print("-" * 30)

        for log in batch:
            print(log)

        batch_number += 1


# =========================
# FIRST N LOGS
# =========================

def show_first_n_logs():
    """Display the first N logs using itertools.islice()."""

    number_of_logs = int(
        input("Enter number of logs: ")
    )

    logs = generate_log_records()

    print("\nFirst N Logs")
    print("-" * 30)

    for log in islice(logs, number_of_logs):
        print(log)


# =========================
# COMBINE LOG SOURCES
# =========================

def combine_log_sources():
    """Combine multiple log sources using itertools.chain()."""

    print("\nCombined Logs")
    print("-" * 30)

    all_logs = chain(
        application_logs,
        system_logs,
        security_logs
    )

    for log in all_logs:
        print(log)


# =========================
# GROUP LOGS
# =========================

def group_logs_by_level():
    """Group logs by log level using itertools.groupby()."""

    logs = list(
        chain(
            application_logs,
            system_logs,
            security_logs
        )
    )

    logs.sort(key=lambda log: log[0])

    print("\nGrouped Logs")
    print("-" * 30)

    for level, group in groupby(
            logs,
            key=lambda log: log[0]
    ):

        print(f"\n{level}")
        print("-" * 20)

        for _, message in group:
            print(message)


# =========================
# ROUND-ROBIN PROCESSING
# =========================

def round_robin_server_processing():
    """Distribute logs between servers using itertools.cycle()."""

    servers = [
        "Server-A",
        "Server-B",
        "Server-C"
    ]

    server_cycle = cycle(servers)

    logs = generate_log_records()

    print("\nRound Robin Processing")
    print("-" * 30)

    for log in islice(logs, 15):

        server = next(server_cycle)

        print(
            f"{log} -> {server}"
        )


# =========================
# REPEAT DEMO
# =========================

def repeat_demo():
    """Demonstrate itertools.repeat()."""

    message = input(
        "Enter a message: "
    )

    times = int(
        input("Repeat how many times? ")
    )

    print()

    for value in repeat(
            message,
            times
    ):
        print(value)


# =========================
# MENU
# =========================

def display_menu():

    print("""
===== LOG BATCH PROCESSOR =====

1. Generate Log Records
2. Process Logs in Batches
3. Show First N Logs
4. Combine Log Sources
5. Group Logs by Level
6. Round-Robin Server Processing
7. Repeat Demo
8. Exit
""")

    try:
        return int(
            input("Enter your choice: ")
        )

    except ValueError:
        return -1


# =========================
# MAIN PROGRAM
# =========================

def main():

    while True:

        choice = display_menu()

        if choice == 1:

            logs = generate_log_records()

            print("\nGenerated Logs")
            print("-" * 30)

            for log in logs[:10]:
                print(log)

            print(
                f"\nTotal Logs Generated: {len(logs)}"
            )

        elif choice == 2:
            process_logs_in_batches()

        elif choice == 3:
            show_first_n_logs()

        elif choice == 4:
            combine_log_sources()

        elif choice == 5:
            group_logs_by_level()

        elif choice == 6:
            round_robin_server_processing()

        elif choice == 7:
            repeat_demo()

        elif choice == 8:
            print("Goodbye!")
            break

        else:
            print(
                "Invalid choice. Please try again."
            )


if __name__ == "__main__":
    main()