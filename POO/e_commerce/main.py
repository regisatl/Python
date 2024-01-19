
import mysql.connector
from mysql.connector import Error

# Produit : Une classe représentant un produit avec les attributs id, nom, et prix.

class Produit:
      def __init__(self, id, nom, prix):
            self.id = id
            self.nom = nom
            self.prix = prix

# BaseDeDonnees : Une classe pour gérer la connexion à la base de données en MySQL. Elle doit avoir des méthodes pour exécuter des requêtes SQL et récupérer les résultats.
class BaseDeDonnees:
      def __init__(self, host, user, password, database):
            self.host = host
            self.user = user
            self.password = password
            self.database = database

      def create_connection(self):
            connection = None
            try:
                  connection = mysql.connector.connect(
                        host=self.host,
                        user=self.user,
                        password=self.password,
                        database=self.database
            )
                  print("Connection to database successful")
            except Error as e:
                  print(f"The error '{e}' occurred")
            return connection

      def execute_query(self, query):
            connection = self.create_connection()
            cursor = connection.cursor()
            try:
                  cursor.execute(query)
                  result = cursor.fetchall()
                  return result
            except Error as e:
                  print(f"The error '{e}' occurred")
            finally:
                  cursor.close()
                  connection.close()