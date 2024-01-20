import csv  # Importe le module csv pour lire et écrire des fichiers csv.
from contact import Contact  
from contact_manager import ContactManager 

def main():  # Définit la fonction principale pour exécuter le programme.
    manager = ContactManager()  # Crée un gestionnaire de contacts.

    while (
        True
    ):  # Boucle infinie pour exécuter le programme jusqu'à ce que l'utilisateur décide de quitter.
        print("\n1. Add a new contact")  # Imprime les options pour l'utilisateur.
        print("2. Show all contacts")
        print("3. Update the contact")
        print("4. Delete the contact")
        print("5. Exit the application")

        choice = input("Select one in the following : ")  # Demande à l'utilisateur de faire un choix.

        if choice == "1":  # Si l'utilisateur choisit d'ajouter un contact.
            firstname = input("Enter your first name : ")  # Demande à l'utilisateur d'entrer les détails du contact.
            lastname = input("Enter your last name : ")
            phoneNumber = input("Enter your phone number : ")
            address = input("Enter your address : ")
            email = input("Enter your email address : ")
            contact = Contact(firstname, lastname, phoneNumber, address, email)  # Crée un nouveau contact avec les détails donnés.
            added_contact = manager.add_contact(contact)  # Ajoute le contact au gestionnaire de contacts.
            if added_contact:  # Si le contact a été ajouté avec succès.
                manager.add_contact_to_csv(contact)  # Ajoute le contact au fichier csv.
                print("Contact added in file csv")  # Imprime un message de succès.
            else:
                print("Contact not add in file csv")  # Imprime un message d'échec.
        elif choice == "2":  # Si l'utilisateur choisit de voir tous les contacts.
            manager.view_contacts()  # Affiche tous les contacts.
        elif choice == "3":  # Si l'utilisateur choisit de mettre à jour un contact.
            firstname = input("Enter your first name for update: ")  # Demande à l'utilisateur d'entrer les détails du contact.
            lastname = input("Enter your last name for update : ")
            phoneNumber = input("Enter yourphone number for update : ")
            address = input("Enter youraddress for update : ")
            email = input("Enter your email for update : ")
            updated_contact = manager.update_contact(firstname, lastname, phoneNumber, address, email) # Met à jour le contact dans le gestionnaire de contacts.
            if updated_contact:  # Si le contact a été mis à jour avec succès.
                manager.add_contact_to_csv(updated_contact)  # Ajoute le contact mis à jour au fichier csv.
        elif choice == "4":  # Si l'utilisateur choisit de supprimer un contact.
            firstname = input("Enter your first name for delete : ")  # Demande à l'utilisateur d'entrer les noms du contact.
            lastname = input("Enter your last name for delete : ")
            deleted_contact = manager.delete_contact(firstname, lastname)  # Supprime le contact du gestionnaire de contacts.
            if deleted_contact:  # Si le contact a été supprimé avec succès.
                manager.add_contact_to_csv(deleted_contact)  # Ajoute le contact supprimé au fichier csv.
        elif choice == "5":  # Si l'utilisateur choisit de quitter l'application.
            break  # Sort de la boucle infinie.
        else:
            print("Invalid choice. Please try again")  # Imprime un message d'erreur si le choix de l'utilisateur n'est pas valide.


if __name__ == "__main__":  # Vérifie si le script est exécuté directement.
    main()  # Appelle la fonction principale pour exécuter le programme.
