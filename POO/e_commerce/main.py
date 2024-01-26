from basededonnees import BaseDeDonnees
from produit import Produit

if __name__ == "__main__":  # Si le script est exécuté directement (et non importé).

      database = BaseDeDonnees()
      product = tuple(Produit('Pizza', 1000))
      table_name = "produits"
      columns = ('nom', 'prix')
      
      values =product
      print(product)
      
      # database.insert_table(table_name, columns, values)
      
      
      

      
      
      
       
      
      
        