import tkinter
from tkinter import messagebox  # needed for popup boxes
import string
import random
import pyperclip

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# Logo
canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=0, row=0, columnspan=3)

# Labels
websitetk = tkinter.Label(text="Website:", bg="white")
websitetk.grid(column=0, row=1)
emailtk = tkinter.Label(text="Email/Username:", bg="white")
emailtk.grid(column=0, row=2)
passwordtk = tkinter.Label(text="Password:", bg="white")
passwordtk.grid(column=0, row=3)

# Textboxes
website_entry = tkinter.Entry()
# columnspan parametar says that object will go through x columns
# sticky parameter says that object will be "glued" to start of column
# that object will spread until the end of column (or columnspan) if defined
# end of each column will be the length of the longest object in that column (minus padding)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
email_entry = tkinter.Entry()
email_entry.insert(tkinter.END, string="example@email.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_entry = tkinter.Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons


def password_generation():
    generated_password = ""
    characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(15):
        generated_password = generated_password + random.choice(characters)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(tkinter.END, string=generated_password)
    pyperclip.copy(generated_password)  # very useful Python library which is used to copy to and paste from clipboard


generate_pw = tkinter.Button(text="Generate Password", command=password_generation)
generate_pw.grid(column=2, row=3, sticky="EW")


def add_entry():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        # Shows warning popup
        messagebox.showwarning(title="Password Manager", message="One or more entries missing!")
    else:
        # Asks for yes or no, returns true if clicked on yes
        if messagebox.askyesno(title="Password Manager", message="Do you want to proceed?"):
            # Shows info popup
            messagebox.showinfo(title="Password Manager", message="Adding entry to database!")
            with open("passwords.txt", "a+") as file:
                file.write(f"{website} | {email} | {password}\n")
                file.close()
            website_entry.delete(0, tkinter.END)
            email_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


add = tkinter.Button(text="Add", command=add_entry)
add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
