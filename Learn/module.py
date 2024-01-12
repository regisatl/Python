import math
nombres = [5, 10, 15, 20, 25]

def calculer_moyenne(nombres):
      somme = 0
      for nombre in nombres:
            somme += nombre
      return somme / len(nombres)
      
def calculer_volume_cone_droit(rayon, hauteur):
      return math.pi * rayon ** 2 * hauteur

def afficher_pair_impair():
      for nombre in nombres:
            if nombre % 2 == 0:
                  print(f"{nombre} est pair")
            else:
                  print(f"{nombre} est impair")