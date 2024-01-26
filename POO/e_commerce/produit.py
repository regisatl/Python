class Produit:  # Définit une classe Produit.
      def __init__(self, nom, prix):  # Initialise la classe avec un id, un nom et un prix.
            self.nom = nom  # Attribut nom du produit.
            self.prix = prix  # Attribut prix du produit.
            
      def __iter__(self):
            return iter((self.nom, self.prix))

      # def __str__(self):  # Méthode pour convertir un objet Produit en chaîne de caractères.
      #       return f"{self.nom} - {self.prix}"  # Retourne la chaîne de caractères correspondant au produit.
