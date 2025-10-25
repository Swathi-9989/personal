x=10
def myfun():
    global x

    x=x+10
    print(x)

myfun()

print(x)
