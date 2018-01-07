from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class Display:
    def __init__(self, master):

        # toggle value for radio button
        v = IntVar()

        #makes radio button for local and remote
        Radiobutton(master, text="One", variable=v, value=1).grid(row=0, column=1)
        Radiobutton(master, text="Two", variable=v, value=2).grid(row=1, column=2)

        #makes label for each section
        Label(master, text="Query Family Name").grid(row=1, column=1)
        Label(master, text="Query File Name").grid(row=2, column=1)
        Label(master, text="Subject File Name").grid(row=3, column=1)
        Label(master, text="Output File Name").grid(row=4, column=1)
        Label(master, text="Forward BLAST").grid(row=5, column=1)
        Label(master, text="FAR BLAST").grid(row=6, column=1)



root = Tk()
root.title("FAR BLAST")
display = Display(root)
root.mainloop()
