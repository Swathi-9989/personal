'''
Given an arr[ ]  of n elements , write a python prg. to
search x element in arr[ ] without using membership
operator LS '''

arr=[12,10,20,23,45]
x=120
found=0

for i in arr:    
    if i==x:
        print("Found")
        found=1
        break
    
if found==0:
    print("Not found")

