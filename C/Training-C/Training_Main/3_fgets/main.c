//
// Created by Willipatafoul
//

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define SPACE 100

int main()
{
    char *textChoisi = 0;
    int i;

    textChoisi = malloc(SPACE * sizeof(int));
    if(textChoisi == NULL)
    {
        printf("Erreur d'alloc");
        return 1;
    }

    printf("Entrez une phrase : ");
    fgets(textChoisi, SPACE, stdin);

    for (i = 0; textChoisi[i]; i++)
    {
        textChoisi[i] = toupper(textChoisi[i]);
    }
    
    printf("La phrase en majuscule est : %s", textChoisi);

    free(textChoisi);

    return 0;
}