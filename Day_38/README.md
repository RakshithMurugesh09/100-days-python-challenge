# 🚀 Day 38 - Python Automation Projects

This day focuses on building practical automation projects using Python, APIs, Google Sheets, AI integration, and file processing.

---

# 📂 Project Structure

```text
Day_38/
│
├── Exercise Tracking/
│   ├── main.py
│   └── service_account.json
│
└── Log Batch Processor/
    └── main.py
```

---

# 🏋️ Project 1: Exercise Tracking with Gemini AI & Google Sheets

## 📌 Overview

This project allows users to enter workout activities in natural language.

The application uses Gemini AI to understand the workout description and automatically extracts:

- Exercise Name
- Duration
- Calories Burned
- Date
- Time

The processed data is then stored in a Google Sheet for tracking and analysis.

---

## ✨ Features

✅ Natural language workout input

✅ Gemini AI integration

✅ Automatic calorie estimation

✅ Google Sheets integration

✅ Date & time tracking

✅ Secure credential handling

✅ Modular and reusable code structure

---

## 🛠 Technologies Used

- Python
- Google Gemini API
- Google Sheets API
- gspread
- Google Service Account Credentials
- datetime module
- environment variables

---

## 📥 Example Input

```text
I ran for 30 minutes and cycled for 20 minutes.
```

---

## 📤 Example Output

```text
Exercise: Running
Duration: 30 min
Calories: 300

Exercise: Cycling
Duration: 20 min
Calories: 180
```

Stored automatically in Google Sheets.

---

## 🔐 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 📊 Google Sheet Columns

| Date | Time | Exercise | Duration | Calories |
|--------|--------|-----------|------------|------------|
| 2026-09-10 | 08:30 AM | Running | 30 | 300 |

---

# 📄 Project 2: Log Batch Processor

## 📌 Overview

A utility application that processes large log files efficiently.

The project reads log entries, analyzes them, filters important information, and generates useful summaries.

---

## ✨ Features

✅ Read log files

✅ Search logs

✅ Count log levels

✅ Error detection

✅ Warning detection

✅ Generate summaries

✅ Batch processing

✅ Memory-efficient operations

---

## 🛠 Technologies Used

- Python
- collections
- Counter
- deque
- file handling
- logging module

---

## 📥 Sample Log

```text
2026-09-10 10:00:01 | INFO | Application Started
2026-09-10 10:01:10 | WARNING | High Memory Usage
2026-09-10 10:03:20 | ERROR | Database Connection Failed
```

---

## 📊 Example Analysis

```text
INFO: 25
WARNING: 8
ERROR: 3

Most Frequent Level:
INFO
```

---

# 🎯 Learning Outcomes

By completing Day 38, you learned:

- Working with APIs
- AI-powered applications
- Prompt engineering basics
- Google Sheets automation
- Service Account authentication
- Environment variable management
- File handling
- Log analysis
- Data processing
- Python automation workflows

---



# 📚 Concepts Covered

- API Integration
- Google Cloud Service Accounts
- Google Sheets Automation
- Gemini AI
- JSON Credentials
- Environment Variables
- Functions
- Modular Programming
- File Processing
- Log Analysis
- Collections Module

---

# 🏆 Day 38 Completed

Built two real-world automation projects:

✅ Exercise Tracking with Gemini AI & Google Sheets

✅ Log Batch Processor

These projects demonstrate practical Python automation skills commonly used in DevOps, Cloud Support, Data Engineering, and Automation roles.

---

## 👨‍💻 Author

**Rakshith M**

100 Days of Python Challenge

Day 38