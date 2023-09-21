# -*- coding: utf-8 -*-
#Created by Willipatafoul at 19:50 on 17/05/2023
#
import random

def result(computer, player):
    print("Player: ", player)
    print("Computer: ", computer)

def main():
    while True:
        choix = ["pierre", "papier", "sciseau"]

        computer = random.choice(choix)
        player = None
    
        while player not in choix:
            player = input("Pierre, papier, sciseau ?: ").lower()
    
        if player == computer:
            result(computer, player)
            print("Egalité ! Recommencez !")
        elif player == choix[0]:
            if computer == choix[1]:
                result(computer, player)
                print("Perdu l'ordi gagne !")
            if computer == choix[2]:
                result(computer, player)
                print("Gagné bravo !")
        elif player == choix[1]:
            if computer == choix[2]:
                result(computer, player)
                print("Perdu l'ordi gagne !")
            if computer == choix[0]:
                result(computer, player)
                print("Gagné bravo !")
        elif player == choix[2]:
            if computer == choix[0]:
                result(computer, player)
                print("Perdu l'ordi gagne !")
            if computer == choix[1]:
                result(computer, player)
                print("Gagné bravo !")
        play_again = input("Voulez vous rejouer ? (yes/no)").lower()
        if play_again != "yes" or play_again != "y":
            break
    print("Ok bye !")
    
if __name__ == '__main__':
    main()