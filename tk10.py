from tkinter import *


def doNothing():
    print("Ok Ok I won't.")

root = Tk()

## ****** Main Menu ******

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)


editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

## ****** Toolbar ******

toolbar = Frame(root, bg="blue")

insertButton = Button(toolbar, text="InsertImage", command=doNothing)
insertButton.pack(side=LEFT, padx=20, pady=20)
printButton = Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=20, pady=20)
toolbar.pack(side=TOP, fill=X)

## ****** Status Bar ******
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W) # bd = border, anchor = West
status.pack(side=BOTTOM, fill=X)




root.mainloop()