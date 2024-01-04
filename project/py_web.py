
age = 5 # Définit l'âge de l'utilisateur

# Crée une liste de tuples, chaque tuple contenant un titre, un auteur et un niveau d'âge
content = [
    ("Rockaby baby", "UNKNOW", 0),
    ("Eignhties Baby", "Jammy Jams", 0),
    ("Babies go Beaties", "UNKNOW", 0),
    ("Le Voyage de chihiro", "Hayao Miyazaki", 1),
    ("Le Roi Lion", "Roger Allers et Rob Minkoff", 1),
    ("Aladin", "John Musker et Ron Clements", 1),
    ("One Piece", "Eiichiro Oda", 2),
    ("Death Note", "Tsugumi Ôba", 2),
    ("Fullmetal Alchemist", "Hiromu Arakawa", 2),
    ("OSS 117", "Michel Hazanavicius", 2),
    ("The Descent", "Neil Marshall", 4),
    ("La Ligne Rouge", "Terrence Malick", 4),
    ("Voyage au bout de l'enfer", "Michael Cimino", 3),
    ("Persuasion", "Carrie Cracknell", 3),
    ("Book of Love", "Analeine Cal y Mayor", 4),
]

# Selon l'âge de l'utilisateur, le code affiche un message de bienvenue approprié et parcourt la liste de contenu

if 0 <= age <= 5 : # Bébé 0  Si l'utilisateur est un bébé (0-5 ans)
      print("********************Bienvenue dans l'interface Bébé !********************")

      for item in content : # Parcourt chaque élément de la liste de contenu
            if item[2] <= 0 :  # Si le niveau d'âge de l'élément est approprié pour un bébé,
                  if not item[1] == "UNKNOW" :
                        print(f"{item[0]} de {item[1]}") # imprime le titre et l'auteur de l'élément
                  else : 
                        print(f"{item[0]}") # imprime uniquement le titre de l'élément

elif 6 <= age <= 12 : # Enfant 1 Si l'utilisateur est un enfant (6-12 ans)
      print("**************************Bienvenue dans l'interface Enfant !**************************")
      for item in content : 
            if item[2] <= 1 : # Si le niveau d'âge de l'élément est approprié pour un enfant,
                  print(f"{item[0]} de {item[1]}")

elif 13 <=  age <= 18 : # Adolescent 2 Si l'utilisateur est un adolescent (13-18 ans)
      print("**************************Bienvenue dans l'interface Ado !**************************")
      for item in content : 
            if item[2] <= 2 : # Si le niveau d'âge de l'élément est approprié pour un adolescent,
                  print(f"{item[0]} de {item[1]}")

elif 19 <= age <= 50 : # Adulte 3 Si l'utilisateur est un adulte (19-50 ans)
      print("**************************Bienvenue dans l'interface Adulte !**************************")
      for item in content :
            if item[2] <= 4 : # Si le niveau d'âge de l'élément est approprié pour un adulte,
                  print(f"{item[0]} de {item[1]}")

else : # Sénior Si l'utilisateur est un senior (plus de 50 ans)
      print("**************************Bienvenue dans l'interface Sénior**************************")
      for item in content :
            if item[2] <= 3 : # Si le niveau d'âge de l'élément est approprié pour un senior,
                  print(f"{item[0]} de {item[1]}")