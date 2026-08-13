# Day 26 - List & Dictionary Comprehensions

## 📚 Overview

Day 26 of the **100 Days of Python Challenge** focuses on:

- List Comprehensions
- Dictionary Comprehensions
- Data Transformation with Pandas
- Building a NATO Phonetic Alphabet Converter
- Understanding Python Decorators through a Function Logger project

---

# Project 1: NATO Alphabet Converter

## 🎯 Objective

Convert a user-entered word into its corresponding NATO phonetic alphabet representation.

Example:

Input:
```
Rakshith
```

Output:
```
['Romeo', 'Alpha', 'Kilo', 'Sierra', 'Hotel', 'India', 'Tango', 'Hotel']
```

---

## 🛠 Concepts Practiced

- Pandas DataFrames
- Dictionary Comprehensions
- Reading CSV Files
- User Input Handling
- Data Lookup

---

## 📂 Project Structure

```
NATO Alphabet Converter/
│
├── main.py
├── nato_phonetic_alphabet.csv
```

---

## 🚀 Features

- Reads NATO alphabet data from CSV.
- Converts letters into code words.
- Automatically handles uppercase input.
- Uses dictionary comprehension for quick lookups.

---

## 💻 Example

```python
Input: Python

Output:
['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
```

---

# Project 2: Function Logger

## 🎯 Objective

Create a reusable decorator that logs information every time a function is called.

---

## 🛠 Concepts Practiced

- Python Decorators
- *args and **kwargs
- Wrapper Functions
- Logging Function Calls
- Code Reusability

---

## 📂 Project Structure

```
Function Logger/
│
└── main.py
```

---

## 🚀 Features

- Logs function name.
- Logs passed arguments.
- Logs returned value.
- Works with any function using `*args` and `**kwargs`.

---

## 💻 Example

```python
@logger
def add(a, b):
    return a + b

add(5, 3)
```

Output:

```
Calling add
Arguments: (5, 3)
Returned: 8
```

---

# 📖 Key Learnings

### List Comprehension

Traditional:

```python
numbers = []

for n in range(1, 6):
    numbers.append(n)
```

Comprehension:

```python
numbers = [n for n in range(1, 6)]
```

---

### Dictionary Comprehension

```python
student_scores = {
    student: score
    for student, score in students.items()
}
```

---

### Decorators

A decorator allows you to extend the behavior of a function without modifying its original code.

Example:

```python
@logger
def greet(name):
    print(f"Hello {name}")
```

---

# 🎓 Skills Gained

✅ List Comprehensions

✅ Dictionary Comprehensions

✅ Pandas CSV Processing

✅ Decorators

✅ Function Wrapping

✅ Reusable Logging

✅ Data Transformation

---

# 🔥 Challenge Completed

Day 26 successfully completed as part of the **100 Days of Python Challenge**.

Author: **Rakshith M**

GitHub: **100-Days-Python-Challenge**