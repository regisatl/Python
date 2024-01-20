# Panier : Une classe représentant le panier de l'utilisateur. Elle doit permettre d'ajouter des produits avec la quantité et de calculer le total.
class Panier:  # Définit une classe Panier.
      def __init__(self):  # Initialise la classe.
            self.produits = []  # Attribut produits du panier.
            self.total = 0  # Attribut total du panier.

      def ajouter_produit(self, produit, quantite):      # Méthode pour ajouter un produit au panier.
            self.produits.append((produit, quantite))  # Ajoute le produit et la quantité au panier.
            self.total += produit.prix * quantite  # Met à jour le total du panier.

      def afficher_panier(self):  # Méthode pour afficher le contenu du panier.
            for (produit, quantite) in self.produits:  # Pour chaque produit et quantité dans le panier.
                print(f"{produit.nom} : {quantite} x {produit.prix} = {produit.prix * quantite}")  # Affiche le produit, la quantité et le sous-total.
                print(f"Total : {self.total}***")  # Affiche le total du panier.
