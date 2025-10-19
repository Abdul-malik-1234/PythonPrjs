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
    found=False
    for contact in range(0,len(contacts)):
        if contacts[contact]["name"]==name:
            found=True
            break
    if found==True:
        print(f"The entry already exists,the requested entry{contacts[contact]["name"]} is not added")
    else:
        dict1={"name":name,"phone":phone,"email":email}
        contacts.append(dict(dict1))
        print("Employee with name: "+name+" is added successfully")
    pass

def view_contacts():
    print(contacts)
    # Your code here
    pass

def search_contact(name):
    # Your code here
    found=False
    for idx in range(0,len(contacts)):
        if contacts[idx]["name"]==name:
            found=True
            print(f"Record with following{name} is found,pfb details: ")
            print(f"Name: {contacts[idx]["name"]}")
            print(f"Phone: {contacts[idx]["phone"]}")
            print(f"Email: {contacts[idx]["email"]}")
    if found==False:
        print(f"The requested contact with name: {name} is not found")
    # print(contacts[idx])
    pass

def delete_contact(name):
    # Your code here
    global contacts
    found=True
    for contact in range(len(contacts) - 1, -1, -1):
        if contacts[contact]["name"]==name:
            found=False
            print("Entry found")
            del contacts[contact]
            print(f"Contact with name: {name} has been deleted successuly")
    if found==True:
        print("The contact with entered name doesn't exit")
    pass

def save_to_file(filename):
    # Your code here
    try:
        with open("./"+filename+".json","w") as file:
            json.dump(contacts, file, indent=2)
        print("Saved to file Successfully")
    except Exception as e:
        print("Process terminated due to exception:"+e)
    pass

def load_from_file(filename):
    # Your code here
    global contacts
    try:
        with open("./"+filename+".json","r") as file:
            content=json.load(file)
            for item in content:
                f=False
                for i in range(0,len(contacts)):
                    if item["name"]==contacts[i]["name"]:
                        f=True
                if f==False:   
                    contacts.append(item)
            print("PFB contents of a file: ")
            print(content)
    except Exception as e:
        print(f"Process terminated due to exception: {e} ")
        
    pass

def validate_email(email):
    # Check if email contains @ and .
    atTheRate=0
    dot=0
    idx=0
    for letter in email:
        if letter=='@':
            if idx==0:
                return False
            atTheRate+=1
        if letter=='.':
            if idx==0:
                return False
            dot+=1
        idx+=1
    if atTheRate==1 and dot==1:
        return True
    return False

def validate_phone(phone):
    # Check if phone contains only numbers
    return len(phone)==10 and phone.isdigit()

def edit_contact(name):
    # Find contact and allow updating phone/email
    global contacts
    while True:
        print("Select your choice")
        print("1 - Name")
        print("2 - Phone Number")
        print("3 - Email Id")
        
        option=int(input("Select an option"))
        idx=0
        found=False
        for i in range(0,len(contacts)):
            if contacts[i]["name"]==name:
                found=True
                idx=i
                break   
        if found==False:
            print("The contact with give name is not found")
            return
        if option>=1 and option<=3:
            if option==1:
                newName=input("Please enter new name")
                contacts[idx]["name"]=newName
                print("Name is updated successfully")
            elif option==2:
                phoneNumber=input("Please enter new Phone Number")
                contacts[idx]["phone"]=phoneNumber
                print("Phone no. is updated successfully")
            elif option==3:
                emailId=input("Please enter new email id")
                contacts[idx]["email"]=emailId
                print("Email is updated successfully")
            break
        else:
            print("You've entered a wrong option,please reenter")
    pass

def create_backup():
    # Save with timestamp in filename
    pass

# Main program loop
def main():
    print("The Database is loaded ")
    load_from_file("contactdb")
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Edit contact")
        print("8. Exit")
        # Implement the menu logic
        choice = input("Enter your choice (1-8): ")
        if choice.isdigit():
            choice=int(choice)
            if not choice in range(1,9):
                print("You've entered an invalid choice value")
            elif choice==1:
                name=input("Enter the Employee name:")
                while True:
                    phone=input("Enter the Employee Phone number")
                    if validate_phone(phone)==True:
                        print("You've entered a valid phone number")
                        break
                    print("You've enter an invalid phone number,please renter")
                        
                while True:
                    email=email=input("Enter Employee email-id")
                    if validate_email(email)==True:
                        print("You've entered a valid email id")
                        break
                    print("You've enter an invalid email-id,please renter")
                add_contact(name, phone, email)
            elif choice==2:
                view_contacts()
            elif choice==3:
                name=input("Enter the Name to be searched: ")
                search_contact(name)
            elif choice==4:
                name=input("Enter the name of employee which needs to be deleted: ")
                delete_contact(name)
            elif choice==5:
                save_to_file("contactdb")
            elif choice==6:
                load_from_file("contactdb")
            elif choice==7:
                name=input("Please enter the contact name for which fields needs to be edited")
                edit_contact(name)
                
            elif choice==8:
                break
        else:
            print("Please enter proper input")
        
        
main()