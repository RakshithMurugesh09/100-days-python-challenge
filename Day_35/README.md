# Day 35: Python Automation Projects

## Table of Contents

- [Overview](#overview)
  - [Project](#projects)
    - [Rain Alert App](https://github.com/RakshithMurugesh09/100-days-python-challenge/tree/main/Day_35/Rain%20Alert%20App)
    - [System Command Manager](https://github.com/RakshithMurugesh09/100-days-python-challenge/tree/main/Day_35/System%20Command%20Manager)
    

- [My Process](#my-process)
  - [Rain Alert App](#rain-alert-app-1)
  - [System Command Manager](#system-command-manager-1)
  - [What I Learned](#what-i-learned)

## Overview

### Projects

Day 35 focused on Python automation and working with external systems.

This day contains two projects:

1. 🌧️ Rain Alert App
2. 💻 System Command Manager

Both projects helped me understand how Python can communicate with external services and operating system commands.



## My Process

### Rain Alert App

The challenge was to build an application that alerts the user when rain is expected.

The original course requirement was to send a text message using Twilio. Instead, I decided to use the Telegram Bot API because it was free and gave me an opportunity to learn how Telegram bots work.

The application retrieves weather forecast data from the OpenWeatherMap API using latitude and longitude coordinates. It then analyzes the forecast and determines whether rain is expected during the day.

If rain is detected, the application sends:

- 🌧️ Rain alert message
- ☔ Weather details
- 🤖 Telegram sticker notification

One of the most challenging parts was learning how Telegram Bots work, especially:

- Creating a Telegram Bot
- Obtaining the Bot Token
- Finding the Chat ID
- Sending messages through the API
- Sending stickers through the API

After reading the documentation and testing several requests, I was able to successfully send weather notifications to Telegram.

---

### System Command Manager

The second project focused on learning Python's `subprocess` module.

The goal was to create a menu-driven application capable of executing common system commands and displaying their results.

The application supports commands such as:

```text
python --version
systeminfo
ipconfig
ping 127.0.0.1
hostname
whoami
```

Features include:

- Execute system commands
- Capture command output
- Display command return codes
- Execute custom commands
- Track the last executed command
- Handle command timeouts
- Error handling for failed commands

This project improved my understanding of how Python interacts with the operating system and how external processes are managed.

---

### Built With

- Python
- OpenWeatherMap API
- Telegram Bot API
- Environment Variables
- Requests Library
- Datetime Module
- Subprocess Module
- Exception Handling
- Windows Command Line Utilities

### APIs and Resources

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Latitude and Longitude Finder](https://www.latlong.net/)
-  Tools: [JSON Viewer](http://jsonviewer.stack.hu/)

---

### What I Learned

#### Rain Alert App

- API Authentication
- API Keys
- Working with JSON Data
- Weather Forecast APIs
- Telegram Bot Creation
- Telegram Messages
- Telegram Stickers
- Environment Variables
- HTTP Requests using Requests Module

#### System Command Manager

- Python Subprocess Module
- Running External Commands
- Process Management
- Capturing Standard Output
- Capturing Standard Error
- Return Codes
- Command Timeouts
- Error Handling
- Menu-Driven Applications
- Working with Operating System Commands

---

## Day 35 Summary

This was one of my favorite learning days because it combined two different types of automation:

- 🌧️ API Automation using OpenWeatherMap and Telegram
- 💻 System Automation using Python's subprocess module

Both projects helped me understand how Python can communicate with external applications, services, and the operating system. These skills are useful for scripting, automation, DevOps tasks, monitoring tools, and real-world software development.