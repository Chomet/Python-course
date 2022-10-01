import tkinter

# Window
window = tkinter.Tk()
window.title("Mile to KM converter")
window.minsize(width=150, height=100)
window.config(padx=50, pady=10)

# Labels
equal = tkinter.Label(text="is equal to")
equal.grid(column=0, row=1)
miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)
kms = tkinter.Label(text="Km")
kms.grid(column=2, row=1)
actual = tkinter.Label(text="0")
actual.grid(column=1, row=1)

# Button


def button_clicked():
    value = float(textline.get())
    actual.config(text=round(value*1.609, 2))


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Textbox
textline = tkinter.Entry(width=10)
textline.grid(column=1, row=0)


window.mainloop()