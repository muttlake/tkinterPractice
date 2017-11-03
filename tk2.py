from tkinter import *

root = Tk()

# frame is like invisible container
topFrame = Frame(root)
topFrame.pack()  # place it somewhere

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg='red') #First create widgets
button2 = Button(topFrame, text="Button 2", fg='blue')
button3 = Button(topFrame, text="Button 3", fg='green')
button4 = Button(bottomFrame, text="Button 4", fg='purple')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()