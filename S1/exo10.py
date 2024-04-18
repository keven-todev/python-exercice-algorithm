# Jeu du devine le nombre:
# Créez un jeu où l'ordinateur choisit un nombre aléatoire entre 1 et 100, et le joueur doit deviner ce nombre. Le programme devrait donner des indices tels que "trop grand" ou "trop petit" jusqu'à ce que le joueur trouve le nombre correct.

import random

nombre_correct = random.randint(1, 100)
tentative = 0

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
