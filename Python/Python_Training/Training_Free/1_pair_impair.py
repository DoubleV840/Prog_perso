#
#Created by Willipatafoul at 15:40 on 10/05/2023
#

"""Écrivez un programme qui demande à l'utilisateur de saisir un nombre entier et affiche si ce nombre est pair ou impair."""

nombre = int(input("Entrez un nombre : "))

if nombre % 2 == 0:
    print("Votre nombre est pair")
else:
    print("Votre nombre est impair")

"""CORRECTION CHATGPT

# Vérification de la parité d'un nombre

nombre = int(input("Entrez un nombre entier : "))

if nombre % 2 == 0:
    print(nombre, "est un nombre pair.")
else:
    print(nombre, "est un nombre impair.")

"""