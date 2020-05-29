# Projet Final

###### GitHub Link: https://github.com/Marshellson/projectfinal

 Ce Readme a été écrit le 19 Mai 2020

---
###### Je(JIANG Yilun) ai terminé ce projet sépatément, donc s'il y a des erreurs grammaticales françaises dans le code ou ce fichier, veuillez me pardonner.



## 1. L'introduction

### 1️⃣ Le but de l'écriture de ce code:

Ceci est mon projet final en python au deuxième semestre de la première année d'EPF

### 2️⃣ Arrière-plan de conception

Il s'agit d'un programme qui sert les serveurs de restaurant et peut mieux gérer les restaurants en ajoutant des commandes ou en gérant les commandes des restaurants.

### 3️⃣ Définition du vocabulaire 

`Nom1_Nom2_Nom3` --> Fonction Nom1 --> Fonction Nom2 --> Fonction Nom3 ex.

 Exemple: `window_del_command_show` == Fonction window --> Fonction del_command --> Fonction tk.TK (Créer une Window)

### 4️⃣ Référence

PDF ([![img](https://moodle.epf.fr/theme/image.php/lambda/core/1590625801/f/pdf-24)](https://moodle.epf.fr/mod/resource/view.php?id=60598) [Projet - TROYES - Sujet](https://moodle.epf.fr/mod/resource/view.php?id=60598))

---

## Résultat de développement réels

### ⚀ Produit

 [Version2.py](Version2.py) 



##### Je vous suggère que d'utiliser l'application `Typora` ou `Haroopad` pour ouvrir ce ficher.

---



```mermaid

graph LR
opLogin[Fonction login]-->condLogin{Si Username == 'Admin' et Password == '123456'}
condLogin-->|Correct|condMain{Fonction main}
condLogin-->|Incorrect|Exit(END)
condMain-->|Menu|condMenu{Menu}
condMain-->|Command|condCommand{Command}

opUpdateMenu[Update Menu]
opUpdateCommand[UpdateCommand]

condMenu-->|Add Menu|opAddMenu[Add Menu]
condMenu-->|Del Menu|opDelMenu[Del Menu]
condMenu-->|Change Menu|opChangeMenu[Change Menu]
condMenu-->|Show Menu|opShowMenu[Show Menu]

condCommand-->|Add Command|opAddCommand[Add Command]
condCommand-->|Del Command|opDelCommand[Del Command]
condCommand-->|Show Command|opShowCommand[Show Command]
condCommand-->|History Command|opHistoryCommand[History Command]

opAddMenu-->condEntryAddMenu{Nom, Type, Quantite, Prix}
condEntryAddMenu-->|Already have this Plat|opShowErrorAddMenu[Error]
opShowErrorAddMenu -->condEntryAddMenu
condEntryAddMenu-->|Don't have this Plat|opUpdateMenu

opDelMenu-->condEntryDelMenu{Find the Plat}
condEntryDelMenu-->|Don't have this Plat|opShowErrorDelMenu[Error]
opShowErrorDelMenu-->condEntryDelMenu
condEntryDelMenu-->|Have this Plat|opUpdateMenu

opChangeMenu-->condEntryChangeMenu{Find the Plat}
condEntryChangeMenu-->|Don't have this Plat|opShowErrorChangeMenu[Error]
opShowErrorChangeMenu-->condEntryChangeMenu
condEntryChangeMenu-->|Have this Plat|condEntry2ChangeMenu{Change Nom, Type, Quantite, Prix}
condEntry2ChangeMenu-->|Nom|opChangeNomChangeMenu[Change Nom]
opChangeNomChangeMenu-->opUpdateMenu
condEntry2ChangeMenu-->|Type|opChangeTypeChangeMenu[Change Tpye]
opChangeTypeChangeMenu-->opUpdateMenu
condEntry2ChangeMenu-->|Quantite|opChangeQuaniteChangeMenu[Change Quantite]
opChangeQuaniteChangeMenu-->opUpdateMenu
condEntry2ChangeMenu-->|Prix|opChangePrixChangeMenu[Change Prix]
opChangePrixChangeMenu-->opUpdateMenu

opAddCommand-->condEntryAddCommand{Name of the Customer}
condEntryAddCommand-->|Already have this Customer|opShowErrorAddCommand[Error]
opShowErrorAddCommand-->opAddCommand
condEntryAddCommand-->|Don't have this Customer|opUpdateCommand

opDelCommand-->condEntryDelCommand{Name of the Customer}
condEntryDelCommand-->|Don't have this Customer|opShowErrorDelCommand[Error]
opShowErrorDelCommand-->opDelCommand
condEntryDelCommand-->|Have this Customer|opUpdateCommand

opShowCommand-->condEntryShowCommand{Name of the Customer}
condEntryShowCommand-->|Dont have this Customer|opShowErrorShowCommand[Error]
opShowErrorShowCommand-->opShowCommand
condEntryShowCommand-->|Have this Command|opShowCommandShowCommand[Show Command]

opHistoryCommand-->opShowCommandHistoryCommand[History Command]



```

---



![avater](https://raw.githubusercontent.com/Marshellson/projectfinal/master/Version2/image Mind.png?token=ALLCJBVERU57WY6LZYVEWTC62DRLW)





