from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

rand_word = {}
word_dict = {}

words = pandas.read_csv("data/french_words.csv")
word_dict = words.to_dict(orient="records")
print(word_dict)

def word_access():
    global rand_word, change_card
    window.after_cancel(change_card)
    rand_word = random.choice(word_dict)
    french_word = rand_word['French']
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(translation_text, text=french_word, fill="black")
    canvas.itemconfig(current_image, image=front_img)
    change_card = window.after(3000, flip_card)

def right_click():
    word_dict.remove(rand_word)
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    word_access()

def flip_card():
    global rand_word
    english_word = rand_word["English"]
    canvas.itemconfig(language_text, text="English", fill="#fff")
    canvas.itemconfig(translation_text, text=english_word, fill="#fff")
    canvas.itemconfig(current_image, image=back_img)

change_card = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_img = PhotoImage(file="image/card_back.png")
front_img = PhotoImage(file="image/card_front.png")
current_image = canvas.create_image(400, 263, image=front_img)
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
translation_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="image/right.png")
right_button = Button(image=right_image, command=right_click)
right_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="image/wrong.png")
wrong_button = Button(image=wrong_image, command=word_access)
wrong_button.grid(column=1, row=1)

word_access()

window.mainloop()
