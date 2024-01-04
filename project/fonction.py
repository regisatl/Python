

def hello (name, age = None) :
      result = None
      if age : 
            result = f"Bonjour {name} vous avez {age} ans ! "
      else : 
            result = f"Bonjour {name} "
      return result

hello("ted", 23) # Passage ordonné

hello(name ="ted", age = 23) # Passage Nommé

ferenc = {"name" : "ferenc", "age": 23}

hello(**ferenc)

regis = ("Régis", 23) # / regis = ["Régis", 23]
hello(*regis) # unpacking