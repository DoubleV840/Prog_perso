# -*- coding: utf-8 -*-
#Created by Willipatafoul at 16:27 on 18/09/2023
#

def somme_chiffre(n):

    if n == 0:
        return 0
    else:
        for i in n:
            somme += somme_chiffre(i)

if __name__ == '__main__':
    print(somme_chiffre(123))