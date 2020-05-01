import sys
import time
from typing import List
from collections import Counter
import tkinter as tk
import tkinter.messagebox


window = tk.Tk()
window.withdraw  #隐藏窗口
window.title("ProjetFinal")
window.geometry('1000x500')


def login():

    window_login = tk.Tk()
    window_login.title("Welcome!")
    window_login.geometry('500x500')
    window_login.wm_attributes('-topmost', 1)
    tk.Label(window_login, text='User name:(admin)', font=('Arial', 14)).place(x=10, y=170)
    tk.Label(window_login, text='Password:(123456)', font=('Arial', 14)).place(x=10, y=210)
    var_usrname = tk.StringVar()
    entry_usrname = tk.Entry(window_login, textvariable=var_usrname, font=('Arial', 14))
    entry_usrname.place(x=150, y=175)
    var_usrpassword = tk.StringVar()
    entry_usrpassword = tk.Entry(window_login, textvariable=var_usrpassword, font=('Arial', 14), show='*')
    entry_usrpassword.place(x=150, y=215)

    def login_btn():
        usr_name = entry_usrname.get()
        usr_password = entry_usrpassword.get()
        if usr_name == 'admin':
            if usr_password == '123456':
                tkinter.messagebox.showinfo(title='Welcome', message='How are you? ' + 'admin')
            else:
                tkinter.messagebox.showerror(message="Error, le code n'est pas correct, saissez le un autre fois SVP!")
        else:
            tkinter.messagebox.showerror(message="On ne trouvez pas ce Utilisateur!")

    btn_login = tk.Button(window_login, text='Login', command=login_btn)
    btn_login.place(x=150, y=260)




