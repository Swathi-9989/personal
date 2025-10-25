''' print alternative words in reverse
    Input: have a nice day dear friend
    output: a yad dneirf 
'''

data="have a nice day dear friend"
print("data is : ",data)

lst=data.split() #[have,a,nice,day,dear,friend]

for i in range(len(lst)):
    if i%2!=0:
        print( lst[i][ ::-1] )

