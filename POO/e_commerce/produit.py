class Produit:  # Définit une classe Produit.
      def __init__(self, id, nom, prix):  # Initialise la classe avec un id, un nom et un prix.
            self.id = id  # Attribut id du produit.
            self.nom = nom  # Attribut nom du produit.
            self.prix = prix  # Attribut prix du produit.

      def __str__(self):  # Méthode pour convertir un objet Produit en chaîne de caractères.
            return f"{self.id} - {self.nom} - {self.prix}"  # Retourne la chaîne de caractères correspondant au produit.
