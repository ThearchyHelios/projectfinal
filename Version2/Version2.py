import sys
import time
from typing import List
from collections import Counter
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


def login():
    window_login = tk.Tk()
    window_login.title("Welcome!")
    window_login.geometry('350x150')
    window_login.wm_attributes('-topmost', 1)
    tk.Label(window_login, text='User name: ', font=('Arial', 14)).place(x=10, y=10)
    tk.Label(window_login, text='Password: ', font=('Arial', 14)).place(x=10, y=40)
    var_usrname = tk.StringVar()
    var_usrname.set('admin')
    entry_usrname = tk.Entry(window_login, textvariable=var_usrname, font=('Arial', 14))
    entry_usrname.place(x=100, y=10)
    var_usrpassword = tk.StringVar()
    var_usrpassword.set('123456')
    entry_usrpassword = tk.Entry(window_login, textvariable=var_usrpassword, font=('Arial', 14), show='*')
    entry_usrpassword.place(x=100, y=40)

    def login_btn():
        usr_name = entry_usrname.get()
        usr_password = entry_usrpassword.get()
        if usr_name == 'admin':
            if usr_password == '123456':
                tkinter.messagebox.showinfo(title='Welcome', message='Welcome ' + usr_name)
                window_login.destroy()
                main()
            else:
                tkinter.messagebox.showerror(message="Error, le code n'est pas correct, saissez le un autre fois SVP!")
                var_usrname.set('admin')
                var_usrpassword.set('123456')
        else:
            tkinter.messagebox.showerror(message="On ne trouvez pas ce Utilisateur!")
            var_usrname.set('admin')
            var_usrpassword.set('123456')

    def cancel_button():
        exit()

    btn_login = tk.Button(window_login, text='Login', command=login_btn)
    btn_login.place(x=180, y=90)
    btn_cancel = tk.Button(window_login, text='Cancel', command=cancel_button)
    btn_cancel.place(x=100, y=90)
    window_login.mainloop()


