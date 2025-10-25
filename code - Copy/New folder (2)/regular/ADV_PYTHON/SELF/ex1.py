class Test:
    def method1(self):
        print("mtd-1")
        print(self)
        print("--------------------")

    def method2(self):
        print("mtd-2")
        print(self)

#calling
t=Test()
print("From outside of the cls")
print("t : ",t)
print("------------------")
t.method1()
t.method2()
