#0 1 2
#s a  i

def strRev(s):
    if s=="":
        return s
    else:
        x=s[len(s)-1]
        print(x,end="")
        s=s[0:len(s)-1:]
        strRev(s)


#calling
strRev("sai")
