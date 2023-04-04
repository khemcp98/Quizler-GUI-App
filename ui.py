from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='SCORE=0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=250, height=300, bg='white')
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
        self.question_text= self.canvas.create_text(125,150,text='1',font=('Ariel',15,'italic'),
                                                    fill=THEME_COLOR,width=240)

        true = PhotoImage(file='images/true.png')
        false = PhotoImage(file='images/false.png')
        self.true_btn = Button(image=true, highlightthickness=0,command=self.true_pressed)
        self.true_btn.grid(row=2,column=0)
        self.false_btn = Button(image=false, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1)

        self.next_que()

        self.window.mainloop()

    def next_que(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text='You have reached end of the Quiz')
            self.false_btn.config(state="disabled")
            self.true_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_ok):
        if is_ok:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.next_que)

