
# Contact storage
contacts = {}

def add_contact(name, phone):
    """Add a new contact to the dictionary."""
    contacts[name] = phone
    print(f"✅ Contact '{name}' added successfully.")

def search_contact(name):
    """Search for a contact by name."""
    if name in contacts:
        print(f"📞 {name}: {contacts[name]}")
    else:
        print(f"⚠️ Contact '{name}' not found.")

def delete_contact(name):
    """Delete a contact by name."""
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted successfully.")
    else:
        print(f"⚠️ Contact '{name}' not found.")

def show_menu():
    """Display the menu options."""
    print("\n=== Contact Book Menu ===")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")

def run_contact_book():
    """Main loop for the contact book application."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == "2":
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == "3":
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == "4":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    run_contact_book()