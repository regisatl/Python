# Initialiser les variables
sumNombrePositif = 0
counter = 0
counterOver100 = 0
loop = True 

while loop :
      valueEnter = int(input("Veuillez entrer une valeur positif ou nul (Veuilez entrer une valeur négatif pour terminer) : "))
      if valueEnter <= 0 :
            print("Vous venez d'entrer une valeur négative : Fin du programme")
            loop = False
      sumNombrePositif += valueEnter
      counter += 1
      if valueEnter > 100 :
            print("Vous venez d'entrer une valeur supérieure à 100 ")
            counterOver100 += 1

print(f"La somme des nombres positifs est : {sumNombrePositif}")
print(f"Le nombre total de données est : {counter}")
print(f"Le nombre de données supérieures à 100 est : {counterOver100}")

