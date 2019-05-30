#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            nums[abs(n)-1]=-abs(nums[abs(n)-1])
        res=[]
        for i in range(len(nums)):
            if(nums[i]>0):
                res.append(i+1)
        return res        
