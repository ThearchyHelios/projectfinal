# coding:utf-8
# @Time    : 4/22/2020 7:12 PM
# @Author  : Wilson JIANG Yilun
# @FileName: main.py
# @Software: PyCharm

import sys
import time


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
    plat_menu = []
    main_menu = []
    boisson_menu = []
    dessert_menu = []
    costomer_want = []
    menu_list = read_menu()
    for i in menu_list:
        if i[1] == "Plat":
            plat_menu.append(i)
    for i in menu_list:
        if i[1] == "Main":
            main_menu.append(i)
    for i in menu_list:
        if i[1] == "Boisson":
            boisson_menu.append(i)
    for i in menu_list:
        if i[1] == "Dessert":
            dessert_menu.append(i)
    while True:
        request_1 = input(
            "Quel type de plat est-ce que vous voudrais ajouter?\nSaissez 'plat' ou 'main' ou 'boisson' ou 'dessert' ou '0' pour exit:")
        if request_1 == "plat":
            print("Nom du plat".ljust(50), "Type".ljust(10), "Quantite".ljust(10), "Prix".ljust(5))
            for i in range(len(plat_menu)):
                print(i + 1, '.', plat_menu[i][0].ljust(50), plat_menu[i][1].ljust(10),
                      plat_menu[i][2].ljust(10),
                      plat_menu[i][3].ljust(5))
            while True:
                request_2 = int(
                    input("Quel plat est-ce que vous voudrais ajouter?\nSaissez un numero, ou '0' pour exit:"))
                if request_2 != 0:
                    costomer_want.append(plat_menu[request_2 - 1])
                    print("Ajouter successfully!")
                else:
                    break

        if request_1 == "main":
            print("Nom du plat".ljust(50), "Type".ljust(10), "Quantite".ljust(10), "Prix".ljust(5))
            for i in range(len(main_menu)):
                print(i + 1, '.', main_menu[i][0].ljust(50), main_menu[i][1].ljust(10),
                      main_menu[i][2].ljust(10),
                      main_menu[i][3].ljust(5))
            while True:
                request_2 = int(
                    input("Quel main est-ce que vous voudrais ajouter?\nSaissez un numero, ou '0' pour exit:"))
                if request_2 != 0:
                    costomer_want.append(main_menu[request_2 - 1])
                    print("Ajouter successfully!")
                else:
                    break
        if request_1 == "boisson":
            print("Nom du plat".ljust(50), "Type".ljust(10), "Quantite".ljust(10), "Prix".ljust(5))
            for i in range(len(boisson_menu)):
                print(i + 1, '.', boisson_menu[i][0].ljust(50), boisson_menu[i][1].ljust(10),
                      boisson_menu[i][2].ljust(10),
                      boisson_menu[i][3].ljust(5))
            while True:
                request_2 = int(
                    input("Quel boisson est-ce que vous voudrais ajouter?\nSaissez un numero, ou '0' pour exit:"))
                if request_2 != 0:
                    costomer_want.append(boisson_menu[request_2 - 1])
                    print("Ajouter successfully!")
                else:
                    break
        if request_1 == "dessert":
            print("Nom du plat".ljust(50), "Type".ljust(10), "Quantite".ljust(10), "Prix".ljust(5))
            for i in range(len(dessert_menu)):
                print(i + 1, '.', dessert_menu[i][0].ljust(50), dessert_menu[i][1].ljust(10),
                      dessert_menu[i][2].ljust(10),
                      dessert_menu[i][3].ljust(5))
            while True:
                request_2 = int(
                    input("Quel dessert est-ce que vous voudrais ajouter?\nSaissez un numero, ou '0' pour exit:"))
                if request_2 != 0:
                    costomer_want.append(dessert_menu[request_2 - 1])
                    print("Ajouter successfully!")
                else:
                    break
        if request_1 == "0":
            break
    return costomer_want


def update_command(command):
    with open('commands', 'w+', encoding='utf-8')as command_w:
        for i in command:
            i = ','.join(i) + '\n'
            command_w.write(i)


def show_command():
    nombre_customer = len(read_command())
    print("Il y a ", str(nombre_customer), "personne, quelle personne est-ce que vous voudrais faire?")
    request = input("Saissez le nom SVP:").strip()
    command_list = read_command()
    for i in command_list:
        if i[0] == request:
            time_command = time.localtime(float(i[-1]))
            time_command_transform = time.strftime('%Y-%m-%d %H:%M:%S', time_command)
            print("Trouver cette personne:", i[0],
                  "Prix: ", i[2],
                  "Temp: ", time_command_transform)


def add_commands():
    print("-" * 80)
    customer_local_time = time.time()
    customer_command_nom = []
    customer_command_prix = 0
    command_list = read_command()
    nom_costomer = input("Saissez le nom SVP")
    customer_command = show_sort_menu()
    for i in range(len(customer_command)):
        customer_command_nom.append(customer_command[i][0])
        customer_command_prix += int(customer_command[i][3])
    add_info = nom_costomer + "," + str(customer_command_nom).strip("[]") + "," + str(
        customer_command_prix) + "," + str(
        customer_local_time)
    add_info_list = add_info.split(",")
    command_list.append(add_info_list)
    update_command(command_list)


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


show_command()
