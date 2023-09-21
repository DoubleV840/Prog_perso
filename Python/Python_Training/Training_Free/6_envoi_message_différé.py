# -*- coding: utf-8 -*-
#Created by Willipatafoul at 12:16 on 13/05/2023
#
import pywhatkit

def main():
    print("Bienvenue dans la messagerie diférée :")
    numero = input("Entrez le numero de telephone : ")
    message = input("Entrez votre message : ")
    heure = input("Entrez l'heure de l'envoi (format HH:MM) : ")
    
    pywhatkit.sendwhatmsg(numero, message, int(heure[:2]), int(heure[3:]))

if __name__ == '__main__':
    main()