'''
  IQ: Can i handle any possible exception by a
  single Except ?
  ans: Yes.It possible by writing
              except without Exception
              except with Exception
'''
    
import sys

try:
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    z=x/y
    
except Exception as e:
    print("Exception : Sorry unable to continue...")
    print("Reason is : ",e)
    
else:
    print("Result is : ",z)










