'''Convert string in reverse without using slicing '''
s="welcome"
print("Data is : ",s)
s2=""
#App-1
for i in range(len(s)-1,-1,-1):
    s2=s2+s[i]
print("s2 : ",s2)

#App-2
lst=[]
for i in s:
    lst.insert(0,i)

#list to string conversion  s.join(iterable) -> str
s3="".join(lst)
print("Res : ",s3)



