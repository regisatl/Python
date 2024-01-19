import csv  # Importe le module csv pour lire et écrire des fichiers csv.
import mysql.connector  # Importe le module mysql.connector pour se connecter à une base de données MySQL.
from mysql.connector import Error  # Importe la classe Error du module mysql.connector pour gérer les erreurs.

class Produit:  # Définit une classe Produit.
      def __init__(self, id, nom, prix):  # Initialise la classe avec un id, un nom et un prix.
            self.id = id  # Attribut id du produit.
            self.nom = nom  # Attribut nom du produit.
            self.prix = prix  # Attribut prix du produit.

      def __str__(self):  # Méthode pour convertir un objet Produit en chaîne de caractères.
            return f"{self.id} - {self.nom} - {self.prix}"  # Retourne la chaîne de caractères correspondant au produit.

class BaseDeDonnees:  # Définit une classe BaseDeDonnees.
      def __init__(self, host="localhost", user="root", password=""):  # Initialise la classe avec un hôte, un utilisateur et un mot de passe.
            self.host = host  # Attribut hôte de la base de données.
            self.user = user  # Attribut utilisateur de la base de données.
            self.password = password  # Attribut mot de passe de la base de données.
            self.connect()  # Appelle la méthode connect pour se connecter à la base de données.

      def connect(self):  # Méthode pour se connecter à la base de données.
            try:  # Essaie d'exécuter le bloc de code suivant.
                  self.cnx = mysql.connector.connect(host=self.host, user=self.user, password=self.password)  # Crée une connexion à la base de données.
                  self.cursor = (self.cnx.cursor())  # Crée un curseur pour exécuter des requêtes SQL.
                  print("Connexion à la base de données réussie.")  # Affiche un message de connexion réussie.
            except Error as e:  # Si une erreur est survenue lors de la connexion à la base de données.
                  print(f"Erreur lors de la connexion à la base de données : {e}")  # Affiche un message d'erreur.
            
      def close(self):  # Méthode pour fermer la connexion à la base de données.
            if (self.cnx.is_connected()):  # Si la connexion à la base de données est ouverte.
                  self.cursor.close()  # Ferme le curseur.
                  self.cnx.close()  # Ferme la connexion à la base de données.
                  print("MySQL connection is closed")  # Affiche un message indiquant que la connexion à la base de données est fermée.

      def execute_query(self, query):  # Méthode pour exécuter une requête SQL.
            try:  # Essaie d'exécuter le bloc de code suivant.
                  mycursor = self.cnx.cursor()  # Crée un nouveau curseur.
                  mycursor.execute(query)  # Exécute la requête SQL.
                  self.cnx.commit()  # Valide les modifications dans la base de données.
                  print("Requête SQL exécutée avec succès.")  # Affiche un message de requête SQL exécutée avec succès.
            except Error as e:  # Si une erreur est survenue lors de l'exécution de la requête SQL.
                  print(f"Erreur lors de l'exécution de la requête SQL : {e}")  # Affiche un message d'erreur.

      def create_table(self, table_name, columns):      # Méthode pour créer une table dans la base de données.
            try:  # Essaie d'exécuter le bloc de code suivant.
                  self.execute_query(f"CREATE DATABASE IF NOT EXISTS e_commerce")  # Crée une base de données si elle n'existe pas.
                  self.cnx.database = "e_commerce"  # Sélectionne la base de données.
                  mycursor = self.cnx.cursor()  # Crée un nouveau curseur.
                  mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")  # Crée une table si elle n'existe pas.
            except Error as e:  # Si une erreur est survenue lors de la création de la table.
                  print(f"Erreur lors de la création de la table : {e}")  # Affiche un message d'erreur.
            
            query = f"CREATE TABLE {table_name} ("  # Débute la requête SQL pour créer une table.
            for column in columns:  # Pour chaque colonne dans la liste des colonnes.
                query += column + ", "  # Ajoute la colonne à la requête SQL.
            query = (
                query[:-2] + ")"
            )  # Enlève la dernière virgule et ajoute une parenthèse fermante.
            mycursor.execute(query)  # Exécute la requête SQL.
            self.cnx.commit()  # Valide les modifications dans la base de données.

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

