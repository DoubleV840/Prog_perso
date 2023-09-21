//
// Created by Willipatafoul at 22:02 on 23/04/2023
//

#include <stdio.h>
#include <math.h>

int main()
{
    int nombre;

    printf("Entrez un nombre entier positif : ");
    scanf("%d", &nombre);

    double racine = sqrt(nombre);

    printf("Voici la racine carrée de votre nombre : %.2lf\n", racine);

    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <math.h>

int main()
{
    int nombre;

    printf("Entrez un nombre entier positif : ");
    scanf("%d", &nombre);

    if (nombre < 0) {
        printf("Erreur : le nombre doit être positif\n");
        return 1; // On quitte le programme avec une erreur
    }

    double racine = sqrt(nombre);

    printf("Voici la racine carrée de votre nombre : %.2lf\n", racine);

    return 0;
}

*/