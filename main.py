from contacts_functions import *
import os

if os.path.isfile("contacts.txt"):
      pass
else:
    f=open('contacts.txt','x')

while True:
    display_menu()
    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        view_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")