# -*- coding: utf-8 -*-
#Created by Willipatafoul at 16:52 on 21/06/2023
#
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

def afficher_mdp(mots_de_passe):
    mots_de_passe = charger_mots_de_passe()
    
    if mots_de_passe:
        time.sleep(1)
        print("\nListe des mots de passe :\n")
        time.sleep(1)
        
        for i, mot_de_passe in enumerate(mots_de_passe, start=1):
            print(f"{i}. Service : {mot_de_passe['Service']}")
            print(f"   Mot de passe : {mot_de_passe['Mot_de_passe']}")
            print() 
        time.sleep(1)
    else:
        time.sleep(2)
        print("Désolé, il n'y a aucun mots de passe..")
        time.sleep(2)