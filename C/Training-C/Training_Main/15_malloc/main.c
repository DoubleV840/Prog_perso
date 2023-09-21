//
// Created by Willipatafoul at 20:05 on 24/04/2023
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n, i, total = 0;
    int *tab;

    printf("Entrez le nombres d'éléments que vous voulez aditionner : ");
    scanf("%d", &n);

    tab = malloc(n * sizeof(int));
    if(tab == NULL)
        return 1;

    printf("Entrez les %d nombres que vous voulez additionner : ", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &tab[i]);
    }
    for (i = 0; i < n; i++)
    {
        total += tab[i];
    }

    printf("Le total de l'addition est de %d", total);

    free(tab);
    
    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, somme = 0;
    int *tab;

    printf("Entrez le nombre d'entiers : ");
    scanf("%d", &n);

    tab = (int*) malloc(n * sizeof(int));
    if(tab == NULL)
        return 1;

    for (i = 0; i < n; i++)
    {
        printf("Entrez l'entier numéro %d : ", i+1);
        scanf("%d", &tab[i]);
    }

    for (i = 0; i < n; i++)
    {
        somme += tab[i];
    }

    printf("La somme de tous les entiers est : %d\n", somme);

    free(tab);

    return 0;
}

*/