# LigneFacture : Une classe représentant une ligne dans la facture. Elle doit contenir un produit, une quantité et permettre de calculer le prix total de la ligne.

class LigneFacture:  # Définit une classe LigneFacture.
      def __init__(self, produit, quantite):      # Initialise la classe avec un produit et une quantité.
            self.produit = produit  # Attribut produit de la ligne de facture.
            self.quantite = quantite  # Attribut quantité de la ligne de facture.
            self.prix = produit.prix * quantite  # Attribut prix de la ligne de facture.
            self.total = self.prix  # Attribut total de la ligne de facture.

      def afficher_ligne(self):  # Méthode pour afficher la ligne de facture.
            print(f"{self.produit.nom} : {self.quantite} x {self.prix} = {self.prix * self.quantite}")  # Affiche le produit, la quantité et le sous-total.
            print(f"Total : {self.total} ***")  # Affiche le total de la ligne de facture.


class Facture:  # Définit une classe Facture.
      def __init__(self, panier):  # Initialise la classe avec un panier.
            self.produits = panier.produits  # Attribut produits de la facture.
            self.total = panier.total  # Attribut total de la facture.
            self.prix_unitaire = self.total / len(self.produits)  # Attribut prix unitaire de la facture.
            self.prix_total = self.prix_unitaire * len(self.produits)  # Attribut prix total de la facture.
            self.file_csv = "facture.csv"  # Attribut nom de fichier de la facture.
            self.creer_fichier()  # Appelle la méthode creer_fichier pour créer un fichier csv.

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
            with open(self.nom_fichier, newline="") as fichier:  # Ouvre le fichier en mode lecture.
                  reader = csv.reader(fichier)  # Crée un lecteur csv.
                  for ligne in reader:  # Pour chaque ligne dans le fichier.
                        print(ligne)  # Affiche la ligne.


if __name__ == "__main__":  # Si le script est exécuté directement (et non importé).
      
      bd = BaseDeDonnees(host="localhost", user="root", password="")  # Crée un objet de la classe BaseDeDonnees. Remplacez par vos informations d'identification.
      
      bd.create_table("produits", "id INTEGER PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(50), prix INTEGER")  # Crée la table produits.
      print("Table produits créée avec succès")  # Affiche un message indiquant que la table produits a été créée avec succès.
      
      bd.create_table("facture", "id INTEGER PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(50), prix INTEGER")  # Crée la table facture.
      print("Table facture créée avec succès")  # Affiche un message indiquant que la table facture a été créée avec succès.
      
      bd.create_table("panier", "id INTEGER PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(50), prix INTEGER")  # Crée la table panier.
      print("Table panier créée avec succès")  # Affiche un message indiquant que la table panier a été créée avec succès.
      
      bd.create_table("lignefacture", "id INTEGER PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(50), prix INTEGER")  # Crée la table lignefacture.
      print("Table lignefacture créée avec succès")  # Affiche un message indiquant que la table lignefacture a été créée avec succès.
      

      bd.close()  # Ferme la connexion à la base de données.
      print("Base de données créée avec succès")  # Affiche un message indiquant que la base de données a été créée avec succès.

      # Création de quelques produits
      produit1 = Produit(1, "Produit 1", 10)
      produit2 = Produit(2, "Produit 2", 20)

      # Ajout des produits au panier
      panier = Panier()
      panier.ajouter_produit(produit1, 2)
      panier.ajouter_produit(produit2, 3)
      panier.afficher_panier()

      # Création d'une ligne de facture
      ligne = LigneFacture(produit1, 2)
      ligne.afficher_ligne()

      # Création d'une facture à partir du panier
      facture = Facture(panier)
      facture.afficher_facture()      