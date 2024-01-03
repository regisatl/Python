import random 

val_min = 10
val_max = 100

nombreMystere = random.randint(val_min, val_max)

essai = 1 
score = 100

loop = True

while loop :
      valeur_player = input (f"Veuillez entree une valeur comprise entre {val_min} et {val_max} !")

      valeur_int = int(valeur_player)

      if  valeur_int > nombreMystere :
            print("Plus grand que le nombre mystere")
            essai +=1
            score -= 10
      elif valeur_int < nombreMystere :
            print("Plus petit que le nombre mystere")
            essai +=1
            score -= 10
      else: 
            print(f"Félicitations à toi tu as trouvé le nombre mystere, le nombre mystère est : {valeur_int} ")
            print(f"Nombre d'essais : {essai}\nScore : {score}")
            loop = False