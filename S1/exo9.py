# Calcul de la factorielle:
# Écrivez un programme qui prend un nombre en entrée et affiche sa factorielle.


# correction

nombre = int(input("Entrez un nombre :"))
factorielle = 1

for i in range(1, nombre+1):
   factorielle *= i
print("La factorielle est : " , factorielle)

# Fonction

# def factorielle(n):
    
#    if n == 0:
#       return 1
#    else:
#       F = 1
#       for k in range(2,n+1):
#          F = F * k

#       return F
   

# print(factorielle(5))