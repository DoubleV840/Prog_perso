//
// Created by Willipatafoul at 17:28 on 03/05/2023
//

#include <stdio.h>

int main()
{
    int entier;

    printf("Entrez un nombre : ");
    scanf("%d", &entier);

    if(entier % 2 == 0)
        printf("Votre nombre est pair.\n");
    else
        printf("Votre nombre est impair.\n");
    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>

int main()
{
    int n;

    printf("Entrez un entier : ");
    scanf("%d", &n);

    if (n % 2 == 0)
    {
        printf("%d est pair.\n", n);
    }
    else
    {
        printf("%d est impair.\n", n);
    }

    return 0;
}

*/