# Day 36 - Python Automation Projects

This repository contains two practical Python projects developed as part of the **100 Days of Python Challenge**.

The projects focus on:

- Logging and monitoring applications
- Working with APIs
- Environment variables
- Exception handling
- Automation using Python
- Telegram notifications
- Real-world monitoring solutions

---

# Project 1: [Application Log Manager](https://github.com/RakshithMurugesh09/100-days-python-challenge/tree/main/Day_36/Application%20Log%20Manager)

## Overview

Application Log Manager is a Python-based utility that demonstrates how logging works in real-world applications.

The project records application events, warnings, errors, and critical failures into a log file for troubleshooting and monitoring purposes.

It helps developers understand how production applications maintain logs for debugging and auditing.

---

## Features

- Create log files automatically
- Log messages with timestamps
- Support for multiple log levels
  - DEBUG
  - INFO
  - WARNING
  - ERROR
  - CRITICAL
- Custom date and time formatting
- 12-hour AM/PM format support
- Log file persistence
- Read recent log entries
- Exception logging
- Production-style logging configuration

---

## Technologies Used

- Python
- Logging Module
- Datetime Module
- File Handling

---

## Sample Log Entry

```text
03/09/2026 10:15:23 AM IST | root | INFO | Application started
03/09/2026 10:15:25 AM IST | root | WARNING | Low disk space
03/09/2026 10:15:27 AM IST | root | ERROR | Failed to connect
```

---

## Learning Outcomes

Through this project, I learned:

- Python logging fundamentals
- Log levels and their purposes
- Custom log formatting
- Error tracking techniques
- Production monitoring concepts
- File-based logging systems

---

# Project 2: [Stock News Monitoring](https://github.com/RakshithMurugesh09/100-days-python-challenge/tree/main/Day_36/Stock%20News%20Monitoring)

## Overview

Stock News Monitoring is an automated alert system that tracks stock price movements and sends relevant news updates through Telegram whenever significant changes occur.

The project combines stock market data with financial news to provide quick updates without manually checking multiple websites.

---

## Features

- Fetch stock data using Alpha Vantage API
- Calculate daily stock price changes
- Detect significant market movements
- Fetch latest company news
- Send Telegram notifications
- Environment variable support
- Error handling and API validation
- Automated news summarization

---

## APIs Used

### Alpha Vantage

Used to retrieve stock market information.

Features used:

- Daily stock prices
- Historical market data
- Closing price comparison

API Documentation: [Alpha Vantage doc](https://www.alphavantage.co/documentation/)

---

### News API

Used to retrieve recent news articles related to a company.

Features used:

- Company news search
- Article filtering
- Latest financial headlines

API Documentation: [NEWS API](https://newsapi.org/docs)

---

### Telegram Bot API

Used to send instant notifications directly to Telegram.

Features used:

- Automated alerts
- News notifications
- Stock movement updates

API Documentation: [Telegram Bot API doc](https://core.telegram.org/bots/api)

---

## Environment Variables

Create environment variables before running the project.

```text
ALPHAVANTAGE_API=your_alpha_vantage_key
NEWS_API=your_news_api_key
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

---

## Project Workflow

### Step 1

Retrieve stock market data from Alpha Vantage.

### Step 2

Compare the latest two trading days.

### Step 3

Calculate percentage difference.

### Step 4

Check if movement exceeds threshold.

### Step 5

Fetch related company news.

### Step 6

Generate formatted alert message.

### Step 7

Send notification to Telegram.

---

## Example Telegram Alert

```text
IBM: 🔺3.45%

Headline:
IBM Reports Strong Quarterly Results

Brief:
IBM exceeded analyst expectations with strong cloud revenue growth.

Read More:
https://example.com/news
```

---

## Error Handling Implemented

The project handles:

- Missing environment variables
- Invalid API keys
- API rate limits
- Network failures
- Timeout errors
- Missing stock data
- Missing news articles
- Telegram API failures

---

## Technologies Used

- Python
- Requests
- Datetime
- OS Module
- Telegram Bot API
- Alpha Vantage API
- News API

---

## Folder Structure

```text
Day_36/
│
├── Application Log Manager/
│   ├── app.log
│   └── main.py
│
└── Stock News Monitoring/
    └── main.py
```

---

## Skills Practiced

- API Integration
- Logging
- Exception Handling
- Environment Variables
- Automation
- Python Functions
- JSON Processing
- HTTP Requests
- Financial Data Analysis
- Telegram Bot Development

---

## Key Concepts Learned

- Production logging practices
- Monitoring systems
- API authentication
- Financial data retrieval
- News aggregation
- Notification automation
- Environment variable management
- Error recovery techniques

---

## Future Improvements

- Support multiple stocks
- Generate daily reports
- Email notifications
- Database storage
- Stock performance charts
- Scheduled execution
- Interactive dashboard
- Multiple news providers

---

## Challenge Information

Day: 36

Challenge: 100 Days of Python

Projects:

1. Application Log Manager
2. Stock News Monitoring

Focus Areas:

- Logging
- APIs
- Automation
- Monitoring
- Notifications

---

## Author

Rakshith M

100 Days of Python Challenge

Day 36 Completed ✅