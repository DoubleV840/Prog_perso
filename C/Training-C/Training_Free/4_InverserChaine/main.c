//
// Created by Willipatafoul
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char chaine[100];
    char inverse[100];
    int longueur, i;

    printf("Entrez une chaine de caracteres : ");
    scanf("%s", chaine);

    longueur = strlen(chaine);

    for (i = 0; i < longueur; i++) 
    {
        inverse[i] = chaine[longueur - i - 1];
    }

    inverse[longueur] = '\0';

    printf("La chaine inverse est : %s\n", inverse);

    return 0;
}

