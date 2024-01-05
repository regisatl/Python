# Calcul du nombre de grains à déposer sur chacune des 64 cases du jeu
total_grains = 0
for i in range(64):
    grains_on_current_square = 2**i
    total_grains += grains_on_current_square
    print(f"Case {i+1}: {grains_on_current_square} grains")

# Affichage du nombre total de grains en notation scientifique
print(
    f"Le nombre total de grains en notation scientifique est : {total_grains:.2e}")
