import subprocess

# Store command history
history_of_work = {}


def add_to_history(command, status, return_code):
    global history_of_work
    history_of_work = {
        "Command": command,
        "Status": status,
        "Return Code": return_code
    }


def display_menu():
    print("""
===== SYSTEM COMMAND MANAGER =====

1. Python Version
2. System Information
3. IP Configuration
4. Ping Localhost
5. Run Custom Command
6. Command History
7. Exit
""")
    return input("Select an option (1-7): ")


def python_version():
    try:
        result = subprocess.run(["python", "--version"],timeout=5,capture_output=True,text=True)

        if result.returncode == 0:
            output = result.stdout.strip() or result.stderr.strip()
            print(output)

            add_to_history(
                "python --version",
                "SUCCESS",
                result.returncode
            )

        else:
            print("Python Version Error")

            add_to_history(
                "python --version",
                "FAILED",
                result.returncode
            )

    except subprocess.TimeoutExpired:
        print("Python Version Timeout")


def system_info():
    try:
        result = subprocess.run(["systeminfo"],timeout=15, capture_output=True,text=True)

        if result.returncode == 0:
            print(result.stdout)

            add_to_history(
                "systeminfo",
                "SUCCESS",
                result.returncode
            )

        else:
            print("System Info Error")

            add_to_history(
                "systeminfo",
                "FAILED",
                result.returncode
            )

    except subprocess.TimeoutExpired:
        print("System Info Timeout")


def ip_configuration():
    try:
        result = subprocess.run(["ipconfig"],timeout=5,capture_output=True,text=True)

        if result.returncode == 0:
            print(result.stdout)

            add_to_history(
                "ipconfig",
                "SUCCESS",
                result.returncode
            )

        else:
            print("IP Configuration Error")

            add_to_history(
                "ipconfig",
                "FAILED",
                result.returncode
            )

    except subprocess.TimeoutExpired:
        print("IP Configuration Timeout")


def ping_localhost():
    try:
        result = subprocess.run( ["ping", "127.0.0.1"],timeout=5,capture_output=True,text=True)

        if result.returncode == 0:
            print(result.stdout)

            add_to_history(
                "ping 127.0.0.1",
                "SUCCESS",
                result.returncode
            )

        else:
            print("Ping Error")

            add_to_history(
                "ping 127.0.0.1",
                "FAILED",
                result.returncode
            )

    except subprocess.TimeoutExpired:
        print("Ping Timeout")


def custom_command():
    print("\nAvailable Commands:")
    print("python --version")
    print("ipconfig")
    print("hostname")
    print("whoami")

    user_command = input("\nCommand: ").strip()

    try:
        result = subprocess.run( user_command,timeout=5,capture_output=True,text=True)

        if result.returncode == 0:

            if result.stdout:
                print(result.stdout)

            add_to_history(
                user_command,
                "SUCCESS",
                result.returncode
            )

        else:
            print("Command Failed")

            if result.stderr:
                print(result.stderr)

            add_to_history(
                user_command,
                "FAILED",
                result.returncode
            )

    except FileNotFoundError:
        print("Command not found")

    except subprocess.TimeoutExpired:
        print("Command Timeout")


def command_history():
    print("\n===== LAST COMMAND =====")

    if not history_of_work:
        print("No commands executed yet.")
        return

    print(f"""
Command     : {history_of_work['Command']}
Status      : {history_of_work['Status']}
Return Code : {history_of_work['Return Code']}
""")


def main():

    while True:

        choice = display_menu()

        if choice == "1":
            python_version()

        elif choice == "2":
            system_info()

        elif choice == "3":
            ip_configuration()

        elif choice == "4":
            ping_localhost()

        elif choice == "5":
            custom_command()

        elif choice == "6":
            command_history()

        elif choice == "7":
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()