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

    nombre = floor(nombre);

    printf("Voici votre nombre arrondi à l'entier inferieur : %.2f\n", nombre);

    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <math.h>

int main() {
    double nombre;
    printf("Entrez un nombre décimal : ");
    scanf("%lf", &nombre);

    double nombreArrondi = floor(nombre);

    printf("Le nombre arrondi à l'entier inférieur est : %lf\n", nombreArrondi);

    return 0;
}

*/