import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1

work_timer = WORK_MIN * 5
short_break_timer = SHORT_BREAK_MIN * 5
long_break_timer = LONG_BREAK_MIN * 5

noworks = 0
checkmark = ""
timercounter = None


def update_screen(count, function):
    global timercounter  # way to access global variables in local functions
    seconds = count % 60
    mins = int(count / 60)
    if seconds < 10:
        if mins < 10:
            canvas.itemconfig(timertext, text=f"0{mins}:0{seconds}")  # changing text we put on canvas
        else:
            canvas.itemconfig(timertext, text=f"{mins}:0{seconds}")
    elif mins < 10:
        canvas.itemconfig(timertext, text=f"0{mins}:{seconds}")
    else:
        canvas.itemconfig(timertext, text=f"{mins}:{seconds}")
    timercounter = window.after(1000, function, count - 1)  # timer function in tkinter


def timebreak(count):
    if count == 0:
        timer.config(text="Work")
        countdown(work_timer)
    else:
        update_screen(count, timebreak)


def countdown(count):
    global checkmark
    global noworks
    if count == 0:
        noworks += 1
        if noworks == 4:
            noworks *= 0
            timer.config(text="Long break")
            checkmark = ""
            checkmarks.config(text=checkmark)
            timebreak(long_break_timer)
        else:
            checkmark = checkmark + "✔"
            timer.config(text="Short break")
            checkmarks.config(text=checkmark)
            timebreak(short_break_timer)
    else:
        update_screen(count, countdown)


window = tkinter.Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")  # Reading image from the folder with tkinter
# Canvas can create multiple objects on screen, they are layered one above other in succession
canvas.create_image(100, 112, image=tomato_image)  # putting image to screen
timertext = canvas.create_text(100, 125, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))  # putting text on screen
canvas.grid(column=1, row=1)

timer = tkinter.Label(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer.grid(column=1, row=0)
checkmarks = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
checkmarks.grid(column=1, row=3)


def start():
    countdown(work_timer)


def reset():
    global noworks
    global checkmark
    global timercounter
    canvas.itemconfig(timertext, text="25:00")
    timer.config(text="Work")
    noworks = 0
    checkmark = ""
    checkmarks.config(text=checkmark)
    window.after_cancel(timercounter)  # cancelling active timer


start = tkinter.Button(text="Start", command=start)  # when we click on button, command executes
start.grid(column=0, row=2)  # shows button on screen
reset = tkinter.Button(text="Reset", command=reset)
reset.grid(column=2, row=2)

window.mainloop()
