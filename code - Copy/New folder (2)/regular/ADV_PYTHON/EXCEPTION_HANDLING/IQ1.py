''' Can i write more then one except for a single try ?
Ans: Yes. '''

import sys

try:
    x=int(sys.argv[1])
except ValueError:
    print("VE : Please Enter integer input....")
except IndexError:
    print("IE :  Please Enter atleast 1 input ....")
else:
    print("The Given num is : ",x)
