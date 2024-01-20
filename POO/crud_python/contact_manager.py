import csv  # Importe le module csv pour lire et écrire des fichiers csv.
class ContactManager:  # Définit une classe ContactManager pour gérer les contacts.
    def __init__(self):  # Initialise la classe avec une liste vide de contacts.
        self.contacts = []  # Liste pour stocker les contacts.

    def add_contact(self, contact):  # Méthode pour ajouter un contact à la liste.
        self.contacts.append(contact)  # Ajoute le contact à la liste.
        print("Contact added with success !!!")  # Imprime un message de succès.
        return self.contacts  # Retourne la liste de contacts.

    def view_contacts(self):  # Méthode pour afficher tous les contacts.
        for contact in self.contacts:  # Parcourt tous les contacts dans la liste.
            print(  # Imprime les détails du contact.
                f"Your firstname: {contact.firstname} \nYour lastaname: {contact.lastname} \nYour phone number: {contact.phoneNumber} \nYour address: {contact.address} \nYour email: {contact.email}\n\n"
            )

    def update_contact(self, firstname, lastname, phoneNumber, address, email):  # Méthode pour mettre à jour un contact.
        for contact in self.contacts:  # Parcourt tous les contacts dans la liste.
            if contact.firstname == firstname and contact.lastname == lastname:  # Vérifie si le contact correspond aux noms donnés.
                contact.firstname = firstname  # Met à jour le prénom.
                contact.lastname = lastname  # Met à jour le nom de famille.
                contact.phoneNumber = phoneNumber  # Met à jour le numéro de téléphone.
                contact.address = address  # Met à jour l'adresse.
                contact.email = email  # Met à jour l'email.
                print("Contact updated with success !!!")  # Imprime un message de succès.
                return contact  # Retourne le contact mis à jour.
        print("Contact not found.")  # Imprime un message si le contact n'est pas trouvé.
        return None  # Retourne None si le contact n'est pas trouvé.

    def delete_contact(self, firstname, lastname):  # Méthode pour supprimer un contact.
        for contact in self.contacts:  # Parcourt tous les contacts dans la liste.
            if contact.firstname == firstname and contact.lastname == lastname:  # Vérifie si le contact correspond aux noms donnés.
                self.contacts.remove(contact)  # Supprime le contact de la liste.
                print("Contact deleted with success !!!")  # Imprime un message de succès.
                return contact  # Retourne le contact supprimé.
        print("Contact not found.")  # Imprime un message si le contact n'est pas trouvé.
        return None  # Retourne None si le contact n'est pas trouvé.

    def add_contact_to_csv(contact):  # Définit une fonction pour ajouter un contact à un fichier csv.
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


