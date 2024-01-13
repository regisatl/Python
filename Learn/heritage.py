class Animal:
      def __init__(self, nom, age):
            self.nom = nom
            self.age = age

      def manger(self):
            print(f"{self.nom} mange.")

class Analyst:
    def analyser(self):
        print(f"{self.nom} est un analyst.")

class Tacticien:
    def tactique(self):
        print(f"{self.nom} est un Tacticien.")

class Soldat(Animal, Analyst, Tacticien):
    def __init__(self, nom, age):
        super().__init__(nom, age)

soldat = Soldat("John", 25)
soldat.manger()
soldat.analyser()
soldat.tactique()