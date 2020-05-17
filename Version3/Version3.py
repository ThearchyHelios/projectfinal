# coding:utf-8
# @Time    : 5/17/2020 12:26 PM
# @Author  : Wilson JIANG Yilun
# @FileName: Version3.py
# @Software: PyCharm


import sys
import time
from collections import Counter
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


class Application_Version3_Main(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.refreshButton = tk.Button(self, text='Refresh', command=self.refreshButtonConfiem)
        self.refreshButton.grid()

        

    def refreshButtonConfiem(self):
        self.destroy()


    

app = Application_Version3_Main()
app.master.title("First String")
wds = app.master.winfo_screenwidth()
hds = app.master.winfo_screenheight()
x = (wds / 2) - (1000 / 2)
y = (hds / 2) - (1300 / 2)
app.master.geometry('%dx%d+%d+%d' % (1000, 1000, x, y))
app.mainloop()



