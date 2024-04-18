# Calcul du carré et du cube:
# Écrivez un programme qui prend un nombre en entrée et affiche son carré et son cube.



p = input("Quel est votre nombre ? ")
# si nous souhaitons un nombre il faut convertir l'entrée de l'utilisateur 
conversion = float(p)
# Pour calculer au carre
calcul1 = conversion ** 2
# Pour calculer au cube
calcul2  = conversion ** 3
print("votre nombre au carre  est : ", calcul1 , ", et votre nombre au cube est :", calcul2,".")