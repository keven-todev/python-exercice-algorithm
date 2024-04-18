# Exercice 3: Programmation orientée objet
# Définissez une classe "Personne" avec des attributs tels que le nom, l'âge, et la ville de résidence. Ajoutez une méthode pour afficher toutes les informations de la personne.

class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def afficher_informations(self):
        print(f"Nom: {self.nom}, Age: {self.age}, Ville: {self.ville}")

# Exemple d'utilisation
personne1 = Personne("Alice", 25, "Paris")
personne1.afficher_informations()
