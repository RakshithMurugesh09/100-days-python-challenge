from openpyxl import load_workbook, Workbook


def create_excel_file():
    wb = Workbook()
    ws = wb.active
    ws.title = "Expense Tracker"
    ws.append(["Date", "Category", "Description", "Amount"])
    wb.save('Expense Tracker.xlsx')

    print("Expense Tracker Excel File has Created")

def add_expense():
    try:
        wb = load_workbook('Expense Tracker.xlsx')
        ws = wb["Expense Tracker"]
        print("Try")
    except FileNotFoundError:
        create_excel_file()
        print("Except")

    user_date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    amount = input("Enter Amount: ")
    ws.append([user_date, category, description, amount])
    wb.save('Expense Tracker.xlsx')
    print("✅ Expense added successfully.")

def view_expenses():
    try:
        wb = load_workbook('Expense Tracker.xlsx')
        ws = wb["Expense Tracker"]
        print("========== EXPENSES ==========")
        for i in range (1, ws.max_row):
            print("Date = ", ws.cell(row=i+1, column=1).value)
            print("Category = ", ws.cell(row=i+1, column=2).value)
            print("Description = ", ws.cell(row=i+1, column=3).value)
            print("Amount = ", ws.cell(row=i+1, column=4).value)
            print("\n ---------------------------------- \n")
    except FileNotFoundError:
        print("Expense Tracker Excel File has Not Created")

def show_total_spent():
    try:
        wb = load_workbook('Expense Tracker.xlsx')
        ws = wb["Expense Tracker"]
        total_spent = sum(float(ws.cell(row=i+1, column=4).value) for i in range(1, ws.max_row))
        print("Total Spent = ", total_spent)
    except FileNotFoundError:
        print("Expense Tracker Excel File has Not Created")


show_total_spent()


