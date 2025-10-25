a=[1,2,3,4]
b=[3,4,5,6]

print("list a : ",a)
print("list b : ",b)

'''
fsa=frozenset(a)  #frozenset(iterable) -> FS
fsb=frozenset(b)
fsc=fsa.intersection(fsb)
c=list(fsc)  '''


print("Res :",list(frozenset(a).intersection(frozenset(b))))







