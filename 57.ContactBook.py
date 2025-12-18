# The code above implements a simple contact book application that allows 
# users to add, view, search, edit, and delete contacts stored in a JSON file. 
# Each contact has an ID, name, phone number, email, and relation. 
# The application runs in a loop until the user chooses to exit.

import json
import os

def Add_Contact():
    f =0
    name = input("Enter Name: ").strip()
    #Spaces allowed in names like "Mary Jane"
    while (f != 1):
        if not name:
            print("Invalid name.")
            name = input("Enter Name: ").strip()
        else:
            f = 1
    phone = input("Enter Phone Number: ")
    while not phone.isdigit():
        print("Invalid phone number. Please enter digits only with at least 7 characters.")
        phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    while "@" not in email or "." not in email:
        print("Invalid email format. Please enter a valid email.")
        email = input("Enter Email: ")
    Relation = input("Enter Relation: ")

# -------- GENERATE UNIQUE ID --------
    try:
        with open("Contacts.json", "r") as file:
            data = json.load(file)
            if data["Contacts"]:
                id = max(contact["ID"] for contact in data["Contacts"]) + 1
            else:
                id = 1
    except (FileNotFoundError, json.JSONDecodeError):
        id = 1
# ------------------------------------
    Contact = {
            "ID": id,
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Relation": Relation
        }

    try:
        with open("Contacts.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
    # File doesn't exist OR is empty OR invalid
        data = {"Contacts": []} # Initialize with empty Contacts list
    if Contact not in data['Contacts']:
        data['Contacts'].append(Contact)    #Append new contact to the list
        
        with open('Contacts.json','w') as file:
            json.dump(data,file,indent=4)  #Write updated data back to the file
        print("Contact added successfully.")
    else:
        print("Contact already exists.")

def View_Contact():
    with open('Contacts.json','r') as file:
        data = json.load(file) #Data is now a Python dict in RAM
        #then we can work with it
        Contacts = data['Contacts'] #This is a list of contacts (dictionaries)
        #data['Contacts'] is used to access the list of contacts within the main dictionary
        if not Contacts:
            print("No contacts found.")
            return
        for contact in Contacts:
            print(f"{contact['ID']}| {contact['Name']} | {contact['Phone']} | {contact['Email']} | {contact['Relation']}")
        
def Search_Contact():
    search_name = input("Enter the name to search: ").strip()
    with open("Contacts.json",'r') as file:
        data = json.load(file)
        Contacts = data['Contacts']
        if not Contacts:
            print("No contacts found.")
            return
        else:
            for contact in Contacts:
                if search_name.lower() in contact['Name'].lower():
                    print(f"Contact Found: {contact['ID']}| {contact['Name']} | {contact['Phone']} | {contact['Email']} | {contact['Relation']}")
                    return
            print("Contact not found.")


def Edit_Contact():
    with open("Contacts.json",'r') as file:
        data = json.load(file)
        Contacts = data['Contacts']
        if not Contacts:
            print("No contacts found.")
            return
        Enter_id = int(input("Enter the ID of the Contact to edit: "))
        for Contact in Contacts:
            if Contact["ID"] == Enter_id:
                name = input("Enter New Name: ")
                phone = input("Enter New phone Number: ")
                Email = input("Enter new Email: ")
                Relation = input("Enter new Relation: ")
                Contact["Name"] = name
                Contact["Phone"] = phone
                Contact["Email"] = Email
                Contact["Relation"] = Relation
                with open('Contacts.json','w') as file:
                    json.dump(data,file,indent=4)
                print("Contact updated successfully.")
                return
    
def Delete_Contact():
    with open("Contacts.json",'r') as file:
        data = json.load(file)
        Contacts = data['Contacts']
        if not Contacts:
            print("No contacts found.")
            return
        Enter_id = int(input("Enter the ID of the Contact to delete: "))
        for Contact in Contacts:
            if Contact['ID'] == Enter_id:
                sure = input(f"Are you sure you want to delete the contact {Contact['Name']}? (Y/N): ")
                if sure.upper() == 'Y':
                    Contacts.remove(Contact)
                    with open ("Contacts.json",'w') as file:
                        json.dump(data,file,indent=4)
                    print("Contact Deleted Sucessfully!!")
                else:
                    print("Deletion Cancelled !!")

if __name__ == "__main__":
    id = 1
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            Add_Contact()
        elif choice == '2':
            View_Contact()
        elif choice == '3':
            Search_Contact()
        elif choice == '4':
            Edit_Contact()
        elif choice == '5':
            Delete_Contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

