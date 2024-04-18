# Exercice 1: Programmation dynamique
# Implémentez une fonction récursive qui calcule le nombre de façons de monter un escalier de n marches, sachant que vous pouvez monter 1, 2, ou 3 marches à la fois.

def ways_to_climb_stairs(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        return ways_to_climb_stairs(n - 1) + ways_to_climb_stairs(n - 2) + ways_to_climb_stairs(n - 3)

# Exemple d'utilisation
num_stairs = 4
print(ways_to_climb_stairs(num_stairs))
