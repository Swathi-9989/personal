sno=int(input("enter a number :"))
print("main menu")
print("=========================")

match sno:
    case sno =="100":
        print("police")
    case sno =="101":
        print("fire")
    case sno =="104":
        print("medical")
    case sno =="108"
         print("EMRO")
    case _:
        print("invalid")
