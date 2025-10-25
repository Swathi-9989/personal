''' Accept no.of.pens , no.of.books,
calculate bill, discount, netbill
          discount is 10% on bill '''

npp=int( input("Enter no.of.pen : ") )
nbp=int( input("Enter no.of.books : "))

bill=(npp*25)+(nbp*50)
dis=(bill*10)/100
net=bill-dis

print("Bill is : ",bill)
print("Dis is : ",dis)
print("Net is : ",net)
