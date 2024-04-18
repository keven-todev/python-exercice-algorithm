# Calcul de la factorielle:
# Écrivez un programme qui prend un nombre en entrée et affiche sa factorielle.

nombre = int(input("Entrez un nombre : "))
factorielle = 1
for i in range(1, nombre+1):
    factorielle *= i
print("La factorielle est :", factorielle)