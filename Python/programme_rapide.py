# -*- coding: utf-8 -*-
#Created by Willipatafoul at 21:18 on 21/05/2023
#
import pyautogui
from pynput import keyboard

def calcul(): #Calcul de 2^64
    i = 1
    
    for jsp in range(64):
        i *= 2
        print(i)

def on_press(key):
    if key == keyboard.Key.esc:
        return False

def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while listener.is_alive():
        # Récupérer les coordonnées actuelles de la souris
        x, y = pyautogui.position()

        # Afficher les coordonnées de la souris
        print(f"Position de la souris : {x}, {y}")

        # Attendre l'appui d'une touche
        #pyautogui.click(x, y)
        
def inverse():
    mot = input("Entrez une chaine de caractère : ")
    print(mot[::-1])

if __name__ == '__main__':
    #calcul()
    main()
    #inverse()
    