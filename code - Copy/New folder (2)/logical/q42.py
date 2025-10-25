lst1=[1,2,3,4]
lst2=[2,4,5,6]
lst3=[2,6,7,8]
res=list() #[1,3,5,7,8]

res.extend(i for i in lst1 if i not in (lst2+lst3) and i not in res)
res.extend(i for i in lst2 if i not in (lst1+lst3) and i not in res)
res.extend(i for i in lst3 if i not in (lst1+lst2) and i not in res)
print(res)
