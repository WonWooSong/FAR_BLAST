#GUI

__author__ = 'Won Woo Song'
__version__ = '1.0'

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class Display:
    def __init__(self, master):

        # toggle value for radio button
        self.v = IntVar()

        # makes radio button for local and remote
        self.localRadioButton = Radiobutton(master, text="LOCAL", variable=self.v, value=1).grid(row=1, column=1)
        self.remoteRadioButton = Radiobutton(master, text="REMOTE", variable=self.v, value=2).grid(row=1, column=2)

        # makes label for each section
        Label(master, text="Query Family Name").grid(row=2, column=1)
        self.QueryFamily = Entry(master).grid(row=2, column=2)

        Label(master, text="Query File Name").grid(row=3, column=1)
        self.QueryFile = Entry(master).grid(row=3, column=2)

        Label(master, text="Subject File Name").grid(row=4, column=1)
        self.SubjectFile = Entry(master).grid(row=4, column=2)

        Label(master, text="Output File Name").grid(row=5, column=1)
        self.OutputName = Entry(master).grid(row=5, column=2)

        #Label(master, text="Forward BLAST").grid(row=6, column=2)
        #Label(master, text="FAR BLAST").grid(row=7, column=2)

        # button for BLAST
        Button(master, text="Forward BLAST", command=self.forwardBlastButton).grid(row=8, column=1)
        Button(master, text="FAR BLAST", command=self.FarBlastButton).grid(row=8, column=2)

    def forwardBlastButton(self):
        messagebox.showinfo("Forward BLAST", "Please wait for forward BLAST to finish")

    def FarBlastButton(self):
        messagebox.showinfo("FAR BLAST", "Please wait for FAR BLAST to finish")

root = Tk()
root.title("FAR BLAST")
display = Display(root)
root.mainloop()
