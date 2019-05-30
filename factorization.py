def isprime(num,primlist):
    for prim in primlist:
        if num%prim==0:
            return False
    return True
def conprimlist(num):
    primlist=[2]
    for i in range(3,num+1):
        if isprime(i,primlist):
            primlist.append(i)
    print(primlist)
    return primlist
def factorize(num):
    primlist=conprimlist(num)
    faclist=[]
    while(num!=1):
        for x in primlist:
            if num%x==0:
                num=num//x
                faclist.append(x)
    return faclist
#QQ Group:598880963
print(factorize(123))