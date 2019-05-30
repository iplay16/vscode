#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def tranprelist(self):
        self.li=[]
        self.preorder(self)
        return self.li

        tranprelist(li)
    def preorder(self,tree):
        if tree is not None:
            # visit=self.visit
            self.visit(tree)
            self.preorder(tree.left)
            self.preorder(tree.right)

    def visit(self,tree):
        self.li.append(tree.val)
        
from typing import List
import binarytree

class Solution:
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

    def recursebuildTree(self,preorder: List[int], inorder: List[int]) -> TreeNode:
        # if not preorder:
        #     return
        # if not inorder:
        #     return
        # # if not tree:
        # #     return
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

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None
    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child
    def set_root_val(self,obj):
        self.key = obj
    def get_root_val(self):
        return self.key

# class TreeNode(BinaryTree):
#     pass

if __name__=='__main__':
    list1=[3,9,20,None,None,15,7]
    preorder=[3,9,20,15,7]
    inorder=[9,3,15,20,7]
    mybst=binarytree.build(list1)
    print(mybst)
    sol=Solution()
    buildtree=sol.buildTree(preorder,inorder)
    print(buildtree.tranprelist())
    x = BinaryTree('a')
    x.insert_left('b')
    x.insert_right('c')
    x.get_right_child().insert_right('f')
