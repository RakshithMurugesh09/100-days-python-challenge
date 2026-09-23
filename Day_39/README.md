# 🚀 Day 39 - Cheap Flight Finder & Context Managers

## 📖 Overview

Day 39 focuses on building a Flight Deal Tracker that searches for cheap flights and notifies users when prices fall below a predefined threshold.

Since some of the original APIs used in the course are no longer freely available, alternative services were used:

✅ SerpAPI (Google Flights Search)  
✅ AirportDB API (Airport Data & IATA Codes)  
✅ Sheety (Google Sheets Integration)

Additionally, Day 39 covers Python Context Managers and resource management.

---

# ✈️ Part 1 - Cheap Flight Finder

## 🎯 Project Goal

Monitor flight prices and alert users when a flight becomes cheaper than the target price stored in a spreadsheet.

---

## 📂 Project Structure

```text
Part 1 - Cheap Flight Finder/
│
├── .env
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

Create a `.env` file:

```env
SERPAPI_API_KEY=YOUR_API_KEY

SHEETY_PRICES_ENDPOINT=YOUR_ENDPOINT

EMAIL_ADDRESS=YOUR_EMAIL
EMAIL_PASSWORD=YOUR_PASSWORD
```

---

## 🔄 Workflow

```text
Read Destination Data
          ↓
Get IATA Codes
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

## 🧠 Concepts Practiced

- REST APIs
- Environment Variables
- API Authentication
- OOP (Object-Oriented Programming)
- JSON Data Handling
- Data Persistence
- Automation Workflows

---

# 🔄 Context Managers

## Topics Covered

- `__enter__()`
- `__exit__()`
- `with` Statement
- Resource Cleanup

### Example

```python
with open("log.txt", "r") as file:
    content = file.read()
```

---

## 🎓 What I Learned

✅ Working with multiple APIs

✅ Handling API limitations using alternatives

✅ Building reusable Python classes

✅ Secure credential management using `.env`

✅ Understanding Context Managers

✅ Creating automation projects using real-world data

---

## 👨‍💻 Author

**Rakshith M.**  
100 Days of Python Challenge  
Day 39 ✅