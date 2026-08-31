# Day 32 – APIs & Automated Emailing

## 📌 Overview

Day 32 focuses on two important Python concepts:

1. **Working with APIs** – Fetching and displaying data from a public API.
2. **Sending Emails with SMTP** – Automating email delivery using Python.

These projects demonstrate how Python can communicate with external services over the internet.

---

## 📂 Project Structure

```text
Day_32
│
├── APIData Explorer
│   └── main.py
│
└── Automated Happy Birthday Email
    ├── letter templates
    │   ├── letter_1.txt
    │   ├── letter_2.txt
    │   └── letter_3.txt
    │
    └── main.py
```

---

# 🚀 Project 1: API Data Explorer

## Description

This project connects to a public REST API and retrieves TODO task data.

The application sends an HTTP request to the API endpoint, receives JSON data, and displays useful information about tasks.

### Concepts Practiced

- APIs
- HTTP Requests
- JSON Data
- Python `requests` module
- Error Handling

### Sample API

```text
https://jsonplaceholder.typicode.com/todos
```

### Features

✅ Connects to a public API

✅ Retrieves TODO data

✅ Parses JSON responses

✅ Displays task information

✅ Handles connection errors

### Example Output

```text
Task ID: 1
Title: delectus aut autem
Completed: False
```

---

# 🎂 Project 2: Automated Happy Birthday Email

## Description

This project automatically sends birthday wishes using Python's SMTP library.

The application:

- Checks birthday information
- Randomly selects a birthday template
- Replaces placeholders with recipient details
- Sends an email automatically

### Concepts Practiced

- Email Automation
- SMTP Protocol
- File Handling
- Environment Variables
- Random Selection
- String Formatting

### Features

✅ Sends email automatically

✅ Uses multiple birthday templates

✅ Random template selection

✅ Secure credential management using environment variables

✅ Personalized birthday messages

### Letter Templates

The application uses templates stored in:

```text
letter templates/
```

Example:

```text
Happy Birthday [NAME]!

Wishing you a wonderful day filled with happiness and success.

Best Regards,
Rakshith
```

---

## 🛠 Technologies Used

- Python 3
- Requests Library
- SMTP (smtplib)
- JSON APIs
- Environment Variables
- File Handling

---

## 📚 What I Learned

### API Project

- How APIs work
- Making HTTP GET requests
- Reading JSON data
- Working with third-party services

### Email Automation Project

- Using SMTP servers
- Sending emails with Python
- Managing sensitive credentials
- Creating automated workflows

--

## 🔒 Environment Variables

For security reasons, email credentials should be stored in environment variables.

Example:

```python
import os

EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["MY_PASSWORD"]
```

Never hardcode passwords inside your Python scripts.

---

## 🎯 Day 32 Learning Outcome

By completing Day 32, I learned how to:

- Consume data from APIs
- Process JSON responses
- Automate tasks using external services
- Send emails programmatically
- Handle credentials securely
- Build real-world automation solutions

---

### 100 Days of Python Challenge

**Day 32 Completed ✅**

Topics Covered:
- APIs
- JSON Data
- Requests Module
- SMTP
- Email Automation
- Environment Variables