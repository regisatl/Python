# Ce code est un jeu de devinettes où l’utilisateur doit deviner un nombre mystère. 
# Le nombre mystère est un nombre aléatoire entre val_min et val_max. 
# L’utilisateur a NB_CHANCE essais pour deviner le nombre. 
# À chaque essai, le programme donne un indice à l’utilisateur en lui disant si le nombre 
# qu’il a entré est plus grand ou plus petit que le nombre mystère. 
# Le jeu se termine lorsque l’utilisateur devine le nombre mystère ou lorsqu’il a épuisé tous ses essais. 
# J’espère que cela vous aide à comprendre le code. Si vous avez d’autres questions, n’hésitez pas à demander. 


import random  # Importe le module random pour générer des nombres aléatoires

val_min = 10 # Définit la valeur minimale de la plage de nombres
val_max = 100 # Définit la valeur maximale de la plage de nombres

nombreMystere = random.randint(val_min, val_max) # Génère un nombre aléatoire entre val_min et val_max

essai = 1  # Initialise le compteur d'essais à 1
score = 100 # Initialise le score à 100

NB_CHANCE = 10 # Définit le nombre maximum d'essais autorisés

loop = True # Initialise une variable booléenne pour contrôler la boucle while

while loop : # Tant que 'loop' est vrai,

      valeur_player = int(input (f"Veuillez entree une valeur comprise entre {val_min} et {val_max} !")) # Demande à l'utilisateur d'entrer un nombre

    
      while valeur_player < val_min or valeur_player > val_max: # Si le nombre entré par l'utilisateur est en dehors de la plage autorisée,
            print("La valeur entrée est hors de la plage autorisée.") # imprime un message d'erreur
            valeur_player = int(input (f"Veuillez entree une valeur comprise entre {val_min} et {val_max} !"))  # Demande à nouveau à l'utilisateur d'entrer un nombre

            valeur_int = int(valeur_player) # Convertit la valeur entrée par l'utilisateur en un entier
            
            if essai <= NB_CHANCE: # Si le nombre d'essais est inférieur ou égal au nombre maximum d'essais autorisés,

                  if  valeur_int > nombreMystere : # Si le nombre entré par l'utilisateur est supérieur au nombre mystère,
                        print("Plus grand que le nombre mystere") # imprime un indice
                        essai +=1 # Incrémente le compteur d'essais
                        score -= 10 # Décrémente le score
                        
                  elif valeur_int < nombreMystere : # Si le nombre entré par l'utilisateur est inférieur au nombre mystère,
                        print("Plus petit que le nombre mystere") # imprime un indice
                        essai +=1 # Incrémente le compteur d'essais
                        score -= 10 # Décrémente le score

                  else: # Si le nombre entré par l'utilisateur est égal au nombre mystère,
                        print(f"Félicitations à toi tu as trouvé le nombre mystere, le nombre mystère est : {valeur_int} ")  # Félicite l'utilisateur
                        print(f"Nombre d'essais : {essai}\nScore : {score}") # Imprime le nombre d'essais et le score
                        loop = False # Met fin à la boucle while

            else: # Si le nombre d'essais dépasse le nombre maximum d'essais autorisés,
                  loop = False # Met fin à la boucle while
                  print(f"Désolé vous avez déjà essayer le nombre maximale de tentative réquise, Le nombre mystères est: {nombreMystere}") # Imprime un message indiquant que l'utilisateur a dépassé le nombre maximum d'essais autorisés et révèle le nombre mystère