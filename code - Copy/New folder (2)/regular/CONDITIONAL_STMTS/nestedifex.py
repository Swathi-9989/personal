''' Nested If ....
       If with in the if... called nested if ...

Example:
   Accept age and gender from the user findout
   status of the condidate
   
   if gen is m or M then check the age
           if age>=21 then print Major else print Minor

   if gen is f or F then check the age
           if age>=18 then print Major else print Minor

   else third-gender
'''
gender = input("Enter any char : ")
age = int(input("Enter age : "))

if gender=='m' or gender=='M':
    print("Gender is Male ")
    if age>=21:
        print("status : Major")
    else:
        print("status : Minor")    

elif gender=='f' or gender=='F':
    print("Gender is Female")
    if age>=18:
        print("status : Major ")
    else:
        print("status : Minor ")
else:
    print("Third-Gender")
















