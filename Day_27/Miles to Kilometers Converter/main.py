from tkinter import *

def convert():
    try:
        miles = float(mile_entry.get())
        km = round(miles * 1.60934, 3)
        km_output_label.config(text = str(km))
    except ValueError:
        km_output_label.config(text = "Invalid Input")

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx = 50, pady = 50)

# entry
mile_entry = Entry(window)
mile_entry.grid(row=0, column=1, padx = 20, pady = 20)

# Label
miles_label = Label(text = "Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text = "is equal to")
is_equal_label.grid(row=1, column=0)

km_output_label = Label(text = "0", font = ("Arial", 10, "bold"))
km_output_label.grid(row=1, column=1)

km_label = Label(text = "KM")
km_label.grid(row=1, column=2)

# button
calculate_button = Button(text = "Calculate", command = convert)
calculate_button.grid(row=2, column=1)

window.mainloop()