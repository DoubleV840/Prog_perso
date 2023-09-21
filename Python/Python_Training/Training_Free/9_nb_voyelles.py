# -*- coding: utf-8 -*-
#Created by Willipatafoul at 12:03 on 05/06/2023
#

#Ecrire un programme qui renvoie le nombres de voyelles dans la chaine

def nb_voyelles(chaine):
    voyelles = ["a","e","i","o","u","y"]
    compteur = 0
    
    for i in chaine:
        if i.lower() in voyelles:
            compteur += 1
    print(f"Votre chaine '{chaine}' contient {compteur} voyelles")

def main():
    chaine = input("Entrez une chaine de caractères : ")
    nb_voyelles(chaine)

if __name__ == '__main__':
    main()
    
""" CORRECTION CHATGPT
def compter_voyelles(chaine):
    voyelles = ['a', 'e', 'i', 'o', 'u']
    compteur = 0

    for caractere in chaine:
        if caractere.lower() in voyelles:
            compteur += 1

    return compteur

# Demande à l'utilisateur de saisir une chaîne de caractères
chaine = input("Entrez une chaîne de caractères : ")

# Appelle la fonction compter_voyelles pour obtenir le nombre de voyelles
nb_voyelles = compter_voyelles(chaine)

# Affiche le résultat
print(f"Le nombre de voyelles dans '{chaine}' est {nb_voyelles}")

"""