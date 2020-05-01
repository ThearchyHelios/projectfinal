import sys
import time
from typing import List
from collections import Counter
import tkinter as tk


class Window(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize = (1500, 1000)
        self.frame = tk.Frame(self.root)
        self.frame.pack()

    def login_window(self):
        self.root.title("Welcome!")
        self.root.geometry('1500x100')
