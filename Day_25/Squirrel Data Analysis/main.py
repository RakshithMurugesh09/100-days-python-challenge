import pandas as pd


FILE_NAME = "Squirrel_data.csv"


def load_data():
    """Load squirrel CSV file."""
    try:
        data = pd.read_csv(FILE_NAME)
        return data

    except FileNotFoundError:
        print(f"\nError: {FILE_NAME} file not found.")
        print("Please keep Squirrel_data.csv in the same folder as main.py")
        return None

    except Exception as e:
        print("Error while reading file:", e)
        return None


def total_squirrels(data):
    """Challenge 1: Show total number of squirrels."""
    print("\nTotal Squirrels:", len(data))


def show_unique_fur_colors(data):
    """Challenge 2: Show available fur colors."""
    print("\nAvailable Fur Colors")
    print("-" * 25)

    colors = data["Primary Fur Color"].dropna().unique()

    for color in colors:
        print(color)


def fur_color_analysis(data):
    """Challenge 3 and 14: Search and count squirrels by fur color."""
    fur_color = input("\nEnter Fur Color: ").strip().title()

    available_colors = data["Primary Fur Color"].dropna().unique().tolist()

    if fur_color not in available_colors:
        print("Fur Color not available.")
        print("Available colors:", available_colors)
        return

    fur_color_count = (data["Primary Fur Color"] == fur_color).sum()

    print(f"{fur_color} squirrels: {fur_color_count}")


def all_fur_color_counts(data):
    """Challenge 4: Count all primary fur colors."""
    print("\nFur Color Counts")
    print("-" * 25)

    fur_counts = data["Primary Fur Color"].value_counts()

    print(fur_counts)


def age_analysis(data):
    """Challenge 5: Count squirrels by age."""
    print("\nAge Analysis")
    print("-" * 25)

    age_data = data["Age"].value_counts()

    print(f"Adult    : {age_data.get('Adult', 0)}")
    print(f"Juvenile : {age_data.get('Juvenile', 0)}")


def shift_analysis(data):
    """Challenge 6 and 18: Count squirrels by shift."""
    print("\nShift Analysis")
    print("-" * 25)

    shift_data = data["Shift"].value_counts()

    print(f"AM : {shift_data.get('AM', 0)}")
    print(f"PM : {shift_data.get('PM', 0)}")


def missing_fur_colors(data):
    """Challenge 7: Count missing Primary Fur Color values."""
    missing_count = data["Primary Fur Color"].isna().sum()

    print("\nMissing Fur Color Count:", missing_count)


def fur_color_percentages(data):
    """Challenge 8: Show fur color percentages."""
    print("\nFur Color Percentages")
    print("-" * 25)

    total = len(data)
    fur_counts = data["Primary Fur Color"].value_counts()

    for color, count in fur_counts.items():
        percentage = round((count / total) * 100, 2)
        print(f"{color}: {percentage}%")


def most_common_fur_color(data):
    """Challenge 9: Find most common fur color."""
    fur_counts = data["Primary Fur Color"].value_counts()

    if fur_counts.empty:
        print("\nNo fur color data available.")
        return

    most_common = fur_counts.idxmax()
    count = fur_counts.max()

    print("\nMost Common Fur Color")
    print("-" * 25)
    print(f"{most_common}: {count}")


def activity_analysis(data):
    """Challenge 10, 11 and 15: Search activity count."""
    activities = ["Running", "Eating", "Climbing"]

    user_input = input("\nEnter Activity (Running/Eating/Climbing): ").strip().title()

    if user_input not in activities:
        print("Activity not available.")
        print("Available activities:", activities)
        return

    activity_count = data[user_input].sum()

    print(f"{user_input} squirrels: {activity_count}")


def compare_activities(data):
    """Challenge 12 and 17: Compare activities and find top activity."""
    activities = ["Running", "Eating", "Climbing"]

    activity_report = {}

    for activity in activities:
        activity_report[activity] = data[activity].sum()

    print("\nActivity Report")
    print("-" * 25)

    for activity, count in activity_report.items():
        print(f"{activity}: {count}")

    most_common_activity = max(activity_report, key=activity_report.get)

    print("\nMost Common Activity:", most_common_activity)


def missing_data_report(data):
    """Challenge 19: Show missing values for important columns."""
    columns = ["Age", "Primary Fur Color", "Location"]

    print("\nMissing Data Report")
    print("-" * 35)
    print(f"{'Column':<25} {'Missing'}")
    print("-" * 35)

    for column in columns:
        if column in data.columns:
            missing_count = data[column].isna().sum()
            print(f"{column:<25} {missing_count}")
        else:
            print(f"{column:<25} Column not found")


def export_reports(data):
    """Challenge 16: Export multiple reports as CSV files."""

    # Fur color report
    fur_report = data["Primary Fur Color"].value_counts().reset_index()
    fur_report.columns = ["Fur Color", "Count"]
    fur_report.to_csv("fur_color_report.csv", index=False)

    # Age report
    age_report = data["Age"].value_counts().reset_index()
    age_report.columns = ["Age", "Count"]
    age_report.to_csv("age_report.csv", index=False)

    # Shift report
    shift_report = data["Shift"].value_counts().reset_index()
    shift_report.columns = ["Shift", "Count"]
    shift_report.to_csv("shift_report.csv", index=False)

    # Activity report
    activities = ["Running", "Eating", "Climbing"]

    activity_data = []

    for activity in activities:
        activity_data.append({
            "Activity": activity,
            "Count": data[activity].sum()
        })

    activity_report = pd.DataFrame(activity_data)
    activity_report.to_csv("activity_report.csv", index=False)

    # Missing data report
    missing_report = data.isna().sum().reset_index()
    missing_report.columns = ["Column", "Missing Count"]
    missing_report.to_csv("missing_data_report.csv", index=False)

    print("\nReports exported successfully!")
    print("- fur_color_report.csv")
    print("- age_report.csv")
    print("- shift_report.csv")
    print("- activity_report.csv")
    print("- missing_data_report.csv")


