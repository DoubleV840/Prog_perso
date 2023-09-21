# -*- coding: utf-8 -*-
#Created by Willipatafoul at 16:58 on 21/06/2023
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

def recherche_mdp(mots_de_passe):
    mots_de_passe = charger_mots_de_passe()
    
    time.sleep(0.5)
    service_rech = input("Mdp de quel service voulez-vous ? ")
    mot_de_passe_trouve = False

    for mot_de_passe in mots_de_passe:
        if mot_de_passe["Service"] == service_rech:
            time.sleep(1)
            print("Voici le mot de passe :")
            time.sleep(1)
            print(f"Service : {mot_de_passe['Service']}")
            print(f"Mot de passe : {mot_de_passe['Mot_de_passe']}")
            mot_de_passe_trouve = True
            time.sleep(1)
            break
    if not mot_de_passe_trouve:
        time.sleep(1)
        print("Aucun service correspondant n'a été trouvé..")
        time.sleep(1)
        