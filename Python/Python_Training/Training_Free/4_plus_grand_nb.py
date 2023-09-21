# -*- coding: utf-8 -*-
#Created by Willipatafoul at 19:06 on 10/05/2023
#

"""Écrivez un programme en Python qui demande à l'utilisateur de saisir 
une liste de nombres entiers séparés par des espaces. Le programme doit trouver et afficher le plus grand nombre de cette liste."""

def main():
    nombres = input("Entrez une liste de nombres séparés par des espaces : ")
    liste_nb = nombres.split()
    
    nb_final = int(liste_nb[0])
    
    for nombre in liste_nb[1:]:
        nombre = int(nombre)
        if nombre > nb_final:
            nb_final = nombre;
        
    print("Le nombre le plus grand dans cette liste est : ", nb_final)
    
if __name__ == '__main__':
    main()
    
""" CORRECTION CHATGPT
def main():
    nombres = input("Entrez une liste de nombres entiers séparés par des espaces : ")
    liste_nb = nombres.split()
    
    # Assumons que le premier nombre est le plus grand
    plus_grand = int(liste_nb[0])
    
    # Parcourir les nombres restants de la liste
    for nombre in liste_nb[1:]:
        nombre = int(nombre)
        if nombre > plus_grand:
            plus_grand = nombre
    
    print("Le plus grand nombre de la liste est :", plus_grand)
    
if __name__ == '__main__':
    main()

"""