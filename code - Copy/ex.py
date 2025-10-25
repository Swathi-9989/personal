lst=['suda','swathi','priya','rama']

'''
for i in lst:
        if len(i)>3 and i[3]=='a' :
             print(i)
        else :
           pass

lst1=[i for i in lst if len(i)>=4 and i[3]=='a']
print(lst1) 
i=list(map(lambda x : x if  lst[3]=='a' else ,lst))
print(i)

def myfun() :
    for i in lst:
        if len(i)>3 and i[3]=='a' :
             print(i)

#calling
print("reslut is :",list(map(myfun(),lst)))

a=list(map(lambda x: x if len(lst)>=4 and if lst[3]=='a'  ,lst))'''
#a=map(lambda x: x if len(x)>4,lst)

result = list(map(lambda x: len(x) >= 4 and x[3] == 'a', lst))
print("result is :",result)


























