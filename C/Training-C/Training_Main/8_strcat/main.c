//
// Created by Willipatafoul at 16:14 on 15/04/2023
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char chaine1[100], chaine2[100];
    

    printf("Entrez la première chaine : ");
    fgets(chaine1, 100, stdin);

    if(chaine1[strlen(chaine1) - 1] == '\n')
    {
        chaine1[strlen(chaine1) - 1] = '\0';
    }

    printf("Entrez la deuxième chaine : ");
    fgets(chaine2, 100, stdin);

    strcat(chaine1, chaine2);

    printf("La chaine modifiée est : %s", chaine1);
    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void remove_newline(char* str);

int main()
{
    char chaine1[100], chaine2[100];

    printf("Entrez la première chaine : ");
    fgets(chaine1, 100, stdin);
    remove_newline(chaine1);

    printf("Entrez la deuxième chaine : ");
    fgets(chaine2, 100, stdin);
    remove_newline(chaine2);

    strcat(chaine1, chaine2);

    printf("La chaine modifiée est : %s", chaine1);
    return 0;
}

void remove_newline(char* str)
{
    if (str[strlen(str) - 1] == '\n')
    {
        str[strlen(str) - 1] = '\0';
    }
}

*/