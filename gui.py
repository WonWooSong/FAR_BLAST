#GUI

__author__ = 'Won Woo Song'
__version__ = '1.0'

import os

from tkinter import *
import tkinter as tk
import subprocess
from tkinter import messagebox
from PIL import ImageTk, Image
from threading import Thread
from Components.Options import Options
from Components.FARlocalBLAST import FARlocalBLAST
from Components.FARremoteBLAST import FARremoteBLAST
from Components.LocalForwardBLAST import LocalForwardBLAST
from Components.RemoteForwardBLAST import RemoteForwardBLAST

class Display:
    def __init__(self, master):

        # toggle value for radio button
        self.v = IntVar()
        self.options = Options()

        # default entry values
        self.defaultQueryFamily = StringVar(master, value = 'Cyanidioschyzon_Merolae')
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
        Button(master, text="Forward BLAST", command=self.localForwardBlast).grid(row=9, column=1)
        Button(master, text="FAR BLAST", command=self.FarBlastButton).grid(row=9, column=2)


    def localRadioOption(self):
        messagebox.showinfo("hello", "hello")

    def remoteRadioOption(self):
        messagebox.showinfo("111", "111")

    def showLocalOption(self):
        self.options = Options
        self.options


    # method for the forward BLAST Button
    def forwardBlastButton(self):
        LocalForwardBLAST()

    # method for the FAR BLAST Button
    def FarBlastButton(self):
        messagebox.showinfo("FAR BLAST", "Please wait for FAR BLAST to finish")

    def localForwardBlast(self):
        remote_database = 'makeblastdb -in DataBase/' + self.inputQueryFamily + '.txt -parse_seqids -dbtype prot -out DataBase/' + self.inputQueryFamily
        #remote_database = 'makeblastdb -in DataBase/' + self.inputQueryFamily + '.txt -parse_seqids -dbtype prot -out DataBase/' + self.inputQueryFamily
        # print (remote_database)
        #t1 = Thread(os.system(remote_database))
        #os.system(remote_database)

        remote_databaseCmd = 'blastdbcmd -db DataBase/' + self.inputQueryFamily + ' -dbtype prot -entry ' + self.inputQueryFile + ' -out DataBase/' + self.inputQueryFile + '.txt'
        #t2 = Thread(os.system(remote_databaseCmd))
        #os.system(remote_databaseCmd)

        remote_test = "makeblastdb -in DataBase/" + self.inputQueryFile + ".txt -out Database/" + self.inputQueryFile + " -parse_seqids -dbtype prot"
        #t3 = Thread(os.system(remote_test))
        #os.system(remote_test)


        #forwardBlastTest = 'blastp -query DataBase/' + self.inputQueryFile + '.txt -db DataBase/' + self.inputSubjectFile + ' -evalue ' + self.inputEvalue + ' -out ' + self.inputOutputName

        #forwardBlastTest = 'blastp -query DataBase/' + self.inputQueryFile + '.txt -db DataBase/' + self.inputSubjectFile + ' -evalue ' + self.inputEvalue + ' -out ' + self.inputOutputName + '_Full_Version.txt'
        #os.system(forwardBlastTest)

        #forwardTopHits = "blastp -query DataBase/" + self.inputQueryFile + ".txt -db DataBase/" + self.inputSubjectFile + " -evalue " + self.inputEvalue + " -max_target_seqs " + self.inputOutputName + " -outfmt \"6 sacc \" -out " + self.inputOutputName + '_TopHits.txt'
        #os.system(forwardTopHits)

        os.system(remote_database)
        #os.wait(5)
        #os.system(remote_databaseCmd)
        #os.wait(5)
        #os.system(remote_test)

        #os.wait(5)
        #os.system(forwardBlastTest)
        #os.wait(5)
        #os.system(forwardTopHits)

        '''
        #t1.start()
        t2.start()
        t3.start()
        #t1.join()
        t2.join()
        t3.join()
        '''


root = Tk()
root.title("FAR BLAST")
display = Display(root)
root.mainloop()
