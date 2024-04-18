# Exercice 6: Manipulation de fichiers JSON
# Créez un programme qui lit un fichier JSON contenant des données sur des étudiants (nom, notes, etc.) et affiche la moyenne de chaque étudiant.

import json

def calculate_student_average(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for student in data['students']:
        name = student['name']
        grades = student['grades']
        average = sum(grades) / len(grades)
        print(f"{name}'s average grade: {average}")

# Exemple d'utilisation
file_path = 'students_data.json'
calculate_student_average(file_path)
