//
// Created by Willipatafoul at 19:52 on 10/05/2023
//

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int tab[100];
    int i;

    printf("Entrez une serie de nombres entiers positifs : ");
    for (i = 0; i < 100; i++)
    {
        scanf("%d", &tab[i]);
        if(tab[i] % 7 == 0)
        {
            printf("Stop ici ce nombre est un multiple de 7");
            break;
        }
    }
    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>

int main()
{
    int nombre;

    while (1) {
        printf("Entrez un nombre entier positif : ");
        scanf("%d", &nombre);

        if (nombre % 7 == 0) {
            printf("Le nombre est un multiple de 7.\n");
            break;  // Sort de la boucle lorsque le nombre est un multiple de 7
        }
    }

    return 0;
}

*/