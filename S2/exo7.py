# Exercice 7: Programmation fonctionnelle
# Utilisez la programmation fonctionnelle pour écrire une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle liste avec le carré de chaque nombre impair.


# methode 1
def calculate():
    list_Number = [1,2,3,4,5,6,7,8,9,10]
    newList = []

    for i in list_Number:
        if i % 2 != 0 and i < len(list_Number):
             number = i ** 2
             newList.append(number)
    
    return newList

    

result = calculate()
print(result)
