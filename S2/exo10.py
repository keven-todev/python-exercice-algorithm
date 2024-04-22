# Exercice 10: Algorithmes avancés
# Implémentez un algorithme de tri avancé (comme le tri rapide ou le tri fusion) et testez-le sur une liste de nombres aléatoires.


# methode 1

def quicksort(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste.pop()

    petit = []
    grand = []

    for nombre in liste:
        if nombre < pivot:
            petit.append(nombre)
        else: 
            grand.append(nombre)  

    return quicksort(petit)+[pivot]+quicksort(grand)  

l = [3,1,2, 5, 10, 7]

print(quicksort(l))


# methode 2 + opti + moin de ligne

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


numbers = [3, 6, 8, 10, 1, 2, 1]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)

