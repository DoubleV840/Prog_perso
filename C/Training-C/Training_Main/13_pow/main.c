//
// Created by Willipatafoul at 21:52 on 23/04/2023
//

#include <stdio.h>
#include <math.h>

int main()
{
    float rayon, surface;

    printf("Entrez le rayon d'un cercle : ");
    scanf("%f", &rayon);

    surface = M_PI * pow(rayon, 2);

    printf("L'aire du cercle est de %.2f", surface);

    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <math.h>

int main() {
    float rayon, surface;
    const float PI = 3.14159265359; // Définition de la constante PI

    printf("Entrez le rayon d'un cercle : ");
    scanf("%f", &rayon);

    surface = PI * pow(rayon, 2);

    printf("La surface du cercle est de %.2f", surface);

    return 0;
}

*/