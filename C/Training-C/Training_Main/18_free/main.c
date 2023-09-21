//
// Created by Willipatafoul at 18:44 on 26/04/2023
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n, i;
    int *tab;

    printf("Entrez le nombre d'éléments que vous voulez afficher : ");
    scanf("%d", &n);

    tab = calloc(n, sizeof(int));
    if(tab == NULL)
        return 1;

    printf("Entrez les %d nombres que vous voulez afficher : ", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &tab[i]);
    }
    
    printf("Voici les nombres que vous avez choisis : ");
    for (i = 0; i < n-1; i++)
    {
        printf("%d ", tab[i]);
    }
    printf("%d", tab[i]);
    free(tab);
    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i;
    int *tab;

    printf("Entrez le nombre d'éléments que vous voulez afficher : ");
    scanf("%d", &n);

    tab = malloc(n * sizeof(int));
    if(tab == NULL)
        return 1;

    printf("Entrez les %d nombres que vous voulez afficher : ", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &tab[i]);
    }

    printf("Voici les nombres que vous avez choisis :");
    for (i = 0; i < n; i++)
    {
        printf(" %d", tab[i]);
        if(i != n-1) {
            printf(",");
        }
    }
    printf("\n");

    free(tab);
    return 0;
}

*/