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

  # bd.create_table("produits", "id INTEGER PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(50), prix FLOAT")  # Crée la table produits.
      # print("Table produits créée avec succès")  # Affiche un message indiquant que la table produits a été créée avec succès.
      
      # bd.create_table("panier", "id INTEGER PRIMARY KEY AUTO_INCREMENT, produit_id INT , quantite INT NOT NULL, FOREIGN KEY (produit_id) REFERENCES produit(id)")  # Crée la table panier.
      # print("Table panier créée avec succès")  # Affiche un message indiquant que la table panier a été créée avec succès.
      
      # bd.create_table("facture", "id INTEGER PRIMARY KEY AUTO_INCREMENT, panier_id INT NOT NULL, FOREIGN KEY (panier_id) REFERENCES panier(id)")  # Crée la table facture.
      # print("Table facture créée avec succès")  # Affiche un message indiquant que la table facture a été créée avec succès.
      
      # bd.create_table("lignefacture", "id INTEGER PRIMARY KEY AUTO_INCREMENT, facture_id INT NOT NULL, produit_id INT NOT NULL, quantite INT NOT NULL, FOREIGN KEY (facture_id) REFERENCES facture(id), FOREIGN KEY (produit_id) REFERENCES produit(id)")  # Crée la table lignefacture.
      # print("Table lignefacture créée avec succès")  # Affiche un message indiquant que la table lignefacture a été créée avec succès.
      
      # bd.close()  # Ferme la connexion à la base de données.
      # print("Base de données créée avec succès")  # Affiche un message indiquant que la base de données a été créée avec succès.

      # # Création de quelques produits
      # produit1 = Produit(1, "Produit 1", 10)
      # produit2 = Produit(2, "Produit 2", 20)

      # # Ajout des produits au panier
      # panier = Panier()
      # panier.ajouter_produit(produit1, 2)
      # panier.ajouter_produit(produit2, 3)
      # panier.afficher_panier()

      # # Création d'une ligne de facture
      # ligne = LigneFacture(produit1, 2)
      # ligne.afficher_ligne()

      # # Création d'une facture à partir du panier
      # facture = Facture(panier)
      # facture.afficher_facture()  