from typing import Any
import pygame
import pygame

class player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('Slime_Medium_Red.png') #Charge à partir d'un fichier l'image que l'on souhaite dans une variable
        self.image = self.get_image(0, 0) #Récuperer la première image du 'slime' dans l'image png
        self.rect = self.image.get_rect() # Crée un rectangle basé sur les dimensions de l'image du sprite. Le rectangle est utilisé pour positionner et manipuler le sprite.
        self.image.set_colorkey([0, 0, 0]) # Définit la couleur transparente de l'image du sprite
        self.position = [x, y] # Définit la position du sprite sur l'écran en utilisant les coordonnées x et y spécifiées. Le sprite sera placé à ces coordonnées lorsqu'il sera dessiné à l'écran.
        self.speed = 3 #Vitesse de déplacement du personnage
        self.images = { #Dictionnaire des images du personnage en fonction du déplacement
            "down": self.get_image(0, 0),
            "right": self.get_image(0, 32),
            "up": self.get_image(0, 64),
            "left": self.get_image(0, 96),
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12) #Crée un rectangle au pied du personnage
        self.old_postion = self.position.copy() #Copie la position du joueur 
        
    def move_right(self): self.position[0] += self.speed #Déplacement personnage à droite
    def move_left(self): self.position[0] -= self.speed #Déplacement personnage à gauche
    def move_up(self): self.position[1] -= self.speed #Déplacement personnage en haut
    def move_down(self): self.position[1] += self.speed #Déplacement personnage en bas
        
    def save_location(self): self.old_postion = self.position.copy()
    
    def change_animation(self, name): 
        self.image = self.images[name] # Attribue à self.image l'image correspondant au nom spécifié à partir du dictionnaire self.images
        self.image.set_colorkey((0, 0, 0)) # Définit la couleur transparente de l'image du sprite
        
    def update(self):
        self.rect.topleft = self.position # Positionne le coin supérieur gauche du rectangle (self.rect) à la position spécifiée par self.position
        self.feet.midbottom = self.rect.midbottom #Positionnement des pieds du joueur par rapport au rectangle
        
    def move_back(self): #Permet de replacer le joueur dans la position precédant une collision
        self.position = self.old_postion #Replace le joueur à son ancienne position
        self.rect.topleft = self.position # Positionne le coin supérieur gauche du rectangle (self.rect) à la position spécifiée par self.position
        self.feet.midbottom = self.rect.midbottom #Positionnement des pieds du joueur par rapport au rectangle
        
    def get_image(self, x, y):
        image = pygame.Surface([32, 32]) # Crée une nouvelle surface d'image de taille 32x32 pixels. Cette surface sera utilisée pour stocker une partie du sprite sheet
       
        #Copie une portion du sprite sheet sur la surface d'image créée.  
        #La portion copiée est définie par les coordonnées (x, y) et la taille de 32x32. Les coordonnées (0, 0) spécifient la position de destination sur la surface d'image
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32)) 
        return image