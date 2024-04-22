# Exercice 6: Manipulation de fichiers JSON
# Créez un programme qui lit un fichier JSON contenant des données sur des étudiants (nom, notes, etc.) et affiche la moyenne de chaque étudiant.

import json 
# spécifier le chemin exact du fichier
import os 


def calculate_moy():
        # os fonctionnement
        json_file = os.path.join(os.path.dirname(__file__), "data.json")

        # ouverture du fichier
        with open(json_file, 'r') as file:
         data = json.load(file)

        for student in data['students']:
            name = student['name']
            grades = student['grades']
        print(f"{name}'s average grade: {grades}")
        print(data.items())


calculate_moy()
