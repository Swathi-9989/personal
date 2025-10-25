''' input :  sky is blue
   Output: blue is sky 
                      don't use predefined functions '''

data="sky is blue"
print("Data is : ",data)
lst=data.split()  #s.split([chars]) -> list
#[sky,is,blue]
for i in lst[ : :-1]:
    print(i,end=' ')

#App-2:
data="sky is blue"
lst=data.split()   #[sky,is,blue]
lst2=[]
for i in range(2,-1,-1):
    lst2.append(lst[i])

#iterable to string type is s.join(iterable) -> str
r=" ".join(lst2)
print("\n res : ",r)







    

