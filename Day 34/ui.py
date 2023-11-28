from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuiszInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler") 
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10))
        self.score.grid(column=1, row= 0)
        
        self.canvas = Canvas(width=300, height=250, bg= "white")
        self.question = self.canvas.create_text(150, 125, text="Some Questio here", font=("Arial", 20, "italic"), fill=THEME_COLOR, width= 280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="Day 34/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.is_true)
        self.true_button.grid(column=0, row=2)
        
        false_image = PhotoImage(file="Day 34/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.is_false)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
    def is_true(self):
        self.give_feedback(self.quiz.check_answer("true"))
        
    def is_false(self):
        self.give_feedback(self.quiz.check_answer("false"))
        
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)