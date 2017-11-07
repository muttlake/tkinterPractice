from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class ProjectUI:

    inputImageLabel = None
    statusLabel = None

    def __init__(self, master): # master means root or main window

        ## ****** Main Menu ******
        menu = Menu(master)

        master.config(menu=menu)
        subMenu = Menu(menu)

        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Exit", command=quit)

        ## ****** Toolbar ******
        toolbar = Frame(master, bg="azure3")

        insertButton = Button(toolbar, text="Get Image", command=self.getInputImage)
        insertButton.pack(side=LEFT, padx=20, pady=20)

        insertButton = Button(toolbar, text="Quit", command=quit)
        insertButton.pack(side=RIGHT, padx=20, pady=20)
        toolbar.pack(side=TOP, fill=X)

        ## ****** Status Bar ******
        self.statusLabel = Label(root, text="Started Project GUI", bd=1, relief=SUNKEN, anchor=W)  # bd = border, anchor = West
        self.statusLabel.pack(side=BOTTOM, fill=X)

        ## ****** Main Window Frame ******
        mainFrame = Frame(root, width=1600, height=800, bg="gainsboro")  # frame is a blank widget
        mainFrame.pack()

        empty_image = ImageTk.PhotoImage(Image.open("empty_image.png"))
        self.inputImageLabel = Label(mainFrame, image=empty_image)
        self.inputImageLabel.place(x=75, y=75)

    def setStatus(self, statusString):
        self.statusLabel.configure(text=statusString)
        self.statusLabel.text = statusString

    def getInputImage(self):
        filename = filedialog.askopenfilename()
        print("input image should be: ", filename)
        input_image = ImageTk.PhotoImage(Image.open(filename))
        self.inputImageLabel.configure(image=input_image)
        self.inputImageLabel.image = input_image
        self.setStatus("Loaded input image.")



root = Tk()

p = ProjectUI(root)

root.mainloop()

