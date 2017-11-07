from tkinter import *
import tkinter.messagebox


root = Tk()

tkinter.messagebox.showinfo("Window Title", "Monkeys can live up to 300 years.")


answer = tkinter.messagebox.askquestion("Question 1", "Are you older than 1?")

if answer == "yes":
    print("Congratulations you are pretty old.")
else:
    print("You are very young.")




root.mainloop()