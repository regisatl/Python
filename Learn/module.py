import math
import random

nombres = [5, 10, 15, 20, 25]
def calculer_moyenne(nombres):
      somme = 0
      for nombre in nombres:
            somme += nombre
      return somme / len(nombres)

# rayon = int(input("Veuillez entrer le rayon de votre cône s'il vous plaît : "))
# hauteur = int(input("Veuillez entrer la hauteur de votre cône s'il vous plaît : "))
def calculer_volume_cone_droit(rayon, hauteur):
      return math.pi * rayon ** 2 * hauteur

# nombre_utilisateur = int(input("Veuillez entrer votre nombre s'il vous plaît: "))
def afficher_pair_impair(nombre_utilisateur):
      if nombre_utilisateur % 2 == 0:
            return nombre_utilisateur, 'est pair'
      else:
            return nombre_utilisateur, 'est impair'
            
start = int(input("Veuillez entrer la valeur de départ s'il vous plaît : "))
end = int(input("Veuillez entrer la valeur de fin s'il vous plaît : "))
def nombre_aleatoire(start, end):
      return random.randint(start, end)