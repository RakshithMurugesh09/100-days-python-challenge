import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def display_menu():
    # TODO
    print('''========================================
          API DATA EXPLORER
========================================

1. Get User
2. Get Todo
3. Search Todo
4. View API Status
5. Exit

========================================''')
    return input("Enter your choice: ")

def display_user(data):
    print("\n========== USER INFORMATION ==========\n")
    print("ID : ", data["id"])
    print("Name : ", data["name"])
    print("Username : ", data["username"])
    print("Email : ", data["email"])
    print("Phone Number : ", data["phone"])
    print(f"Website : www.{data['website']}")
    print(" ")


def get_user():
    try:
        user_id = int(input("Enter your User ID: "))

        if user_id <= 0:
            print("User ID must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    try:
        response = requests.get(f"{BASE_URL}/users/{user_id}",timeout=10)

        response.raise_for_status()

        data = response.json()

        display_user(data)

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error occurred: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")

def display_todo(data):
    print("\n========== TODO INFORMATION ==========\n")
    print("ID : ", data["id"])
    print("User Id : ", data["userId"])
    print("Title : ", data["title"])
    if data["completed"]:
        print("Work Status: Completed")
    else:
        print("Work Status: Not completed")

def get_todo():
    # TODO
    try:
        todo_id = int(input("Enter your Todo ID: "))
        if todo_id <= 0:
            print("Todo ID must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        response = requests.get(f"{BASE_URL}/todos/{todo_id}",timeout=10)

        response.raise_for_status()

        data = response.json()

        display_todo(data)

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error occurred: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")

def search_todo():
    # TODO
    try:
        response = requests.get(f"{BASE_URL}/todos",timeout=10)
        data = response.json()
        response.raise_for_status()

        while True:
            key_words = input("Enter your search keywords: ").strip().lower()
            if key_words:
                break
            print("Keyword cannot be empty.")

        matching_todos = []

        for elements in data:
            if key_words in elements.get("title", "").lower():
                matching_todos.append(elements)

        if not matching_todos:
            print("No search results found.")
            return

        print(f"Found {len(matching_todos)} matching todos.")
        for todo in matching_todos:
            display_todo(todo)


    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error occurred: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")

def display_app_status(response):
    print("\n======== APPLICATION STATUS =======\n")
    print("API URL : ", response.url)
    print("API Status : ", response.status_code)
    print(f"Response Time: {response.elapsed.total_seconds()} seconds")
    if 200 <= response.status_code < 300:
        print("API Status: API is healthy ✅")

def check_api_status():
    # TODO
    try:
        response = requests.get(BASE_URL,timeout=10)
        response.raise_for_status()

        display_app_status(response)

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error occurred: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")


def main():
    while True:

        choice = display_menu()

        if choice == "1":
            get_user()

        elif choice == "2":
            get_todo()

        elif choice == "3":
            search_todo()

        elif choice == "4":
            check_api_status()

        elif choice == "5":
            print("Thank you for using API Data Explorer! 👋")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()