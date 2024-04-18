# Addition de deux nombres:
# Écrivez un programme qui prend deux nombres en entrée et affiche leur somme.

# float is for transform number in float ,....
num1 = float(input("quel est votre nombre ? : "))
# input is for ask in the console something 
num2 = float(input("quel est votre nombre ? : "))
somme = num1 + num2
print(somme)

# other way to making the algorithm 

def calculate(nbr1, nbr2):
     return nbr1 + nbr2

print(calculate(3, 4))