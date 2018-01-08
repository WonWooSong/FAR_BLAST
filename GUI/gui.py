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

        # default entry values
        self.defaultQueryFamily = StringVar(master, value = 'Cyanidioschyzon_Merola')
        self.defaultQueryFile = StringVar(master, value = 'Q85FV4.1')
        self.defaultSubject = StringVar(master, value = 'nr')
        self.defaultOutputName = StringVar(master, value = 'test')
        self.defaultNumTopHitsForward = StringVar(master, value='5')
        self.defaultNumTopHitsReverse = StringVar(master, value='5')
        self.defaultEvalue = StringVar(master, value='10e-5')

        # makes radio button for local and remote
        self.localRadioButton = Radiobutton(master, text="LOCAL", variable=self.v, value=1, command = self.localRadioOption).grid(row=1, column=1)
        self.remoteRadioButton = Radiobutton(master, text="REMOTE", variable=self.v, value=2, command = self.remoteRadioOption).grid(row=1, column=2)

        # makes label for each section
        Label(master, text="Query Family Name").grid(row=2, column=1)
        self.QueryFamily = Entry(master, textvariable = self.defaultQueryFamily, justify='center')
        self.QueryFamily.grid(row=2, column=2)

        Label(master, text="Query File Name").grid(row=3, column=1)
        self.QueryFile = Entry(master, textvariable = self.defaultQueryFile, justify='center')
        self.QueryFile.grid(row=3, column=2)

        Label(master, text="Subject File Name").grid(row=4, column=1)
        self.SubjectFile = Entry(master, textvariable = self.defaultSubject, justify='center')
        self.SubjectFile.grid(row=4, column=2)

        Label(master, text="Output File Name").grid(row=5, column=1)
        self.OutputName = Entry(master, textvariable = self.defaultOutputName, justify='center')
        self.OutputName.grid(row=5, column=2)

        Label(master, text="E-value").grid(row=6, column=1)
        self.evalue = Entry(master, textvariable = self.defaultEvalue, justify='center')
        self.evalue.grid(row=6, column=2)

        Label(master, text="Number of Top Hits for Forward BLAST").grid(row=7, column=1)
        self.forwardTopHits = Entry(master, textvariable = self.defaultNumTopHitsForward, justify='center')
        self.forwardTopHits.grid(row=7, column=2)

        # this will change the top hits for reverse BLAST
        Label(master, text="Number of Top Hits for Reverse BLAST").grid(row=8, column=1)
        self.reverseTopHits = Entry(master, textvariable = self.defaultNumTopHitsReverse, justify='center')
        self.reverseTopHits.grid(row=8, column=2)

        # gets the Entry input for the BLAST
        self.inputQueryFamily = self.QueryFamily.get()
        self.inputQueryFile = self.QueryFile.get()
        self.inputSubjectFile = self.SubjectFile.get()
        self.inputOutputName = self.OutputName
        self.inputEvalue = self.evalue.get()
        self.inputForwardTopHits = self.forwardTopHits.get()
        self.inputReverseTopHits = self.reverseTopHits.get()

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
        messagebox.showinfo("Forward BLAST", self.hi)

    def FarBlastButton(self):
        messagebox.showinfo("FAR BLAST", "Please wait for FAR BLAST to finish")

root = Tk()
root.title("FAR BLAST")
display = Display(root)
root.mainloop()
