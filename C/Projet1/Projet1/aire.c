//
//  aire.c
//  Projet1
//
//  Created by William Berger on 31/03/2022.
//

#include "aire.h"

int increment(void)
{
    static int nombre = 0;
    
    nombre++;
    
    return nombre;
}
