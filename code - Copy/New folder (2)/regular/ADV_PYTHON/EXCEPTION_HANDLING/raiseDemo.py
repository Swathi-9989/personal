''' Accept acno from the user
print valid, if acno is +ve else print
invalid acno by raising the ValueError

      Syn: raise <exceptionClsName>([list of args])
'''

acno=int(input("Enter acno : "))

if acno>=0:
    print("Valid Acno ")
else:
    try:
        raise ValueError()
    except ValueError:
        print("VE : Invalid Acno ")







