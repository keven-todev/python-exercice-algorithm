# Exercice 1: Manipulation avancée de listes
# Écrivez une fonction qui prend une liste en entrée et renvoie une nouvelle liste ne contenant que les éléments uniques de la liste d'origine, sans utiliser de boucle for.

def unique_elements(input_list):
    return list(set(input_list))

# Exemple d'utilisation
original_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(original_list)
print(result)