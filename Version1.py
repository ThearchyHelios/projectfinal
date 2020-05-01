# coding:utf-8
# @Time    : 4/22/2020 7:12 PM
# @Author  : Wilson JIANG Yilun
# @FileName: Version1.py
# @Software: PyCharm

import sys
import time
from typing import List
from collections import Counter


def login():
    user = 'admin'
    password = '123456'
    print("Saissez votre nome d'utilisateur et keycode!")
    user_user = input("Nom d'utilisateur:")
    user_password = input("PassWord:")
    if user_user == user and user_password == password:
        print("Bienvenue!", user)
        time.sleep(1)
    else:
        print("Failed Login!")
        sys.exit(1)


def print_restaurant_info():
    a = str("-" * 80 + "\n" +
            "-" * 30 + "RESTAURANT LIPSUM" + "-" * 30 + "\n" +
            "-" * 30 + " 15 RUE DES ECOLE" + "-" * 30 + "\n" +
            "-" * 79)
    print(a)


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
            action_menu()
        else:
            menu.append(user_add_menu_list)
            update_menu(menu)
            time.sleep(1)
            print("Ajouter Successfully")
            action_menu()

    else:
        print("Error")
        time.sleep(1)


def del_menu():
    print("-" * 80)
    print("Saissez le nom du plat SVP")
    print("-" * 80, "\n")
    show_menu()
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
                time.sleep(1)
                action_menu()
            else:
                print("Exit")


def show_menu():
    print("-" * 80)
    menu = read_menu()
    print("Nom du plat".ljust(50), "Type".ljust(10), "Quantite".ljust(10), "Prix".ljust(5))
    for i in menu:
        print(i[0].ljust(50), i[1].ljust(10), i[2].ljust(10), i[3].ljust(5))
    time.sleep(1)


def changer_menu():
    count = 0
    menu_list = read_menu()
    print("-" * 80)
    show_menu()
    plat_changer = input("Quel plat est-ce que vous voudrais changer?")
    for i in menu_list:
        if i[0] == plat_changer:
            print("Trouver ce plat:",
                  "Nom: ", i[0], '\n',
                  "Type: ", i[1], '\n',
                  "Quantite: ", i[2], '\n',
                  "Prix: ", i[3])
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
                        print("Maintenant: \n",
                              "Nom: ", i[0], '\n',
                              "Type: ", i[1], '\n',
                              "Quantite: ", i[2], '\n',
                              "Prix: ", i[3])
                        action_menu()
            if request == "type":
                for i in menu_list:
                    if i[0] == plat_changer:
                        i[1] = input("Quel Type?\n")
                        update_menu(menu_list)
                        print("Changer successfully")
                        print("Maintenant: \n",
                              "Nom: ", i[0], '\n',
                              "Type: ", i[1], '\n',
                              "Quantite: ", i[2], '\n',
                              "Prix: ", i[3])
                        action_menu()
            if request == "quantite":
                for i in menu_list:
                    if i[0] == plat_changer:
                        i[2] = input("Quel est le nombre de quantite?\n")
                        update_menu(menu_list)
                        print("Changer successfully")
                        print("Maintenant: \n",
                              "Nom: ", i[0], '\n',
                              "Type: ", i[1], '\n',
                              "Quantite: ", i[2], '\n',
                              "Prix: ", i[3])
                        action_menu()
            if request == "prix":
                for i in menu_list:
                    if i[0] == plat_changer:
                        i[3] = input("Quel est le prix?\n")
                        update_menu(menu_list)
                        print("Changer successfully")
                        print("Maintenant: \n",
                              "Nom: ", i[0], '\n',
                              "Type: ", i[1], '\n',
                              "Quantite: ", i[2], '\n',
                              "Prix: ", i[3])
                        time.sleep(1)
                        action_menu()
        else:
            if count == len(menu_list) - 1:
                print("Il n y a ce plat!")
                break
            count += 1
    time.sleep(1)


def action_menu():
    print("-" * 80)
    print("Qu'est que vous voulais faire?")
    print("-" * 80)
    request = input("Saissez (1) pour add un plat\n"
                    "Saissez (2) pour del un plat\n"
                    "Saissez (3) pour changer des info sur le menu\n"
                    "Saissez (0) pour retourner a la principal menu")
    if request == "1":
        add_menu()
    elif request == "2":
        del_menu()
    elif request == "3":
        changer_menu()
    elif request == "0":
        main()



def show_sort_menu():
    sort_menu_list = []
    plat_menu = []
    main_menu: List[List[str]] = []
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


def action_command():
    print("-" * 80)
    print("Qu'est que vous voulais faire?")
    print("-" * 80)
    request = input("Saissez (1) pour add un command\n"
                    "Saissez (2) pour del un command\n"
                    "Saissez (3) pour regard touts les commands par chaque personne\n"
                    "Saissez (4) pour regarder le histoire des commands\n"
                    "Saissez (0) pour retourner a la menu principal")
    if request == "1":
        add_commands()
    if request == "2":
        del_command()
    if request == "3":
        show_command()
    if request == "4":
        history_commands()
    if request == "0":
        time.sleep(1)
        main()


