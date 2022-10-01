# http://tcl.tk/man/tcl8.6/TkCmd/contents.htm -> documentation for all Tkinter objects

import tkinter

# Window
window = tkinter.Tk()
window.title("Title")
window.minsize(width=400, height=300)
window.config(padx=10, pady=10)  # sets number of pixels from the edge of window which will be empty, can be done for
# any other object

# Label
label = tkinter.Label(text="This is label!", font=("Ariel", 20, "bold"))
label["text"] = "somethingnew"
label.config(text="somethingnew")  # different way to change initial config

#label.pack()  # shows label on screen
#label.place(x=50, y=50)  # much more precision with placing tkinter objects
label.grid(column=0, row=0)  # shows label on screen

# Button


def button_clicked():
    label.config(text="Button got clicked!")
    text = textline.get()  # gets text entered in textbox
    window.title(text)


button = tkinter.Button(text="buttontext", command=button_clicked)  # when we click on button, command executes
button.grid(column=1, row=1)  # shows button on screen
# the way that grid works that it assigns each unique column and row to its internal column and row
# that means if we put only 1 element and give it column 151 and row 98 it will still be shown at beginning
# of course, if we put new element with lower column and row that the one created before it will be put upleft

# Textboxes - single line
textline = tkinter.Entry(width=35)
textline.grid(column=7825, row=78)  # shows textline on screen


window.mainloop()  # similar to exitonscreen from turtle