//
// Created by Willipatafoul at 18:07 on 26/04/2023
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int n, i, total = 0;
    int *tab;

    printf("Entrez le nombre d'éléments que vous voulez additionner : ");
    scanf("%d", &n);

    tab = malloc(n * sizeof(int));
    if(tab == NULL)
        return 1;
    
    printf("Entrez les %d nombres que vous voulez additionner : ", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &tab[i]);
    }

    tab = realloc(tab, (n+1) * sizeof(int));
    if(tab == NULL)
    {
        printf("Erreur de realloc");
        return 1; 
    }

    printf("Ajoutez un nouveau nombre à additionner avec le reste : ");
    scanf("%d", &tab[i]);

    for (i = 0; i <= n; i++)
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

int main() {
    int n, i, sum = 0;
    int *arr;

    printf("Entrez le nombre d'entiers à stocker : ");
    scanf("%d", &n);

    arr = (int *) malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Erreur d'allocation de mémoire\n");
        return 1;
    }

    // Saisie des entiers et stockage dans le tableau
    printf("Entrez les %d entiers :\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Redimensionnement du tableau pour ajouter un entier supplémentaire
    n++; // Augmenter le nombre d'entiers de 1
    arr = (int *) realloc(arr, n * sizeof(int));
    if (arr == NULL) {
        printf("Erreur de réallocation de mémoire\n");
        return 1;
    }
    printf("Entrez un nouvel entier à ajouter : ");
    scanf("%d", &arr[n-1]); // Ajouter l'entier à la fin du tableau

    // Calcul de la somme des entiers
    for (i = 0; i < n; i++) {
        sum += arr[i];
    }

    // Affichage de la somme
    printf("La somme des %d entiers est : %d\n", n, sum);

    // Libération de la mémoire allouée
    free(arr);

    return 0;
}

*/