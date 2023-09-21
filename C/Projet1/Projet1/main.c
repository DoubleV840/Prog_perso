//
//  main.c
//  Projet1
//
//  Created by William Berger on 21/03/2022.
//

#include <stdio.h>
#include <stdlib.h>
#include "aire.h"

int main(int argc, char *argv[]) // Équivalent de int main()
{
    int nombre2 = 0;
    
    while (nombre2 != 100)
    {
        printf("Incrément de 1 : %d\n", increment());
        nombre2++;
    }
    
    return 0;
}

