'''
    IS-A Relationship
        >> Process of Creating the sub class
        by extending the properties of the
        super class into the sub class.

    Syn: <class>   <SuperClsName>:
    .... Fields
    .... Methods

    <class>   <SubClsName>(<SuperClsName>):
    .... Fields
    .... Methods

    Note:
    > private members are not inherited
    > static and class members are inherited
    > Inherited members are acts as regular members
    of the class.   
'''
class SuperA:
    def method1(self):
        print("Mtd-1 of SA")

    @classmethod
    def method2(cls):
        print("cls mtd of SA")

    @staticmethod
    def method3():
        print("static mtd of SA")

class SubB(SuperA):
    pass

#calling
sb=SubB()
sb.method1()
sb.method2()
sb.method3()





















