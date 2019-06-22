# class tools:    
#     def resuildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if len(preorder)==0:
#             return
#         tree=TreeNode(preorder[0])
#         index=inorder.index(preorder[0])
#         leftin=inorder[:index]
#         rightin=inorder[index+1:]
#         index=len(leftin)+1
#         leftpre=preorder[1:index]
#         rightpre=preorder[index:]
#         tree.left=self.recurseresuildTree(leftpre,leftin)
#         tree.right=self.recurseresuildTree(rightpre,rightin)
#         return tree
#%%
def runTest(instance,action,data):
    li=[]
    for a,d in zip(action[1:],data[1:]):
        ret=getattr(instance,a)
        res=ret(*d) #d列表解包成参数列表
        li.append(res)
        # print(res)
    return li