'''Input: B4A3C1
   Output: ABC134 '''

data="B4A3C1"
print("Data is : ",data)

char=[]
digits=[]

for i in data:
    if i.isalpha():
        char.append(i)
    elif i.isdigit():
        digits.append(i)

#list to string conversion  s.join(iterable) -> str
x="".join(  sorted(char)  )  #ABC
y="".join( sorted(digits) ) #431
res=x+y
print("Res : ",res)








        


    
