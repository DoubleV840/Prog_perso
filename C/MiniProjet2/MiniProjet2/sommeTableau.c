//
//  sommeTableau.c
//  MiniProjet2
//
//  Created by William Berger on 14/04/2022.
//

#include "sommeTableau.h"

int sommeTableau(int tableau[], int tailleTableau)
{
    int i, somme = 0;
    
    for (i=0; i < 4; i++)
    {
        somme += tableau[i];
    }
    return somme;
}
double moyenneTableau(int tableau[], int tailleTableau)
{
    int i, somme = 0;
    
    for (i=0; i < 4; i++)
    {
        somme += tableau[i];
    }
    return (double)somme/(double)tailleTableau;
}
