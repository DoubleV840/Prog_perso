//
// Created by Willipatafoul at 18:33 on 11/04/2023
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char chaine[100];
    int longueurChaine = 0;
    char *positionRALL;

    printf("Entrez une chaine de caractères : ");
    fgets(chaine, 100, stdin); //Utiliser 'scanf' pour eviter d'ecrire ce qu'il y a en dessous mais aprèes 'espaces' non compris.(Voir correction ChatGPT dessous)

    positionRALL = strchr(chaine, '\n'); // On recherche '\n'
    if (positionRALL != NULL) // Si on a trouvé '\n'
    {
        *positionRALL = '\0'; // On remplace ce caractère par '\0'
    }

    longueurChaine = strlen(chaine);

    printf("La longueur de la chaine de caractère est de %d", longueurChaine);

    return 0;
}
/* CORRECTION CHATGPT
#include <stdio.h>
#include <string.h>

int main()
{
    char chaine[100];

    printf("Entrez une chaine de caractère : ");
    scanf("%s", chaine);

    int longueur = strlen(chaine);

    printf("La chaine de caractères \"%s\" contient %d caractères.\n", chaine, longueur);

    return 0;
}

*/