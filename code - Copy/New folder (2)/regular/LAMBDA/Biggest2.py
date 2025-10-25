
def biggest(x,y):
    if x>y:
        return x
    else:
        return y

big=biggest(10,20)
print("Biggest is : ",big)
print("=========================")

biggest=lambda x,y:  x if x>y else y
b=biggest(10,20)
print("Biggest is : ",b)
