#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from queue import Queue
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        q=Queue()
        q.put(root)
        i=1
        length=self.__findlast(root)
        res=[None]*lenth

    def __findlast(self,root,index=0):
        if root is None:
            return -1
        leftval=self.__findlast(root.right,index*2+2)
        rigthval=self.__findlast(root.left,index*2+1)
        maxval=max(leftval,rightval)
        return max(index,maxval)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data.pop
        data.pop(0)
        li=data.split(',')
        if li:
            return
        length=len(li)
        for i in range(length):
            if li[i]!="null":
                li[i]=TreeNode(li[i])
            else:
                li[i]==None
        for i in range(length):
            if li[i] is not None:
                li[i].left=li[2*i+1]
                li[i].left=li[2*i+2]
        return li[0]

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

c=Codec()
s=c.serialize(TreeNode("df"))
print(s)
            
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

