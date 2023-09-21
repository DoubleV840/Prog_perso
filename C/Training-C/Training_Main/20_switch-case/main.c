//
// Created by Willipatafoul at 19:33 on 03/05/2023
//

#include <stdio.h>

int main()
{
    int nombre = 0;

    while (nombre != 8)
    {
        printf("Choisissez un nombre entre 1 et 7 (8 pour quitter) : ");
        scanf("%d", &nombre);
            switch (nombre)
            {
                case 1 :
                    printf("Le nombre %d correspond à LUNDI\n", nombre);
                break;
                case 2 :
                    printf("Le nombre %d correspond à MARDI\n", nombre);
                break;
                case 3 :
                    printf("Le nombre %d correspond à MERCREDI\n", nombre);
                break;
                case 4 :
                    printf("Le nombre %d correspond à JEUDI\n", nombre);
                break;
                case 5 :
                    printf("Le nombre %d correspond à VENDREDI\n", nombre);
                break;
                case 6 :
                    printf("Le nombre %d correspond à SAMEDI\n", nombre);
                break;
                case 7 :
                    printf("Le nombre %d correspond à DIMANCHE\n", nombre);
                break;
                case 8 :
                    printf("Merci d'avoir essayé !\n");
                    return 0;                   
                default:
                    printf("Erreur le nombre choisi n'est pas valide.\n");
                break;
            }
    }
    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>

int main()
{
    int nombre = 0;

    while (nombre < 1 || nombre > 7)
    {
        printf("Choisissez un nombre entre 1 et 7 : ");
        scanf("%d", &nombre);

        switch (nombre)
        {
            case 1:
                printf("Lundi\n");
                break;
            case 2:
                printf("Mardi\n");
                break;
            case 3:
                printf("Mercredi\n");
                break;
            case 4:
                printf("Jeudi\n");
                break;
            case 5:
                printf("Vendredi\n");
                break;
            case 6:
                printf("Samedi\n");
                break;
            case 7:
                printf("Dimanche\n");
                break;
            default:
                printf("Le nombre n'est pas valide. Veuillez choisir un nombre entre 1 et 7.\n");
                break;
        }
    }

    return 0;
}

*/