# Tuple of month names
month_names = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# Tuple of days in each month (non-leap year)
days_in_each_month = (
    31,  # January
    28,  # February
    31,  # March
    30,  # April
    31,  # May
    30,  # June
    31,  # July
    31,  # August
    30,  # September
    31,  # October
    30,  # November
    31  # December
)

def check_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def display_days_in_month(month_number, year):
    """Display the number of days in a given month and year."""
    month_name = month_names[month_number - 1]

    if month_number == 2 and check_leap_year(year):
        print(f"{month_name} {year} has 29 days (leap year).")
    else:
        print(f"{month_name} {year} has {days_in_each_month[month_number - 1]} days.")


def run_days_in_month_checker():
    """Main function to run the days-in-month checker program."""
    print("📅 Days in a Month Checker")
    try:
        month_input = int(input("Enter month number (1-12): "))
        year_input = int(input("Enter year (e.g., 2025): "))

        if 1 <= month_input <= 12:
            display_days_in_month(month_input, year_input)
        else:
            print("❌ Invalid month number. Please enter a value between 1 and 12.")
    except ValueError:
        print("❌ Please enter valid numeric Input for both month and year.")


# Run the program
run_days_in_month_checker()
