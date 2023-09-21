//
// Created by Willipatafoul
//

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *chaine;
    int EntierPositif, Somme = 0;

    printf("Combien d'entier voulez vous ? : ");
    scanf("%d", &EntierPositif);

    chaine = malloc(EntierPositif * sizeof(int));
    if(chaine == NULL)
    {
        printf("Erreur d'alloc");
        return 1;
    }
    if(EntierPositif <= 0)
    {
        printf("Le nombre d'entiers doit être positif.");
        return 1;
    }
    printf("Entrez les nombres entiers : \n");
    
    for (int i = 0; i < EntierPositif; i++)
    {
        scanf("%d", &chaine[i]);
        Somme += chaine[i];
    }
    printf("La somme de tous les entiers est : %d", Somme);

    free(chaine);

    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>

int main() {
    int n, entier, somme = 0;
    printf("Entrez un entier positif : ");
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        printf("Entrez l'entier numero %d : ", i+1);
        scanf("%d", &entier);
        somme += entier;
    }

    printf("La somme des entiers saisis est : %d", somme);

    return 0;
}
*/