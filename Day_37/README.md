# Day 37 - Habit Tracking & Log Analytics Manager

## 📌 Overview

Day 37 focuses on two practical Python projects:

1. **Habit Tracking Application**
   - Uses REST APIs to create, update, and delete habit-tracking data.
   - Learned how to work with HTTP requests using the `requests` module.
   - Practiced API integration using `POST`, `PUT`, and `DELETE` methods.

2. **Log Analytics Manager**
   - Analyzes application log files.
   - Uses Python's `collections` module to efficiently process and summarize log data.
   - Provides insights into log levels, errors, warnings, and application activity.

---

# 📂 Project Structure

```text
Day_37/
│
├── Habit Tracking/
│   └── main.py
│
└── Log Analytics Manager/
    └── main.py
```

---

# 🚀 Project 1: Habit Tracking

## 📖 Description

A Python application that communicates with a Habit Tracking API to record daily habits and manage tracking data.

The project demonstrates how applications interact with REST APIs using different HTTP methods.

---

## 🎯 Features

- Create new habit entries using **POST**
- Update existing habit records using **PUT**
- Delete habit entries using **DELETE**
- Send and receive JSON data
- Handle API responses and status codes
- Work with authentication tokens and API endpoints

---

## 🛠 Technologies Used

- Python 3
- Requests Module
- REST APIs
- JSON

---

## 📚 Concepts Learned

### POST Request

Used to create new resources.

```python
requests.post()
```

### PUT Request

Used to update existing resources.

```python
requests.put()
```

### DELETE Request

Used to remove resources.

```python
requests.delete()
```

### Working with JSON

```python
response.json()
```

### Status Code Validation

```python
response.raise_for_status()
```

---

# 🚀 Project 2: Log Analytics Manager

## 📖 Description

A command-line application that analyzes application logs and generates useful insights.

The project focuses on efficient data processing using Python's `collections` module.

---

## 🎯 Features

- Read application log files
- Count occurrences of log levels
- Display recent log entries
- Search logs by keyword
- Generate summary statistics
- Track application activity patterns

---

## 🛠 Technologies Used

- Python 3
- Collections Module
- File Handling
- Logging Module

---

## 📚 Concepts Learned

### Counter

Count occurrences of log levels.

```python
from collections import Counter
```

Example:

```python
Counter({
    "INFO": 120,
    "WARNING": 15,
    "ERROR": 5
})
```

---

### Deque

Maintain a fixed-size history of recent log entries.

```python
from collections import deque
```

Example:

```python
recent_logs = deque(maxlen=10)
```

---

### File Processing

Read and analyze log files efficiently.

```python
with open("app.log", "r") as file:
    logs = file.readlines()
```

---

### Log Searching

Search log entries using keywords.

```python
if keyword.lower() in line.lower():
    print(line)
```

---

# 💡 Key Learning Outcomes

By completing Day 37, I learned:

✅ Working with REST APIs

✅ Sending POST requests

✅ Updating resources with PUT requests

✅ Removing resources with DELETE requests

✅ Handling JSON responses

✅ Understanding HTTP status codes

✅ Using Python Collections module

✅ Working with Counter for analytics

✅ Using Deque for history management

✅ Building real-world log analysis tools

✅ Processing and summarizing large datasets efficiently

---


# 📈 Future Enhancements

### Habit Tracking

- Add graphical dashboard
- Generate weekly reports
- Store habits in a database
- Add data visualization charts

### Log Analytics Manager

- Export analytics to CSV
- Generate PDF reports
- Create log trend charts
- Real-time log monitoring

---

# 🏆 Day 37 Summary

Day 37 introduced API-based application development and log analytics.

The Habit Tracking project provided hands-on experience with REST APIs and HTTP methods (`POST`, `PUT`, `DELETE`), while the Log Analytics Manager strengthened understanding of Python's `collections` module, data analysis techniques, and efficient log processing.

These skills are widely used in DevOps, Cloud Engineering, Site Reliability Engineering (SRE), and Backend Development.