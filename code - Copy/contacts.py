import sys
contacts={}
class contact:
    def add(self):
        self.name=input("Enter u r name :").upper()
        if self.name in contacts.keys():
            print("Sorry contact already existing")
        else:
            self.mob=input("Enter Mobile Number")
            contacts[self.name]=self.mob
            print("contact saved")
        print("=====================")
        
    def search(self):
        self.name=input("Enter name to search ").upper()
        if self.name in contacts :
            print(f"name is :{self.name}")
            print(f"Contact is : {contacts.get(self.name)}")
        else:
            print("Contact Not Found ")
            
    def remove(self):
        self.name=input("Enter a name to remove").upper()
        if self.name in contacts:
            delete.contacts[self.name]
            print("Contact is deleted...")
        else :
            print("Contact Not Found")
            
    def List(self):
        if contacts :
            for k,d in contacts.items():
                print("name is",k)
                print("contact is ",d)
                print("============")
        else :
            print("No Contacts Available")


c=contact()
while True :
    print("Contact Operations")
    print("================")
    print("1.Add contact \n 2.Search contact \n 3.Remove contact \n 4.List contact \n 5.Exit")
    print("==============================")
    opt=int(input("Enter u r choice :"))
    
    match opt:
        case 1:
            c.add()
        case 2:
            c.search()
        case 3:
            c.remove()
        case 4:
            c.List()
        case 5:
            sys.exit()
        case _:
            print("operation Not Found")
                
        
