import csv  # Importe le module csv pour lire et écrire des fichiers csv.
from contact import Contact
class ContactManager:  # Définit une classe ContactManager pour gérer les contacts.
    def __init__(self):  # Initialise la classe avec une liste vide de contacts.
        self.contacts = []  # Liste pour stocker les contacts.

    def add_contact(self, contact):  # Méthode pour ajouter un contact à la liste.
        self.contacts.append(contact)  # Ajoute le contact à la liste.
        with open("contacts.csv", "a", newline="") as file:  # Ouvre le fichier csv en mode append.
            writer = csv.writer(file)  # Crée un écrivain csv.
            writer.writerow(  # Écrit une ligne dans le fichier csv.
                [
                    contact.firstname,
                    contact.lastname,
                    contact.phoneNumber,
                    contact.address,
                    contact.email,
                ]
            )
        print("Contact added with success !!!")  # Imprime un message de succès.

    def view_contacts(self):  # Méthode pour afficher tous les contacts.
        with open("contacts.csv", "r", newline="") as file:  # Ouvre le fichier csv en mode append.
                read = csv.reader(file)  # Crée un écrivain csv.
                for row in read:  # Parcourt chaque ligne du fichier csv.
                    print(  # Imprime les détails du contact.
                        f"Your firstname: {row[0]} \nYour lastaname: {row[1]} \nYour phone number: {row[2]} \nYour address: {row[3]} \nYour email: {row[4]}\n"
            )
        
    def update_contact(self, email, contact):  # Méthode pour mettre à jour un contact.
        with open("contacts.csv", "r", newline="") as file:  # Ouvre le fichier csv en mode append.
            read = csv.reader(file)  # Crée un écrivain csv.
            newList = []
            for row in read:  # Parcourt chaque ligne du fichier csv.
                if row[4] == email:  # Vérifie si le contact correspond aux noms donnés.
                    newList.append(
                        [
                            contact.firstname,
                            contact.lastname,
                            contact.phoneNumber,
                            contact.address,
                            contact.email
                        ]
                    )
                    print("Contact updated with success!!!")  # Imprime un message de succès.
                else:
                    newList.append(row)
                    print("Contact not found.")  # Imprime un message si le contact n'est pas trouvé.
                    
                with open("contacts.csv", "w", newline="") as file:  # Ouvre le fichier csv en mode append.
                    writer = csv.writer(file)  # Crée un écrivain csv.
                    writer.writerows(newList)  # Écrit les nouvelles lignes dans le fichier csv.
                     
    def delete_contact(self, firstname, lastname):  # Méthode pour supprimer un contact.
        for contact in self.contacts:  # Parcourt tous les contacts dans la liste.
            if contact.firstname == firstname and contact.lastname == lastname:  # Vérifie si le contact correspond aux noms donnés.
                self.contacts.remove(contact)  # Supprime le contact de la liste.
                print("Contact deleted with success !!!")  # Imprime un message de succès.
                return contact  # Retourne le contact supprimé.
        print("Contact not found.")  # Imprime un message si le contact n'est pas trouvé.
        return None  # Retourne None si le contact n'est pas trouvé.



