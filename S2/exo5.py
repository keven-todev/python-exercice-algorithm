# Exercice 5: Générateurs
# Écrivez une fonction génératrice qui génère les termes de la suite de Fibonacci jusqu'à un certain nombre donné.

def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Exemple d'utilisation
limit = 50
for num in fibonacci_generator(limit):
    print(num)
