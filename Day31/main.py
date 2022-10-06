BACKGROUND_COLOR = "#B1DDC6"

import tkinter
import random
import pandas

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

french_words = pandas.read_csv("data\\french_words.csv")
french_words_dict = {data["French"]: data["English"] for (_, data) in french_words.iterrows()}
french_image = tkinter.PhotoImage(file="images\\card_front.png")
english_image = tkinter.PhotoImage(file="images\\card_back.png")
random_word = ""
timer = None


def change_to_english():
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=random_word[1])
    canvas.itemconfig(current_image, image=english_image)


def change_to_french():
    global random_word
    global timer
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    random_word = random.choice(list(french_words_dict.items()))
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(word, text=random_word[0])
    canvas.itemconfig(current_image, image=french_image)
    timer = window.after(3000, change_to_english)


canvas = tkinter.Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
current_image = canvas.create_image(400, 263, image=french_image)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
change_to_french()


def not_remember():
    change_to_french()


crossmark = tkinter.PhotoImage(file="images\\wrong.png")
not_remember = tkinter.Button(image=crossmark, command=not_remember, bg=BACKGROUND_COLOR, border=0, highlightthickness=0)
not_remember.grid(column=0, row=1)


def remember():
    french_words_dict.pop(random_word[0])
    french = []
    english = []
    for (key, value) in french_words_dict.items():
        french.append(key)
        english.append(value)
    newdict = {"French": french, "English": english}
    newdata = pandas.DataFrame(newdict)
    newdata.to_csv("data\\french_words.csv")
    change_to_french()


checkmark = tkinter.PhotoImage(file="images\\right.png")
remember = tkinter.Button(image=checkmark, command=remember, bg=BACKGROUND_COLOR, border=0, highlightthickness=0)
remember.grid(column=1, row=1)

window.mainloop()
