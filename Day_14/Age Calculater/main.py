from datetime import datetime, date


def display_logo():
    logo = r"""
     █████╗  ██████╗ ███████╗
    ██╔══██╗██╔════╝ ██╔════╝
    ███████║██║  ███╗█████╗
    ██╔══██║██║   ██║██╔══╝
    ██║  ██║╚██████╔╝███████╗
    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝

          AGE CALCULATOR
    """
    return logo


def get_birth_date():
    while True:
        try:
            birth_date = input("Enter your birth date (DD-MM-YYYY): ")
            return datetime.strptime(birth_date, "%d-%m-%Y").date()

        except ValueError:
            print("❌ Invalid date! Please use DD-MM-YYYY format.")


def get_current_date():
    return date.today()


def calculate_age(birth_date, current_date):
    age = current_date.year - birth_date.year

    if (current_date.month, current_date.day) < (
        birth_date.month,
        birth_date.day
    ):
        age -= 1

    return age


def calculate_months_lived(age):
    return age * 12


def calculate_days_lived(birth_date, current_date):
    return (current_date - birth_date).days


def days_until_next_birthday(birth_date, current_date):
    next_birthday = date(
        current_date.year,
        birth_date.month,
        birth_date.day
    )

    if next_birthday < current_date:
        next_birthday = date(
            current_date.year + 1,
            birth_date.month,
            birth_date.day
        )

    return (next_birthday - current_date).days


def display_results(
    birth_date,
    current_date,
    age,
    months_lived,
    days_lived,
    remaining_days
):
    print(display_logo())

    print(f"Today's Date           : {current_date}")
    print(f"Birth Date             : {birth_date}")
    print(f"Age                    : {age} years")
    print(f"Approximate Months     : {months_lived}")
    print(f"Total Days Lived       : {days_lived}")
    print(f"Days Until Birthday    : {remaining_days}")

    print("=" * 40)


def play_again():
    choice = input(
        "\nDo you want to calculate another age? (y/n): "
    ).lower()

    return choice == "y"


def main():
    display_logo()

    while True:
        birth_date = get_birth_date()
        current_date = get_current_date()

        age = calculate_age(
            birth_date,
            current_date
        )

        months_lived = calculate_months_lived(age)

        days_lived = calculate_days_lived(
            birth_date,
            current_date
        )

        remaining_days = days_until_next_birthday(
            birth_date,
            current_date
        )

        display_results(
            birth_date,
            current_date,
            age,
            months_lived,
            days_lived,
            remaining_days
        )

        if not play_again():
            print("\n👋 Thank you for using Age Calculator!")
            break


if __name__ == "__main__":
    main()