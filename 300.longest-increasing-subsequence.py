#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        dp=[1]*len(nums)
        maxlengthoflis=1
        for i in range(1,len(nums)):
            for j in range(i-maxlengthoflis,i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[j]+1,dp[i])
            maxlengthoflis=max(maxlengthoflis,dp[i])
        return maxlengthoflis

x=Solution()
x.lengthOfLIS([1,3,6,7,9,4,10,5,6])
