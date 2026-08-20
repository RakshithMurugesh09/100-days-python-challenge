from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# TODO: Generate Password


# ---------------------------- SAVE PASSWORD ------------------------------- #

# TODO: Save password

# ---------------------------- SEARCH PASSWORD ------------------------------- #

# TODO: Search Password

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


window.mainloop()