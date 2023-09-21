# -*- coding: utf-8 -*-
#Created by Willipatafoul at 16:55 on 20/05/2023
#

#Creer un programme pour verifier si le mot entré est un palindrome ou non

def main():
    mot = input("Entrez un mot : ")
    
    milieu = len(mot) // 2
    partie1 = mot[:milieu]
    if len(mot) % 2 == 0:
        partie2 = mot[milieu:]
    else:
        partie2 = mot[milieu+1:]

    if partie1 == partie2[::-1]:
        print("Votre mot est un palindrome")
    else:
        print("Votre mot n'est pas un palindrome")

if __name__ == '__main__':
    main()
    
""" CORRECTION CHATGPT
def est_palindrome(chaine):
    chaine = chaine.lower()  # Convertit la chaîne en minuscules pour ignorer la casse
    chaine = chaine.replace(" ", "")  # Supprime les espaces de la chaîne

    if chaine == chaine[::-1]:
        return True
    else:
        return False

def main():
    chaine = input("Entrez une chaîne de caractères : ")

    if est_palindrome(chaine):
        print(f"La chaîne '{chaine}' est un palindrome")
    else:
        print(f"La chaîne '{chaine}' n'est pas un palindrome")

if __name__ == '__main__':
    main()

"""