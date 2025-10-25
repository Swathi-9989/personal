import time

lst=[10,12.12,"Ramesh",123,"Sudha"]
print("lst : ",lst)

for i in lst:
    time.sleep(.5)
    print(i)
print("=============")

class Shashi:
    def __init__(self):
        self.courses=["Java","Oracle","Python"]
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index=self.index+1
        if self.index<len(self.courses):
            return self.courses[self.index]
        else:
            raise StopIteration()        

#calling
s=Shashi()
for i in s:
    time.sleep(.2)
    print(i)










        
