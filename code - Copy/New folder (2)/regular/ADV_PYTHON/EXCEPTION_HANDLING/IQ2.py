''' Can i handle more than one Exception
    by a single except ?
    Ans:  yes, In this case we have write all possible
    Exceptions in the form of tuple in Except block '''

import sys

try:
    x=int(sys.argv[1])
except (ValueError,IndexError):
    print("VE | IE : Please Enter atleast an integer input.")
else:
    print("The given number is : ",x)


