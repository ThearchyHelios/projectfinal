# coding:utf-8
# @Time    : 4/22/2020 7:12 PM
# @Author  : Wilson JIANG Yilun
# @FileName: main.py
# @Software: PyCharm

import sys




def print_restaurant_info():
    print("-" * 80,"\n",
          "-" * 30, "RESTAURANT LIPSUM", "-" * 30, "\n",
          "-" * 30, " 15 RUE DES ECOLE", "-" * 30, "\n",
          "-" * 79
          )


def login(function):
    user = 'admin'
    password = '123456'
    print("Saissez votre nome d'utilisateur et keycode!")
    user_user = input("Nom d'utilisateur:")
    user_password = input("PassWord:")
    if user_user == user and user_password == password:
        print("Bienvenue!", user)
    else:
        print("Failed Login!")
        sys.exit(1)



def read_menu():
    menu = []
    with open("menu", 'r', encoding='utf-8')as menu_r:
        for i in menu_r:
            i = i.strip('\n').split(',')
            menu.append(i)
    return menu
            

def update_menu():
    with open()


def add_menu():
    print("-" * 80,"\n")


