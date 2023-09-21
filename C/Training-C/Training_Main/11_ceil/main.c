//
// Created by Willipatafoul at 21:06 on 23/04/2023
//

#include <stdio.h>
#include <math.h>

int main()
{
    float nombre;

    printf("Entrez un nombre décimal : ");
    scanf("%f", &nombre);

    nombre = ceil(nombre);

    printf("Voici votre nombre arrondi à l'entier superieur : %.2f\n", nombre);

    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <math.h>

int main()
{
    float nombre;

    printf("Entrez un nombre décimal : ");
    scanf("%f", &nombre);

    nombre = ceil(nombre);

    printf("Voici votre nombre arrondi à l'entier supérieur : %.0f\n", nombre);

    return 0;
}

*/