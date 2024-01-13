import contact

class ContactManager(contact.Contact):
      def __init__(self, nom, prenom, telephone, adresse, email):
            self.nom = nom
            self.prenom = prenom
            self.telephone = telephone
            self.adresse = adresse
            self.email = email
            self.contacts = []
      def ajouter_contact(self, contact):
            self.contacts.append(contact)
      
      def affiche_contacts(self):
            for contact in self.contacts:
                  print(contact.nom, contact.prenom, contact.telephone, contact.adresse, contact.email)
                  
      
      def supprimer_contact(self, contact):
            self.contacts.remove(contact)
      
      def chercher_contact(self, nom,prenom):
            for contact in self.contacts:
                  if contact.nom == nom and contact.prenom == prenom:
                        return contact
      
 
                  
     