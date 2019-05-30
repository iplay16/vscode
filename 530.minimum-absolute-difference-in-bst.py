#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if len(preorder)==0:
        return
    tree=TreeNode(preorder[0])
    index=inorder.index(preorder[0])
    leftin=inorder[:index]
    rightin=inorder[index+1:]
    index=len(leftin)+1
    leftpre=preorder[1:index]
    rightpre=preorder[index:]
    tree.left=self.recursebuildTree(leftpre,leftin)
    tree.right=self.recursebuildTree(rightpre,rightin)
    return tree
    
def buildtreefromlist(li):
    if len(li)==0:
        return
    # tree=TreeNode(li.pop(0))
    # queue=[]
    # queue.push(tree)
    # while(len(li)!=0):
    #     node=queue.pop(0)
    #     if len(li)!=0:
    #         node.left=li.pop(0)
    #         queue.push(node)
    #     if  len(li)!=0:
    #         node.left=li.pop(0)
    #         queue.push(node)               
    # return tree
    treelist=[]
    for i in li:
        if i is None:
            treelist.append(None)
        else:
            treelist.append(TreeNode(i))

    length=len(treelist)
    for i in range(len(treelist)):
        if treelist[i] is not None and 2*i+1<length:
            treelist[i].left=treelist[2*i+1]
        if treelist[i] is not None and 2*i+2<length:
            treelist[i].right=treelist[2*i+2]
    return treelist[0]

def preorder(tree):
    if tree is not None:
        print(tree.val)
        preorder(tree.left)
        preorder(tree.right)

def inorder(tree):
    if tree is not None:
        preorder(tree.left)
        print(tree.val)
        preorder(tree.right)



import binarytree
import sys
class Solution:
    def __init__(self):
        self.pre={"val":sys.maxsize}
        self.minAD=sys.maxsize
    def getMinimumDifference(self, root:TreeNode) -> int:
        self.inordersolveSD(root,self.pre)
        return self.minAD

    def inordersolveSD(self,tree,pre):
        if tree is not None:
            print("pre:",pre,"tree.val:",tree.val,"self.minAD",self.minAD)
            self.inordersolveSD(tree.left,pre)
            self.minAD=min(self.minAD,abs(tree.val-pre["val"]))
            pre["val"]=tree.val
            self.inordersolveSD(tree.right,pre)


if __name__=='__main__':
    l=[1564,1434,3048,1,None,None,3184]
    print(binarytree.build(l))
    tree=buildtreefromlist(l)
    sol=Solution()
    sol.getMinimumDifference(tree)
    print(sol.minAD)
    