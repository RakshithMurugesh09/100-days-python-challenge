# 📅 Day 25 - Pandas, Turtle Graphics & Functional Programming

## 🎯 Overview

Day 25 focused on learning **Pandas for data analysis**, building an interactive **Indian States Guessing Game** using **Turtle Graphics**, and exploring **Functional Programming** concepts using **Lambda, Map, Filter, and Reduce**.

The projects helped improve skills in:

- Data Analysis with Pandas
- CSV File Handling
- Data Filtering and Aggregation
- Turtle Graphics
- Functional Programming
- Working with Real-World Data

---

# 📂 Project Structure

```text
Day_25/
│
├── Squirrel Data Analysis/
│   ├── main.py
│   └── Squirrel_data.csv
│
├── states_game/
│   ├── main.py
│   ├── india_states.csv
│   ├── india_map.gif
│   └── states_to_learn.csv
│
├── Student Grading System/
│   └── main.py
│
└── README.md
```

---

# 🐿️ Project 1: Squirrel Data Analysis

## 📌 Objective

Analyze squirrel census data using Pandas and extract useful insights from the dataset.

## ✅ Features

- Load squirrel dataset from CSV
- Count squirrels based on fur color
- Analyze age distribution
- Handle missing values
- Filter records using conditions
- Generate summary statistics
- Practice DataFrame operations

## 🛠 Concepts Used

- Pandas DataFrame
- CSV File Handling
- Data Filtering
- Boolean Indexing
- value_counts()
- isna() / notna()
- Data Aggregation

## Example Analysis

```python
data["Primary Fur Color"].value_counts()
```

### Sample Output

```text
Gray       2473
Cinnamon    392
Black       103
```

## 📚 Skills Learned

- Loading and exploring datasets
- Working with DataFrames
- Filtering and querying data
- Handling null values
- Extracting meaningful information from data

---

# 🇮🇳 Project 2: Indian States Guessing Game

## 📌 Objective

Create an interactive game where users guess Indian states and see them displayed on an India map.

## ✅ Features

- Interactive Turtle GUI
- Indian map visualization
- User input through Turtle text box
- Track correctly guessed states
- Display state names on map coordinates
- Store unguessed states in a CSV file

## 🛠 Concepts Used

- Turtle Graphics
- Pandas
- CSV Files
- Lists
- Loops
- Conditional Statements
- Data Exporting

## 🎮 How It Works

1. India map opens.
2. User enters a state name.
3. If the answer is correct:
   - State name appears on the map.
   - Score increases.
4. Game continues until all states are guessed.
5. Remaining states are saved to:

```text
states_to_learn.csv
```

## 📚 Skills Learned

- Combining Pandas with Turtle Graphics
- Working with coordinate-based datasets
- Creating educational games
- Exporting data using Pandas

---

# 🎓 Project 3: Student Grading System

## 📌 Objective

Build a grading system using Functional Programming techniques such as Lambda, Map, Filter, and Reduce.

## ✅ Features

- Store student records
- Automatically assign grades
- Display highest and lowest marks
- Calculate average marks
- Show passed students
- Demonstrate Lambda, Map, Filter, and Reduce

## 🛠 Concepts Used

### Lambda

```python
lambda x: x * 2
```

### Map

```python
marks = list(map(lambda s: s["marks"], students))
```

### Filter

```python
passed_students = list(
    filter(lambda s: s["marks"] >= 35, students)
)
```

### Reduce

```python
from functools import reduce

total_marks = reduce(
    lambda total, student: total + student["marks"],
    students,
    0
)
```

## 📊 Grade Criteria

| Marks | Grade |
|---------|---------|
| 90 - 100 | A |
| 75 - 89 | B |
| 60 - 74 | C |
| 35 - 59 | D |
| 0 - 34 | F |

## Sample Output

```text
Rakshith : 85 : B
Anu      : 42 : D
John     : 22 : F
Kiran    : 97 : A

Total Students : 4
Highest Marks  : 97
Lowest Marks   : 22
Average Marks  : 61.5
```

## 📚 Skills Learned

- Functional Programming
- Lambda Expressions
- Map Function
- Filter Function
- Reduce Function
- Data Transformation
- Data Aggregation

---

# 🏆 Day 25 Summary

Day 25 combined **Data Analysis**, **GUI Development**, and **Functional Programming** into three practical projects. Through these projects I learned how to analyze datasets using Pandas, create interactive map-based games using Turtle Graphics, and write cleaner, more efficient code using Lambda, Map, Filter, and Reduce.

### ✅ Projects Completed

1. 🐿️ Squirrel Data Analysis
2. 🇮🇳 Indian States