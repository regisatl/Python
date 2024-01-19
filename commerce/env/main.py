import mysql.connector  # Importe le module mysql.connector pour se connecter à MySQL.
import sys  # Importe le module sys pour interagir avec l'interpréteur Python.
from mysql.connector import (
    Error,
)  # Importe la classe Error du module mysql.connector pour gérer les erreurs.

sql_create = """ 
INSERT INTO produits (nom, prix) VALUES ('T-shirt', 25); """  # Termine la requête SQL.

try:  # Essaie d'exécuter le bloc de code suivant.
    conn = mysql.connector.connect(  # Se connecte à la base de données MySQL.
        host="localhost", user="root", password="", database="e_commerce"
    )
    cursor = conn.cursor()  # Crée un curseur pour exécuter des requêtes SQL.
    cursor.execute(sql_create)  # Exécute la requête SQL.
    conn.commit()  # Valide les modifications dans la base de données.
    cursor.close()  # Ferme le curseur.
    conn.close()  # Ferme la connexion à la base de données.
    print(
        "Table created successfully"
    )  # Affiche un message indiquant que la table a été créée avec succès.
    sys.exit(
        0
    )  # Termine l'exécution du script avec le code de sortie 0 (qui indique que le script s'est terminé avec succès).

except Error as e:  # Si une erreur se produit, exécute le bloc de code suivant.
    print(e)  # Affiche l'erreur.
    sys.exit(
        1
    )  # Termine l'exécution du script avec le code de sortie 1 (qui indique qu'une erreur s'est produite).


# fonction commander qui fait la commande un produit


def commander(produit):
    produit_id = produit.id
    produit_nom = produit.nom
    produit_prix = produit.prix
    produit_quantite = produit.quantite
