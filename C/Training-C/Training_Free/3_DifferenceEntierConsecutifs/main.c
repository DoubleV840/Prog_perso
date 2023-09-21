 //
 // Created by Willipatafoul
 //
 
 #include <stdio.h>
 #include <stdlib.h>
 
 int main()
 {
    int EntierPositif, NombreFinal, NombreTransitoire1, NombreTransitoire2 = 0, i = 0;
    int *EntierRelatifs;

    printf("Combien de nombres relatifs voulez-vous ? ");
    scanf("%d", &EntierPositif);

    EntierRelatifs = malloc(EntierPositif * sizeof(int));

    printf("Entrez les nombres relatifs que vous avez choisi : \n");

    for(i = 0; i < EntierPositif; i++)
    {
        scanf(" %d", &EntierRelatifs[i]);
    }
    for(i = 0; i < EntierPositif; i++)
    {
        if(EntierRelatifs[i + 1] == '\0')
        {
            printf("Nombre final est : %d\n", NombreFinal);
            free(EntierRelatifs);
            return 0;
        }
        if(EntierRelatifs[i] < EntierRelatifs[i + 1])
        {
            NombreTransitoire1 = EntierRelatifs[i + 1] - EntierRelatifs[i];
        }
        else if(EntierRelatifs[i] >= EntierRelatifs[i + 1])
        {
            NombreTransitoire1 = EntierRelatifs[i] - EntierRelatifs[i + 1];
        }
        if(NombreTransitoire1 > NombreTransitoire2)
        {
            NombreFinal = NombreTransitoire1;
            NombreTransitoire2 = NombreTransitoire1;
        }
    }
    printf("Nombre final est : %d\n", NombreFinal);
    
    free(EntierRelatifs);

    return 0;
 }

/* CORRECTION CHATGPT

#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, max_diff = 0, current_diff;
    int *numbers;

    // Demander à l'utilisateur de saisir N
    printf("Entrez un entier positif N : ");
    scanf("%d", &n);

    // Allouer de la mémoire pour stocker N entiers relatifs
    numbers = malloc(n * sizeof(int));

    // Demander à l'utilisateur de saisir les N entiers relatifs
    printf("Entrez %d entiers relatifs :\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &numbers[i]);
    }

    // Calculer la plus grande différence entre deux entiers consécutifs
    for (int i = 0; i < n - 1; i++) {
        current_diff = abs(numbers[i+1] - numbers[i]);
        if (current_diff > max_diff) {
            max_diff = current_diff;
        }
    }

    // Afficher la plus grande différence
    printf("La plus grande différence entre deux entiers consécutifs est : %d\n", max_diff);

    // Libérer la mémoire allouée pour stocker les entiers relatifs
    free(numbers);

    return 0;
}
*/