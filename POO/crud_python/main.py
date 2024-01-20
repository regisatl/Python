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
            firstname = input("Enter your first name : ")  # Demande à l'utilisateur d'entrer les détails du contact à ajouter.
            lastname = input("Enter your last name : ")
            phoneNumber = input("Enter your phone number : ")
            address = input("Enter your address : ")
            email = input("Enter your email address : ")
            contact = Contact(firstname, lastname, phoneNumber, address, email)  # Crée un nouveau contact avec les détails donnés.
            manager.add_contact(contact)  # Ajoute le contact au gestionnaire de contacts.
        elif choice == "2":  # Si l'utilisateur choisit de voir tous les contacts.
            manager.view_contacts()  # Affiche tous les contacts.
        elif choice == "3":  # Si l'utilisateur choisit de mettre à jour un contact.
            emailOld = input("Enter your old email : ") # Demande à l'utilisateur d'entrer les détails du contact à mettre à jour.
            firstname = input("Enter your first name for update: ")  
            lastname = input("Enter your last name for update : ")
            phoneNumber = input("Enter yourphone number for update : ")
            address = input("Enter youraddress for update : ")
            email = input("Enter your email for update : ")
            contact = Contact(firstname, lastname, phoneNumber, address, email)  # Crée un nouveau contact avec les détails donnés.
            manager.update_contact(contact) # Met à jour le contact dans le gestionnaire de contacts.
        elif choice == "4":  # Si l'utilisateur choisit de supprimer un contact.
            firstname = input("Enter your first name for delete : ")  # Demande à l'utilisateur d'entrer les noms du contact.
            lastname = input("Enter your last name for delete : ")
            manager.delete_contact(firstname, lastname)  # Supprime le contact du gestionnaire de contacts.
        elif choice == "5":  # Si l'utilisateur choisit de quitter l'application.
            break  # Sort de la boucle infinie.
        else:
            print("Invalid choice. Please try again")  # Imprime un message d'erreur si le choix de l'utilisateur n'est pas valide.


if __name__ == "__main__":  # Vérifie si le script est exécuté directement.
    main()  # Appelle la fonction principale pour exécuter le programme.
