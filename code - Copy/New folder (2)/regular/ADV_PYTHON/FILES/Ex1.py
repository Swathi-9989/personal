
f=open("data1.txt","w")

print("File name is : ",f.name)
print("File mode is : ",f.mode)
print("File is readable ? : ",f.readable())
print("File is writable ? : ",f.writable())
print("File is closed ? : ",f.closed)

f.close()
print("File is closed ? : ",f.closed)
