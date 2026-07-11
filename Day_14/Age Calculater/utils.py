from datetime import datetime, date


def get_birth_date():
    while True:
        try:
            birth_date = input(
                "Enter your birth date (DD-MM-YYYY): "
            )

            return datetime.strptime(
                birth_date,
                "%d-%m-%Y"
            ).date()

        except ValueError:
            print(
                "❌ Invalid date! Use DD-MM-YYYY format."
            )


def get_current_date():
    return date.today()


def calculate_age(birth_date, current_date):
    age = current_date.year - birth_date.year

    if (
            current_date.month,
            current_date.day
    ) < (
            birth_date.month,
            birth_date.day
    ):
        age -= 1

    return age


def calculate_months_lived(age):
    return age * 12


def calculate_days_lived(
        birth_date,
        current_date
):
    return (
        current_date - birth_date
    ).days


def days_until_next_birthday(
        birth_date,
        current_date
):
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

    return (
        next_birthday - current_date
    ).days


def play_again():
    while True:
        choice = input(
            "\nCalculate again? (y/n): "
        ).lower()

        if choice in ["y", "n"]:
            return choice == "y"

        print(
            "❌ Enter y or n only."
        )