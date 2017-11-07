from tkinter import *

# Grid Layout
root = Tk()



def printName(event):
    print("Hello my name is Bucky!")


#button_1 = Button(root, text="Print Name", command=printName) # prints name one way

button_1 = Button(root, text="Print Name") # prints name one way
button_1.bind("<Button-1>", printName) # <Button-1> is left click
button_1.pack()





root.mainloop()