
class minmaxnode:
    def __init__(self,x,val=0):
        self.stand=x #A stand me ,B stand you 
        self.val=val #val stand the A's profit
        self.childnodelist=[]
    
    def addchild(self,c):
        self.childnodelist.append(c)
    
    def preorder(self,root):
        if root:
            for c in root.childnodelist:
                self.preorder(c)
            # print(root.stand)
            # print(root.val)
    #A will chose the biggest val of child
    #B will chose the smallest val of child
    def counttree(self,root):
        if root:
            if not root.childnodelist:
                return root.val
            else:
                if root.stand=="A":
                    max_val=0
                    for c in root.childnodelist:
                        val=self.counttree(c)
                        # print("childval:",val)
                        if val>max_val:
                            max_val=val
                            # print("max_val:",max_val)
                    root.val=max_val
                    return root.val

                #B will chose the smallest val of child
                if root.stand=="B":
                    min_val=100000
                    for c in root.childnodelist:
                        val=self.counttree(c)
                        # print("childval:",val)
                        if val<min_val:
                            min_val=val
                            # print("min_val:",min_val)
                    root.val=min_val
                    # print(root.val)
                    return root.val            

# https://blog.csdn.net/tangchenyi/article/details/22920031
if __name__=='__main__':
    root=minmaxnode("A")
    root.addchild(minmaxnode("B"))
    root.addchild(minmaxnode("B"))
    root.addchild(minmaxnode("B"))
    n1=root.childnodelist[0]
    n2=root.childnodelist[1]
    n3=root.childnodelist[2]

    n1.addchild(minmaxnode("A",7))
    n1.addchild(minmaxnode("A",3))
    
    n2.addchild(minmaxnode("A",15))

    n3.addchild(minmaxnode("A",1))
    n3.addchild(minmaxnode("A",12))
    n3.addchild(minmaxnode("A",20))
    n3.addchild(minmaxnode("A",22))

    res=root.counttree(root)
    print(res)