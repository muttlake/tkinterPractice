from tkinter import *

# Grid Layout
root = Tk()

# can bind multiple events to one widget
# if you left click it something happens
# if you right click it something happens

def leftClick(event):
    print("Left Clicked")

def middleClick(event):
    print("Middle Clicked")

def rightClick(event):
    print("Right Clicked")


frame = Frame(root, width=900, height=600) # frame is a blank widget

frame.bind("<Button-1>", leftClick)
frame.bind("<Button-3>", middleClick)
frame.bind("<Button-2>", rightClick)
frame.pack()


root.mainloop()