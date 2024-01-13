from contact import Contact
from contact_manager import ContactManager

if __name__ == "__main__":
      contact_manager = ContactManager(Contact.nom, Contact.prenom, Contact.telephone, Contact.adresse, Contact.email)

      while True:
            print("1. Ajouter un nouveau contact")
            print("2. Afficher tous les contacts")
            print("3. Mettre à jour un contact")
            print("4. Supprimer un contact")
            print("5. Quitter l'application")
            choice = input("Veuillez saisir votre choix: ")

            if choice == "1":
                  nom = input("Veuillez saisir le nom: ")
                  prenom = input("Veuillez saisir le prenom: ")
                  telephone = input("Veuillez saisir le numéro de téléphone: ")
                  adresse = input("Veuillez saisir l'adresse: ")
                  email = input("Veuillez saisir l'email: ")
                  contact_manager.ajouter_contact(nom, prenom, telephone, adresse, email)
                  with open('contacts.csv', 'a', encoding='utf-8') as fichier_csv:
                        fichier_csv.write(f"{nom}, {prenom},{telephone},{adresse},{email}\n")
            elif choice == "2":
                  contact_manager.afficher_contacts()
            elif choice == "3":
                  contact_manager.mettre_a_jour_contact(nom, prenom, telephone, adresse, email)
            elif choice == "4":
                  contact_manager.supprimer_contact(nom, prenom, telephone, adresse, email)
            elif choice == "5":
                  break
            else:
                  print("Veuillez saisir un numéro de choix valide")
     
      
      
      