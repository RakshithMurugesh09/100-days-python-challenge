from art import logo

from converter import (
    show_currencies,
    convert_currency,
    get_amount,
    get_currency,
    play_again,
)


def main():

    print(logo)

    while True:

        show_currencies()

        amount = get_amount()

        currency = get_currency()

        converted_amount = convert_currency(
            amount,
            currency
        )

        print(
            f"\n₹{amount:.2f} = "
            f"{converted_amount:.2f} {currency}"
        )

        if not play_again():
            print("\nThank you for using Currency Converter!")
            break


if __name__ == "__main__":
    main()