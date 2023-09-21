# -*- coding: utf-8 -*-
#Created by Willipatafoul at 18:56 on 10/05/2023
#

#Écrivez un programme en Python qui demande à l'utilisateur de saisir une phrase et compte le nombre de mots dans cette phrase.

def main():
    phrase = input("Entrez une phrase : ")
    liste_mots = phrase.split()
    print(f"Votre phrase contient {len(liste_mots)} mots.")

if __name__ == '__main__':
    main()
    
""" CORRECTION CHATGPT
def main():
    phrase = input("Entrez une phrase : ")
    mots = phrase.split()
    nombre_mots = len(mots)
    print("Le nombre de mots dans la phrase est :", nombre_mots)

if __name__ == '__main__':
    main()

"""