//
//  main.c
//  Training C - 1 - Moyenne
//
//  Created by William Berger on 03/04/2023.
//

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i = 0;
    int *nombres;
    float moyenne = 0, somme = 0;
    
    printf("Combien de nombres voulez-vous saisir ? ");
    scanf("%d", &n);
    
    nombres = malloc(n * sizeof(int));
    if (nombres == NULL) // On vérifie si l'allocation a marché ou non
    {
        exit(0); // On arrête tout
    }
    for (i = 0; i < n; i++)
    {
        printf("Entrez le nombre %d : ", i+1);
        scanf("%d", &nombres[i]);
        somme = somme + nombres[i];
    }
    moyenne = somme / n;
    
    printf("La moyenne des %d nombres est : %.1f\n", n, moyenne);
    free(nombres);
    
    return 0;
}
/*CORRECTION CHATGPT

#include <stdio.h>

int main() {
    int n, i, nombre;
    float somme = 0, moyenne;
    
    printf("Combien de nombres voulez-vous saisir ? ");
    scanf("%d", &n);
    
    for (i = 1; i <= n; i++) {
        printf("Entrez le nombre %d : ", i);
        scanf("%d", &nombre);
        somme += nombre;
    }
    
    moyenne = somme / n;
    
    printf("La moyenne des %d nombres est : %.1f", n, moyenne);
    
    return 0;
}

*/