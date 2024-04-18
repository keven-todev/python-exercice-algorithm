# Exercice 4: Décorateurs
# Créez un décorateur qui mesure le temps d'exécution d'une fonction. Utilisez-le pour mesurer le temps d'exécution d'une fonction de votre choix.

import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Temps d'exécution : {end_time - start_time} secondes")
        return result
    return wrapper

# Exemple d'utilisation
@measure_execution_time
def example_function():
    time.sleep(2)

example_function()
