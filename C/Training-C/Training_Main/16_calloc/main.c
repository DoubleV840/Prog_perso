//
// Created by Willipatafoul at 16:40 on 26/04/2023
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n, i;
    float total;
    float *tab;

    printf("Entrez le nombre d'éléments que vous voiulez additionner : ");
    scanf("%d", &n);

    tab = calloc(n, sizeof(float));
    if(tab == NULL)
        return 1;

    printf("Entrez les %d nombres que vous voulez additionner : ", n);
    for (i = 0; i < n; i++)
    {
        scanf("%f", &tab[i]);
    }
    for (i = 0; i < n; i++)
    {
        total += tab[i];
    }

    printf("La somme de tout les nombres est de %.3f.\n", total);

    free(tab);
    
    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, total = 0;
    int *tab;

    printf("Entrez le nombre d'éléments que vous voulez ajouter : ");
    scanf("%d", &n);

    tab = calloc(n, sizeof(int));
    if(tab == NULL)
        return 1;

    printf("Le tableau a été initialisé à 0.\n");

    printf("Entrez les %d nombres que vous voulez ajouter : ", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &tab[i]);
    }

    for (i = 0; i < n; i++)
    {
        total += tab[i];
    }

    printf("Le total de l'addition est de %d.\n", total);

    free(tab);

    return 0;
}

*/