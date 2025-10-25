'''
    Q: how to reverse the string without using slicing 
              data='welcome'

     Q: findout the given string is polindrome or not
             data='madam'

     Step1. revese the string
     step 2 : compare the reversed string with org string
     if both are same then it is polindrome else not
     
'''
data="madam"
rev=data[ : :-1]   #madam
if data==rev:
    print("Polindrome")
else:
    print("Not Polindrome")

#App-2
data="madam"
if data==data[ : :-1]:
    print("Polindrome")
else:
    print("Not polindrome")

#App-3
print("pol") if data==data[ : :-1] else print("not polin")


    











