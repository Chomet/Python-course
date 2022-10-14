import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Ui:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.textscore = tkinter.Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.textscore.grid(column=1, row=0, padx=20, pady=20)
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        # If we specify width parameter in canvas text, text will be separated into multiple lines with specified width
        self.questiontext = self.canvas.create_text(150, 125, text="Question", fill=THEME_COLOR, width=280, font=("Arial", 20, "italic"))
        self.green = tkinter.PhotoImage(file="images\\true.png")
        self.correct = tkinter.Button(image=self.green, command=self.check_true, highlightthickness=0)
        self.correct.grid(column=0, row=2, padx=20, pady=20)
        self.red = tkinter.PhotoImage(file="images\\false.png")
        self.incorrect = tkinter.Button(image=self.red, command=self.check_false, highlightthickness=0)
        self.incorrect.grid(column=1, row=2, padx=20, pady=20)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        question_text = self.quiz.next_question()
        if question_text is None:
            self.canvas.itemconfig(self.questiontext, text="End of the quiz!")
            # Disabling the buttons
            self.correct.config(state="disabled")
            self.incorrect.config(state="disabled")
        else:
            self.canvas.itemconfig(self.questiontext, text=question_text)

    def check_true(self):
        result = self.quiz.check_answer("True")
        if result:
            self.score += 1
            self.textscore.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

    def check_false(self):
        result = self.quiz.check_answer("True")
        if not result:
            self.score += 1
            self.textscore.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

