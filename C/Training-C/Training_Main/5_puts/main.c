//
// Created by Willipatafoul at 18:10 on 11/04/2023
//

//Programme alloué dynamiquement mais ne comprend pas les "espaces" dans l'initailisation de la chaine de caractère.
//Utiliser 'fgets' pour resoudre cela mais l'allocation dynamique n'est plus prise en compte.

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{
    char *chaine;
    int i;

    chaine = malloc(100 * sizeof(char));

    printf("Entrez une chaine de caractère : ");
    scanf("%s", chaine);

    for (i = 0; chaine[i] ; i++)
    {
        chaine[i] = toupper(chaine[i]);
    }
    puts(chaine);
    
    free(chaine);
    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX_SIZE 100

int main() {
    char chaine[MAX_SIZE];

    printf("Entrez une chaine de caractères : ");
    fgets(chaine, MAX_SIZE, stdin);

    for (int i = 0; i < strlen(chaine); i++) {
        chaine[i] = toupper(chaine[i]);
    }

    puts(chaine);

    return 0;
}

*/