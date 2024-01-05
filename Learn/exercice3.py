# Initialiser les variables
sumNombrePositif = 0
count = 0
countOver100 = 0
loop = True 

while loop :
      valueEnter = int(input("Veuillez entrer une valeur positif ou nul (Veuilez entrer une valeur négatif pour terminer) : "))
      if valueEnter <= 0 :
            print("Vous venez d'entrer une valeur négative : Fin du programme")
            loop = False
      sumNombrePositif += valueEnter
      count += 1
      if valueEnter > 100 :
            print("Vous venez d'entrer une valeur supérieure à 100 ")
            countOver100 += 1

print(f"La somme des nombres positifs est : {sumNombrePositif}")
print(f"Le nombre total de données est : {count}")
print(f"Le nombre de données supérieures à 100 est : {countOver100}")

