import sys
import time

contacts={}

def add_contact():
    name=input("Enter u r name : ").upper()
    if name in contacts.keys():
        print("Sorry Rec  is already Existed ")
    else:
        mobile=input("Enter u r contact no : ")
        contacts[name]=mobile
        print("Contact is Saved ")            

    print("---------------------------")
    time.sleep(3)

def search_contact():
    name=input("Enter name for search : ").upper()
    
    if name in contacts.keys():
        print(f"Name is : {name}")
        print(f"Contact is : {contacts.get(name)}")               
    else:
        print("Sorry Contact is not found ")
        time.sleep(3)

def remove_contact():
    name=input("Enter name : ").upper()

    if name in  contacts.keys():
        del contacts[name]
        print("Cont is deleted ....!!! ")
    else:
        print("Sorry Contact is not found ")
    time.sleep(3)

def list_contacts():
    if contacts:
        for k,d in contacts.items():
            time.sleep(.5)
            print("Name is : ",k)
            print("Contact is : ",d)
            print("------------------------")
    else:
        print("Sorry No Contacts ")
    time.sleep(3)

while True:
    print("Contacts Operations")
    print("==================")
    print("1.Add contact \n2.Search contact  \n3.Remove Contact \n4.List Contacts \n5.Exit")
    print("------------------------------")
    opt=int(input("Enter u r choice : "))

    match opt:
        case 1:
            add_contact()            
        case 2:
            search_contact()            
        case 3:
            remove_contact()
        case 4:
            list_contacts()
        case 5:
            sys.exit()
        case _:
            print("Invalid Operation")


        

