# Exercice 1: Manipulation avancée de listes
# Écrivez une fonction qui prend une liste en entrée et renvoie une nouvelle liste ne contenant que les éléments uniques de la liste d'origine, sans utiliser de boucle for.

origineList = ["a", "a", "b", "c", "d", "e", "e"]

# set() permet plusieurs choses, dans ce cas supprimer les doublons
origineList = list(set(origineList))
print(origineList)