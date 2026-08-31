# Day 33: File & Log Manager and ISS Overhead Notifier

## Overview

Day 33 of the **100 Days of Python Challenge** includes two Python projects.

1. File & Log Manager
2. ISS Overhead Notifier

---

# Project Structure

```text
Day_33/
│
├── File & Log Manager/
│   ├── logs/
│   │   ├── app.log
│   │   ├── security.log
│   │   └── server.log
│   └── main.py
│
├── ISS Overhead Notifier Project/
│   └── main.py
│
├── requirements.txt
└── README.md
```
---
## Project 1: File & Log Manager
**Description**

This project uses Python's pathlib module to work with files and folders.

The program searches the logs folder and finds all .log files. It displays information about each file.

- Features
- Finds log files
- Reads file content
- Displays file name
- Displays file extension
- Displays file path
- Displays file size
- Handles missing folders and files 

### Module Used
```python
from pathlib import Path
```

### Important Methods
```python
path.exists()
path.is_dir()
path.is_file()
path.glob("*.log")
path.rglob("*.log")
path.read_text()
path.write_text()
path.name
path.stem
path.suffix
path.parent
path.stat().st_size
```

### Sample Log Files
*app.log*
```text
Application started successfully.
User opened the application.
Application closed successfully.
```

*security.log*
```text
User login successful.
Invalid login attempt detected.
Password updated successfully.
```

*server.log*
```text
Server started successfully.
Client connected to the server.
Server connection closed.
```

### How It Works
1) Checks whether the logs folder exists.
2) Finds all .log files.
3) Reads each file.
4) Displays file information.
5) Handles possible errors.

---
## Project 2: ISS Overhead Notifier
*Description*

This project tracks the current location of the International Space Station (ISS).

The program checks:

- Current ISS location
- Your location
- Sunrise time
- Sunset time
- Current time

If the ISS is near your location and it is dark, the program sends an email notification.

*Modules Used*
```python
import requests
import smtplib
import os
import time
from datetime import datetime
```



### Features
- Gets the current ISS location
- Uses APIs
- Processes JSON data
- Checks sunrise and sunset times
- Checks whether it is dark
- Sends an email notification
- Uses environment variables for email credentials
- Handles API and email errors 


### APIs Used
- ISS Location API

The ISS API provides the current location of the International Space Station.

```python
response = requests.get(
    "http://api.open-notify.org/iss-now.json"
)
```


The API returns JSON data containing:
- Latitude
- Longitude
- Timestamp

Example:
```json
{
    "message": "success",
    "iss_position": {
        "latitude": "20.1234",
        "longitude": "75.5678"
    }
}
```

### Sunrise and Sunset API

This API provides sunrise and sunset information.
```json
parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}
```
```python
response = requests.get(
    "https://api.sunrise-sunset.org/json",
    params=parameters
)
```

### How the ISS Project Works
- Gets the current ISS location.
- Extracts the ISS latitude and longitude.
- Checks whether the ISS is near your location.
- Gets sunrise and sunset information.
- Checks whether it is dark.
- Sends an email if both conditions are true.
- Repeats the process every 60 seconds.

---
### Email Configuration
Email credentials are stored using environment variables.
```python
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")
```

PowerShell
```python
$env:MY_EMAIL="your_email@gmail.com"
$env:MY_PASSWORD="your_app_password"
$env:RECEIVER_EMAIL="receiver_email@gmail.com"
```
