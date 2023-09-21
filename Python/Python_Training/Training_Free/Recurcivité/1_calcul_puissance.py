# -*- coding: utf-8 -*-
#Created by Willipatafoul at 15:24 on 18/09/2023
#

def puissance(nb, exposant):
    
    if exposant == 0:
        return 1
    else:
        return nb * puissance(nb, exposant - 1)
    
nb = 2
exposant = 3
print(puissance(nb, exposant))