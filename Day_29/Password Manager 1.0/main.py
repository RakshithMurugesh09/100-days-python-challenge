from tkinter import *
import random
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# TODO: Generate Password
def generate_password():
    alphabet = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    )

    # Tuple of number characters
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    # Tuple of symbol characters
    symbols = (
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
        ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{',
         '}', '~'
    )

    alphabet_letters = [random.choice(alphabet) for _ in range(random.randint(5, 10))]
    numbers_letters = [random.choice(numbers) for _ in range(random.randint(5, 10))]
    symbols_letters = [random.choice(symbols) for _ in range(random.randint(5, 10))]

    password = alphabet_letters + numbers_letters + symbols_letters
    random.shuffle(password)
    joined_password = ''.join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, joined_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# TODO: Save password
def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if website == "" or email == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        with open("password.txt", "r") as file:
            data = file.readlines()

            for line in data:
                saved_website = line.split("|")[0].strip()

                if saved_website.lower() == website.lower():
                    messagebox.showerror("Duplicate Website","{website} already exists.")
                    return

    except FileNotFoundError:
        pass

    is_ok = messagebox.askyesno(title=f"Website: {website}",message=f"Email: {email}\nPassword: {password}")

    if is_ok:
        with open("password.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")

        messagebox.showinfo("Success", "Password has been saved")

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

# TODO: Search Password
def search_website():
    website = website_entry.get().strip()
    if website == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        try:
            with open("password.txt" , mode="r") as file:
                data = file.readlines()
                is_data = FALSE
                for lines in data:
                    if lines.strip().startswith(website):
                        is_data = TRUE
                        website, email, password = lines.strip().split("|")
                        messagebox.showinfo(website, message=(f"Email:{email}\n"
                                                            f"Password:{password}"))
                if not is_data:
                    messagebox.showerror("Error", f"There is no data of website: {website}")
        except FileNotFoundError:
            messagebox.showerror("Error", "Password file not found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canva = Canvas(width=300, height=300)
image = PhotoImage(file="./logo.png")
canva.create_image(50, 50, image=image, anchor="nw")
canva.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=("Arial", 25))
website_label.grid(row=1, column=0)

email_label = Label(text="Email Address:", font=("Arial", 25))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Arial", 25))
password_label.grid(row=3, column=0)

# Entry Box
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1)

email_entry = Entry(width=65)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "raskhith.09m@gmail.com")

password_entry = Entry(width=40)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=20, command=generate_password)
generate_password_button.grid(row=3, column=2)

search_button = Button(text="Search", width=20, command=search_website)
search_button.grid(row=1, column=2)

add = Button(text="Add", width=50, command=save_password)
add.grid(row=5, column=1, columnspan=2)



window.mainloop()