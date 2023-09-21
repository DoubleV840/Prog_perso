//
// Created by Willipatafoul at 15:58 on 22/04/2023
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "struct.h"

int main()
{
    coordonnees points1;
    coordonnees points2;

    int x, y;
    float distance = 0;
    double calcul = 0;

    printf("Entrez les coordonnées du premier point (x1, y1) : ");
    scanf("%d %d", &points1.x, &points1.y);

    printf("Entrez les coordonnées du deuxième point (x2, y2) : ");
    scanf("%d %d", &points2.x, &points2.y);

    x = points2.x - points1.x;
    y = points2.y - points1.y;

    x = abs(x);
    y = abs(y);
    calcul = (x * x)+(y * y);
    distance = sqrt(calcul);

    printf("La distance entre ces deux points est de %f\n", distance);

    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int x1, y1, x2, y2;
    float distance;

    printf("Entrez les coordonnees du premier point (x1, y1) : ");
    scanf("%d %d", &x1, &y1);

    printf("Entrez les coordonnees du deuxieme point (x2, y2) : ");
    scanf("%d %d", &x2, &y2);

    distance = sqrt(pow(abs(x2 - x1), 2) + pow(abs(y2 - y1), 2));

    printf("La distance entre les deux points est de : %.2f", distance);

    return 0;
}

*/