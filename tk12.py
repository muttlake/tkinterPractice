from tkinter import *
import tkinter.messagebox


root = Tk()


canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 20, fill="red") # everything in tkinter has a fill

greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

#canvas.delete(blackLine)
#canvas.delete(ALL)  # deletes everything


root.mainloop()