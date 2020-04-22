# coding:utf-8
# @Time    : 4/22/2020 7:12 PM
# @Author  : Wilson JIANG Yilun
# @FileName: main.py
# @Software: PyCharm


def print_restaurant_info():
    print("-" * 80,
          "\n",
          "-" * 30,
          "RESTAURANT LIPSUM",
          "-" * 30,
          "\n",
          "-" * 30,
          " 15 RUE DES ECOLE",
          "-" * 30,
          "\n",
          "-" * 79)


print_restaurant_info()
nom_client = input("Saissez voyre nom SVP")

print_restaurant_info()
print("Bonjour", nom_client, "! ", "\n")
print("1. GESTION DE COMMANDE\n2. ")


m = open("menu", 'r')
menu_list = m.read().splitlines()



exit()