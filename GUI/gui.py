#GUI

__author__ = 'Won Woo Song'
__version__ = '1.0'

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from Components.Options import Options

class Display:
    def __init__(self, master):

        # toggle value for radio button
        self.v = IntVar()
        self.options = Options()
        self.numTopHitsForward = StringVar(master, value='5')
        self.numTopHitsReverse = StringVar(master, value='5')
        self.defaultEvalue = StringVar(master, value='10e-5')

        # makes radio button for local and remote
        self.localRadioButton = Radiobutton(master, text="LOCAL", variable=self.v, value=1, command = self.localRadioOption).grid(row=1, column=1)
        self.remoteRadioButton = Radiobutton(master, text="REMOTE", variable=self.v, value=2, command = self.remoteRadioOption).grid(row=1, column=2)

        # makes label for each section
        Label(master, text="Query Family Name").grid(row=2, column=1)
        self.QueryFamily = Entry(master, justify='center').grid(row=2, column=2)

        Label(master, text="Query File Name").grid(row=3, column=1)
        self.QueryFile = Entry(master, justify='center').grid(row=3, column=2)

        Label(master, text="Subject File Name").grid(row=4, column=1)
        self.SubjectFile = Entry(master, justify='center').grid(row=4, column=2)

        Label(master, text="Output File Name").grid(row=5, column=1)
        self.OutputName = Entry(master, justify='center').grid(row=5, column=2)

        Label(master, text="E-value").grid(row=6, column=1)
        self.evalue = Entry(master, textvariable = self.defaultEvalue, justify='center').grid(row=6, column=2)

        Label(master, text="Number of Top Hits for Forward BLAST").grid(row=7, column=1)
        self.topHits = Entry(master, textvariable = self.numTopHitsForward, justify='center').grid(row=7, column=2)

        # this will change the top hits for reverse BLAST
        Label(master, text="Number of Top Hits for Reverse BLAST").grid(row=8, column=1)
        self.topHits = Entry(master, textvariable = self.numTopHitsReverse, justify='center').grid(row=8, column=2)

        # button for BLAST
        Button(master, text="Forward BLAST", command=self.forwardBlastButton).grid(row=9, column=1)
        Button(master, text="FAR BLAST", command=self.FarBlastButton).grid(row=9, column=2)

    def localRadioOption(self):
        messagebox.showinfo("hello", "hello")

    def remoteRadioOption(self):
        messagebox.showinfo("111", "111")

    def showLocalOption(self):
        self.options = Options
        self.options

    def forwardBlastButton(self):
        messagebox.showinfo("Forward BLAST", "Please wait for forward BLAST to finish")

    def FarBlastButton(self):
        messagebox.showinfo("FAR BLAST", "Please wait for FAR BLAST to finish")

root = Tk()
root.title("FAR BLAST")
display = Display(root)
root.mainloop()
