from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps

    if timer:
        window.after_cancel(timer)

    reps = 0

    header.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")

    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    # Prevent multiple timers
    start_button.config(state="disabled")

    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        header.config(text="Break", fg=RED)
        count_down(long_break_seconds)

    elif reps % 2 == 0:
        header.config(text="Break", fg=PINK)
        count_down(short_break_seconds)

    else:
        header.config(text="Work", fg=GREEN)
        count_down(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text,text=f"{count_min:02d}:{count_sec:02d}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        # Check marks
        work_sessions = reps // 2
        marks = "✔" * work_sessions
        check_label.config(text=marks)

        # Start next session automatically
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Header
header = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME, 35, "bold"))
header.grid(row=0, column=1)

# Canvas
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start_button = Button(text="Start",command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(row=2, column=2)

# Check Marks
check_label = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME, 20, "bold"))
check_label.grid(row=3, column=1)

window.mainloop()