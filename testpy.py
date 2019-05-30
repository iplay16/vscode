def convertToTitle(self, n) -> str:
    a=n/26
    b=n%26
    if(a==0):
        return chr(b)
    else:
        return chr(a)+chr(b)
convertToTitle(2)