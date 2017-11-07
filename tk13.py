from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

root = Tk()

# photo = ImageTk.PhotoImage(file="soccer.jpg")
#
# label = Label(root, image=photo)
# label.pack()
path="lenna.png"
img = ImageTk.PhotoImage(Image.open(path))

panel = Label(root, image = img)


panel.pack(side = "bottom", fill = "both", expand = "yes")


root.mainloop()
