# Programme qui affiche les 20 premiers termes de la table de multiplication par # 7, en signalant au passage (à l'aide d'une astérisque) ceux qui sont des       # multiples de 3.

i, j = 0, 7

while(i<20):

    if((i*j)%3!=0):

        print(i*j,end=" ")

    elif((i*j)%3==0):

        print(i*j,"*",end="")

    i = i+1






