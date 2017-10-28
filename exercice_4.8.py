# Programme qui calcule les 50 premiers termes de la table de multiplication par # 13, mais n'affiche que ceux qui sont des multiples de 7.

i, j = 0, 13

while(i<=50):
    if((i*j)%7==0):
        print(i*j,end=" ")
    else:
        pass
    i = i+1
