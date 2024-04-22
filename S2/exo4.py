# Exercice 4: Décorateurs
# Créez un décorateur qui mesure le temps d'exécution d'une fonction. Utilisez-le pour mesurer le temps d'exécution d'une fonction de votre choix.

import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
      
        # Fonction interne qui enveloppe la fonction d'origine.
        
        # Args:
            # *args: Arguments positionnels de la fonction d'origine.// nommage uni
            # **kwargs: Arguments nommés de la fonction d'origine. // nommage uni
            
        # Returns:
            # Tout: Résultat de l'appel de la fonction d'origine.
       
        start_time = time.time()  # Enregistre le temps de début d'exécution
        result = func(*args, **kwargs)  # Appelle la fonction d'origine avec les arguments
        end_time = time.time()  # Enregistre le temps de fin d'exécution
        # Affiche le temps écoulé en soustrayant le temps de fin par le temps de début
        print(f"Temps d'exécution : {end_time - start_time} secondes")
        return result  # Retourne le résultat de l'appel initial à la fonction d'origine
    
    return wrapper  # Retourne la fonction interne wrapper, maintenant décorée

