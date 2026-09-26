# Day 42 - Python Data Validation and HTML Fundamentals 🚀

## Overview

Day 42 of my **100 Days of Python Challenge** focuses on two important areas:

1. **Data Validation Pipeline using Python**
2. **Web Development Fundamentals using HTML**

The Data Validation Pipeline project helped me understand how to verify and validate data before processing it. The HTML exercises introduced the building blocks of web development, including lists, images, links, nesting, and creating a simple webpage.

---

## Project Structure

```text
Day_42/
│
├── Data Validation Pipeline/
│   └── main.py
│
└── Web Development/
    ├── Anchor Elements/
    ├── Birthday Invite Project/
    ├── Image Elements/
    ├── List Elements/
    └── Nested and Indentation/
```

---

# Part 1: Data Validation Pipeline ✅

## Project Description

The Data Validation Pipeline validates structured log records before processing them.

The project ensures:

- Required fields exist
- Correct data types are used
- Values follow predefined rules
- Invalid records are identified

This helps improve application reliability and data quality.

---

## Log Schema

Each log record contains:

| Field | Type |
|---------|---------|
| service | str |
| status | Literal["INFO", "WARNING", "ERROR"] |
| duration | float |
| metadata | Dict[str, Any] |
| error_code | Optional[int] |
| request_id | Union[str, int] |

---

## Validation Workflow

```text
Receive Log Data
       ↓
Check Required Fields
       ↓
Validate Data Types
       ↓
Validate Status Values
       ↓
Separate Valid & Invalid Logs
       ↓
Generate Results
```

---

## Sample Valid Log

```python
{
    "service": "payment-service",
    "status": "INFO",
    "duration": 1.45,
    "metadata": {
        "method": "POST",
        "endpoint": "/payment"
    },
    "error_code": None,
    "request_id": "REQ-1001"
}
```

---

## Sample Invalid Log

```python
{
    "service": "order-service",
    "status": "FAILED",
    "duration": "five seconds",
    "metadata": {},
    "error_code": "500",
    "request_id": None
}
```

Problems:

- Invalid status value
- Duration should be float
- Error code should be integer
- Request ID should not be None

---

## Python Concepts Used

- Type Hints
- Literal
- Optional
- Union
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Error Handling
- Data Validation

---

# Part 2: Web Development Fundamentals 🌐

## Overview

This section introduces HTML, the standard markup language used to create webpages.

Topics covered:

- List Elements
- Image Elements
- Anchor Elements
- Nesting & Indentation
- Birthday Invite Project

---

## 1. List Elements

Learned how to create ordered and unordered lists.

### Example

```html
<h2>My Skills</h2>

<ul>
  <li>Python</li>
  <li>HTML</li>
  <li>GitHub</li>
</ul>
```

---

## 2. Image Elements

Learned how to add images to webpages.

### Example

```html
image-url
```

Topics covered:

- Image URLs
- Alternative Text
- Accessibility

---

## 3. Anchor Elements

Learned how to create hyperlinks.

### Example

```html
https://www.google.comGoogle</a>
```

Topics covered:

- External Links
- Navigation
- Hyperlinks

---

## 4. Nesting and Indentation

Learned how to properly organize HTML