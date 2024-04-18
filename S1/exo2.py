# Calcul de la moyenne:
# Écrivez un programme qui prend trois nombres en entrée et affiche leur moyenne.

nbr1 = float(input("quel est votre premié nombre ? :"))
nbr2 = float(input("quel est votre deuxième nombre ? :"))
nbr3 = float(input("quel est votre troisième nombre ? :"))

somme = float((nbr1+nbr2+nbr3) // 3)

print("la moyenne est : ", somme)