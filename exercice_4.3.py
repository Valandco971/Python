# petit programme qui affiche une table de conversion de sommes d'argent 
# exprimées en euros, en dollars canadiens.
# La forme devra être celle-ci 1 euro(s) = 1.65 dollar(s)

i, j = 1, 1.65
while i < 16384:
    print(i,"euro(s) =",i*j,"dollar(s)")
    i=i+1
