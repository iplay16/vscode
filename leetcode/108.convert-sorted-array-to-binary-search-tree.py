#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        self.nums=nums
        root=TreeNode('#')
        self.arraytoBST(root,0,len(nums)-1)
        return root

    def arraytoBST(self,root,low,high):
        middle=low+((high-low)>>1)
        root.val=self.nums[middle]
        if low<=middle-1:
            root.left=TreeNode('#')
            self.arraytoBST(root.left,low,middle-1)
        if middle+1<=high: 
            root.right=TreeNode('#')   
            self.arraytoBST(root.right,middle+1,high)

