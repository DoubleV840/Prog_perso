# -*- coding: utf-8 -*-
#Created by Willipatafoul at 15:56 on 21/06/2023
#
import time

def menu_principal():
    print("\n_-_-_-_- GESTIONNAIRE DE MDP -_-_-_-_\n")
    time.sleep(0.2)
    print("1. Ajout d'un mot de passe")
    time.sleep(0.2)
    print("2. Supprimer un mot de passe")
    time.sleep(0.2)
    print("3. Afficher la liste des mots de passe")
    time.sleep(0.2)
    print("4. Rechercher un mot de passe")
    time.sleep(0.2)
    print("5. Quitter le gestionnaire\n")
    time.sleep(0.2)
    choix_menu = input("Votre choix : ")
    return choix_menu
   