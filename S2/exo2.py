# Exercice 2: Gestion d'exceptions avancée
# Créez une fonction qui ouvre un fichier, lit son contenu, et affiche le nombre de lignes. Gérez les exceptions de manière à ce que votre programme ne plante pas si le fichier n'existe pas.


# methode 1

# open permet d'ouvrir un fichier //  'r' veut dire read
file_path = open( 'exemple.txt','r' )  

# readlines() lis les lignes
contenu = file_path.readlines()

count = 0   
for n in contenu:
    count+=1

print(count)

# METHODE 2 ( à corriger ) 
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'existe pas.")
        return 0
