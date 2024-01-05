def tapisserie(taille):
    for i in range(taille+1):
        for j in range(taille+1):
            if i == j or j == taille - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# Exemple d'appel de la fonction avec une taille de 10
tapisserie(10)
