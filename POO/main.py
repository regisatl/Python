import csv
import contact_manager

def main():
    manager = contact_manager.ContactManager()

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
            contact = contact_manager.Contact(firstname, lastname, phoneNumber, address, email)
            print(contact)
            manager.add_contact(contact)
            # with open('contacts.csv', 'a', newline='') as file:
            #     writer = csv.writer(file)
            #     for contact in manager.contacts:
            #         writer.writerow([contact.firstname, contact.lastname, contact.phoneNumber, contact.address, contact.email])
        elif choice == "2":
            with open('contacts.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  
                        contact = contact_manager.Contact(row[0], row[1], row[2], row[3], row[4])
                        manager.view_contacts()

        elif choice == "3":
            firstname = input("Enter your first name for update: ")
            lastname = input("Enter your last name for update : ")
            phoneNumber = input("Enter yourphone number for update : ")
            address = input("Enter youraddress for update : ")
            email = input("Enter your email for update : ")
            manager.update_contact(firstname, lastname, phoneNumber, address, email)
        elif choice == "4":
            firstname = input("Enter your first name for delete : ")
            lastname = input("Enter your last name for delete : ")
            manager.delete_contact(firstname, lastname)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()