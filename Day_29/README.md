# 🚀 Day 29 - Python Environment & Password Manager

This repository contains two projects completed as part of my **100 Days of Python Challenge**.

## 📂 Project Structure

```text
Day_29/
│
├── Environment/
│   ├── .newvenv/
│   ├── main.py
│   └── requirements.txt
│
└── Password Manager 1.0/
    ├── logo.png
    ├── main.py
    └── password.txt
```

---

# 1️⃣ Environment Management

## 📌 Overview

This project demonstrates how to create, activate, and manage a Python Virtual Environment (venv). Virtual environments help isolate project dependencies and prevent package conflicts between different Python projects.

## 🎯 Features

- Create a virtual environment
- Activate and deactivate environments
- Check Python version
- Verify installed packages
- Generate `requirements.txt`
- Understand dependency management

## 🛠 Technologies Used

- Python
- Virtual Environment (venv)
- pip

## ▶️ Commands Used

### Create Virtual Environment

```bash
py -m venv .newvenv
```

### Activate Environment

#### Windows PowerShell

```powershell
.\.newvenv\Scripts\Activate.ps1
```

#### Command Prompt

```cmd
.newvenv\Scripts\activate.bat
```

### Deactivate Environment

```bash
deactivate
```

### Install Packages

```bash
pip install package_name
```

### Export Dependencies

```bash
pip freeze > requirements.txt
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 📚 Key Learnings

- Why virtual environments are important
- Dependency isolation
- Managing project-specific packages
- Using pip effectively
- Reproducible development environments

---

# 2️⃣ Password Manager 1.0

## 📌 Overview

A GUI-based Password Manager built using **Tkinter**. This application helps users generate secure passwords and save website login credentials locally.

## 🎯 Features

- User-friendly GUI
- Password generation
- Random secure passwords
- Save credentials to file
- Auto-copy generated password to clipboard
- Form validation
- Store Website, Email, and Password details

## 🛠 Technologies Used

- Python
- Tkinter
- Pyperclip
- Random Module

## 📷 GUI Components

- Website Entry
- Email/Username Entry
- Password Entry
- Generate Password Button
- Add/Save Button
- Logo Image

## ▶️ How to Run

Navigate to the Password Manager directory:

```bash
cd "Password Manager 1.0"
```

Run the application:

```bash
python main.py
```

## 💾 Data Storage

Credentials are stored locally in:

```text
password.txt
```

Example:

```text
Website: github.com
Email: user@gmail.com
Password: Xy@12Ab#89
```

## 📚 Key Learnings

- Tkinter GUI development
- Event-driven programming
- Password generation logic
- File handling
- User input validation
- Clipboard operations using Pyperclip

---

# 🎓 Skills Practiced

✅ Virtual Environment Management

✅ Package Installation & Dependency Management

✅ Tkinter GUI Development

✅ File Handling

✅ Password Generation

✅ Clipboard Integration

✅ Python Project Structure

---

# 🚀 Challenge Progress

**Day 29 of 100 Days of Python Challenge**

Focused on:
- Python Virtual Environments (venv)
- Dependency Management
- GUI Application Development
- Password Manager Implementation

---

## 👨‍💻 Author

**Rakshith M**
