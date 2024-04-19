# Jeu du devine le nombre:
# Créez un jeu où l'ordinateur choisit un nombre aléatoire entre 1 et 100, et le joueur doit deviner ce nombre. Le programme devrait donner des indices tels que "trop grand" ou "trop petit" jusqu'à ce que le joueur trouve le nombre correct.

# Module import permet de choisir un nombre aléatoire
from random import *

# Methode 1

def randomNumber():
    liste = []
    for i in range(1000):
    #  rading() permet de choisir un nbr aléatoire
     liste.append( randint(0, 100) )

    # sample permet de choisir un nbr dans une liste, tuple, ..
    jeu = sample(liste, 1)
    jeuResult = int(''.join(map(str, jeu)))
    print(jeuResult)

    player = int(input('A votre avis, quel elle le nombre ?'))

    if (player > jeuResult) :
       print("Trop grand !")

    else :
        print("Trop petit .. ")

randomNumber()    

# Methode 2 

nombre_correct = random.randint(1, 100)
tentative = 0

# utilisation de while

while True:
    tentative += 1
    guess = int(input("Devinez le nombre (entre 1 et 100) : "))

    if guess == nombre_correct:
        print("Bravo ! Vous avez deviné le nombre en", tentative, "tentatives.")
        break
    elif guess < nombre_correct:
        print("Trop petit. Essayez encore.")
    else:
        print("Trop grand. Essayez encore.")
