# -*- coding: utf-8 -*-
#Created by Willipatafoul at 16:57 on 10/05/2023
#

#Écrivez un programme qui demande à l'utilisateur de saisir un mot et qui affiche ce mot à l'envers.

def main():
    mot = input("Entrez un mot à inverser : ")
    longueur = len(mot)
    for x in range(longueur - 1, -1, -1):
        print(mot[x], end="")
    print("")
if __name__ == '__main__':
    main()
    
""" CORRECTION CHATGPT
def main():
    mot = input("Entrez un mot : ")
    mot_inverse = mot[::-1] #mot[::-1] est un découpage de la chaine 'mot' que l'on vient réecrire dans une nouvelle chaine 'mot_inverse'
    print("Le mot inversé est :", mot_inverse)

if __name__ == '__main__':
    main()
"""