

def hello (name, age) :
      print(f"Bonjour {name}, Vous avez {age} !")

hello("ted", 23)

regis = ("Régis", 23)
hello(*regis) # unpacking