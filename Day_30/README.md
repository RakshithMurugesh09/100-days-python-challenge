# 💰 Expense Tracker

A simple Command-Line Expense Tracker built with Python and CSV file handling.

This application allows users to record, view, search, and analyze their expenses. All expense data is stored in a CSV file, making it easy to maintain and review spending habits.

---

## 🚀 Features

✅ Add New Expense

✅ View All Expenses

✅ Search Expenses

✅ Delete Expense

✅ Display Total Expenses

✅ Category-wise Expense Summary

✅ Automatic CSV File Creation

✅ Input Validation

✅ Error Handling

---

## 📂 Project Structure

```
Expense_Tracker/
│
├── main.py
├── expenses.csv
├── README.md
└── requirements.txt
```

---

## 📊 Expense Information Stored

Each expense contains:

| Field | Description |
|---------|-------------|
| Date | Expense Date |
| Category | Expense Category |
| Description | Expense Description |
| Amount | Expense Amount |

Example:

```csv
Date,Category,Description,Amount
25-08-2026,Food,Lunch,150
25-08-2026,Transport,Bus Ticket,40
```

---

## 🖥️ Menu Options

```text
========== EXPENSE TRACKER ==========

1. Add Expense
2. View Expenses
3. Search Expense
4. Delete Expense
5. Total Expenses
6. Category Summary
7. Exit
```

---

## ➕ Add Expense

The user enters:

```text
Enter date (DD-MM-YYYY):
Enter category:
Enter description:
Enter amount:
```

Example:

```text
Date: 25-08-2026
Category: Food
Description: Dinner
Amount: ₹250
```

---

## 📋 View Expenses

Displays all expenses in a formatted manner.

Example:

```text
---------------------------------------------
Expense
---------------------------------------------
Date        : 25-08-2026
Category    : Food
Description : Dinner
Amount      : ₹250.00
---------------------------------------------
```

---

## 🔍 Search Expenses

Search by:

- Category
- Description
- Date

Example:

```text
Enter search term: food
```

Result:

```text
Found 2 expense(s).
```

---

## ❌ Delete Expense

Delete an expense by selecting its number.

Example:

```text
Enter expense number to delete:
```

---

## 💵 Total Expenses

Calculates overall spending.

Example:

```text
Total Expenses: ₹5,450.00
```

---

## 📈 Category Summary

Displays spending grouped by category.

Example:

```text
========== CATEGORY SUMMARY ==========

Food            : ₹1500.00
Transport       : ₹650.00
Entertainment   : ₹1200.00
```

---

## 🛠️ Technologies Used

- Python 3
- CSV Module
- Datetime Module
- OS Module

---

## ✅ Skills Practiced

- Functions
- Loops
- Dictionaries
- Lists
- File Handling
- CSV Operations
- Exception Handling
- Input Validation
- Modular Programming

---

## 🎯 Learning Outcome

This project helped in understanding:

- Working with CSV files
- CRUD Operations (Create, Read, Update, Delete)
- Data Validation
- Error Handling
- Building Real-World CLI Applications

---

## 📌 Future Improvements

- Monthly Reports
- Expense Categories Dashboard
- Data Visualization using Matplotlib
- Export to Excel
- Budget Tracking
- SQLite Database Integration
- GUI Version using Tkinter

