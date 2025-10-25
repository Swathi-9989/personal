'''
   Enter 2 numbers
   
   Main Menu
   ===============
   1.add
   2.sub
   3.mul
   4.exit
   ===============
   Enter u r choice :  1
   
'''
import sys

a=int(input("Enter a number : "))
b=int(input("Enter b number : "))

print("Main Menu ")
print("==================")
print("1.add \n2.sub \n3.mul \n4.exit")
print("==================")
ch=int(input("Enter u r choice : "))

match ch:
    case 1:
        c=a+b
        print("Add is : ",c)
    case 2:
        if a>b:
            c=a-b
        else:
            c=b-a
        print("Sub is : ",c)
    case 3:
        c=a*b
        print("Mul is : ",c)
    case 4:
        sys.exit()
    case _:
        print("Invalid choice ")
















