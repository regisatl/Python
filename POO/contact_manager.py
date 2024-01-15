class Contact:
    def __init__(self, firstname, lastname, phoneNumber, address, email):
        self.firstname = firstname
        self.lastname = lastname
        self.phoneNumber = phoneNumber
        self.address = address
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added with success !!!") 

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Your firstname: {contact.firstname} \nYour lastaname: {contact.lastname}, \nYour phone number: {contact.phoneNumber}, \nYour address: {contact.address}, \nYour email: {contact.email}")

    def update_contact(self, firstname, lastname, phoneNumber, address, email):
        for contact in self.contacts:
            if contact.firstname == firstname and contact.lastname == lastname:
                if phoneNumber:
                    contact.phoneNumber = phoneNumber
                if address:
                    contact.address = address
                if email:
                    contact.email = email
                return
            print("Contact updated with success !!!")
        print("Contact not found.")

    def delete_contact(self, firstname, lastname):
        for contact in self.contacts:
            if contact.firstname == firstname and contact.lastname == lastname:
                self.contacts.remove(contact)
                return
            print("Contact deleted with success !!!")
        print("Contact not found.")