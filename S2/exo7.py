# Exercice 7: Programmation fonctionnelle
# Utilisez la programmation fonctionnelle pour écrire une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle liste avec le carré de chaque nombre impair.

def square_of_odd_numbers(numbers):
    return list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))

# Exemple d'utilisation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = square_of_odd_numbers(numbers)
print(result)
