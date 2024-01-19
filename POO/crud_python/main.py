import csv
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
        return self.contacts

    def view_contacts(self):
        for contact in self.contacts:
            print(
                f"Your firstname: {contact.firstname} \nYour lastaname: {contact.lastname} \nYour phone number: {contact.phoneNumber} \nYour address: {contact.address} \nYour email: {contact.email}\n\n"
            )

    def update_contact(self, firstname, lastname, phoneNumber, address, email):
        for contact in self.contacts:
            if contact.firstname == firstname and contact.lastname == lastname:
                contact.firstname = firstname
                contact.lastname = lastname
                contact.phoneNumber = phoneNumber
                contact.address = address
                contact.email = email
                print("Contact updated with success !!!")
                return contact
        print("Contact not found.")
        return None

    def delete_contact(self, firstname, lastname):
        for contact in self.contacts:
            if contact.firstname == firstname and contact.lastname == lastname:
                self.contacts.remove(contact)
                print("Contact deleted with success !!!")
                return contact
        print("Contact not found.")
        return None

def add_contact_to_csv(contact):
    with open("contacts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                contact.firstname,
                contact.lastname,
                contact.phoneNumber,
                contact.address,
                contact.email,
            ]
        )


def main():
    manager = ContactManager()

    while True:
        print("\n1. Add a new contact")
        print("2. Show all contacts")
        print("3. Update the contact")
        print("4. Delete the contact")
        print("5. Exit the application")

        choice = input("Select one of the following : ")

        if choice == "1":
            firstname = input("Enter your first name : ")
            lastname = input("Enter your last name : ")
            phoneNumber = input("Enter your phone number : ")
            address = input("Enter your address : ")
            email = input("Enter your email address : ")
            contact = Contact(firstname, lastname, phoneNumber, address, email)
            print(contact)
            added_contact = manager.add_contact(contact)
            if added_contact:
                add_contact_to_csv(contact)
                print("Contact added in file csv")
            else:
                print("Contact not add in file csv")
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            firstname = input("Enter your first name for update: ")
            lastname = input("Enter your last name for update : ")
            phoneNumber = input("Enter yourphone number for update : ")
            address = input("Enter youraddress for update : ")
            email = input("Enter your email for update : ")
            updated_contact = manager.update_contact(
                firstname, lastname, phoneNumber, address, email
            )
            if updated_contact:
                add_contact_to_csv(updated_contact)
        elif choice == "4":
            firstname = input("Enter your first name for delete : ")
            lastname = input("Enter your last name for delete : ")
            deleted_contact = manager.delete_contact(firstname, lastname)
            if deleted_contact:
                add_contact_to_csv(deleted_contact)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again")


if __name__ == "__main__":
    main()
