# Exercice 4: Traitement d'image
# Utilisez la bibliothèque OpenCV pour charger une image, appliquer un filtre de convolution personnalisé, puis enregistrez l'image résultante.

import cv2
import numpy as np

def apply_custom_filter(image_path):
    image = cv2.imread(image_path)

    # Définir un filtre de convolution personnalisé (exemple : flou)
    kernel = np.ones((5, 5), np.float32) / 25
    result_image = cv2.filter2D(image, -1, kernel)

    # Enregistrer l'image résultante
    cv2.imwrite('result_image.jpg', result_image)

# Exemple d'utilisation
image_path = 'input_image.jpg'
apply_custom_filter(image_path)
