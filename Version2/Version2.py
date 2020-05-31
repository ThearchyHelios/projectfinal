# coding:utf-8
# @Time    : 5/1/2020 9:37 AM
# @Author  : Wilson JIANG Yilun
# @FileName: Version2.py
# @Software: PyCharm

import sys
import time
from collections import Counter
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


def login():
    window_login = tk.Tk()  # Creer un Login Window
    window_login.title("Welcome!")
    window_login.geometry('350x150')
    window_login.wm_attributes('-topmost', 1)
    tk.Label(window_login,
             text='User name: ',
             font=('Arial', 14)).place(x=10, y=10)
    tk.Label(window_login,
             text='Password: ',
             font=('Arial', 14)).place(x=10, y=40)
    var_usrname = tk.StringVar()
    var_usrname.set('admin')  # Nom d'utilisateur de saisie automatique
    entry_usrname = tk.Entry(window_login,
                             textvariable=var_usrname,
                             font=('Arial', 14))
    entry_usrname.place(x=120, y=10)
    var_usrpassword = tk.StringVar()
    var_usrpassword.set('123456')  # Not de passe de saisie automatique
    entry_usrpassword = tk.Entry(window_login,
                                 textvariable=var_usrpassword,
                                 font=('Arial', 14),
                                 show='*')
    entry_usrpassword.place(x=120, y=40)

    def login_btn():
        usr_name = entry_usrname.get()
        usr_password = entry_usrpassword.get()
        if usr_name == 'admin':  # Déterminer si le nom d'utilisteur est correct
            if usr_password == '123456':  # Déterminer si le mot de pass est correct
                tkinter.messagebox.showinfo(title='Welcome',
                                            message='Welcome ' + usr_name)
                window_login.destroy()
                main()
            else:
                tkinter.messagebox.showerror(
                    message="Error, le code n'est pas correct, saissez le un autre fois SVP!")  # Si le mot de passe n'est pas correct
                # Réinitialiser le nom d'utilisateur et le mot de pass
                var_usrname.set('admin')
                var_usrpassword.set('123456')
        else:
            tkinter.messagebox.showerror(
                message="On ne trouvez pas ce Utilisateur!")  # Si le nom d'utilisateur n'est oas correct
            var_usrname.set('admin')
            var_usrpassword.set('123456')

    def cancel_button():
        sys.exit(1)

    btn_login = tk.Button(window_login,
                          text='Login',
                          command=login_btn)
    btn_login.place(x=180, y=90)
    btn_cancel = tk.Button(window_login,
                           text='Cancel',
                           command=cancel_button)
    btn_cancel.place(x=100, y=90)
    window_login.mainloop()


