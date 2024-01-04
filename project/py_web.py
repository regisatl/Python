
age = 50

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

if 0 <= age <= 5 : # Bébé 0
      print("Bienvenue dans l'interface Bébé !")
      for item in content :
            if item[2] <= 0 :
                  print(f"{item[0]} de {item[1]}")
elif 6 <= age <= 12 : # Enfant 1
      print("Bienvenue dans l'interface Enfant !")
      for item in content :
            if item[2] <= 1 :
                  print(f"{item[0]} de {item[1]}")
elif 13 <=  age <= 18 : # Adolescent 2
      print("Bienvenue dans l'interface Ado !")
      for item in content :
            if item[2] <= 2 :
                  print(f"{item[0]} de {item[1]}")
elif 19 <= age <= 50 : # Adulte 3
      print("Bienvenue dans l'interface Adulte !")
      for item in content :
            if item[2] <= 4 :
                  print(f"{item[0]} de {item[1]}")
else : # Sénior
      print("Bienvenue dans l'interface Sénioir")
      for item in content :
            if item[2] <= 3 :
                  print(f"{item[0]} de {item[1]}")