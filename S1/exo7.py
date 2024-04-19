# Inversion d'une chaîne de caractères:
# Écrivez un programme qui prend une chaîne de caractères en entrée et affiche sa version inversée.

# méthode slicing

foo = input('Que voulez vous dires ?')
fooreversed = foo[::-1]

# fonction reversed

foo = input('Que voulez vous dire ?')
fooreversed = ''.join(reversed(foo))

# fonction personnalisée

chaine = input('Quel est le mot du jour ?')

def inverser_chaine(chaine):
    chaine_inverse = ""
    for caractere in chaine:
        chaine_inverse = caractere + chaine_inverse
    return chaine_inverse

print(inverser_chaine(chaine))

