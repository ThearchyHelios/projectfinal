# coding:utf-8
# @Time    : 4/22/2020 7:12 PM
# @Author  : Wilson JIANG Yilun
# @FileName: main.py
# @Software: PyCharm

import sys


def print_restaurant_info():
    print("-" * 80, "\n",
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
    print("-" * 80)
    print("Saissez des info comme 'TIAN DE LÉGUMES DU SOLEIL(Nom),Dessert(Type),12(Quantite)',5(Prix) SVP")
    print("-" * 80, "\n")
    menu = read_menu()
    user_add_menu = input("Ajouter ici:\n").strip()
    user_add_menu_list = user_add_menu.split(',')
    if len(user_add_menu_list) == 4:
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


def del_menu():
    print("-" * 80)
    print("Saissez le nom du plat SVP")
    print("-" * 80, "\n")
    menu_list = read_menu()
    nombre_menu = len(read_menu())
    del_quel_menu = input("Le nom du Plat: \n").strip()
    for i in menu_list:
        if i[0] == del_quel_menu:
            print("Trouver ce plat:",
                  "Nom: ", i[0], '\n',
                  "Type: ", i[1], '\n',
                  "Quantite: ", i[2], '\n',
                  "prix", i[3])
            request = input("Vous etes sure que vous voudrais del ce plat?(oui/non)")
            if request == "oui":
                index_del_menu = menu_list.index(i)
                del menu_list[index_del_menu]
                update_menu(menu_list)
                print("Successful")
            else:
                print("Exit")


def show_menu():
    print("-" * 80)
    menu = read_menu()
    print("Nom du plat".ljust(50), "Type".ljust(10), "Quantite".ljust(10), "Prix".ljust(5))
    for i in menu:
        print(i[0].ljust(50), i[1].ljust(10), i[2].ljust(10), i[3].ljust(5))


def changer_menu():
    count = 0
    menu_list = read_menu()
    print("-" * 80)
    plat_changer = input("Quel plat est-ce que vous voudrais changer?")
    for i in menu_list:
        if i[0] == plat_changer:
            print("Trouver ce plat:",
                  "Nom: ", i[0], '\n',
                  "Type: ", i[1], '\n',
                  "Quantite: ", i[2], '\n',
                  "prix", i[3])
            print("Quel info est-ce que vous voudrais changer?")
            request = input("Saissez 'nom' pour changer le Nom\n"
                            "Saissez 'type' pour changer le Type\n"
                            "Saissez 'quantite' pour changer le Quantite\n"
                            "Saissez 'prix' pour changer le Prix\n")
            if request == "nom":
                for i in menu_list:
                    if i[0] == plat_changer:
                        nom_changer_apres = input("Vous voudrais changer a quel nom?\n")
                        i[0] = nom_changer_apres
                        update_menu(menu_list)
                        print("Changer successfully")
            if request == "type":
                for i in menu_list:
                    if i[0] == plat_changer:
                        i[1] = input("Quel Type?\n")
                        update_menu(menu_list)
                        print("Changer successfully")
            if request == "quantite":
                for i in menu_list:
                    if i[0] == plat_changer:
                        i[2] = input("Quel est le nombre de quantite?\n")
                        update_menu(menu_list)
                        print("Changer successfully")
            if request == "prix":
                for i in menu_list:
                    if i[0] == plat_changer:
                        i[3] = input("Quel est le prix?\n")
                        update_menu(menu_list)
                        print("Changer successfully")
        else:
            if count == len(menu_list) - 1:
                print("Il n y a ce plat!")
                break
            count += 1


def action_menu():
    print("-" * 80)
    print("Qu'est que vous voulais faire?")
    print("-" * 80)
    request = input("Saissez (1) pour add un plat\n"
                    "Saissez (2) pour del un plat\n"
                    "Saissez (3) pour changer des info sur le menu")
    if request == "1":
        add_menu()
    elif request == "2":
        del_menu()
    elif request == "3":
        changer_menu()


def show_sort_menu():
    sort_menu_list = []
    menu_list = read_menu()
    nombre_plat = 0
    nombre_main = 0
    nombre_boisson = 0
    nombre_dessert = 0
    for i in menu_list:
        if i[1] == "Plat":
            nombre_plat += 1
            sort_menu_list.append(i)
    for i in menu_list:
        if i[1] == "Main":
            nombre_main += 1
            sort_menu_list.append(i)
    for i in menu_list:
        if i[1] == "Boisson":
            nombre_boisson += 1
            sort_menu_list.append(i)
    for i in menu_list:
        if i[1] == "Dessert":
            nombre_dessert += 1
            sort_menu_list.append(i)


def add_commands():
    print("-" * 80)
    nom_costomer = input("Saissez le nom SVP")
    print(show_sort_menu())


def main():
    while True:
        print_restaurant_info()
        print("Quest-ce que vous voudrais faire?")
        request = input("Saissez '1' pour faire qqch sur le Menu\n"
                        "Saissez '2' pour faire qqch sur les commands\n"
                        "Saissez '3' pour regard le Menu\n")
        if request == "1":
            action_menu()

        if request == "3":
            show_menu()


sort_menu()
