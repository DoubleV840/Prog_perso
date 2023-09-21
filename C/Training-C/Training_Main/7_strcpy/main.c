//
// Created by Willipatafoul at 15:39 on 15/04/2023
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char chaine1[100];
    char chaine2[100];

    printf("Entrez la première chaine à copier dans la seconde : ");
    fgets(chaine1, 100, stdin);

    printf("Entrez la deuxième chaine de caractère : ");
    fgets(chaine2, 100, stdin);

    printf("La deuxième chaine de caractère actuelle est : %s", chaine2);

    strcpy(chaine2, chaine1);
    printf("La deuxième chaine de caractère est maintenant : %s", chaine2);

    return 0;
}

/* CORRECTION CHATGPT
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char chaine1[100], chaine2[100];

    printf("Entrez une chaine de caractères : ");
    fgets(chaine1, 100, stdin);

    // Supprime le caractère de retour à la ligne
    if (chaine1[strlen(chaine1) - 1] == '\n') {
        chaine1[strlen(chaine1) - 1] = '\0';
    }

    // Copie la première chaîne dans la deuxième
    strcpy(chaine2, chaine1);

    printf("La première chaine est : %s\n", chaine1);
    printf("La deuxième chaine est : %s\n", chaine2);

    return 0;
}

*/