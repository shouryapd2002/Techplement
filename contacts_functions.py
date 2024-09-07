def display_menu():
    print("\n----- Contact Management System -----")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def view_contacts():
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if contacts:
                print("\n----- Contacts -----")
                for idx, contact in enumerate(contacts, start=1):
                    print(f"{idx}. {contact.strip()}")
            else:
                print("/nNO Contacts Added. Please add contacts to view.")

def add_contact():
    name = input("\nEnter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")

    contact_info = f"name: {name} |  Phone: {phone} |  Email: {email}\n"

    with open("contacts.txt", "a") as file:
        file.write(contact_info)

    print(f"Contact '{name}' was added successfully.")

def search_contact():
    keyword = input("\nEnter a keyword from name, phone number or email to search for a contact: ")

    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

        matching_contacts = [contact.strip() for contact in contacts if keyword.lower() in contact.lower()]

        if matching_contacts:
            print("\n----- Matched Contacts -----")
            for idx, contact in enumerate(matching_contacts, start=1):
                print(f"{idx}. {contact}")
        else:
            print("\nNo matching contacts found.")

def delete_contact():
    view_contacts()

    sr_number = int(input("\nEnter the contact number to delete: "))
    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

        if 1 <= sr_number <= len(contacts):
            deleted_contact = contacts.pop(sr_number - 1)

            with open("contacts.txt", "w") as file:
                file.writelines(contacts)

            print(f"Contact '{deleted_contact.strip()}' deleted successfully.")
        else:
            print("Invalid contact number. Please try again.")