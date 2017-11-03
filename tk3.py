from tkinter import *

root = Tk()

one = Label(root, text="Label ONE", bg = 'red', fg = 'white')
one.pack()
two = Label(root, text="Label Two", bg = 'green', fg = 'black')
two.pack(fill=X)
three = Label(root, text="Label Three", bg = 'blue', fg = 'white')
three.pack(side=LEFT, fill=Y)




root.mainloop()