# class Animal:
#     def __init__(self, nom, age):
#         self.nom = nom
#         self.age = age

#     def se_presenter(self):
#         print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")

# class Chien(Animal):
#     def __init__(self, nom, age, race):
#         super().__init__(nom, age)
#         self.race = race

#     def se_presenter(self):
#         super().se_presenter()
#         print(f"Je suis un chien de race {self.race}.")

# chien = Chien("Rex", 3, "Berger Allemand")
# chien.se_presenter()

class Animal:
      def __init__(self, nom, age):
            self.nom = nom
            self.age = age

      def manger(self):
            print(f"{self.nom} mange.")

class Chien(Animal):
      def __init__(self, nom, age):
            super().__init__(nom, age)

      def aboyer(self):
            print(f"{self.nom} aboie.")

class Chat(Animal):
      def __init__(self, nom, age):
            super().__init__(nom, age)

      def miauler(self):
            print(f"{self.nom} miaule.")

mon_animal = Chat("chien", 3)
mon_animal.miauler()
# mon_animal.aboyer()