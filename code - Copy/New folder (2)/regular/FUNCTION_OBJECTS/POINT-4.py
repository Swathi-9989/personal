''' A Function can return another function ... '''

def OuterFun():
    def InnerFun():
        for i in range(1,11):
            print("*",end=' ')

    return InnerFun

#calling
inf=OuterFun()
inf()

'''IF u want use the inner function from
outside of the outer function then
outer function need to return the inner function '''
