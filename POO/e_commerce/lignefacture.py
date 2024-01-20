# LigneFacture : Une classe représentant une ligne dans la facture. Elle doit contenir un produit, une quantité et permettre de calculer le prix total de la ligne.

class LigneFacture:  # Définit une classe LigneFacture.
      def __init__(self, produit, quantite):  # Initialise la classe avec un produit et une quantité.
            self.produit = produit  # Attribut produit de la ligne de facture.
            self.quantite = quantite  # Attribut quantité de la ligne de facture.
            self.prix = produit.prix * quantite  # Attribut prix de la ligne de facture.
            self.total = self.prix  # Attribut total de la ligne de facture.

      def __str__(self): # Méthode pour convertir un objet LigneFacture en chaîne de caractères.
            return f"{self.produit.nom} : {self.quantite} x {self.prix} = {self.prix * self.quantite}"  # Affiche le produit, la quantité et le sous-total.
      
      def afficher_ligne(self):  # Méthode pour afficher la ligne de facture.
            print(f"{self.produit.nom} : {self.quantite} x {self.prix} = {self.prix * self.quantite}")  # Affiche le produit, la quantité et le sous-total.
            print(f"Total : {self.total} ***")  # Affiche le total de la ligne de facture.
