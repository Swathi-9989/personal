
f=open("data3.txt","w")
data=input("Enter data press * for exit ") #shashi

while data!='*':
    f.write(data+"\n")
    data=input()

f.close()
print("Data is Saved ")
    
