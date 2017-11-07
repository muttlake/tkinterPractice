from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


root = Tk()

img = ImageTk.PhotoImage(Image.open("empty_image.png"))
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def callback(e):
    img2 = ImageTk.PhotoImage(Image.open("lenna.png"))
    panel.configure(image=img2)
    panel.image = img2

root.bind("<Return>", callback)
root.mainloop()