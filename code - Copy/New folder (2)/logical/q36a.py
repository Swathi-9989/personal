
def foo(x):
    x[0]=['def']
    x[1]=['abc']
    return id(x)

#calling
q=['abc','def']
print(id(q)  )
print( foo(q) )

print(id(q)==foo(q))
