# -*- coding: utf-8 -*-
#Created by Willipatafoul at 16:07 on 21/06/2023
#
import time
import random
import string

def sauvegarder_mots_de_passe(mots_de_passe):
    with open("mots_de_passe.txt", "a") as fichier:
        for mot_de_passe in mots_de_passe:
            ligne = f"{mot_de_passe['Service']},{mot_de_passe['Mot_de_passe']}\n"
            fichier.write(ligne)

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

def ajout_mdp(mots_de_passe):
    service = input("Quel service (site internet, ordi...) : ")
    mdp_rdm = input("Voulez-vous un mot de passe sécurisé inventé par l'ordi ? (y/n) ").lower()
    mot_de_passe = ""
    
    if mdp_rdm == "y":
        longueur_mdp = 0
        try:
            longueur_mdp = int(input("Combien de caractères voulez-vous dans votre mot de passe ? "))
            if longueur_mdp <= 0:
                    print("La longueur du mot de passe doit être supérieure à zéro.")
                    longueur_mdp = 0
        except ValueError:
                print("Veuillez entrer un nombre entier valide.")
        mot_de_passe = generer_mot_de_passe(longueur_mdp)
        print("Mot de passe généré : ", mot_de_passe)
    else:
        mot_de_passe = input("Votre mot de passe : ")
    
    new_mot_de_passe = {"Service" : service,
                        "Mot_de_passe" : mot_de_passe}
    mots_de_passe.append(new_mot_de_passe)
    sauvegarder_mots_de_passe(mots_de_passe)
    
    time.sleep(0.5)
    print(".")  
    time.sleep(0.5)  
    print(".")  
    time.sleep(0.5)  
    print(".")
    time.sleep(1)  
    print("Votre mot de passe à été ajouté avec succès !")
    time.sleep(1)
