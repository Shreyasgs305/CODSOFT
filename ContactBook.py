import json

# Function to load contacts from a file
def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save contacts to a file
def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

# Function to search for a contact
def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            return
    print("Contact not found.")

# Function to update a contact
def update_contact(contacts):
    search_term = input("Enter name or phone number to update: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            contact['name'] = input("Enter new name: ")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    search_term = input("Enter name or phone number to delete: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    filename = 'contacts.json'
    contacts = load_contacts(filename)

    while True:
        print("\nContact Book Menu:")
        print("1. Add New Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Please enter your selection: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(filename, contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
