# Vérification de nombre pair ou impair:
# Écrivez un programme qui vérifie si un nombre donné par l'utilisateur est pair ou impair.
ask = int(input('Quel est votre nombre ? '))      


# %2 => permet de savoir le reste d'un nombre divisé par 2, si le nombre a un reste alors il est impair et inversement 

if ask%2 == 0:
    print("pair")
else: 
    print("impair")
