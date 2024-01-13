class ContactManager():
      def __init__(self, nom, prenom, telephone, adresse, email):
            self.nom = nom
            self.prenom = prenom
            self.telephone = telephone
            self.adresse = adresse
            self.email = email
            self.contacts = []
      def ajouter_contact(self, nom, prenom, telephone, adresse, email):
            self.contacts.append(nom, prenom, telephone, adresse, email)
      
      def afficher_contacts(self):
            for contact in self.contacts:
                  print(contact.nom, contact.prenom, contact.telephone, contact.adresse, contact.email)
      
      def mettre_a_jour_contact(self, nom, prenom, telephone, adresse, email):
            for contact in self.contacts:
                 if contact.nom == nom and contact.prenom == prenom:
                        contact.nom = nom
                        contact.prenom = prenom
                        contact.telephone = telephone
                        contact.adresse = adresse
                        contact.email = email
      
      def supprimer_contact(self, nom, prenom, telephone, adresse, email):
            self.contacts.remove(nom, prenom, telephone, adresse, email)
      
      def chercher_contact(self, nom,prenom):
            for contact in self.contacts:
                  if contact.nom == nom and contact.prenom == prenom:
                        return contact
      
 
                  
     