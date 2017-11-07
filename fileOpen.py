from tkinter import filedialog
from tkinter import *
root = Tk()


def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)

root = Tk()


browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()

pathlabel = Label(root)
pathlabel.pack()

root.mainloop()