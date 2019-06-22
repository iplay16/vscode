class hashtable:
    def __init__(self,n):
        self.length=2
        while(self.length<n):
            self.length=self.length*self.length
        self.li=[None]*n


    def putint(self,obj):
        # h=id(obj)
        # print("h:",h)
        # hashval=h^(h>>16)
        print("self.length:",self.length)
        key=obj&(self.length-1)
        print("key:",key)
        if self.li[key] is None:
            self.li[key]=hashnode(obj)
        else:
            p=self.li[key]
            while(p.node is not None):
                if p.val==obj:#already exist,in some conditions,==need to be override
                    return
                p=p.node
            p.node=hashnode(obj)

class hashnode:
    def __init__(self,val):
        self.val=val
        self.node=None

if __name__=='__main__':
    ha=hashtable(20)
    for x in range(20):
        ha.putint(x)
    a=1
    

