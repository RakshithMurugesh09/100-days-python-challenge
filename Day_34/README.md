# 🚀 Day 34 - Environment & System Information Manager & GUI Quiz App

Welcome to **Day 34** of my **100 Days of Python Challenge**.

Today, I built two exciting Python projects that helped me understand:

- Environment Variables & Secure Configuration
- Operating System Information
- API Integration
- Object-Oriented Programming (OOP)
- GUI Development with Tkinter

---

# 🖥️ Project 1: Environment & System Information Manager

## 📌 Overview

The **Environment & System Information Manager** is a menu-driven Python application that displays system information, Python environment details, and environment variables.

This project demonstrates how Python can interact with the operating system using the **os** and **platform** modules.

---

## 🎯 Features

✅ Display Current Working Directory

✅ List Files and Folders

✅ Show Operating System Information

✅ Display Python Version

✅ Detect Active Python Environment

✅ View Environment Variables

✅ Show Application Configuration

✅ Menu-Driven Interface

✅ Environment Variable Management

✅ System Diagnostics

---

## 🛠️ Technologies Used

- Python 3
- os Module
- platform Module
- Environment Variables
- Functions
- Error Handling

---

## 📂 Project Structure

```text
Environment & System Information Manager/
│
└── main.py
```

---

## 📚 Concepts Learned

### 🔹 OS Module

The `os` module allows Python to communicate with the operating system.

Examples:

```python
import os

os.getcwd()
os.listdir()
os.environ
```

Used for:

- Accessing Environment Variables
- Reading Current Directory
- Listing Files and Folders
- Managing Paths

---

### 🔹 Platform Module

The `platform` module provides information about the operating system.

Example:

```python
import platform

platform.system()
platform.release()
platform.machine()
platform.python_version()
```

Used for:

- OS Name
- OS Version
- Machine Architecture
- Python Version

---

### 🔹 Environment Variables

Environment Variables store data outside the source code and can be accessed securely.

Example:

```python
import os

email = os.environ["MY_EMAIL"]
password = os.environ["EMAIL_APP_PASSWORD"]
```

Common Use Cases:

- Email Credentials
- API Keys
- Database Passwords
- Secret Tokens
- Configuration Settings

---
## 🌐 API Documentation
This project uses the **[Open Trivia Database API](https://opentdb.com/api_config.php)** to fetch quiz questions dynamically.
## 🔐 Secure Password Storage

Instead of storing passwords directly in the source code:

❌ Bad Practice

```python
password = "mypassword123"
```

✅ Better Practice

```python
password = os.environ["EMAIL_APP_PASSWORD"]
```

Benefits:

- Improved Security
- Prevents Sensitive Data Exposure
- Safe GitHub Uploads
- Easy Configuration Management

---

## 💡 Real-World Applications

- DevOps Automation
- Cloud Applications
- CI/CD Pipelines
- Infrastructure Monitoring
- Secure Credential Management

---

# 🧠 Project 2: GUI Quiz App

## 📌 Overview

The **GUI Quiz App** is a Trivia Quiz Application built using **Tkinter**, **Requests**, and **Object-Oriented Programming (OOP)**.

Questions are fetched from an online API and displayed through a graphical user interface.

---

## 🎯 Features

✅ Interactive Graphical User Interface

✅ Fetches Questions from Online API

✅ True / False Quiz

✅ Dynamic Question Loading

✅ Score Tracking

✅ Object-Oriented Design

✅ Quiz Completion Detection

✅ Image Support

✅ Instant Feedback

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- Requests
- APIs
- OOP (Classes & Objects)

---

## 📂 Project Structure

```text
GUI Quiz App/
│
├── image/
│
├── data.py
├── question_model.py
├── quiz_brain.py
├── ui.py
└── main.py
```

---

## 📚 File Description

### data.py

Responsible for:

- Fetching Quiz Data
- API Communication
- Processing JSON Response

Example:

```python
import requests

response = requests.get(url)
response.raise_for_status()

data = response.json()
```

---

### question_model.py

Contains:

```python
class Question
```

Stores:

- Question Text
- Correct Answer

---

### quiz_brain.py

Contains:

```python
class QuizBrain
```

Handles:

- Question Progress
- Answer Validation
- Score Tracking
- Quiz Logic

---

### ui.py

Contains:

```python
class QuizInterface
```

Responsible for:

- Window Design
- Question Display
- Button Actions
- Score Updates

---

### main.py

Application Entry Point

Responsible for:

- Object Creation
- Starting GUI
- Running Application

---

## 🌐 API Integration

Questions are retrieved from an online trivia API using the Requests library.

Example:

```python
import requests

response = requests.get(url)
response.raise_for_status()

question_data = response.json()
```

Benefits:

- Real-Time Questions
- Dynamic Content
- Better User Experience

---

## 🎨 Tkinter Components Used

### Create Window

```python
from tkinter import Tk

window = Tk()
```

### Labels

```python
Label()
```

### Canvas

```python
Canvas()
```

### Buttons

```python
Button()
```

### Images

```python
PhotoImage()
```

---

## 🏗️ Object-Oriented Programming Concepts

### Classes

```python
Question
QuizBrain
QuizInterface
```

### Objects

```python
question = Question(...)
quiz = QuizBrain(...)
ui = QuizInterface(...)
```

### Encapsulation

Each class manages a specific responsibility:

- Question → Data Model
- QuizBrain → Quiz Logic
- QuizInterface → User Interface

---

## 🎯 Learning Outcomes

Through this project I learned:

✅ Working with APIs

✅ Using the Requests Library

✅ Parsing JSON Data

✅ Creating Desktop Applications with Tkinter

✅ Implementing Object-Oriented Programming

✅ Managing Multiple Python Files

✅ Separating Business Logic from UI Logic

✅ Building Interactive User Interfaces

---

# 🏆 Key Learnings From Day 34

✅ Environment Variables

✅ Secure Password Handling

✅ OS Module

✅ Platform Module

✅ System Information Retrieval

✅ API Integration

✅ Requests Library

✅ Tkinter GUI Development

✅ Classes and Objects

✅ Object-Oriented Programming

✅ Modular Project Structure

✅ Application Configuration Management

---

# 🎓 Challenge Progress

**Day 34 Completed ✅**

### Topics Covered

- Environment & System Information Management
- Environment Variables & Security
- Secure Configuration Practices
- API Integration
- GUI Development
- Object-Oriented Programming
- Tkinter
- Requests Library

---

# 🔮 Future Improvements

### Environment Manager

- Export Environment Information to File
- Search Environment Variables
- Edit Environment Variables
- Delete Environment Variables
- GUI Version

### GUI Quiz App

- Multiple Categories
- Difficulty Levels
- High Score Saving
- Timer Feature
- Dark Mode UI
- Leaderboard System

---

## 👨‍💻 Author

**Rakshith M**

📍 Bengaluru, India

🚀 100 Days of Python Challenge

🎯 Learning Python, Automation, Cloud, DevOps, and AI one day at a time.