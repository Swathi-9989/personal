'''
   Accept a number from the user and print
   the number in the word form
      1 - One | 2 - Two | 3 - Three | invalid
'''

n=int(input("Enter a number : "))  #3

match n:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case default:
        print("Invalid")


        

