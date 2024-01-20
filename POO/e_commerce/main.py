from basededonnees import BaseDeDonnees

if __name__ == "__main__":  # Si le script est exécuté directement (et non importé).

      database = BaseDeDonnees()
      columns = "id, nom, prix"
      values = "'2', 'Pizza', '1000'"
      table_name = "produits"
      database.insert_table(table_name, columns, values)
      
      
      

      
      
      
       
      
      
        