from game import game
import pygame #Importation de la bibliotèque pygame

if __name__ == '__main__':
    pygame.init() #Initialisation des modules de la bibliotèque pygame
    jeu = game() 
    jeu.run()
