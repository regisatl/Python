import mysql.connector  # Importe le module mysql.connector pour se connecter à une base de données MySQL.
from mysql.connector import Error  # Importe la classe Error du module mysql.connector pour gérer les erreurs.

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

      def create_table(self, table_name, columns): # Méthode pour créer une table dans la base de données.
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

      def insert_table(self, table_name, columns, values): # Méthode pour insérer dans une table des données dans la base de données avec la commande INSERT INTO
            try:  # Essaie d'exécuter le bloc de code suivant.
                  self.execute_query(f"CREATE DATABASE IF NOT EXISTS e_commerce")  # Crée une base de données si elle n'existe pas.
                  self.cnx.database = "e_commerce"  # Sélectionne la base de données.
                  mycursor = self.cnx.cursor()  # Crée un nouveau curseur.
                  mycursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")  # Crée une table si elle n'existe pas.
            except Error as e:  # Si une erreur est survenue lors de la création de la table.
                  print(f"Erreur lors de l'ajout des données dans la table : {e}")  # Affiche un message d'erreur.
            
      def update_table(self, table_name, columns, values, condition): # Méthode pour mettre à jour dans une table des données dans la base de données avec la commande UPDATE SET
            try:  # Essaie d'exécuter le bloc de code suivant.
                  self.execute_query(f"CREATE DATABASE IF NOT EXISTS e_commerce")  # Crée une base de données si elle n'existe pas.
                  self.cnx.database = "e_commerce"  # Sélectionne la base de données.
                  mycursor = self.cnx.cursor()  # Crée un nouveau curseur.
                  mycursor.execute(f"UPDATE {table_name} SET {columns} = {values} WHERE {condition}")  # Crée une table si elle n'existe pas.
            except Error as e:  # Si une erreur est survenue lors de la création de la table.
                  print(f"Erreur lors de la mise à jour des données dans la table : {e}")  # Affiche un message d'erreur.
                  
      def drop_table(self, table_name): # Méthode pour supprimer une table dans la base de données avec la commande DROP TABLE
            try:  # Essaie d'exécuter le bloc de code suivant.
                  self.execute_query(f"CREATE DATABASE IF NOT EXISTS e_commerce")  # Crée une base de données si elle n'existe pas.
                  self.cnx.database = "e_commerce"  # Sélectionne la base de données.
                  mycursor = self.cnx.cursor()  # Crée un nouveau curseur.
                  mycursor.execute(f"DROP TABLE {table_name}")  # Crée une table si elle n'existe pas.
            except Error as e:  # Si une erreur est survenue lors de la création de la table.
                  print(f"Erreur lors de la suppression de la table : {e}")  # Affiche un message d'erreur.
