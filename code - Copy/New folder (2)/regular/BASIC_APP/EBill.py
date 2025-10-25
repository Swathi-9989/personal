''' Accept Present Reading ,
Previous Reading calculate no.of.units
and findout the bill amount
'''

present=int(input("Enter present Reading : "))
previous=int(input("Enter previous Reading : "))

nu=present-previous
bill = nu*2

print("No.of.units : ",nu)
print("Bill amount is : ",bill)

