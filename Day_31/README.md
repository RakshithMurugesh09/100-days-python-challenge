# Day 31: Flash Card and Flexible Function Calculator

## 100 Days of Python Challenge

Day 31 contains two Python projects designed to review previously learned skills and practise flexible function arguments:

1. **Flash Card**: A graphical flash-card application used to review and test concepts learned during the previous 30 days.
2. **Flexible Function Calculator**: A calculator that demonstrates how to accept a variable number of positional and keyword arguments using `*args` and `**kwargs`.

---

## Project 1: Flash Card

The Flash Card application provides an interactive way to review knowledge and check learning progress. A card displays a prompt first and then flips to reveal the answer. The user can mark the answer as known or unknown.

Although the current data files contain French vocabulary, the same application structure can be adapted to review Python concepts, questions, definitions, syntax, or any other learning material from the first 30 days of the challenge.

### Features

- Displays one flash card at a time.
- Reads flash-card information from a CSV file.
- Automatically flips the card to display the answer.
- Provides **right** and **wrong** buttons for user feedback.
- Removes correctly answered cards from the active learning list.
- Saves unknown cards in `words_to_learn.csv` for future practice.
- Continues learning progress between application sessions.
- Uses images to provide a clear graphical interface.
- Handles the learning data using Pandas.

### Skills Reviewed

The Flash Card project applies several concepts learned during the previous 30 days:

- Python variables and constants
- Functions
- Conditional statements
- Event-driven programming
- Tkinter GUI development
- Canvas widgets and image handling
- Reading CSV files
- Writing CSV files
- Pandas DataFrames
- Dictionary records
- Random data selection
- File and folder paths
- Exception handling
- Application state management
- Code organization

### Flash Card Workflow

1. The application loads `words_to_learn.csv` when saved learning progress is available.
2. If saved learning progress is unavailable, the application loads `french_words.csv`.
3. A random card is selected and displayed.
4. The front of the card shows the question or word.
5. After a configured delay, the card flips and displays the answer.
6. Clicking the **right** button marks the current card as learned.
7. Learned cards are removed from the active learning collection.
8. Remaining cards are saved to `words_to_learn.csv`.
9. Clicking the **wrong** button keeps the card available for later practice.

### Flash Card Files

- `main.py`: Contains the Flash Card application logic and graphical interface.
- `data/french_words.csv`: Contains the original flash-card dataset.
- `data/words_to_learn.csv`: Stores cards that still require practice.
- `image/card_front.png`: Front design of the flash card.
- `image/card_back.png`: Back design of the flash card.
- `image/right.png`: Image used for the correct-answer button.
- `image/wrong.png`: Image used for the incorrect-answer button.

---

## Project 2: Flexible Function Calculator

The Flexible Function Calculator demonstrates how Python functions can process different numbers of arguments without requiring a fixed parameter count.

The project uses:

- `*args` to receive multiple positional numbers.
- `**kwargs` to receive named configuration values or operation details.

### Features

- Accepts a flexible number of numeric values.
- Supports calculations involving two or more numbers.
- Demonstrates positional argument unpacking with `*args`.
- Demonstrates keyword argument unpacking with `**kwargs`.
- Performs arithmetic operations through reusable functions.
- Includes input validation and clear calculation results.
- Handles invalid operations and division by zero safely.

### Understanding `*args`

`*args` collects multiple positional arguments into a tuple.

```python
def add(*args):
    return sum(args)


result = add(10, 20, 30, 40)
print(result)
```

Output:

```text
100
```

### Understanding `**kwargs`

`**kwargs` collects named arguments into a dictionary.

```python
def calculate(*args, **kwargs):
    operation = kwargs.get("operation", "add")

    if operation == "add":
        return sum(args)

    return "Unsupported operation"


result = calculate(10, 20, 30, operation="add")
print(result)
```

Output:

```text
60
```

### Calculator Skills Practised

- Defining and calling functions
- Positional arguments
- Keyword arguments
- Arbitrary positional arguments with `*args`
- Arbitrary keyword arguments with `**kwargs`
- Tuples and dictionaries
- Loops
- Conditional statements
- Mathematical operations
- Input validation
- Exception handling
- Reusable function design

---

## Project Structure

```text
Day_31/
├── Flash Card/
│   ├── data/
│   │   ├── french_words.csv
│   │   └── words_to_learn.csv
│   ├── image/
│   │   ├── card_back.png
│   │   ├── card_front.png
│   │   ├── right.png
│   │   └── wrong.png
│   └── main.py
├── FLEXIBLE FUNCTION CALCULATOR/
│   └── main.py
└── README.md
```


---

## Learning Outcomes

After completing Day 31, I am able to:

- Build an interactive GUI application using Tkinter.
- Use Canvas elements, images, buttons, and timed events.
- read, update, and save structured CSV data.
- Use Pandas to manage application data.
- Preserve a user's learning progress between sessions.
- Create reusable functions that accept flexible arguments.
- Explain the difference between `*args` and `**kwargs`.
- Perform calculations using an arbitrary number of values.
- Apply validation and exception handling to make applications more reliable.
- Combine skills from earlier challenge days into complete projects.

---

## Day 31 Reflection

Day 31 acts as both a revision day and a step toward more flexible Python programming. The Flash Card application combines GUI development, Pandas, CSV file handling, randomization, and persistent data storage. The Flexible Function Calculator strengthens function knowledge by showing how `*args` and `**kwargs` support reusable and adaptable code.

These projects demonstrate how individual Python concepts learned during the first 30 days can be combined to build useful applications.

---

## Author

**Rakshith M**

Part of my **100 Days of Python Challenge**.
