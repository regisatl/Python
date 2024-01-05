# Demander à l'utilisateur d'entrer un entier strictement positif
nombre = int(input("Entrez un entier strictement positif : "))

# Initialiser une liste pour stocker les diviseurs propres
diviseurs = []

# Trouver les diviseurs propres du nombre
for i in range(1, nombre):
    if nombre % i == 0:
        diviseurs.append(i)

# Vérifier s'il y a des diviseurs propres et afficher le résultat
if len(diviseurs) > 0:
    print(
        f"Diviseurs propres sans répétition de {nombre} : {', '.join(map(str, set(diviseurs)))} (soit {len(diviseurs)} diviseurs propres)")
else:
    print(
        f"Diviseurs propres sans répétition de {nombre} : aucun ! Il est premier")
