# 🐍 Day 45 - BeautifulSoup and Functional ETL Pipeline

## 📌 Overview

Day 45 contains two Python projects:

1. **BeautifulSoup (BS4)** - Reading, parsing, and extracting information from HTML.
2. **Functional ETL Pipeline** - Processing data using `map()`, `filter()`, and `reduce()`.

---

## 📁 Project Structure

```text
Day 45/
│
├── BS-4/
│   ├── index.html
│   └── main.py
│
├── Functional ETL Pipeline/
│   └── main.py
│
└── README.md
```

---

# 🌐 Project 1: BeautifulSoup (BS4)

## 🎯 Objective
The objective of this project is to understand how Python can read and extract information from HTML using the `BeautifulSoup` library.

The project contains:

- `index.html` - Contains the sample HTML content.
- `main.py` - Contains the Python code used to parse the HTML.

---

## 📦 Installation

Install the `beautifulsoup4` package:

```bash
pip install beautifulsoup4
```

Import `BeautifulSoup` into Python:

```python
from bs4 import BeautifulSoup
```

---

## 🧠 Concepts Practiced

- Reading an HTML file using Python
- Parsing HTML using BeautifulSoup
- Finding HTML tags
- Extracting text from HTML elements
- Accessing HTML tag attributes
- Understanding basic web scraping concepts

---

## 💻 Example

```python
from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

print(soup.title)
print(soup.title.string)

heading = soup.find("h1")

print(heading.text)
```

Example HTML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Day 45</title>
</head>
<body>
    <h1>Hello Python</h1>
    <p>Learning BeautifulSoup</p>
</body>
</html>
```

Expected output:

```text
<title>Day 45</title>
Day 45
Hello Python
```

---

# ⚙️ Project 2: Functional ETL Pipeline

## 🎯 Objective

The objective of this project is to understand how functional programming can be used to process and transform data.

The project focuses on:

- `map()`
- `filter()`
- `reduce()`

These functions can be combined to create an ETL-style data-processing pipeline.

---

## 🔄 What is ETL?

ETL stands for:

```text
Extract → Transform → Load
```

### Extract

Collect or read raw data from a source.

### Transform

Clean, filter, normalize, or modify the extracted data.

### Load

Store the processed data or produce the final result.

---

## 🔹 map()

The `map()` function applies a function to every item in an iterable.

```python
numbers = [1, 2, 3, 4]

result = map(lambda number: number * 2, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8]
```

---

## 🔹 filter()

The `filter()` function keeps only the elements that satisfy a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda number: number > 3, numbers)

print(list(result))
```

Output:

```text
[4, 5, 6]
```

---

## 🔹 reduce()

The `reduce()` function combines multiple values and produces a single result.

`reduce()` must be imported from the `functools` module.

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda first, second: first + second, numbers)

print(result)
```

Output:

```text
10
```

---

## 🔄 Functional ETL Flow

```text
Raw Data
   ↓
filter()
   ↓
Remove unwanted data
   ↓
map()
   ↓
Transform the data
   ↓
reduce()
   ↓
Generate the final result
```

---

## 💻 ETL Pipeline Example

```python
from functools import reduce

numbers = [10, 20, 30, 40, 50]

filtered_data = filter(
    lambda number: number >= 30,
    numbers
)

transformed_data = map(
    lambda number: number * 2,
    filtered_data
)

final_result = reduce(
    lambda first, second: first + second,
    transformed_data
)

print(final_result)
```

Data processing:

```text
Original data:
[10, 20, 30, 40, 50]

After filter():
[30, 40, 50]

After map():
[60, 80, 100]

After reduce():
240
```

---

## 🧠 What I Learned

During Day 45, I learned:

- How to parse HTML using BeautifulSoup
- How to extract HTML tags and text
- How to access HTML element attributes
- How Python can be used for basic HTML data extraction
- How functional programming works in Python
- How to use `map()` for data transformation
- How to use `filter()` for data selection
- How to use `reduce()` for data aggregation
- How to build a functional ETL pipeline

---

## 🛠️ Technologies Used

- Python
- HTML
- BeautifulSoup
- `beautifulsoup4`
- `functools`
- Functional programming

---

## 🚀 Key Takeaway

BeautifulSoup helps extract structured information from HTML:

```text
HTML → BeautifulSoup → Extracted Data
```

The Functional ETL Pipeline helps process and transform data:

```text
Raw Data → Filter → Map → Reduce → Final Result
```

Together, these projects provide a foundation for HTML parsing, data extraction, functional programming, and data-processing workflows.

---

## ✅ Day 45 Complete

Completed two projects:

- BeautifulSoup HTML Parser
- Functional ETL Pipeline

Continuing the Python learning journey one project at a time. 🚀