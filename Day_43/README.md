# Day 43 - CSS Foundations & Pluggable Data Ingestion

This repository contains my Day 43 learning activities from my coding journey. The day focuses on learning CSS fundamentals and implementing a Python project using the Pluggable Data Ingestion design pattern.

---

## 📚 Table of Contents

- CSS Foundations
  - Basic CSS
  - Color Vocabulary
  - CSS Selectors
- Pluggable Data Ingestion
- Technologies Used
- Learning Outcomes
- Project Structure

---

# 🎨 CSS Foundations

The CSS Foundations section introduces the core concepts required to style web pages.

## 1. Basic CSS

Topics covered:

- Inline CSS
- Internal CSS
- External CSS
- Styling HTML elements
- Applying colors and fonts
- Understanding CSS syntax

Example:

```css
h1 {
    color: blue;
}
```

---

## 2. Color Vocabulary

Topics covered:

- CSS color names
- RGB colors
- HEX colors
- Background colors
- Text colors

Example:

```css
body {
    background-color: lightblue;
}
```

---

## 3. CSS Selectors

Topics covered:

- Element selectors
- Class selectors
- ID selectors
- Group selectors
- Descendant selectors

Example:

```css
.red-text {
    color: red;
}
```

---

# 🐍 Pluggable Data Ingestion

This Python project demonstrates how to create a flexible data ingestion system using Abstract Base Classes (ABC).

## Features

- Common interface for all data sources
- Easily extendable architecture
- Supports multiple data providers
- Demonstrates abstraction and polymorphism

## Components

### DataSource (Abstract Class)

Defines the contract for:

- connect()
- read()
- close()

### APIDataSource

Simulates data retrieval from an API.

### CSVDataSource

Simulates reading data from CSV files.

### DatabaseDataSource

Simulates reading data from a database.

### DataPipeline

Processes data from any compatible data source.

---

## Example Output

```text
Connecting to API...
Reading API data...
Closing API connection...
```

---

# 🛠 Technologies Used

- HTML5
- CSS3
- Python 3
- Object-Oriented Programming
- Abstract Base Classes (ABC)

---

# 🎯 Learning Outcomes

After completing Day 43, I learned:

- CSS styling fundamentals
- Different CSS selector types
- Working with colors in CSS
- Creating reusable Python architectures
- Implementing abstraction using ABC
- Applying polymorphism in real-world scenarios
- Building extensible data ingestion systems

---

# 📂 Project Structure

```text
Day_43/
│
├── CSS Foundation/
│   ├── Basic CSS/
│   ├── ColorVocab/
│   └── CSS Selectors/
│
└── Pluggable Data Ingestion/
    └── main.py
```

---

## 🚀 Author

Rakshith Murugesh

Day 43 of my learning journey focusing on Web Development and Python Design Patterns.