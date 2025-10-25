s="hello"
d={}
for i in s:
    d[i]=d.get(i,0)+1
print(d)

print("============")

from collections import Counter
def repeat():
    s = "swiss"
    count = Counter(s)
    for c in s:
        if count[c] == 1:
            print("First non-repeating character:", c)
            break
    else:
        print(" non-repeating character not found")
r=repeat()
print(r)


print("=============")

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibo(n-1)+fibo(n-2)

f=fibo(3)
print(f)

print("===========")

a=input("enter a value : ")
b=input("enter a value : ")
if len(a) == len(b):
    if sorted(a) == sorted(b):
        print("given is an anagram")
else:
    print("not an anagram")

print("===============")


a=int(input("Enter First number "))
sumf=0
b=int(input("Enter Second number : "))
sums=0

for i in range(1,a):
    if a%i==0:
        sumf=sumf+i

for j in range(1,b):
    if b%j==0:
        sums=sums+j

if sumf==b and sums==a:
    print("Both are amicable")
else:
    print("Both are not amicable")


p=input("enter a string :")
q=input("enter a string :")
sumf=0
sumg=0
for i in range(1,a):
    sumf=sumf+i
for j in range(1,b):
    sumg=sumg+j

    
 if sumf==b and sumg==a :
     print("Is an anagram")
else:
    print("not an anagram")




