# 🚀 Day 40 - Flight Club & Log Record Manager

## 📖 Overview

Day 40 extends the Cheap Flight Finder project by introducing a Flight Club system where users can register to receive flight deal notifications.

This day also covers creating custom Context Managers using Python classes.

---

# 📝 Log Record Manager

## 🎯 Objective

Create a custom Context Manager that automatically manages opening and closing log files.

---

## 📂 Project Structure

```text
Log Record Manager/
│
└── main.py
```

---

## Features

✅ Open files automatically

✅ Close files automatically

✅ Handle exceptions gracefully

✅ Improve code readability

✅ Prevent resource leaks

---

## Example

```python
with LogFileManager("app.log", "a") as file:
    file.write("Application Started")
```

---

## Concepts Practiced

- Context Managers
- `__enter__()`
- `__exit__()`
- File Handling
- Exception Handling
- Resource Cleanup

---

# ✈️ Part 2 - Flight Club

## 🎯 Project Goal

Allow users to sign up for cheap flight alerts and receive notifications whenever a deal is found.

---

## 📂 Project Structure

```text
Part 2 - Cheap Flight Finder/
│
├── .env
├── customer.py
├── data.py
├── flight_data.py
├── flight_search.py
├── notification_manager.py
└── main.py
```

---

## 🔧 Technologies Used

- Python 3
- Requests
- SerpAPI
- Sheety
- python-dotenv

---

## 🔐 Environment Variables

```env
SERPAPI_API_KEY=YOUR_API_KEY

SHEETY_USERS_ENDPOINT=YOUR_ENDPOINT
SHEETY_PRICES_ENDPOINT=YOUR_ENDPOINT

EMAIL_ADDRESS=YOUR_EMAIL
EMAIL_PASSWORD=YOUR_PASSWORD
```

---

## 🔄 Workflow

```text
User Registration
         ↓
Store User Data
         ↓
Search Flights
         ↓
Compare Prices
         ↓
Deal Found?
      ↓ Yes
Send Notification
```

---

## Features

✅ User Registration

✅ Customer Data Storage

✅ Flight Deal Search

✅ Price Comparison

✅ Email Notifications

✅ Modular OOP Design

---

## 🧠 Concepts Practiced

- CRUD Operations
- API Integration
- Object-Oriented Programming
- Environment Variables
- Data Storage
- User Management
- Automation

---

## 🚀 Future Improvements

- Telegram Notifications
- WhatsApp Alerts
- GUI Dashboard
- Multiple Departure Airports
- Scheduled Daily Flight Checks

---

## 🎓 What I Learned

✅ Extending existing Python projects

✅ Managing customer subscriptions

✅ Separating business logic into modules

✅ Creating scalable applications

✅ Building custom Context Managers

✅ Designing real-world automation systems

---

## 👨‍💻 Author

**Rakshith M.**  
100 Days of Python Challenge  
Day 40 ✅