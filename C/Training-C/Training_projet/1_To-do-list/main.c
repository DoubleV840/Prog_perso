//
// Created by Willipatafoul at 16:51 on 15/04/2023
//

#include <stdio.h>
#include <stdlib.h>
#include "informations.h"

void ajouter_tache(tache *liste_tache, int *n_taches);

int main()
{
    
    return 0;
}

void ajouter_tache(tache *liste_taches, int *n_taches)
{
    tache nouvelle_tache;

    printf("Nom de la nouvelle tache : ");
    fgets(nouvelle_tache.nom, 100, stdin);

    printf("Descrition de la nouvelle tache : ");
    fgets(nouvelle_tache.description, 100, stdin);

    printf("Date d'echeance de la nouvelle tache :");
    scanf("%d/%d/%d", &nouvelle_tache.jour, &nouvelle_tache.mois, &nouvelle_tache.année);

    liste_taches[n_taches] = nouvelle_tache;
    (*n_taches)++;
}
void supprimer_tache(tache *listes_taches, int *n_taches)
{
    tache 
}


