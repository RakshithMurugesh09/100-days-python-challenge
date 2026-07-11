from art import logo

from utils import (
    get_birth_date,
    get_current_date,
    calculate_age,
    calculate_months_lived,
    calculate_days_lived,
    days_until_next_birthday,
    play_again
)


def display_results(
        birth_date,
        current_date,
        age,
        months_lived,
        days_lived,
        remaining_days
):
    print("\n" + "=" * 40)

    print(
        f"Today's Date          : "
        f"{current_date}"
    )

    print(
        f"Birth Date            : "
        f"{birth_date}"
    )

    print(
        f"Age                   : "
        f"{age} years"
    )

    print(
        f"Months Lived          : "
        f"{months_lived}"
    )

    print(
        f"Days Lived            : "
        f"{days_lived}"
    )

    print(
        f"Days Until Birthday   : "
        f"{remaining_days}"
    )

    print("=" * 40)


def main():
    print(logo)

    while True:

        birth_date = get_birth_date()

        current_date = get_current_date()

        age = calculate_age(
            birth_date,
            current_date
        )

        months_lived = (
            calculate_months_lived(age)
        )

        days_lived = (
            calculate_days_lived(
                birth_date,
                current_date
            )
        )

        remaining_days = (
            days_until_next_birthday(
                birth_date,
                current_date
            )
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
            print(
                "\n👋 Thanks for using "
                "Age Calculator!"
            )
            break


if __name__ == "__main__":
    main()