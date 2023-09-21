//
// Created by Willipatafoul at 17:00 on 21/04/2023
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void remove_newline(char* str);

int main()
{
    char chaine1[100], chaine2[100];

    printf("Ecrivez la première chaine : ");
    fgets(chaine1, 100, stdin);

    remove_newline(chaine1);
    // chaine1[strcspn(chaine1, "\n")] = 0;

    printf("Ecrivez la deuxième chaine : ");
    fgets(chaine2, 100, stdin);

    remove_newline(chaine2);
    // chaine2[strcspn(chaine2, "\n")] = 0;

    if(strcmp(chaine1, chaine2) == 0)
        printf("Les deux chaines sont identiques : \n1-%s\t2-%s", chaine1, chaine2);
    else
        printf("Les deux chaines sont différentes : \n1-%s\t2-%s", chaine1, chaine2);

    return 0;
} 

void remove_newline(char* str)
{
    if (str[strlen(str) - 1] == '\n')
    {
        str[strlen(str) - 1] = '\0';
    }
}

/* CORRECTION CHATGPT
#include <stdio.h>
#include <string.h>

int main() {
    char chaine1[100], chaine2[100];
    
    printf("Entrez la première chaîne : ");
    fgets(chaine1, 100, stdin);
    
    printf("Entrez la deuxième chaîne : ");
    fgets(chaine2, 100, stdin);
    
    // Enlever le caractère de retour à la ligne ajouté par fgets
    chaine1[strcspn(chaine1, "\n")] = 0;
    chaine2[strcspn(chaine2, "\n")] = 0;
    
    if (strcmp(chaine1, chaine2) == 0) {
        printf("Les deux chaînes sont identiques.\n");
    } else {
        printf("Les deux chaînes sont différentes.\n");
    }
    
    return 0;
}

*/