//
// Created by Willipatafoul at 22:02 on 03/05/2023
//

//A REFAIRE

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *tab;
    int i = 0, total = 0;

    tab = malloc((i + 1) * sizeof(int));
    if(tab == NULL)
        return 1;

    do
    {
        printf("Entrez un nombre positif (arrêt si un nombre positif ou nul est entré par l'utilisateur) : ");
        scanf("%d", &tab[i]);
        i++;
        tab = realloc(tab, (i + 1) * sizeof(int));
        if(tab == NULL)
            return 1;
    } while (tab[i-1] > 0);

    for (i = 0; tab[i] > 0; i++)
    {
        total += tab[i];
    }
    printf("La somme des nombres positifs entrés est de %d\n", total);

    free(tab);

    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>

int main()
{
    int nombre, total = 0;

    printf("Entrez des nombres entiers positifs (saisissez un nombre négatif ou nul pour arrêter) : ");

    while (1)
    {
        scanf("%d", &nombre);

        if (nombre <= 0)
            break;

        total += nombre;
    }

    printf("La somme des nombres positifs saisis est : %d\n", total);

    return 0;
}

*/