'''
   input: a4d3e4
   output: aedgei
'''

data="a4d3e4"
print("Data is : ",data)

res=""

for i in data:
    if i.isalpha():
        x=i  #a
        res=res+x
        
    else:
        nl=chr(ord(x)+int(i))
        res=res+(nl)

print("Res : ",res)
        




    
