import pygame #Importation de la bibliotèque pygame
import pytmx #Importation de la bibliotèque pytmx
import pyscroll #Importation de la bibliotèque pyscroll

from player import player #Importation du fichier 'player.py'

class game: #Définition du groupe de fonctions 'game'
    
    def __init__(self):
        #PYGAME SETUP
        self.screen = pygame.display.set_mode((800, 600)) #Taille de la fenetre du jeu
        pygame.display.set_caption("Premier Jeu - Apprentissage") #Nom de la fenetre du jeu
        self.clock = pygame.time.Clock() #Création d'une temporalité pour gerer le taux de rafraichissement

        #Charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('Premier Jeu - App.tmx') #Charge le fichier de la carte du jeu pour pouvoir acceder à ses propiétés
        map_data = pyscroll.data.TiledMapData(tmx_data) #Crée un objet nécessaire à l'affichage et au defilement de la carte dans une fenetre de jeu pygame
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size()) #Affiche la carte et gère le rendu dans le jeu
        map_layer.zoom = 2 #Crée un zoom
        
        #Générer un joueur
        player_position = tmx_data.get_object_by_name("player") #Détection de l'objet 'player' sur la carte pour la position initiale du joueur
        self.player = player(player_position.x, player_position.y) #Coordonnées du joueur (x, y) en fonction de la position de départ
        
        #Gérer les collisions
        self.walls = [] #Liste nommée 'walls'
        
        for obj in tmx_data.objects: #Pour tout les objets dans la carte
            if obj.type == 'collision': #Si l'objet est de type 'collision'
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height)) #Ajout d'un rectangle pour chaque collision
            
        #Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5) #Facilite le défilement de la carte et permet de placer le joueur sur le bon niveau de calque
        self.group.add(self.player) #Ajout du joueur sur la map
        
    def input(self):
        pressed = pygame.key.get_pressed() #Récupère toutes les touches physiques de l'ordinateur
        
        if pressed[pygame.K_UP]:
            self.player.move_up() #Appel de la fonction 'move_up' pour le déplacement haut du joueur
            self.player.change_animation("up") #Appel de la fonction 'change_animation' pour changer l'aspect du personnage vers le haut
        elif pressed[pygame.K_DOWN]:
            self.player.move_down() #Appel de la fonction 'move_down' pour le déplacement bas du joueur
            self.player.change_animation("down") #Appel de la fonction 'change_animation' pour changer l'aspect du personnage vers le bas
        elif pressed[pygame.K_LEFT]:
            self.player.move_left() #Appel de la fonction 'move_left' pour le déplacement gauche du joueur
            self.player.change_animation("left") #Appel de la fonction 'change_animation' pour changer l'aspect du personnage vers la gauche
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right() #Appel de la fonction 'move_right' pour le déplacement droite du joueur
            self.player.change_animation("right") #Appel de la fonction 'change_animation' pour changer l'aspect du personnage vers la droite
            
    def update(self):
        self.group.update()
        #Verification des collisions
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()
    
    def run(self):
        #BOUCLE DE FONCTIONNEMENT
        running = True #Variable pour faire tourner le jeu (ON)

        while running:
            
            self.player.save_location()
            self.input() #Appel de la fonction 'input' pour le déplacement du joueur
            self.update() #Appel de la fonction 'update' pour mettre a jour la position du joueur
            self.group.center(self.player.rect.center) #Centre la "camera" pour positionner le joueur au centre de l'ecran
            self.group.draw(self.screen) #Dessine le joueur sur l'ecran
            
            for event in pygame.event.get(): #Récupère les evenements du clavier et de la souris
                if event.type == pygame.QUIT: #Permet à l'utilisateur de fermer la fenètre du jeu avec la X croix
                    running = False #Arret du fonctionnement du jeu

            pygame.display.flip() #Mettre à jour l'affichage avec les nouvelles modifications
            
            self.clock.tick(60) #Gérer le nombre de FPS max
            
        pygame.quit() #Quitte et ferme pygame