def update_command(command):
    with open('commands', 'w+', encoding='utf-8')as command_w:
        for i in command:
            i = ','.join(i) + '\n'
            command_w.write(i)


def del_command():
    print("-" * 80)
    print("Saissez le nom du client SVP")
    print("-" * 80, "\n")
    command_list = read_command()
    nombre_command = len(read_command())
    del_quel_command = input("Le nom du Client: \n").strip()
    for i in command_list:
        if i[0] == del_quel_command:
            time_command = time.localtime(float(i[-1]))
            time_command_transform = time.strftime('%Y-%m-%d %H:%M:%S', time_command)
            print("Trouver ce client:",
                  "Nom: ", i[0], '\n',
                  "Type: ", i[1], '\n',
                  "Prix: ", i[-2], '\n',
                  "Temp: ", time_command_transform)
            request = input("Vous etes sure que vous voudrais del ce client? (oui/non)")
            if request == "oui":
                index_del_command = command_list.index(i)
                del command_list[index_del_command]
                update_command(command_list)
                print("Successful")
                action_command()
                time.sleep(1)
            else:
                print("Exit")
                time.sleep(1)


def show_command():
    nombre_customer = len(read_command())
    print("Il y a ", str(nombre_customer), "personne, quelle personne est-ce que vous voudrais faire?")
    command_list = read_command()
    while True:
        request = input("Saissez le nom SVP, ou saissez 0 pour exit:").strip()
        count = 0
        for i in command_list:
            if i[0] == request:
                time_command = time.localtime(float(i[-1]))
                time_command_transform = time.strftime('%Y-%m-%d %H:%M:%S', time_command)
                show_command_plat = len(i[1:-2])
                print("Trouver cette personne:", i[0], '\t',
                      "Prix:", i[-2], '\t',
                      "Plats: ")
                for k in range(show_command_plat):
                    print(k + 1, ": ", i[k + 1].strip("[]'' "))
                print("Temp de command ajouter:", time_command_transform)
            elif request == "0":
                time.sleep(1)
                action_command()
            else:
                count += 1
                if count == len(command_list):
                    print("On ne trouvez pas cette personne!")


def add_commands():
    print("-" * 80)
    customer_local_time = time.time()
    customer_command_nom = []
    customer_command_prix = 0
    command_list = read_command()
    nom_costomer = input("Saissez le nom SVP")
    for i in command_list:
        if i[0] == nom_costomer:
            print("Il y a un autre customer qui s'appelle: " + nom_costomer)
            break
        else:
            customer_command = show_sort_menu()
            for k in range(len(customer_command)):
                customer_command_nom.append(customer_command[k][0])
                customer_command_prix += int(customer_command[k][3])
            add_info = nom_costomer + "," + str(customer_command_nom).strip("[]") + "," + str(
                customer_command_prix) + "," + str(
                customer_local_time)
            add_info_list = add_info.split(",")
            command_list.append(add_info_list)
            update_command(command_list)
            print("Success")
    time.sleep(2)


def history_commands():
    print("-" * 80)
    command_list = read_command()
    prix = 0
    prix_dans_les_sept_jours = 0
    commands_dans_les_sept_jours = 0
    local_time = time.time()
    plat_des_commands_passe = []
    plat_des_commands_passe_apres = []
    for i in command_list:
        prix += int(i[-2])
        if local_time - float(i[-1]) < 86400 * 7:
            prix_dans_les_sept_jours += int(i[-2])
            commands_dans_les_sept_jours += 1
    print("Nombre total de commands passes: ", len(command_list), "\n")
    print("Commandes passees dans les 7 jours: ", commands_dans_les_sept_jours, "\n")
    print("Montant total des commandes: ", prix, "\n")
    print("Montants total dans les 7 jours: ", prix_dans_les_sept_jours, "\n")
    for i in command_list:
        plat_des_commands_passe.append(i[1:-2])
    t = 0
    for i in plat_des_commands_passe:
        for k in range(len(i)):
            plat_des_commands_passe_apres.append(str(plat_des_commands_passe[t][k].strip("[]\'\"\\ ")))
        t += 1
    top_ten = Counter(plat_des_commands_passe_apres).most_common(10)
    print("-" * 40, '\n'
                    "Voici des TOP 10 Plat: \n")

    for i in range(len(top_ten)):
        print(top_ten[i][0])
    time.sleep(2)


def main():
    while True:
        print_restaurant_info()
        print("Quest-ce que vous voudrais faire?")
        request = input("Saissez '1' pour faire qqch sur le Menu\n"
                        "Saissez '2' pour faire qqch sur les commands\n"
                        "Saissez '3' pour regard le Menu\n"
                        "Saissez '0' pour Exit")
        if request == "1":
            action_menu()
        if request == "2":
            action_command()
        if request == "3":
            show_menu()
        if request == "0":
            print("Au Revoir!")
            time.sleep(2)
            sys.exit(1)


login()
main()
