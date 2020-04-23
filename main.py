# coding:utf-8
# @Time    : 4/22/2020 7:12 PM
# @Author  : Wilson JIANG Yilun
# @FileName: main.py
# @Software: PyCharm


def print_restaurant_info():
    print("-" * 80,"\n",
          "-" * 30, "RESTAURANT LIPSUM", "-" * 30, "\n",
          "-" * 30, " 15 RUE DES ECOLE", "-" * 30, "\n",
          "-" * 79
          )


def text_save(content, filename, mode='w+'):
    file = open(filename,mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()


def text_read(file_name):
    try:
        file = open(file_name, 'r')
    except IOError:
        error = []
        return error
    data = []
    content = file.read().splitlines()
    for i in range(len(content)):
        data[i] = content[i]

    file.close()
    return data


print_restaurant_info()
nom_client = input("Saissez voyre nom SVP: \n")

print_restaurant_info()
print("Bonjour", nom_client, "! ", "\n")
print("1. GESTION DE COMMANDE\n2. ")




exit()