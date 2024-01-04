"""

boissons = [(name, age_min)]
repas = [(nom, (heure_min, heure_max), age_min)]

"""

plats = [
    ("Pizza", (0, 23), 10),
    ("Hamburger", (7, 22), 8),
    ("Riz", (0, 23), 5),
    ("Spagueti blanc", (11, 19), 0),
    ("Salade de Fruit", (0, 23), 0),
    ("Salade simple", (15, 23), 4),

    ("Cafe", (6, 16), 16),
    ("Expresso", (6, 14), 19),
    ("Cappucino", (6, 16), 16),
    
    ("Soupe au legume", (18, 23), 0),
    ("Soupe de boeuf", (16, 21), 10)
]

boissons = [
    ("Coca cola", 10),
    ("Lait", 0),
    ("Jus Naturel de Mange", 2),
    ("Sprite", 10),
    ("Jack Danniels", 19),
    ("Champagne",25),
]

age = 22
heure = 10

print()

print("---------------------Le Menu Du Jour---------------------")

for plat in plats:
      if age >= plat[2]:
            print(plat[0])

print()
print("---------------------Les boissons Du Jour---------------------")

for boisson in  boissons:
      if age >=  boisson[1]:
            print( boisson[0])