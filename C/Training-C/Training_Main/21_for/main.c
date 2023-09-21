//
// Created by Willipatafoul at 20:22 on 03/05/2023
//

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int nombre, total = 0;

    printf("Entrez un nombre pour effectuer la somme des n premiers entiers :");
    scanf("%d", &nombre);

    for (int i = 1; i <= nombre; i++)
    {
        total += i;
        // printf("%d\n", i);
    }

    printf("Le total de la somme des %d premiers enters est de %d\n", nombre, total);
    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>

int main()
{
    int n, sum = 0;

    printf("Entrez un nombre entier positif : ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        sum += i;
    }

    printf("La somme des %d premiers entiers est : %d\n", n, sum);

    return 0;
}

*/