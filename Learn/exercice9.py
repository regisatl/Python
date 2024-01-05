def est_palindrome(mot):
    mot = mot.lower()  # Convertir le mot en minuscules
    return mot == mot[::-1]


# Exemple d'appel de la fonction
resultat = est_palindrome("radar")
print(resultat)  # Cela affichera True
resultat = est_palindrome("python")
print(resultat)  # Cela affichera False
