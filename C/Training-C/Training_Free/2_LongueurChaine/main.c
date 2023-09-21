//
//  main.c
//  Training C - 2 - Longueur d'une chaine
//
//  Created by William Berger on 03/04/2023.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAILLE_MAX 100

int main(int argc, const char * argv[])
{
    int longueurChaine = 0;
    char *chaine;
    
    chaine = malloc(TAILLE_MAX * sizeof(char));
    if (chaine == NULL) // On vérifie si l'allocation a marché ou non
    {
        printf("Erreur d'alloc");
        return 1; // On arrête tout
    }
    printf("Entrez une chaine de caractères : ");
    scanf("%s", chaine);
    
    longueurChaine = strlen(chaine);
    
    printf("La chaine '%s' contient %d caractères.\n", chaine, longueurChaine);
    
    free(chaine);
    
    return 0;
}
/*CORRECTION CHATGPT

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char* chaine = NULL;
    size_t longueur = 0;
    printf("Entrez une chaine de caracteres : ");
    getline(&chaine, &longueur, stdin);

    longueur = strlen(chaine);

    printf("La chaine '%s' contient %ld caracteres.\n", chaine, longueur);

    free(chaine);

    return 0;
}

*/