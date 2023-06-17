import sys
import queue

def initial_phonebook():
    # Get the number of contacts from the user
    rows, cols = int(input("Please enter Initial Number of contacts: ")), 6
    phone_book = queue.Queue()
    
    for i in range(rows):
        print("\nEnter contact %d details in the Following Order (ONLY):" % (i+1))
        print("NOTE: * indicates mandatory fields")
        print("....................................................................")
        temp = queue.Queue()
        
        for j in range(cols):
            if j == 0:
                # Get the name from the user
                name = str(input("Enter name*: "))
                
                if name == '' or name == ' ':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
                
                temp.put(name)
                
            if j == 1:
                # Get the number from the user
                number = int(input("Enter number*: "))
                temp.put(number)
                
            if j == 2:
                # Get the email address from the user
                email = str(input("Enter e-mail address: "))
                if email == '' or email == ' ':
                    email = None
                temp.put(email)
                
            if j == 3:
                # Get the date of birth from the user
                dob = str(input("Enter date of birth(dd/mm/yy): "))
                if dob == '' or dob == ' ':
                    dob = None
                temp.put(dob)
                
            if j == 4:
                # Get the category from the user
                category = str(input("Enter category(Family/Friends/Work/Others): "))
                if category == '' or category == ' ':
                    category = None
                temp.put(category)
        
        phone_book.put(temp)
    
    return phone_book


def menu():
    # Display the menu options to the user
    print("\n********************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY")
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Edit a contact")
    print("5. Search Contact")
    print("6. Display all contacts")
    print("7. Exit phonebook")

    # Get the user's choice
    choice = int(input("Please enter your choice: "))
    return choice


def edit_contact(pb):
    contact = str(input("Please enter the name of the contact you wish to edit: "))

    for i in range(pb.qsize()):
        temp = pb.get()
        
        if contact == temp.queue[0]:
            print("....................................................................")
            print("\nEnter updated contact details in the following order (ONLY):")
            print("NOTE: '*' Indicates Mandatory Fields")
            print("....................................................................")

            updated_contact = queue.Queue()
            updated_contact.put(contact)

            for j in range(1, temp.qsize()):
                field = temp.queue[j]

                if j == 1:
                    field = int(input("Enter number '*' : "))
                    if field == '' or field == ' ':
                        sys.exit("Number is a mandatory field. Process exiting due to blank field...")
                
                elif j == 2:
                    field = str(input("Enter e-mail address: "))
                    if field == '' or field == ' ':
                        field = None
                
                elif j == 3:
                    field = str(input("Enter date of birth (dd/mm/yy): "))
                    if field == '' or field == ' ':
                        field = None
                
                elif j == 4:
                    field = str(input("Enter category (Family/Friends/Work/Others): "))
                    if field == '' or field == ' ':
                        field = None

                updated_contact.put(field)

            pb.put(updated_contact)
            print("Contact has been updated successfully.")
            return
        else:
            pb.put(temp)
    print("Contact not found. Please try again.")

def remove_existing(pb):
    # Prompt the user to enter the name of the contact to remove
    contact = str(input("Please enter the name of the contact you wish to remove: "))

    for i in range(pb.qsize()):
        # Get the next contact from the phone book
        temp = pb.get()

        if contact == temp.queue[0]:
            print("Contact Found. Contact is now being deleted from the phonebook...")
            print("....................................................................")
            print("Contact deleted")
            return
        else:
            # Add the contact back to the phone book if it doesn't match the one to be removed
            pb.put(temp)

    print("Contact not found. Please try again.")


def search_existing(pb):
    # Prompt the user to enter the name of the contact to search
    name = str(input("Please enter the name of the contact you wish to search: "))

    for i in range(pb.qsize()):
        # Get the next contact from the phone book
        temp = pb.get()

        if name == temp.queue[0]:
            print("Contact Found!")
            print("....................................................................")
            print("\nContact Details:")
            print("....................................................................")
            print("Name: ", temp.queue[0])
            print("Number: ", temp.queue[1])
            print("E-mail: ", temp.queue[2])
            print("D.O.B: ", temp.queue[3])
            print("Category: ", temp.queue[4])
            print("....................................................................")
            return
        else:
            # Add the contact back to the phone book if it doesn't match the one being searched
            pb.put(temp)

    print("Contact not found. Please try again.")

def add_contact(pb):
    # Create a new contact queue
    contact = queue.Queue()
    
    print("Enter contact details in the following order (ONLY):")
    print("NOTE: '*' indicates mandatory fields")
    print("....................................................................")
    
    # Prompt the user to enter the contact details
    name = str(input("Enter name '*' : "))

    if name == '' or name == ' ':
        sys.exit("Name is a mandatory field. Process exiting due to blank field...")

    contact.put(name)
    
    number = int(input("Enter number '*' : "))
    contact.put(number)
    
    email = str(input("Enter e-mail address: "))

    if email == '' or email == ' ':
        email = None

    contact.put(email)
    
    dob = str(input("Enter date of birth (dd/mm/yy): "))

    if dob == '' or dob == ' ':
        dob = None

    contact.put(dob)
    
    category = str(input("Enter category (Family/Friends/Work/Others): "))

    if category == '' or category == ' ':
        category = None

    contact.put(category)
    
    pb.put(contact)
    print("Contact has been added successfully.")

def display_all(pb):
    if pb.empty():
        print("Your phonebook is empty.")
        return
    
    print("\nPHONEBOOK CONTACTS: ")
    print("....................................................................")
    
    for i in range(pb.qsize()):
        # Get the next contact from the phone book
        temp = pb.get()
        
        print("Contact ", i+1, ":")
        print("....................................................................")
        print("Name: ", temp.queue[0])
        print("Number: ", temp.queue[1])
        print("E-mail: ", temp.queue[2])
        print("D.O.B: ", temp.queue[3])
        print("Category: ", temp.queue[4])
        print(".....................................................................")
        
        # Add the contact back to the phone book
        pb.put(temp)

def delete_all(pb):
    confirm = str(input("Are you sure you want to delete all contacts? (y/n): "))

    if confirm.lower() == 'y':
        while not pb.empty():
            pb.get()
        print("All contacts have been deleted successfully.")
        return

    print("Operation canceled.")

def run_phonebook():
    # Create the initial phonebook
    pb = initial_phonebook()

    while True:
        # Display the menu and get user's choice
        choice = menu()

        if choice == 1:
            # Add a new contact
            add_contact(pb)
        elif choice == 2:
            # Remove an existing contact
            remove_existing(pb)
        elif choice == 3:
            # Delete all contacts
            delete_all(pb)
        elif choice == 4:
            # Edit a contact
            edit_contact(pb)
        elif choice == 5:
            # Search for a contact
            search_existing(pb)
        elif choice == 6:
            # Display all contacts
            display_all(pb)
        elif choice == 7:
            # Exit the phonebook
            print("********************************************************************")
            print("\t\t\tThank you for using SmartPhone Directory")
            print("********************************************************************")
            sys.exit(0)
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")


# Call the function to run the phonebook
run_phonebook()
