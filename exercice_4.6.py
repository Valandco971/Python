# Programme qui convertit un nombre entier de secondes fourni audépart en un
# nombre  d'années, de mois, de jours, de minutes et de secondes.
# Les base de notre calcul seront: 1h=3600s, 1j=24h, 1mois=30j, 1 année=12mois,
# donc 3600*24*30*12=31104000

donnees = 12334578766576789                        # nombre de secondes initiales

annee = donnees // 31104000                     # résultante du nombre d'année

mois =  (donnees % 31104000) // 2592000         # résultante du nombre de mois

jours = ((donnees % 31104000) % 2592000) // 86400    # nombre de jours

minutes = (((donnees % 31104000) % 2592000) % 86400) // 60

secondes = (((donnees % 31104000) % 2592000) % 86400) % 60


print("cela correspond donc à",annee,"ans,",mois,"mois,",jours,"jours,",minutes, "minutes,", secondes,"secondes")
