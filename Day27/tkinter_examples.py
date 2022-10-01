# http://tcl.tk/man/tcl8.6/TkCmd/contents.htm -> documentation for all Tkinter objects

import tkinter

# Window
window = tkinter.Tk()
window.title("Title")
window.minsize(width=400, height=300)

# Label
label = tkinter.Label(text="This is label!", font=("Ariel", 20, "bold"))
label.pack()  # shows label on screen

label["text"] = "somethingnew"
label.config(text="somethingnew")  # different way to change initial config

# Button


def button_clicked():
    label.config(text="Button got clicked!")
    text = textline.get()  # gets text entered in textbox
    window.title(text)


button = tkinter.Button(text="buttontext", command=button_clicked)  # when we click on button, command executes
button.pack()  # shows button

# Textboxes - single line
textline = tkinter.Entry(width=35)
textline.insert(tkinter.END, string="somestartingtext")  # inserts some starting text inside
textline.pack()  # shows textline on screen

# Textboxes - multiple lines
box = tkinter.Text(height=5, width=30)
box.insert(tkinter.END, "This is too large to be in a single line, so this is in multi lines")
box.focus()  # puts cursor inside box
print(box.get("1.2", tkinter.END))  # gets text from box starting from first line, second character
box.pack()  # shows textbox on screen

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()  # similar to exitonscreen from turtle