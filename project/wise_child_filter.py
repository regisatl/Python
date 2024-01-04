"""
Objectif : Categorisé les enfant pour voir s'il ont droit a un cadeaux ou non
Condition de validité :
      -
      - age max égale à 18 ans
      - avoir été sage les 12 derniers mois

Variables :
      - nom : (str) le nom de l'enfant 
      - age : (int) l'âge de l'enfant
      - sage : (bool) sage ou non

Sortie : 
      - (str) Félicitation nom_de_l'enfant tu as été sage, le père Noël attend impatiemment ta lettre 
      - (str) Désolé nom_de_l'enfant tu n'as pas été sage cette abbéen papa Noël n'est pas content de toi

"""

nom = "" 
age = 9
sage = False

if age <= 10 and sage == True :
      print(f"Félicitation {nom} tu as été sage, le père Noël attend impatiemment ta lettre")
else : 
      print(f"Désolé {nom} tu n'as pas été sage cette abbéen papa Noël n'est pas content de toi")