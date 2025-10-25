class Shashi:
    def __init__(self):
        self.name="Mr.Shashi Kumar"
        self.job="Digital IT Coach "

    def __str__(self):
        return self.name+" as "+self.job

#calling
lst=list()
print(lst)

s=Shashi()
print(s)

''' While printing the reference variable
internally PVM calls _ _str_ _(self) from
object class.

_ _str_ _(self) always return the hashcode
   of the object.

If u want other than the hash code then
we have to override _ _str_ _(self) from
object class. '''
















