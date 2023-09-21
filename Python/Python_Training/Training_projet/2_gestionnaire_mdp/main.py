# -*- coding: utf-8 -*-
#Created by Willipatafoul at 15:54 on 21/06/2023
#
from menu import menu_principal
from ajout_mdp import ajout_mdp
from supp_mdp import supprimer_mdp
from afficher_mdp import afficher_mdp
from recherche_mdp import recherche_mdp
import time
import os

def charger_mots_de_passe():
    mots_de_passe = []
    if os.path.exists("mots_de_passe.txt"):
        with open("mots_de_passe.txt", "r") as fichier:
            for ligne in fichier:
                service, mot_de_passe = ligne.strip().split(",")
                mots_de_passe.append({"Service": service, "Mot_de_passe": mot_de_passe})
    return mots_de_passe

def main():

    mots_de_passe = []
    
    while True:
        choix = menu_principal()
        
        if choix == "1":
            ajout_mdp(mots_de_passe)
        elif choix == "2":
            supprimer_mdp(mots_de_passe)
        elif choix == "3":
            afficher_mdp(mots_de_passe)
        elif choix == "4":
            recherche_mdp(mots_de_passe)
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Erreur veuillez entrer une valeur correcte !")
            time.sleep(1)
            
    mots_de_passe = charger_mots_de_passe()

if __name__ == '__main__':
    main()