def main():
    window = tk.Tk()
    window.title("ProjetFinal")
    wds = window.winfo_screenwidth()
    hds = window.winfo_screenheight()
    x = (wds / 2) - (2000 / 2)
    y = (hds / 2) - (1000 / 2)
    window.geometry('%dx%d+%d+%d' % (2000, 1000, x, y))

    def add_menu():
        tk.Label(window, text="Saissez des info comme TIAN DE LÉGUMES DU SOLEIL(Nom),Dessert(Type),12(Quantite),"
                              "5(Prix) SVP", font=('Arial', 20)).place(x=10, y=170)
        tk.Label(window, text="il y a Type comme Main, Plat, Boisson, Dessert", font=('Arial', 20)).place(x=10, y=210)
        var_add_menu = tk.StringVar()
        var_add_menu.set("TIAN DE LÉGUMES DU SOLEIL,Dessert,12,5")
        entry_add_menu = tk.Entry(window, textvariable=var_add_menu, font=('Arial', 14))
        entry_add_menu.place(x=10, y=240, width=800)

        def add_menu_confirm():
            add_menu_plat = entry_add_menu.get()
            user_add_menu = str(add_menu_plat).strip()
            user_add_menu_list = user_add_menu.split(',')
            btn_add_menu_confirm.place(x=50, y=240)
            menu = read_menu()
            if len(user_add_menu_list) == 4:
                nom_menu = []
                for i in menu:
                    nom_menu.append(i[0])
                if user_add_menu_list[0] in nom_menu:
                    tkinter.messagebox.showinfo(title='Error', message="Le Plat a deja ajouter!")
                else:
                    menu.append(user_add_menu_list)
                    update_menu(menu)
                    tkinter.messagebox.showinfo(title='Successful', message="Ajouter Successfully")
                    window.destroy()
                    time.sleep(1)
                    main()
            else:
                tkinter.messagebox.showerror(title='Error', message='Unknown Error')

        btn_add_menu_confirm = tk.Button(window, text='Confirm', command=add_menu_confirm)
        btn_add_menu_confirm.place(x=50, y=270)

    def del_menu():
        tk.Label(window, text="Saissez le nom du plat SVP", font=('Arial', 20)).place(x=10, y=300)
        number = ttk.Treeview(window)
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
            number.insert("", count, text=count, values=(i[0], i[1], i[2], i[3]))
        number.pack()
        var_del_quel_menu = tk.StringVar()
        var_del_quel_menu.set("TIAN DE LÉGUMES DU SOLEIL")
        entry_del_quel_menu = tk.Entry(window, textvariable=var_del_quel_menu, font=('Arial', 14))
        entry_del_quel_menu.place(x=10, y=330, width=400)

        def del_menu_confirm():
            menu_list = read_menu()
            del_quel_menu = str(entry_del_quel_menu.get()).strip()
            for i in menu_list:
                if i[0] == del_quel_menu:
                    window_del_menu_show = tk.Tk()
                    window_del_menu_show.title("Del Menu")
                    wds2 = window_del_menu_show.winfo_screenwidth()
                    hds2 = window_del_menu_show.winfo_screenheight()
                    x2 = (wds2 / 2) - (1000 / 2)
                    y2 = (hds2 / 2) - (500 / 2)
                    window_del_menu_show.geometry('%dx%d+%d+%d' % (500, 500, x2, y2))
                    tk.Label(window_del_menu_show, text="Trouver se plat:", font=('Arial', 20)).place(x=10, y=10)
                    tk.Label(window_del_menu_show, text=("Nom: " + i[0]), font=('Arial', 20)).place(x=10, y=50)
                    tk.Label(window_del_menu_show, text=("Type: " + i[1]), font=('Arial', 20)).place(x=10, y=80)
                    tk.Label(window_del_menu_show, text=("Quantite: " + i[2]), font=('Arial', 20)).place(x=10, y=110)
                    tk.Label(window_del_menu_show, text=("Prix: " + i[3]), font=('Arial', 20)).place(x=10, y=140)
                    tk.Label(window_del_menu_show, text="Vous etes sure que vous voudrais del ce plat?",
                             font=('Arial', 20)).place(x=10, y=190)

                    def del_menu_show_oui():
                        index_del_menu = menu_list.index(i)
                        del menu_list[index_del_menu]
                        update_menu(menu_list)
                        tkinter.messagebox.showinfo(title='Successful', message="Del Successfully")
                        window_del_menu_show.destroy()
                        window.destroy()
                        main()

                    def del_menu_show_non():
                        tkinter.messagebox.showinfo(title="Cancel", message="Cancel")
                        window_del_menu_show.destroy()

                    btn_del_menu_show_non = tk.Button(window_del_menu_show, text="NON", command=del_menu_show_non)
                    btn_del_menu_show_non.place(x=250, y=220)
                    btn_del_menu_show_oui = tk.Button(window_del_menu_show, text="OUI", command=del_menu_show_oui)
                    btn_del_menu_show_oui.place(x=300, y=220)
                    window_del_menu_show.mainloop()

        btn_del_menu_confirm = tk.Button(window, text="Confirm", command=del_menu_confirm)
        btn_del_menu_confirm.place(x=300, y=350)

    def changer_menu():
        menu_list = read_menu()
        number = ttk.Treeview(window)
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
            number.insert("", count, text=count, values=(i[0], i[1], i[2], i[3]))
        number.pack()
        tk.Label(window, text="Quel plat est-ce que vous voudrais changer?", font=('Arial', 20)).place(x=100, y=400)
        var_changer_menu_plat = tk.StringVar()
        var_changer_menu_plat.set("TIAN DE LÉGUMES DU SOLEIL")
        entry_changer_menu_plat = tk.Entry(window, textvariable=var_changer_menu_plat, font=('Arial', 14))
        entry_changer_menu_plat.place(x=100, y=430, width=800)

        def change_menu_confirm():
            plat_changer = str(entry_changer_menu_plat.get()).strip()
            count2 = 0
            for i in menu_list:
                if plat_changer != i[0]:
                    count2 += 1
                    if count2 == len(menu_list):
                        tk.messagebox.showerror(title="Error", message="Il n y a pas ce plat!")

            for i in menu_list:
                plat_changer = str(entry_changer_menu_plat.get()).strip()
                if i[0] == plat_changer:
                    window_change_menu_show = tk.Tk()
                    window_change_menu_show.title("Change Menu")
                    wds2 = window_change_menu_show.winfo_screenwidth()
                    hds2 = window_change_menu_show.winfo_screenheight()
                    x2 = (wds2 / 2) - (1000 / 2)
                    y2 = (hds2 / 2) - (500 / 2)
                    window_change_menu_show.geometry('%dx%d+%d+%d' % (500, 500, x2, y2))
                    tk.Label(window_change_menu_show, text="Trouver se plat:", font=('Arial', 20)).place(x=10, y=10)
                    tk.Label(window_change_menu_show, text=("Nom: " + i[0]), font=('Arial', 20)).place(x=10, y=50)
                    tk.Label(window_change_menu_show, text=("Type: " + i[1]), font=('Arial', 20)).place(x=10, y=80)
                    tk.Label(window_change_menu_show, text=("Quantite: " + i[2]), font=('Arial', 20)).place(x=10, y=110)
                    tk.Label(window_change_menu_show, text=("Prix: " + i[3]), font=('Arial', 20)).place(x=10, y=140)
                    tk.Label(window_change_menu_show, text="Est-ce que vous voudrais changer?",
                             font=('Arial', 20)).place(x=10, y=190)
                    var_change_menu_show = tk.StringVar()
                    entry_changer_menu_show = tk.Entry(window_change_menu_show,
                                                       textvariable=var_change_menu_show, font=('Arial', 14))
                    entry_changer_menu_show.place(x=10, y=220)

                    def change_menu_show_nom():
                        for i in menu_list:
                            if i[0] == plat_changer:
                                nom_changer_apres = entry_changer_menu_show.get()
                                i[0] = nom_changer_apres
                                update_menu(menu_list)
                                tkinter.messagebox.showinfo(title="Successful", message='Change Successfully')
                                window_change_menu_show.destroy()
                                window.destroy()
                                main()

                    def change_menu_show_type():
                        for i in menu_list:
                            if i[0] == plat_changer:
                                i[1] = entry_changer_menu_show.get()
                                update_menu(menu_list)
                                tkinter.messagebox.showinfo(title="Successful", message='Change Successfully')
                                window_change_menu_show.destroy()
                                window.destroy()
                                main()

                    def change_menu_show_quantite():
                        for i in menu_list:
                            if i[0] == plat_changer:
                                i[2] = entry_changer_menu_show.get()
                                update_menu(menu_list)
                                tkinter.messagebox.showinfo(title="Successful", message='Change Successfully')
                                window_change_menu_show.destroy()
                                window.destroy()
                                main()

                    def change_menu_show_prix():
                        for i in menu_list:
                            if i[0] == plat_changer:
                                i[3] = entry_changer_menu_show.get()
                                update_menu(menu_list)
                                tkinter.messagebox.showinfo(title="Successful", message='Change Successfully')
                                window_change_menu_show.destroy()
                                window.destroy()
                                main()

                    btn_change_menu_show_nom = tk.Button(window_change_menu_show, text="Nom",
                                                         command=change_menu_show_nom)
                    btn_change_menu_show_nom.place(x=10, y=250)
                    btn_change_menu_show_type = tk.Button(window_change_menu_show, text="Type",
                                                          command=change_menu_show_type)
                    btn_change_menu_show_type.place(x=80, y=250)
                    btn_change_menu_show_quantite = tk.Button(window_change_menu_show, text="Quantite",
                                                              command=change_menu_show_quantite)
                    btn_change_menu_show_quantite.place(x=150, y=250)
                    btn_change_menu_show_prix = tk.Button(window_change_menu_show, text="Prix",
                                                          command=change_menu_show_prix)
                    btn_change_menu_show_prix.place(x=250, y=250)
                    window_change_menu_show.mainloop()

        btn_change_menu_confirm = tk.Button(window, text="Confirm", command=change_menu_confirm)
        btn_change_menu_confirm.place(x=200, y=470)

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

    def del_command():
        number = ttk.Treeview(window)
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
            time_command_transform = time.strftime('%Y-%m-%d %H:%M:%S', time_command)
            number.insert("", count, text=count, values=(i[0], i[-2], time_command_transform))
        number.pack()
        tk.Label(window, text="Saissez le nom du client SVP", font=('Arial', 20)).place(x=10, y=300)
        command_list = read_command()
        ver_del_quel_command = tk.StringVar()
        entry_del_quel_command = tk.Entry(window, textvariable=ver_del_quel_command, font=('Arial', 20))
        entry_del_quel_command.place(x=10, y=350)

        def del_command_cancel():
            window.destroy()
            main()

        def del_command_confirm():
            del_quel_command = str(entry_del_quel_command.get()).strip()
            for i in command_list:
                if i[0] == del_quel_command:
                    time_command = time.localtime(float(i[-1]))
                    time_command_transform = time.strftime('%Y-%m-%d %H:%M:%S', time_command)
                    window_del_command_show = tk.Tk()
                    window_del_command_show.title("Change Menu")
                    wds3 = window_del_command_show.winfo_screenwidth()
                    hds3 = window_del_command_show.winfo_screenheight()
                    x3 = (wds3 / 2) - (1000 / 2)
                    y3 = (hds3 / 2) - (500 / 2)
                    window_del_command_show.geometry('%dx%d+%d+%d' % (1000, 500, x3, y3))
                    tk.Label(window_del_command_show, text="Trouver se client:", font=('Arial', 20)).place(x=10, y=10)
                    tk.Label(window_del_command_show, text=("Nom: " + i[0]), font=('Arial', 20)).place(x=10, y=50)
                    tk.Label(window_del_command_show, text=("Plat: " + i[1]), font=('Arial', 20)).place(x=10, y=80)
                    tk.Label(window_del_command_show, text=("Prix " + i[-2]), font=('Arial', 20)).place(x=10, y=110)
                    tk.Label(window_del_command_show, text=("Temp: " + time_command_transform), font=('Arial', 20)).place(x=10, y=140)
                    tk.Label(window_del_command_show, text="Vous etes sure que vous voudrais del ce client? (oui/non)",
                             font=('Arial', 20)).place(x=10, y=190)

                    def del_command_show_comfirm():
                        index_del_command = command_list.index(i)
                        del command_list[index_del_command]
                        update_command(command_list)
                        tkinter.messagebox.showinfo(title="Successful", message="Del successfully")
                        window_del_command_show.destroy()
                        window.destroy()
                        main()

                    def del_command_show_cancel():
                        window_del_command_show.destroy()
                        window.destroy()
                        main()

                    btn_del_command_show_confirm = tk.Button(window_del_command_show, text="Confirm",
                                                             command=del_command_show_comfirm)
                    btn_del_command_show_confirm.place(x=100, y=170)
                    btn_del_command_show_cancel = tk.Button(window_del_command_show, text="Cancel",
                                                            command=del_command_show_cancel)
                    btn_del_command_show_cancel.place(x=150, y=170)
                    window_del_command_show.mainloop()

        btn_del_quel_command_confirm = tk.Button(window, text="Confirm", command=del_command_confirm)
        btn_del_quel_command_confirm.place(x=120, y=380)
        btn_del_quel_command_cancel = tk.Button(window, text="Cancel", command=del_command_cancel)
        btn_del_quel_command_cancel.place(x=50, y=380)

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

    menu_bar = tk.Menu(window)
    filemenu = tk.Menu(menu_bar, tearoff=0)
    submenu_menu = tk.Menu(filemenu)
    submenu_command = tk.Menu(filemenu)
    menu_bar.add_cascade(label='File', menu=filemenu)
    filemenu.add_cascade(label='Menu', menu=submenu_menu, underline=0)
    submenu_menu.add_command(label='Add Menu', command=add_menu)
    submenu_menu.add_command(label='Del Menu', command=del_menu)
    submenu_menu.add_command(label='Change Menu', command=changer_menu)
    submenu_menu.add_command(label='Show Menu', command=show_menu)
    filemenu.add_cascade(label='Command', menu=submenu_command, underline=0)
    submenu_command.add_cascade(label='Add Command', command=add_commands)
    submenu_command.add_command(label='Del command', command=del_command)
    submenu_command.add_cascade(label='Show Command(One person)', command=show_command)
    submenu_command.add_cascade(label='Command History(Total)', command=history_commands)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=window.quit)
    window.config(menu=menu_bar)

    def main_refresh():
        window.destroy()
        main()

    btn_main_refresh = tk.Button(window, text="REFFRESH", command=main_refresh)
    btn_main_refresh.place(x=0, y=0)
    window.mainloop()


def show_menu():
    window_show_menu = tk.Tk()
    window_show_menu.title('Menu')
    number = ttk.Treeview(window_show_menu)
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
        number.insert("", count, text=count, values=(i[0], i[1], i[2], i[3]))

    number.pack()
    window_show_menu.mainloop()


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


login()
