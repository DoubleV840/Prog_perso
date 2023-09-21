# -*- coding: utf-8 -*-
#Created by Willipatafoul at 16:13 on 05/06/2023
#

#Ecrire un programme qui renvoie le nombre de mots qu'il y a dans la chaine

def nb_mots(chaine):
    mots = chaine.split()
    
    print(f"Votre phrase contient {len(mots)} mot(s).")

def main():
    chaine = input("Entrez une phrase : ")
    nb_mots(chaine)

if __name__ == '__main__':
    main()
    
""" CORRECTION CHATGPT
def compter_mots(phrase):
    mots = phrase.split()
    nombre_mots = len(mots)
    return nombre_mots

def main():
    phrase = input("Entrez une phrase : ")
    nombre_mots = compter_mots(phrase)
    print("Le nombre de mots dans la phrase est :", nombre_mots)

if __name__ == '__main__':
    main()

"""