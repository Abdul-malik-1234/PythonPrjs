# Task: Simple Contact Manager
# Create a Python program that manages a contact list with the following features:

# Basic Requirements:
# Add new contacts (name, phone, email)

# View all contacts

# Search contacts by name

# Delete contacts

# Save contacts to a file

# Load contacts from a file

# Starter Code:

# contact_manager.py

import json
contacts = []

def add_contact(name, phone, email):
    # Your code here
    global contacts
    flag=False
    for i in range(0,len(contacts)):
        if contacts[i]["name"]==name:
            flag=True
            break
    if flag==True:
        print("The entry already exists,the requested entry is not added")
    else:
        dict1={"name":name,"phone":phone,"email":email}
        contacts.append(dict(dict1))
        print("Employee with name:"+name+"is added successfully")
    # save_to_file("contactdb")
    pass

def view_contacts():
    print(contacts)
    # Your code here
    pass

def search_contact(name):
    # Your code here
    for idx in range(0,len(contacts)):
        if contacts[idx]["name"]==name:
            print(f"Record with following{name} is found,pfb details:")
            print(f"Name:{contacts[idx]["name"]}")
            print(f"Phone:{contacts[idx]["phone"]}")
            print(f"Email:{contacts[idx]["email"]}")
    # print(contacts[idx])
    pass

def delete_contact(name):
    # Your code here
    global contacts
    for i in range(len(contacts) - 1, -1, -1):
        if contacts[i]["name"]==name:
            print("Entry found")
            del contacts[i]
            print(f"Contact with name:{name}has been deleted successuly")
    # save_to_file("contactdb")
    # idx=dict[name]
    
    # del contacts[idx]
    pass

def save_to_file(filename):
    # Your code here
    with open("./"+filename+".json","w") as file:
        json.dump(contacts, file, indent=2)
    print("Saved to file Successfully")
    pass

def load_from_file(filename):
    # Your code here
    global contacts
    with open("./"+filename+".json","r") as file:
        content=json.load(file)
        for item in content:
            f=False
            for i in range(0,len(contacts)):
                if item["name"]==contacts[i]["name"]:
                    f=True
            if f==False:   
                contacts.append(item)
        print("PFB contents of a file:")
        print(content)
    pass

# Main program loop
def main():
    print("The Database is loaded")
    load_from_file("contactdb")
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")
        
        choice = int(input("Enter your choice (1-7): "))
        if choice==1:
            name=input("Enter the Employee name:")
            phone=input("Enter the Employee Phone number")
            email=input("Enter employee email-id")
            add_contact(name, phone, email)
        elif choice==2:
            view_contacts()
        elif choice==3:
            name=input("Enter the Name to be searched")
            search_contact(name)
        elif choice==4:
            name=input("Enter the name of employee which needs to be deleted")
            delete_contact(name)
        elif choice==5:
            save_to_file("contactdb")
        elif choice==6:
            load_from_file("contactdb")
        elif choice==7:
            # save_to_file("contactdb")
            break
        # Implement the menu logic
        
main()