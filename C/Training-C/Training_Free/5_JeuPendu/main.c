//
// Created by Willipatafoul at 18:43 on 27/04/2023
//

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char motSecret[] = "ROUGE";
    char *motTrouvé;
    char lettres;
    int compte = 10;
    int i;

    printf("Bienvenue au jeu du pendu !\nVous avez %d coups pour trouver le bon mot.\n", compte);

    while(motSecret != motTrouvé || compte == 0)
    {
        printf("Quel est le mot secret ? ");
        for (i = 0; motSecret[i]; i++)
        {
            printf("%s", motTrouvé);
        }
        
        printf("\nProposez une lettre : ");
        scanf("%c", &lettres);

        for (i = 0; motSecret[i]; i++)
        {  
            if(motSecret[i] == lettres)
                printf("%c", lettres);
            else
                printf("*");
            motTrouvé = 
        }
        compte--;
    }
    
    
    return 0;
}