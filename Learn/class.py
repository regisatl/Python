class Chien:
      def __init__(self, nom, age):
            self.nom = nom
            self.age = age
      
      def aboyer(self):
            print(self.nom + " a aboyer")
            
# création d'un objet de la classe Chien
bob = Chien("Bob", 30)
print(bob)