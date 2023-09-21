# -*- coding: utf-8 -*-
#Created by Willipatafoul at 16:21 on 20/05/2023
#

#Écrivez un programme qui demande à l'utilisateur de saisir un nombre entier positif 
 #et affiche la somme de tous les nombres pairs de 1 jusqu'à ce nombre.

def main():
    nombre = int(input("Entrez un nombre : "))
    total = 0
    
    if nombre % 2 == 0:
        for i in range(nombre-2, 0, -2):
            total += i
    else:
        nombre -= 1
        for i in range(nombre-2, 0, -2):
            total += i
    print(total)


if __name__ == '__main__':
    main()
    
""" CORRECTION CHATGPT
def main():
    nombre = int(input("Entrez un nombre entier positif : "))
    somme = 0

    for i in range(2, nombre + 1, 2):
        somme += i

    print("La somme des nombres pairs de 1 à", nombre, "est :", somme)

if __name__ == '__main__':
    main()

"""