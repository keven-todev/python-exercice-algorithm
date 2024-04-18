# Exercice 2: Gestion d'exceptions avancée
# Créez une fonction qui ouvre un fichier, lit son contenu, et affiche le nombre de lignes. Gérez les exceptions de manière à ce que votre programme ne plante pas si le fichier n'existe pas.

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'existe pas.")
        return 0

# Exemple d'utilisation
file_path = 'exemple.txt'
line_count = count_lines(file_path)
print(f"Le nombre de lignes dans le fichier est : {line_count}")

