# Liste des nombres premiers:
# Écrivez un programme qui génère une liste des nombres premiers jusqu'à un certain nombre donné.



limite = int(input("Entrez une limite : "))

# on utilise la "liste comprehension" ça permet d'optimiser le code, de le rendre plus visible et moins gros contrairement à la méthode 2

nombres_premiers = [num for num in range(2, limite) if all(num % i != 0 for i in range(2, int(num**0.5)))]

# Deuxième méthode, c'est la méthode une sans la liste comprehension
nombre_premier = []

for num in range(2, limite+1):
    if all(num %i != 0 for i in range(2, int(num**0.5))):
        nombre_premier.append(num)
print("Nombres premiers jusqu'à", limite, ":", nombre_premier)


# /////////////////////////

# list comprehension 

# range() => https://www.w3schools.com/python/ref_func_range.asp

# all() => returns True if all items in an iterable are true, otherwise it returns False.




        