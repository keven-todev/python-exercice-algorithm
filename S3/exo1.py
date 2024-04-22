# Exercice 1: Programmation dynamique
# Implémentez une fonction récursive qui calcule le nombre de façons de monter un escalier de n marches, sachant que vous pouvez monter 1, 2, ou 3 marches à la fois.

# methode 1 basé sur un algo itératif sur la suite de Fibonacci
def escalier(n):
    # Initialisation des variables a, b et c à 1, car il y a une seule façon de monter 0 ou 1 marche.
    a, b, c = 1, 1, 1

    # Utilisation de la récursivité pour calculer le nombre de façons de monter l'escalier.
    for i in range(2, n + 1):
        # Calcul du nombre de façons de monter les escaliers en utilisant des pas de 1, 2 ou 3 marches.
        # À chaque itération, la variable c contient le nombre de façons de monter les i premières marches.
        c = a + b
        # Mise à jour des variables a, b et c pour la prochaine itération.
        a, b = b, c
    
    # À la fin de la boucle, c contient le nombre total de façons de monter l'escalier de n marches.
    return c

# Boucle for pour tester la fonction escalier pour différentes valeurs de n.
for i in range(0, 14):
    # Affichage du résultat avec le nombre de façons de monter i marches.
    print("escalier {0} : {1} façons de monter".format(i, escalier(i)))



# methode 2 de manière récursive

def ways_to_climb_stairs(n):
    if n < 0:
        return 0  # Si le nombre de marches est négatif, il n'y a pas de façon de monter les escaliers
    elif n == 0:
        return 1  # Si le nombre de marches est 0, il n'y a qu'une façon de monter les escaliers (ne pas bouger)
    elif n == 1:
        return 1  # Si le nombre de marches est 1, il n'y a qu'une façon de monter les escaliers (monter une marche)
    elif n == 2:
        return 2  # Si le nombre de marches est 2, il y a deux façons de monter les escaliers (monter une ou deux marches)
    else:
        # Sinon, on calcule le nombre de façons de monter les escaliers en ajoutant les façons de monter les escaliers
        # avec des pas de 1, 2 et 3 marches à partir des façons de monter les escaliers avec n-1, n-2 et n-3 marches.
        return ways_to_climb_stairs(n - 1) + ways_to_climb_stairs(n - 2) + ways_to_climb_stairs(n - 3)

# Exemple d'utilisation
num_stairs = 14
print("Pour", num_stairs, "marches, il y a", ways_to_climb_stairs(num_stairs), "façons de monter.")

