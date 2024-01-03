import random 

val_min = 10
val_max = 100

nombreMystere = random.randint(val_min, val_max)

essai = 1 
score = 100

NB_CHANCE = 10

loop = True

while loop :

      valeur_player = int(input (f"Veuillez entree une valeur comprise entre {val_min} et {val_max} !"))
    
      while valeur_player < val_min or valeur_player > val_max:
            print("La valeur entrée est hors de la plage autorisée.")
            valeur_player = int(input (f"Veuillez entree une valeur comprise entre {val_min} et {val_max} !"))

            valeur_int = int(valeur_player)
            
            if essai <= NB_CHANCE:
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
            else:
                  loop = False
                  print(f"Désolé vous avez déjà essayer le nombre maximale de tentative réquise, Le nombre mystères est: {nombreMystere}")