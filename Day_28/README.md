# 🚀 Day 28 - CLI Calculator & Pomodoro Timer

Today I built two Python projects to explore different ways users interact with applications:

1. 🖥️ A Command-Line Interface (CLI) Calculator using the `sys` module.
2. 🍅 A Pomodoro Timer GUI application using Tkinter.

These projects helped me understand both terminal-based and graphical user interface development in Python.

---

# 📂 Project Structure

```text
Day_28/
│
├── CLI Calculator/
│   └── main.py
│
└── Pomodoro Timer/
    ├── main.py
    └── tomato.png
```

---

# 🖥️ CLI Calculator

A simple calculator that performs basic arithmetic operations directly from the command line using command-line arguments.

## 📚 Concepts Practiced

- `sys` module
- `sys.argv`
- Command-Line Interface (CLI)
- Arithmetic Operations
- Exception Handling
- Input Validation
- Error Handling

## ▶️ Usage

Run the program from the terminal:

```bash
python main.py 10 + 5
```

### Examples

```bash
python main.py 10 + 5
Result: 15.0
```

```bash
python main.py 20 - 8
Result: 12.0
```

```bash
python main.py 6 * 4
Result: 24.0
```

```bash
python main.py 25 / 5
Result: 5.0
```

## ✅ Features

- Addition
- Subtraction
- Multiplication
- Division
- Invalid operator handling
- Division by zero protection

## 🎯 Learning Outcomes

- Learned how CLI applications work.
- Used command-line arguments with `sys.argv`.
- Validated user input.
- Handled runtime exceptions gracefully.

---

# 🍅 Pomodoro Timer

A productivity application based on the Pomodoro Technique built with Tkinter.

The Pomodoro Technique helps improve focus by alternating between work sessions and breaks.

## 📚 Concepts Practiced

- Tkinter GUI
- Labels
- Buttons
- Canvas Widget
- Images in Tkinter
- Event-driven Programming
- `window.after()` Timer
- Global Variables
- Function Calls

## ✅ Features

- Work Sessions
- Short Breaks
- Long Breaks
- Start Button
- Reset Button
- Session Tracking
- Progress Checkmarks

## 🖼️ Resources

- `tomato.png`

## 🎯 Learning Outcomes

- Built a graphical desktop application.
- Learned event-driven programming.
- Used the Tkinter Canvas widget.
- Displayed images in GUI applications.
- Updated interface components dynamically.
- Managed timers using