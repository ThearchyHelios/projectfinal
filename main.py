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
            

def read_command():
    commands = []
    with open('commands', 'r', encoding="utf-8")as commands_r:
        for i in commands_r:
            i = i.strip('\n').split(',')
            commands.append(i)
    return commands


def update_menu(menu):
    with open("menu", 'w+', encoding="utf-8")as menu_w:
        for i in menu:
            i = ','.join(i) + '\n'
            menu_w.write(i)




def add_menu():
    print("-" * 80, "\n")
    print("Saissez des info comme 'TIAN DE LÉGUMES DU SOLEIL, Dessert, 12' SVP")
    print("-" * 80, "\n")
    menu = read_menu()
    user_add_menu = input("Ajouter ici:\n").strip()
    user_add_menu_list = user_add_menu.split(', ')
    if len(user_add_menu_list) == 3:
        nom_menu = []
        for i in menu:
            nom_menu.append(i[0])
        if user_add_menu_list[0] in nom_menu:
            print("Le Plat a deja ajouter!")
        else:
            menu.append(user_add_menu_list)
            update_menu(menu)
            print("Ajouter Successfully")
    else:
        print("Error")


add_menu()
