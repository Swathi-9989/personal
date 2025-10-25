
fn=int(input("Enter First number "))
sumf=0
sn=int(input("Enter Second number : "))
sums=0

for i in range(1,fn):
    if fn%i==0:
        sumf=sumf+i

for j in range(1,sn):
    if sn%j==0:
        sums=sums+j

print("Sumf is : ",sumf)
print("Sums is : ",sums)

if sumf==sn and sums==fn:
    print("Both are amicable")
else:
    print("Both are not amicable")


        