def dashboard(data):
    """Challenge 20: Show complete squirrel statistics dashboard."""
    print("\n" + "=" * 45)
    print("        SQUIRREL STATISTICS DASHBOARD")
    print("=" * 45)

    total = len(data)

    fur_counts = data["Primary Fur Color"].value_counts()
    age_counts = data["Age"].value_counts()

    activities = ["Running", "Eating", "Climbing"]
    activity_report = {}

    for activity in activities:
        activity_report[activity] = data[activity].sum()

    most_common_activity = max(activity_report, key=activity_report.get)

    print(f"\nTotal Squirrels: {total}")

    print("\nFur Colors")
    print("-" * 25)

    for color, count in fur_counts.items():
        print(f"{color:<15}: {count}")

    print("\nAges")
    print("-" * 25)
    print(f"{'Adult':<15}: {age_counts.get('Adult', 0)}")
    print(f"{'Juvenile':<15}: {age_counts.get('Juvenile', 0)}")

    print("\nActivities")
    print("-" * 25)

    for activity, count in activity_report.items():
        print(f"{activity:<15}: {count}")

    print("\nMost Common Activity:", most_common_activity)
    print("Missing Fur Colors:", data["Primary Fur Color"].isna().sum())

    print("=" * 45)


def pandas_value_counts_demo(data):
    """Challenge 22: Practice value_counts()."""
    print("\nUsing value_counts()")
    print("-" * 25)

    print(data["Primary Fur Color"].value_counts())


def pandas_groupby_demo(data):
    """Challenge 23: Practice groupby()."""
    print("\nUsing groupby()")
    print("-" * 25)

    group_data = data.groupby("Primary Fur Color").size()

    print(group_data)


def sorted_fur_color_counts(data):
    """Challenge 24: Sort fur color counts high to low."""
    print("\nSorted Fur Color Counts")
    print("-" * 25)

    fur_counts = data["Primary Fur Color"].value_counts().sort_values(ascending=False)

    print(fur_counts)


def complete_summary_csv(data):
    """Challenge 25: Create final squirrel summary CSV."""
    total_squirrels_count = len(data)

    fur_counts = data["Primary Fur Color"].value_counts()
    age_counts = data["Age"].value_counts()
    shift_counts = data["Shift"].value_counts()

    activities = ["Running", "Eating", "Climbing"]

    summary_data = []

    summary_data.append({
        "Category": "Total",
        "Name": "Total Squirrels",
        "Count": total_squirrels_count
    })

    for color, count in fur_counts.items():
        summary_data.append({
            "Category": "Fur Color",
            "Name": color,
            "Count": count
        })

    for age, count in age_counts.items():
        summary_data.append({
            "Category": "Age",
            "Name": age,
            "Count": count
        })

    for shift, count in shift_counts.items():
        summary_data.append({
            "Category": "Shift",
            "Name": shift,
            "Count": count
        })

    for activity in activities:
        summary_data.append({
            "Category": "Activity",
            "Name": activity,
            "Count": data[activity].sum()
        })

    summary_df = pd.DataFrame(summary_data)
    summary_df.to_csv("squirrel_summary.csv", index=False)

    print("\nsquirrel_summary.csv created successfully!")


def display_menu():
    """Display menu options."""
    print("\n" + "=" * 45)
    print("          SQUIRREL CENSUS ANALYZER")
    print("=" * 45)
    print("1. Total Squirrels")
    print("2. Show Unique Fur Colors")
    print("3. Search Fur Color")
    print("4. All Fur Color Counts")
    print("5. Age Analysis")
    print("6. Shift Analysis")
    print("7. Missing Fur Colors")
    print("8. Fur Color Percentages")
    print("9. Most Common Fur Color")
    print("10. Search Activity")
    print("11. Compare Activities")
    print("12. Missing Data Report")
    print("13. Export Reports")
    print("14. Dashboard")
    print("15. value_counts Demo")
    print("16. groupby Demo")
    print("17. Sorted Fur Color Counts")
    print("18. Create Complete Summary CSV")
    print("0. Exit")
    print("=" * 45)


def main():
    """Main program."""
    data = load_data()

    if data is None:
        return

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            total_squirrels(data)

        elif choice == "2":
            show_unique_fur_colors(data)

        elif choice == "3":
            fur_color_analysis(data)

        elif choice == "4":
            all_fur_color_counts(data)

        elif choice == "5":
            age_analysis(data)

        elif choice == "6":
            shift_analysis(data)

        elif choice == "7":
            missing_fur_colors(data)

        elif choice == "8":
            fur_color_percentages(data)

        elif choice == "9":
            most_common_fur_color(data)

        elif choice == "10":
            activity_analysis(data)

        elif choice == "11":
            compare_activities(data)

        elif choice == "12":
            missing_data_report(data)

        elif choice == "13":
            export_reports(data)

        elif choice == "14":
            dashboard(data)

        elif choice == "15":
            pandas_value_counts_demo(data)

        elif choice == "16":
            pandas_groupby_demo(data)

        elif choice == "17":
            sorted_fur_color_counts(data)

        elif choice == "18":
            complete_summary_csv(data)

        elif choice == "0":
            print("\nThank you for using Squirrel Census Analyzer!")
            break

        else:
            print("Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    main()
