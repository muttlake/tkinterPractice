from tkinter import *


class BuckysButtons:

    def __init__(self, master): # master means root or main window
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("This is the message.")


root = Tk()

B = BuckysButtons(root)

root.mainloop()