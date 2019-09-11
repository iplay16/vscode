#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.mDepth(root)

    def mDepth(self,root,depth=0):
        if not root:
            return depth
        ld=self.mDepth(root.left,depth+1) 
        rd=self.mDepth(root.right,depth+1)
        return ld if ld<rd else rd
