def nombre_chiffres(nombre, chiffre):
    return str(nombre).count(str(chiffre))


# Exemple d'appel de la fonction
resultat = nombre_chiffres(123456789, 5)
print(resultat)  # Cela affichera 1
