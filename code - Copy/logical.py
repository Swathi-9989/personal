#convert string in reverse with out using slicing
s="welcome"
print("data is :",s)
s2=""
for i in range(len(s)-1,-1,-1):
    s2=s2+s[i]
print("s2:",s2)
#count the frequency of char
s="hello"
res={}
for i in s :
    res[i]=res.get(i,0)+1
print("res :",res)
#finding missing number
lst=[1,2,4,5]
n=len(lst)+1
exp_sum=n*(n+1)//2
act_sum=sum(lst)
mn=exp_sum-act_sum
print("missing number is :",mn)
#swapping the first and last elements in the list
lst=[10,20,30,40,50,60]
print("list :",lst)
temp=lst[0]
lst[0]=lst[-1]
lst[-1]=temp
print(lst)




