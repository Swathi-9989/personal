
class SuperA:
    def method1(self):
        print("mtd-1 of SA")

class SubB:
    def method2(self):
        sa=SuperA()
        sa.method1()
        print("mtd-2 of SB")

#calling
sb=SubB()
sb.method2()
        
