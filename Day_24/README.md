# 🐍 Day 24 - Mail Merge & Prime Number Finder

## 📌 Overview

Day 24 focused on two important Python concepts:

- 📂 File Handling through the Mail Merge Project
- ⚡ List Comprehension through the Prime Number Finder

These projects improved my understanding of reading and writing files, automating repetitive tasks, and writing cleaner Python code using list comprehensions.

---

# 📧 Project 1: Mail Merge

## 🎯 Objective

Generate personalized invitation letters automatically by replacing a placeholder in a template letter with names from a text file.

---

## 📂 Project Structure

```text
Mail Merge/
│
├── Input/
│   ├── Letter/
│   │   └── Starting_letter.txt
│   │
│   └── Names/
│       └── invited_names.txt
│
├── Output/
│   └── ReadyToSend/
│       ├── letter_for_Aang.txt
│       ├── letter_for_Appa.txt
│       ├── letter_for_Katara.txt
│       ├── letter_for_Sokka.txt
│       ├── letter_for_Toph.txt
│       └── letter_for_Zuko.txt
│
└── main.py
```

## 🧠 Concepts Practiced

### Reading Files

```python
with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()
```

### Reading a Template Letter

```python
with open("Input/Letter/Starting_letter.txt") as file:
    letter_template = file.read()
```

### Replacing Placeholders

```python
letter = letter_template.replace("[name]", person_name)
```

### Writing New Files

```python
with open(f"Output/ReadyToSend/letter_for_{person_name}.txt", "w") as file:
    file.write(letter)
```

## 📚 File Handling Skills Learned

✅ Opening files

✅ Reading files

✅ Writing files

✅ Creating multiple files automatically

✅ Working with folders and file paths

✅ Text processing

✅ Automation using Python

---

## 🚀 Example

### Template Letter

```text
Dear [name],

You are invited to my birthday party.

Regards,
Rakshith
```

### Generated Letter

```text
Dear Aang,

You are invited to my birthday party.

Regards,
Rakshith
```

---

# 🔢 Project 2: Prime Number Finder

## 🎯 Objective

Find prime numbers within a range using Python List Comprehension.

---

## 📂 Project Structure

```text
Prime Number Finder/
│
└── main.py
```

## 🧠 Concepts Practiced

### Basic List Comprehension

```python
numbers = [num for num in range(1, 11)]
```

### Conditional List Comprehension

```python
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
```

### Prime Number Logic

A prime number is divisible only by:

- 1
- Itself

Examples:

```text
2, 3, 5, 7, 11, 13, 17...
```

### Finding Prime Numbers

```python
primes = [
    num
    for num in range(2, 101)
    if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
]
```

## 📚 List Comprehension Skills Learned

✅ Creating lists efficiently

✅ Adding conditions inside comprehensions

✅ Generator expressions

✅ Prime number algorithms

✅ Writing cleaner and shorter code

✅ Improving readability

---

## 🚀 Example Output

```text
Prime Numbers from 1 to 100

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61,
67, 71, 73, 79, 83, 89, 97]
```
