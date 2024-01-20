import csv  # Importe le module csv pour lire et écrire des fichiers csv.
class Facture:  # Définit une classe Facture.
      def __init__(self, panier):  # Initialise la classe avec un panier.
            self.produits = panier.produits  # Attribut produits de la facture.
            self.total = panier.total  # Attribut total de la facture.
            self.prix_unitaire = self.total / len(self.produits)  # Attribut prix unitaire de la facture.
            self.prix_total = self.prix_unitaire * len(self.produits)  # Attribut prix total de la facture.
            self.file_csv = "facture.csv"  # Attribut nom de fichier de la facture.
            self.creer_fichier()  # Appelle la méthode creer_fichier pour créer un fichier csv.

      def __str__(self): # Méthode pour convertir un objet Facture en chaîne de caractères.
            return f"Total : {self.total}\nPrix unitaire : {self.prix_unitaire}\nPrix total : {self.prix_total}"  # Affiche le total, le prix unitaire et le prix total.

      def creer_fichier(self):  # Méthode pour créer un fichier csv.
            with open(self.file_csv, "a", encoding="utf-8", newline="") as fichier:  # Ouvre le fichier en mode écriture.
                writer = csv.writer(fichier)  # Crée un écrivain csv.
                writer.writerows(self.produits)  # Écrit les produits dans le fichier.
                writer.writerow([self.total, self.prix_unitaire, self.prix_total])  # Écrit le total, le prix unitaire et le prix total dans le fichier.
                print(f"Fichier {self.file_csv} créé avec succès")  # Affiche un message de succès.
                print(self.produits)  # Affiche les produits.
                print(self.total)  # Affiche le total.
                print(self.prix_unitaire)  # Affiche le prix unitaire.
            print(self.prix_total)  # Affiche le prix total.

      def afficher_facture(self):  # Méthode pour afficher la facture.
            with open(self.file_csv, newline="") as fichier:  # Ouvre le fichier en mode lecture.
                  reader = csv.reader(fichier)  # Crée un lecteur csv.
                  for ligne in reader:  # Pour chaque ligne dans le fichier.
                        print(ligne)  # Affiche la ligne.
