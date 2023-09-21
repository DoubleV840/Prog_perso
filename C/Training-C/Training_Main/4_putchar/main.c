//
// Created by Willipatafoul
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char chaine[100];
    char *positionRALL;

    printf("Entrez une chaine de caractère : ");
    fgets(chaine, 100, stdin);

    positionRALL = strchr(chaine, '\n'); // On recherche '\n'
    if (positionRALL != NULL) // Si on a trouvé '\n'
    {
        *positionRALL = '\0'; // On remplace ce caractère par '\0'
    }
    for (int i = 0; chaine[i]; i++)
    {
        putchar(chaine[i]);
        putchar('\n');

    }
    
    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

int main()
{
    char chaine[MAX_SIZE];

    printf("Entrez une chaine de caractères : ");
    fgets(chaine, MAX_SIZE, stdin);

    for (int i = 0; i < strlen(chaine); i++) {
        putchar(chaine[i]);
        putchar('\n');
    }

    return 0;
}

*/