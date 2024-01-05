def calcul_volume_cone(rayon, hauteur):
    volume = (1/3) * 3.14159 * (rayon ** 2) * hauteur
    return volume


# Exemple d'appel de la fonction
rayon = 5
hauteur = 10
volume = calcul_volume_cone(rayon, hauteur)
print(volume)  # Cela affichera le volume calculé
