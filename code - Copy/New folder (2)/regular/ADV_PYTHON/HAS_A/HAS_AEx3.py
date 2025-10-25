class SuperA:
    @staticmethod
    def method1():
        print("static mtd-1 of SA")

class SubB:
    def method2(self):
        sa=SuperA()
        sa.method1()
        SuperA.method1()
        print("Ins mtd-2 of SB")

#calling
sb=SubB()
sb.method2()