def main():
    window = tk.Tk()
    window.title("ProjetFinal")
    # Obtenir des infomations sur la taille de l'écran
    wds = window.winfo_screenwidth()
    hds = window.winfo_screenheight()
    x = (wds / 2) - (wds / 4)
    y = (hds / 2) - (hds / 4)
    # Centrez l'écran
    window.geometry('%dx%d+%d+%d' % (wds / 2, hds / 4, x, y))
    label_window_main_help = tk.Label(window,
                                      text="Cliquer le 'File' dans le Menu pour regarde des fonction\n"
                                           "Si vous souhaitez rafraîchir ce program,\n"
                                           "⬆Veuillez cliquer sur le bouton 'RETURN MAIN'",
                                      font=('Arial', 20))
    label_window_main_help.place(x=10, y=100)

    # Cette fonction est utilisée pour afficher toutes les informations sur le plat.
    def show_menu():
        label_window_main_help.place_forget()
        window_show_menu = tk.Tk()
        window_show_menu.title('Menu')
        number = ttk.Treeview(window_show_menu)
        count = 0
        menu = read_menu()
        # Créer un tableau pour afficher toutes les informations.
        number['columns'] = ("Nom du Plat", "Type", "Quantite", "Prix")
        # La valeur de la colonne.
        number.column("Nom du Plat", width=300)
        number.column("Type", width=100)
        number.column("Quantite", width=100)
        number.column("Prix", width=100)
        # La texte de la colonne.
        number.heading("Nom du Plat", text="Nom du Plat")
        number.heading("Type", text="Type")
        number.heading("Quantite", text="Quantite")
        number.heading("Prix", text="Prix")

        for i in menu:
            count += 1
            number.insert("", count, text=count, values=(
                i[0], i[1], int(i[2]), int(i[3])))

        # Cette fonction est utilisée pour trier les informations.
        def show_sort_menu(tv, column, reverse):
            l = [(tv.set(k, column), k) for k in tv.get_children('')]
            # print(tv.get_children(''))
            l.sort(reverse=reverse)
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            tv.heading(column, command=lambda: show_sort_menu(
                tv, column, not reverse))

        for col in number['columns']:
            number.heading(
                col, text=col, command=lambda _col=col: show_sort_menu(number, _col, False))

        number.pack()

    def add_menu():  # Cette fonction est utilisée pour augmenter le menu.
        label_window_main_help.place_forget()
        tk.Label(window,
                 text="Saissez des info SVP",
                 font=('Arial', 20)).place(x=10, y=50)
        tk.Label(window,
                 text="Il y a Type comme Main, Plat, Boisson, Dessert",
                 font=('Arial', 20)).place(x=10, y=90)
        # Définir des types numériques.
        var_add_menu_nom = tk.StringVar()
        var_add_menu_type = tk.StringVar()
        var_add_menu_quantite = tk.StringVar()
        var_add_menu_prix = tk.StringVar()
        # Créer 5 Labels et Entry pour pouvoir entier des informations sur le plat.
        tk.Label(window, text="Nom: ", font=('Arial', 20)).place(x=10, y=150)
        entry_add_menu_nom = tk.Entry(window,
                                      textvariable=var_add_menu_nom,
                                      font=('Arial', 14))
        entry_add_menu_nom.place(x=150,
                                 y=150,
                                 width=300)
        tk.Label(window, text="Type:", font=('Arial', 20)).place(x=10, y=200)
        entry_add_menu_type = tk.Entry(window,
                                       textvariable=var_add_menu_type,
                                       font=('Arial', 14))
        entry_add_menu_type.place(x=150,
                                  y=200,
                                  width=150)
        tk.Label(window, text="Quantite:", font=(
            'Arial', 20)).place(x=10, y=250)
        entry_add_menu_quantite = tk.Entry(window,
                                           textvariable=var_add_menu_quantite,
                                           font=('Arial', 14))
        entry_add_menu_quantite.place(x=150,
                                      y=250,
                                      width=100)
        tk.Label(window, text="Prix:", font=('Arial', 20)).place(x=10, y=300)
        entry_add_menu_prix = tk.Entry(window,
                                       textvariable=var_add_menu_prix,
                                       font=('Arial', 14))
        entry_add_menu_prix.place(x=150,
                                  y=300,
                                  width=100)

        # ----------------------------------------------

        def add_menu_confirm():  # Cette fonction est utilisée pour répondre aux événements de clic de button 'Confirm'
            # Obteir des informations sur le plat.
            add_menu_plat_nom = entry_add_menu_nom.get()
            add_menu_plat_type = entry_add_menu_type.get()
            add_menu_plat_quantite = entry_add_menu_quantite.get()
            add_menu_plat_prix = entry_add_menu_prix.get()

            add_menu_plat_nom = str(add_menu_plat_nom)
            add_menu_plat_type = str(add_menu_plat_type)
            add_menu_plat_quantite = int(add_menu_plat_quantite)
            add_menu_plat_prix = int(add_menu_plat_prix)
            user_add_menu_list = []
            menu = read_menu()
            nom_menu = []
            user_add_menu_list.append(add_menu_plat_nom.lstrip().rstrip())
            user_add_menu_list.append(add_menu_plat_type.lstrip().rstrip())
            user_add_menu_list.append(str(add_menu_plat_quantite))
            user_add_menu_list.append(str(add_menu_plat_prix))
            for i in menu:
                nom_menu.append(i[0])
            # Déterminer si le plat existe déjà.
            if user_add_menu_list[0] in nom_menu:
                tkinter.messagebox.showinfo(title='Error',
                                            message="Le Plat a deja ajouter!")
            else:
                menu.append(user_add_menu_list)
                update_menu(menu)
                tkinter.messagebox.showinfo(title='Successful',
                                            message="Ajouter Successfully")
                window.destroy()
                main()

        btn_add_menu_confirm = tk.Button(window, text='Confirm',
                                         command=add_menu_confirm)
        btn_add_menu_confirm.place(x=500,
                                   y=300)

    def del_menu():  # Cette fonction est utilisée pour supprimer le plat.
        label_window_main_help.place_forget()
        tk.Label(window,
                 text="Saissez le nom du plat SVP",
                 font=('Arial', 20)).place(x=10, y=50)

        var_del_quel_menu = tk.StringVar()
        entry_del_quel_menu = tk.Entry(window,
                                       textvariable=var_del_quel_menu,
                                       font=('Arial', 14))

        entry_del_quel_menu.place(x=10,
                                  y=100,
                                  width=400)
        # Créer une fenêtre pour afficher le menu.
        window_show_menu_del_menu = tk.Tk()
        window_show_menu_del_menu.title('Menu')
        number = ttk.Treeview(window_show_menu_del_menu)
        count = 0
        menu = read_menu()
        number['columns'] = ("Nom du Plat", "Type", "Quantite", "Prix")
        number.column("Nom du Plat", width=300)
        number.column("Type", width=100)
        number.column("Quantite", width=100)
        number.column("Prix", width=100)
        number.heading("Nom du Plat", text="Nom du Plat")
        number.heading("Type", text="Type")
        number.heading("Quantite", text="Quantite")
        number.heading("Prix", text="Prix")

        for i in menu:
            count += 1
            number.insert("", count, text=count, values=(
                i[0], i[1], int(i[2]), int(i[3])))

        def numbreview_click(event):  # cette formule est utilisée
            # pour effecteur l'opération après avoir cliqué sur le plat.
            for item in number.selection():
                item_text = number.item(item, "values")
                # print(item_text)
                click_menu = list(item_text)
                click_menu_nom = click_menu[0]
                var_del_quel_menu.set(click_menu_nom)

        def show_sort_menu(tv, column, reverse):
            l = [(tv.set(k, column), k) for k in tv.get_children('')]
            # print(tv.get_children(''))
            l.sort(reverse=reverse)
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            tv.heading(column, command=lambda: show_sort_menu(
                tv, column, not reverse))

        for col in number['columns']:
            number.heading(
                col, text=col, command=lambda _col=col: show_sort_menu(number, _col, False))

        number.pack()
        # Cette formule est utilisé pour juger le clic de souris.
        number.bind('<ButtonRelease-1>', numbreview_click)

        def del_menu_confirm():
            menu_list = read_menu()
            count = 0
            del_quel_menu = str(entry_del_quel_menu.get()).strip()
            for i in menu_list:
                if i[0] != del_quel_menu:
                    count += 1
                    if count == len(menu_list):
                        tkinter.messagebox.showerror(title="Error",
                                                     message="On ne trouve pas ce plat!")

                if i[0] == del_quel_menu:
                    window_del_menu_show = tk.Tk()
                    window_del_menu_show.title("Del Menu")
                    wds2 = window_del_menu_show.winfo_screenwidth()
                    hds2 = window_del_menu_show.winfo_screenheight()
                    x2 = (wds2 / 2) - (1000 / 2)
                    y2 = (hds2 / 2) - (1300 / 2)
                    window_del_menu_show.geometry(
                        '%dx%d+%d+%d' % (1000, 1500, x2, y2))
                    tk.Label(window_del_menu_show,
                             text="Trouver se plat:",
                             font=('Arial', 20)).place(x=10,
                                                       y=10)
                    tk.Label(window_del_menu_show,
                             text=("Nom: " + i[0]),
                             font=('Arial', 20)).place(x=10,
                                                       y=50)
                    tk.Label(window_del_menu_show,
                             text=("Type: " + i[1]),
                             font=('Arial', 20)).place(x=10,
                                                       y=80)
                    tk.Label(window_del_menu_show,
                             text=("Quantite: " + i[2]),
                             font=('Arial', 20)).place(x=10,
                                                       y=110)
                    tk.Label(window_del_menu_show,
                             text=("Prix: " + i[3]),
                             font=('Arial', 20)).place(x=10,
                                                       y=140)
                    tk.Label(window_del_menu_show,
                             text="Vous etes sure que vous voudrais del ce plat?",
                             font=('Arial', 20)).place(x=10,
                                                       y=190)

                    def del_menu_show_oui():
                        index_del_menu = menu_list.index(i)
                        del menu_list[index_del_menu]
                        update_menu(menu_list)
                        tkinter.messagebox.showinfo(title='Successful',
                                                    message="Del Successfully")
                        window_del_menu_show.destroy()
                        window_show_menu_del_menu.destroy()
                        window.destroy()
                        main()

                    def del_menu_show_non():
                        tkinter.messagebox.showinfo(title="Cancel",
                                                    message="Cancel")
                        window_del_menu_show.destroy()

                    btn_del_menu_show_non = tk.Button(window_del_menu_show,
                                                      text="NON",
                                                      command=del_menu_show_non)
                    btn_del_menu_show_non.place(x=250,
                                                y=220)
                    btn_del_menu_show_oui = tk.Button(window_del_menu_show,
                                                      text="OUI",
                                                      command=del_menu_show_oui)
                    btn_del_menu_show_oui.place(x=300,
                                                y=220)
                    window_del_menu_show.mainloop()

        btn_del_menu_confirm = tk.Button(window,
                                         text="Confirm",
                                         command=del_menu_confirm)
        btn_del_menu_confirm.place(x=300,
                                   y=150)

    def changer_menu():
        label_window_main_help.place_forget()
        menu_list = read_menu()

        tk.Label(window,
                 text="Quel plat est-ce que vous voudrais changer?",
                 font=('Arial', 20)).place(x=10,
                                           y=50)
        var_changer_menu_plat = tk.StringVar()
        entry_changer_menu_plat = tk.Entry(window,
                                           textvariable=var_changer_menu_plat,
                                           font=('Arial', 14))
        entry_changer_menu_plat.place(x=10,
                                      y=100,
                                      width=800)

        window_show_menu_change_menu = tk.Tk()
        window_show_menu_change_menu.title('Menu')
        number = ttk.Treeview(window_show_menu_change_menu)
        count = 0
        menu = read_menu()
        number['columns'] = ("Nom du Plat", "Type", "Quantite", "Prix")
        number.column("Nom du Plat", width=300)
        number.column("Type", width=100)
        number.column("Quantite", width=100)
        number.column("Prix", width=100)
        number.heading("Nom du Plat", text="Nom du Plat")
        number.heading("Type", text="Type")
        number.heading("Quantite", text="Quantite")
        number.heading("Prix", text="Prix")

        for i in menu:
            count += 1
            number.insert("", count, text=count, values=(
                i[0], i[1], int(i[2]), int(i[3])))

        def numbreview_click(event):
            for item in number.selection():
                item_text = number.item(item, "values")
                # print(item_text)
                click_menu = list(item_text)
                click_menu_nom = click_menu[0]
                var_changer_menu_plat.set(click_menu_nom)

        def show_sort_menu(tv, column, reverse):
            l = [(tv.set(k, column), k) for k in tv.get_children('')]
            # print(tv.get_children(''))
            l.sort(reverse=reverse)
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            tv.heading(column, command=lambda: show_sort_menu(
                tv, column, not reverse))

        for col in number['columns']:
            number.heading(
                col, text=col, command=lambda _col=col: show_sort_menu(number, _col, False))

        number.pack()
        number.bind('<ButtonRelease-1>', numbreview_click)

        def change_menu_confirm():
            plat_changer = str(entry_changer_menu_plat.get()).strip()
            count2 = 0
            for m in menu_list:
                if plat_changer != m[0]:
                    count2 += 1
                    if count2 == len(menu_list):
                        tk.messagebox.showerror(title="Error",
                                                message="Il n y a pas ce plat!")

            for m in menu_list:
                plat_changer = str(entry_changer_menu_plat.get()).strip()
                if m[0] == plat_changer:
                    window_change_menu_show = tk.Tk()
                    window_change_menu_show.title("Change Menu")
                    wds2 = window_change_menu_show.winfo_screenwidth()
                    hds2 = window_change_menu_show.winfo_screenheight()
                    x2 = (wds2 / 2) - (1000 / 2)
                    y2 = (hds2 / 2) - (500 / 2)
                    window_change_menu_show.geometry(
                        '%dx%d+%d+%d' % (500, 500, x2, y2))
                    tk.Label(window_change_menu_show,
                             text="Trouver se plat:",
                             font=('Arial', 20)).place(x=10,
                                                       y=10)
                    tk.Label(window_change_menu_show,
                             text=("Nom: " + m[0]),
                             font=('Arial', 20)).place(x=10,
                                                       y=50)
                    tk.Label(window_change_menu_show,
                             text=("Type: " + m[1]),
                             font=('Arial', 20)).place(x=10,
                                                       y=80)
                    tk.Label(window_change_menu_show,
                             text=("Quantite: " + m[2]),
                             font=('Arial', 20)).place(x=10,
                                                       y=110)
                    tk.Label(window_change_menu_show,
                             text=("Prix: " + m[3]),
                             font=('Arial', 20)).place(x=10,
                                                       y=140)
                    tk.Label(window_change_menu_show,
                             text="Est-ce que vous voudrais changer?",
                             font=('Arial', 20)).place(x=10,
                                                       y=190)
                    var_change_menu_show = tk.StringVar()
                    entry_changer_menu_show = tk.Entry(window_change_menu_show,
                                                       textvariable=var_change_menu_show,
                                                       font=('Arial', 14))
                    entry_changer_menu_show.place(x=10,
                                                  y=220)

                    def change_menu_show_nom():
                        for k in menu_list:
                            if k[0] == plat_changer:
                                nom_changer_apres = entry_changer_menu_show.get()

                                k[0] = nom_changer_apres
                                update_menu(menu_list)
                                tkinter.messagebox.showinfo(title="Successful",
                                                            message='Change Successfully')
                                window_change_menu_show.destroy()
                                window_show_menu_change_menu.destroy()
                                window.destroy()
                                main()

                    def change_menu_show_type():
                        for k in menu_list:
                            if k[0] == plat_changer:
                                k[1] = entry_changer_menu_show.get()
                                update_menu(menu_list)
                                tkinter.messagebox.showinfo(title="Successful",
                                                            message='Change Successfully')
                                window_change_menu_show.destroy()
                                window_show_menu_change_menu.destroy()
                                window.destroy()
                                main()

                    def change_menu_show_quantite():
                        for k in menu_list:
                            if k[0] == plat_changer:
                                k[2] = entry_changer_menu_show.get()
                                update_menu(menu_list)
                                tkinter.messagebox.showinfo(title="Successful",
                                                            message='Change Successfully')
                                window_change_menu_show.destroy()
                                window_show_menu_change_menu.destroy()
                                window.destroy()
                                main()

                    def change_menu_show_prix():
                        for k in menu_list:
                            if k[0] == plat_changer:
                                k[3] = entry_changer_menu_show.get()
                                update_menu(menu_list)
                                tkinter.messagebox.showinfo(title="Successful",
                                                            message='Change Successfully')
                                window_change_menu_show.destroy()
                                window_show_menu_change_menu.destroy()
                                window.destroy()
                                main()

                    btn_change_menu_show_nom = tk.Button(window_change_menu_show,
                                                         text="Nom",
                                                         command=change_menu_show_nom)
                    btn_change_menu_show_nom.place(x=10, y=250)
                    btn_change_menu_show_type = tk.Button(window_change_menu_show,
                                                          text="Type",
                                                          command=change_menu_show_type)
                    btn_change_menu_show_type.place(x=80, y=250)
                    btn_change_menu_show_quantite = tk.Button(window_change_menu_show,
                                                              text="Quantite",
                                                              command=change_menu_show_quantite)
                    btn_change_menu_show_quantite.place(x=150, y=250)
                    btn_change_menu_show_prix = tk.Button(window_change_menu_show,
                                                          text="Prix",
                                                          command=change_menu_show_prix)
                    btn_change_menu_show_prix.place(x=250,
                                                    y=250)
                    window_change_menu_show.mainloop()

        btn_change_menu_confirm = tk.Button(window,
                                            text="Confirm",
                                            command=change_menu_confirm)
        btn_change_menu_confirm.place(x=200,
                                      y=140)

    def del_command():
        label_window_main_help.place_forget()

        tk.Label(window,
                 text="Saissez le nom du client SVP",
                 font=('Arial', 20)).place(x=10,
                                           y=50)
        command_list = read_command()
        var_del_quel_command = tk.StringVar()
        entry_del_quel_command = tk.Entry(window,
                                          textvariable=var_del_quel_command,
                                          font=('Arial', 20))
        entry_del_quel_command.place(x=10,
                                     y=100)

        window_show_command_del_command = tk.Tk()
        window_show_command_del_command.title('Command')
        number = ttk.Treeview(window_show_command_del_command)
        count = 0
        command = read_command()
        number['columns'] = ("Nom du Client", "Prix", "Date")
        number.column("Nom du Client", width=100)
        number.column("Prix", width=100)
        number.column("Date", width=300)
        number.heading("Nom du Client", text="Nom du Client")
        number.heading("Prix", text="Prix")
        number.heading("Date", text="Date")

        for i in command:
            count += 1
            time_command = time.localtime(float(i[-1]))
            time_command_transform = time.strftime(
                '%Y-%m-%d %H:%M:%S', time_command)
            number.insert("", count, text=count, values=(
                i[0], i[-2], time_command_transform))

        def numbreview_click(event):
            for item in number.selection():
                item_text = number.item(item, "values")
                # print(item_text)
                click_command = list(item_text)
                click_menu_nom = click_command[0]
                var_del_quel_command.set(click_menu_nom)

        def show_sort_menu(tv, column, reverse):
            l = [(tv.set(k, column), k) for k in tv.get_children('')]
            # print(tv.get_children(''))
            l.sort(reverse=reverse)
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            tv.heading(column, command=lambda: show_sort_menu(
                tv, column, not reverse))

        for col in number['columns']:
            number.heading(
                col, text=col, command=lambda _col=col: show_sort_menu(number, _col, False))

        number.pack()
        number.bind('<ButtonRelease-1>', numbreview_click)

        def del_command_cancel():
            window.destroy()
            main()

        def del_command_confirm():
            del_quel_command = str(entry_del_quel_command.get()).strip()
            count = 0
            for i in command_list:
                if i[0] != del_quel_command:
                    count += 1
                    if count == len(command_list):
                        tkinter.messagebox.showerror(title="Error",
                                                     message="Il n y a pas ce command!")
            for i in command_list:
                if i[0] == del_quel_command:
                    time_command = time.localtime(float(i[-1]))
                    time_command_transform = time.strftime(
                        '%Y-%m-%d %H:%M:%S', time_command)
                    window_del_command_show = tk.Tk()
                    window_del_command_show.title("Change Menu")
                    wds3 = window_del_command_show.winfo_screenwidth()
                    hds3 = window_del_command_show.winfo_screenheight()
                    x3 = (wds3 / 2) - (1000 / 2)
                    y3 = (hds3 / 2) - (1300 / 2)
                    show_command_plat = len(i[1:-2])
                    count_line = 80
                    window_del_command_show.geometry(
                        '%dx%d+%d+%d' % (1000, 1500, x3, y3))
                    tk.Label(window_del_command_show,
                             text="Trouver se client:",
                             font=('Arial', 20)).place(x=10,
                                                       y=10)
                    tk.Label(window_del_command_show,
                             text=("Nom: " + i[0]),
                             font=('Arial', 20)).place(x=10,
                                                       y=50)
                    tk.Label(window_del_command_show,
                             text=("Plat: " + i[1]),
                             font=('Arial', 20)).place(x=10,
                                                       y=80)

                    for k in range(show_command_plat):
                        count_line += 40
                        tk.Label(window_del_command_show,
                                 text=(str(k + 1) + ": " +
                                       i[k + 1].strip("[]'' ")),
                                 font=('Arial', 20)).place(x=10,
                                                           y=count_line)

                    tk.Label(window_del_command_show,
                             text=("Prix " + i[-2]),
                             font=('Arial', 20)).place(x=10,
                                                       y=count_line + 30)
                    tk.Label(window_del_command_show,
                             text=("Temp: " + time_command_transform),
                             font=('Arial', 20)).place(x=10,
                                                       y=count_line + 60)
                    tk.Label(window_del_command_show,
                             text="Vous etes sure que vous voudrais del ce client?",
                             font=('Arial', 20)).place(x=10,
                                                       y=count_line + 90)

                    def del_command_show_comfirm():
                        index_del_command = command_list.index(i)
                        del command_list[index_del_command]
                        update_command(command_list)
                        tkinter.messagebox.showinfo(title="Successful",
                                                    message="Del successfully")
                        window_del_command_show.destroy()
                        window_show_command_del_command.destroy()
                        window.destroy()
                        main()

                    def del_command_show_cancel():
                        window_del_command_show.destroy()

                    btn_del_command_show_confirm = tk.Button(window_del_command_show,
                                                             text="Confirm",
                                                             command=del_command_show_comfirm)
                    btn_del_command_show_confirm.place(x=250,
                                                       y=count_line + 120)
                    btn_del_command_show_cancel = tk.Button(window_del_command_show,
                                                            text="Cancel",
                                                            command=del_command_show_cancel)
                    btn_del_command_show_cancel.place(x=100,
                                                      y=count_line + 120)
                    window_del_command_show.mainloop()

        btn_del_quel_command_confirm = tk.Button(window,
                                                 text="Confirm",
                                                 command=del_command_confirm)
        btn_del_quel_command_confirm.place(x=120,
                                           y=150)
        btn_del_quel_command_cancel = tk.Button(window,
                                                text="Cancel",
                                                command=del_command_cancel)
        btn_del_quel_command_cancel.place(x=50,
                                          y=150)

    def add_commands():
        label_window_main_help.place_forget()
        tk.Label(window,
                 text="Saissez le nom SVP",
                 font=('Arial', 20)).place(x=10,
                                           y=50)
        var_add_command = tk.StringVar()
        entry_add_command = tk.Entry(window,
                                     textvariable=var_add_command,
                                     font=('Arial', 20))
        entry_add_command.place(x=10,
                                y=100)

        def add_commands_confirm():

            customer_local_time = time.time()
            command_list = read_command()
            customer_command_nom = []
            nom_costomer = entry_add_command.get()
            for i in command_list:
                if i[0] == nom_costomer:
                    tkinter.messagebox.showinfo(title="Error",
                                                message=("Il y a un autre customer qui s'appelle: " + nom_costomer))
                    raise Exception

            tk.Label(window,
                     text="Saissez le Numero du Plat SVP! Utilise (,) entre un et autre",
                     font=('Arial', 20)).place(x=10, y=150)
            var_customer_command = tk.StringVar()
            entry_customer_command = tk.Entry(window,
                                              textvariable=var_customer_command,
                                              font=('Arial', 20))
            entry_customer_command.place(x=10,
                                         y=200,
                                         width=400)

            window_show_menu_add_commands = tk.Tk()
            window_show_menu_add_commands.title('Menu')
            number = ttk.Treeview(window_show_menu_add_commands)
            count = 0
            menu_quantite = []
            menu = read_menu()
            for i in menu:  # Cette formule ici est pour pas realiser le quantite si == 0
                if i[2] != str(0):
                    menu_quantite.append(i)
            number['columns'] = ("Nom du Plat", "Type", "Quantite", "Prix")
            number.column("Nom du Plat", width=300)
            number.column("Type", width=100)
            number.column("Quantite", width=100)
            number.column("Prix", width=100)
            number.heading("Nom du Plat", text="Nom du Plat")
            number.heading("Type", text="Type")
            number.heading("Quantite", text="Quantite")
            number.heading("Prix", text="Prix")

            for i in menu_quantite:
                count += 1
                number.insert("", count, text=count, values=(
                    i[0], i[1], int(i[2]), int(i[3])))

            def show_sort_menu(tv, column, reverse):
                l = [(tv.set(k, column), k) for k in tv.get_children('')]
                # print(tv.get_children(''))
                l.sort(reverse=reverse)
                for index, (val, k) in enumerate(l):
                    tv.move(k, '', index)

                tv.heading(column, command=lambda: show_sort_menu(
                    tv, column, not reverse))

            for col in number['columns']:
                number.heading(
                    col, text=col, command=lambda _col=col: show_sort_menu(number, _col, False))

            number.pack()

            def customer_command_confirm():

                customer_command = []
                customer_command_prix = 0
                customer_command_number_list = str(
                    entry_customer_command.get()).split(",")
                for m in customer_command_number_list:
                    customer_command.append(menu_quantite[int(m) - 1])

                for k in range(len(customer_command)):
                    for me in menu:
                        if me[0] == customer_command[k][0]:
                            b = str(int(me[2]))
                            if int(b) <= 0:
                                tkinter.messagebox.showerror(title="Error", message=(
                                    "Il y n a pas encore ce plat: " + me[0]))
                                window.destroy()
                                main()
                            b = str(int(me[2])-1)
                            me[2] = b

                    customer_command_nom.append(customer_command[k][0])
                    customer_command_prix += int(customer_command[k][3])
                add_info = nom_costomer + "," + str(customer_command_nom).strip("[]") + "," + str(
                    customer_command_prix) + "," + str(
                    customer_local_time)

                add_info_list = add_info.split(",")
                command_list.append(add_info_list)
                update_command(command_list)
                update_menu(menu)
                tkinter.messagebox.showinfo(title="Success",
                                            message="Ajouter successfully")
                window_add_command_kichen = tk.Tk()
                window_add_command_kichen.title('Kichen')
                window_add_command_kichen.geometry('700x1000')
                tk.Label(window_add_command_kichen,
                         text=('COMMAND ' + str(len(command_list))),
                         font=('Arial', 50)).place(x=50,
                                                   y=50)
                count_line = 90
                count = 0
                for k in add_info_list[1:-2]:
                    count += 1
                    count_line += 40
                    tk.Label(window_add_command_kichen,
                             text=(str(count) + ": " + k.strip("[]'' ")),
                             font=('Arial', 20)).place(x=10,
                                                       y=count_line)
                window.destroy()
                window_show_menu_add_commands.destroy()
                main()

            def customer_command_cancel():
                window.destroy()
                main()

            btn_customer_commamd_confirm = tk.Button(window,
                                                     text="Confirm",
                                                     command=customer_command_confirm)
            btn_customer_commamd_confirm.place(x=60,
                                               y=250)
            btn_customer_commamd_cancel = tk.Button(window,
                                                    text="Cancel",
                                                    command=customer_command_cancel)
            btn_customer_commamd_cancel.place(x=10,
                                              y=250)

        btn_add_commands_confirm = tk.Button(window,
                                             text="Confirm",
                                             command=add_commands_confirm)
        btn_add_commands_confirm.place(x=330,
                                       y=100)

    def show_command():
        label_window_main_help.place_forget()
        nombre_customer = len(read_command())
        tk.Label(window,
                 text="Quelle personne est-ce que vous voudrais trouver?",
                 font=('Arial', 20)).place(x=10,
                                           y=50)
        var_personne_nom = tk.StringVar()
        entry_personne_nom = tk.Entry(window,
                                      textvariable=var_personne_nom,
                                      font=('Arial', 20))
        entry_personne_nom.place(x=10,
                                 y=100)

        window_show_command_show_command = tk.Tk()
        window_show_command_show_command.title('Command')
        number = ttk.Treeview(window_show_command_show_command)
        count = 0
        command = read_command()
        number['columns'] = ("Nom du Client", "Prix", "Date")
        number.column("Nom du Client", width=100)
        number.column("Prix", width=100)
        number.column("Date", width=300)
        number.heading("Nom du Client", text="Nom du Client")
        number.heading("Prix", text="Prix")
        number.heading("Date", text="Date")

        for i in command:
            count += 1
            time_command = time.localtime(float(i[-1]))
            time_command_transform = time.strftime(
                '%Y-%m-%d %H:%M:%S', time_command)
            number.insert("", count, text=count, values=(
                i[0], i[-2], time_command_transform))

        def numbreview_click(event):
            for item in number.selection():
                item_text = number.item(item, "values")
                # print(item_text)
                click_command = list(item_text)
                click_menu_nom = click_command[0]
                var_personne_nom.set(click_menu_nom)

        def show_sort_menu(tv, column, reverse):
            l = [(tv.set(k, column), k) for k in tv.get_children('')]
            # print(tv.get_children(''))
            l.sort(reverse=reverse)
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            tv.heading(column, command=lambda: show_sort_menu(
                tv, column, not reverse))

        for col in number['columns']:
            number.heading(
                col, text=col, command=lambda _col=col: show_sort_menu(number, _col, False))

        number.pack()
        number.bind('<ButtonRelease-1>', numbreview_click)

        def show_command_confirm():
            window_show_command_show_command.destroy()
            request = entry_personne_nom.get()
            command_list = read_command()
            count = 0
            for i in command_list:
                if i[0] == request:
                    time_command = time.localtime(float(i[-1]))
                    time_command_transform = time.strftime(
                        '%Y-%m-%d %H:%M:%S', time_command)
                    show_command_plat = len(i[1:-2])
                    count_line = 140

                    window_command_show = tk.Tk()
                    window_command_show.title("Show Command")
                    wds2 = window_command_show.winfo_screenwidth()
                    hds2 = window_command_show.winfo_screenheight()
                    x2 = (wds2 / 2) - (1000 / 2)
                    y2 = (hds2 / 2) - (500 / 2)
                    window_command_show.geometry(
                        '%dx%d+%d+%d' % (1000, 1500, x2, y2))
                    tk.Label(window_command_show,
                             text="Command trouvé",
                             font=('Arial', 20)).place(x=10,
                                                       y=10)
                    tk.Label(window_command_show,
                             text=("Nom du Costomer: " + i[0]),
                             font=('Arial', 20)).place(x=10,
                                                       y=50)
                    tk.Label(window_command_show,
                             text=("Prix: " + i[-2]),
                             font=('Arial', 20)).place(x=10,
                                                       y=80)
                    tk.Label(window_command_show,
                             text="Plat: ",
                             font=('Arial', 20)).place(x=10,
                                                       y=120)
                    for k in range(show_command_plat):
                        count_line += 40
                        tk.Label(window_command_show,
                                 text=(str(k + 1) + ": " +
                                       i[k + 1].strip("[]'' ")),
                                 font=('Arial', 20)).place(x=10,
                                                           y=count_line)
                    tk.Label(window_command_show,
                             text=("Temp de command ajouter: " +
                                   time_command_transform),
                             font=('Arial', 20)).place(x=10,
                                                       y=count_line + 40)

                    def window_command_show_exit():
                        window_command_show.destroy()
                        window.destroy()
                        main()

                    btn_window_command_show_exit = tk.Button(window_command_show,
                                                             text='Exit',
                                                             command=window_command_show_exit)
                    btn_window_command_show_exit.place(x=100,
                                                       y=count_line + 80)

                else:
                    count += 1
                    if count == len(command_list):
                        tkinter.messagebox.showerror(title="Error",
                                                     message="On ne trouve pas cette personne")

        def show_command_cancel():
            window.destroy()
            main()

        btn_show_command_confirm = tk.Button(window,
                                             text="Confirm",
                                             command=show_command_confirm)
        btn_show_command_confirm.place(x=100,
                                       y=150)
        btn_show_command_cancel = tk.Button(window,
                                            text="Cancel",
                                            command=show_command_cancel)
        btn_show_command_cancel.place(x=30,
                                      y=150)

    def history_commands():
        window_history_history_show = tk.Tk()
        window_history_history_show.title("Show Command")
        wds2 = window_history_history_show.winfo_screenwidth()
        hds2 = window_history_history_show.winfo_screenheight()
        x2 = (wds2 / 2) - (1000 / 2)
        y2 = (hds2 / 2) - (500 / 2)
        window_history_history_show.geometry(
            '%dx%d+%d+%d' % (600, 750, x2, y2))
        label_window_main_help.place_forget()
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
        tk.Label(window_history_history_show,
                 text=("Nombre total de commands passes: " +
                       str(len(command_list))),
                 font=('Arial', 20)).place(x=10,
                                           y=50)
        tk.Label(window_history_history_show,
                 text=("Commandes passees dans les 7 jours: " +
                       str(commands_dans_les_sept_jours)),
                 font=('Arial', 20)).place(x=10,
                                           y=90)
        tk.Label(window_history_history_show,
                 text=("Montant total des commandes: " + str(prix)),
                 font=('Arial', 20)).place(x=10,
                                           y=130)
        tk.Label(window_history_history_show,
                 text=("Montants total dans les 7 jours: " +
                       str(prix_dans_les_sept_jours)),
                 font=('Arial', 20)).place(x=10,
                                           y=170)
        tk.Label(window_history_history_show,
                 text="-----------------------------------------------\n"
                      "Voici des TOP 10 Plat: ",
                 font=('Arial', 20)).place(x=10,
                                           y=210)
        for i in command_list:
            plat_des_commands_passe.append(i[1:-2])
        t = 0
        for i in plat_des_commands_passe:
            for k in range(len(i)):
                plat_des_commands_passe_apres.append(
                    str(plat_des_commands_passe[t][k].strip("[]\'\"\\ ")))
            t += 1
        top_ten = Counter(plat_des_commands_passe_apres).most_common(10)
        count_line = 240
        count = 0
        for i in range(len(top_ten)):
            count += 1
            count_line += 40
            tk.Label(window_history_history_show,
                     text=(str(count) + ' : ' + top_ten[i][0]),
                     font=('Arial', 20)).place(x=10,
                                               y=count_line)

        def history_command_exit():
            window_history_history_show.destroy()
            window.destroy()
            main()

        btn_history_command_exit = tk.Button(window_history_history_show,
                                             text="Exit",
                                             command=history_command_exit)
        btn_history_command_exit.place(x=50,
                                       y=count_line + 40)

    def program_quit():
        label_window_main_help.place_forget()
        tkinter.messagebox.showinfo(title="Au Revoir",
                                    message="Merci pour votre conperention, Au revoir!")
        sys.exit(1)

    menu_bar = tk.Menu(window)
    filemenu_menu = tk.Menu(menu_bar,
                            tearoff=0)
    filemenu_command = tk.Menu(menu_bar,
                               tearoff=0)
    filemenu_exit = tk.Menu(menu_bar,
                            tearoff=0)

    menu_bar.add_cascade(label='MENU',
                         menu=filemenu_menu)
    menu_bar.add_cascade(label='COMMAND',
                         menu=filemenu_command)
    menu_bar.add_cascade(label='EXIT',
                         menu=filemenu_exit)
    filemenu_exit.add_command(label='EXIT',
                              command=program_quit)

    filemenu_menu.add_command(label='Add Menu',
                              command=add_menu)
    filemenu_menu.add_command(label='Del Menu',
                              command=del_menu)
    filemenu_menu.add_command(label='Change Menu',
                              command=changer_menu)
    filemenu_menu.add_command(label='Show Menu',
                              command=show_menu)
    filemenu_command.add_cascade(label='Add Command',
                                 command=add_commands)
    filemenu_command.add_command(label='Del command',
                                 command=del_command)
    filemenu_command.add_cascade(label='Show Command(One person)',
                                 command=show_command)
    filemenu_command.add_cascade(label='Command History(Total)',
                                 command=history_commands)
    filemenu_menu.add_separator()
    filemenu_command.add_separator()

    window.config(menu=menu_bar)

    def main_refresh():
        window.destroy()
        main()

    btn_main_refresh = tk.Button(window,
                                 text="RETURN MAIN",
                                 command=main_refresh)
    btn_main_refresh.place(x=0,
                           y=0)
    window.mainloop()


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


def update_command(command):
    with open('commands', 'w+', encoding='utf-8')as command_w:
        for i in command:
            i = ','.join(i) + '\n'
            command_w.write(i)


if __name__ == '__main__':
    login()
