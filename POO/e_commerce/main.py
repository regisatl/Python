import mysql.connector

# Produit : Une classe représentant un produit avec les attributs id, nom, et prix.
class Produit:
    def __init__(self, id, nom, prix):
        self.id = id
        self.nom = nom
        self.prix = prix

# BaseDeDonnees : Une classe pour gérer la connexion à la base de données en MySQL ayant un host = "localhost", user = "root" et password = "".Ensuite créer une base de données e_commerce.
class BaseDeDonnees:
    def __init__(self, host="localhost", user="root", password=""):
        self.host = host
        self.user = user
        self.password = password
        self.connect()

    def connect(self):
        self.cnx = mysql.connector.connect(
            host=self.host, user=self.user, password=self.password
        )
        self.cursor = self.cnx.cursor()

    def close(self):
        self.cnx.close()

    def execute_query(self, query):
        mycursor = self.cnx.cursor()
        mycursor.execute(query)
        self.cnx.commit()

    def create_table(self, table_name, columns):
        self.execute_query(f"CREATE DATABASE IF NOT EXISTS e_commerce")
        self.cnx.database = "e_commerce"
        mycursor = self.cnx.cursor()
        query = f"CREATE TABLE {table_name} ("
        for column in columns:
            query += column + ", "
        query = query[:-2] + ")"
        mycursor.execute(query)
        self.cnx.commit()


if __name__ == "__main__":
    bd = BaseDeDonnees()
    bd.create_table(
        "produit",
        [
            "id INT NOT NULL AUTO_INCREMENT PRIMARY KEY",
            "nom VARCHAR(255) NOT NULL",
            "prix INT NOT NULL",
        ],
    )
    bd.close()
    print("Base de données créée avec succès")
