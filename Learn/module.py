nombres = [5, 10, 15, 20, 25]

def calculer_moyenne(nombres):
      somme = 0
      for nombre in nombres:
            somme += nombre
      return somme / len(nombres)
      
moyenne = calculer_moyenne(nombres)
print(f"La moyenne est : {moyenne} ")