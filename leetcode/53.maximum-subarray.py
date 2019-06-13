#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length=len(nums)
        dp=[None for i in range(length)]
        # self.maxsum=-sys.maxsize-1
        dp[0]=nums[0]
        for i in range(1,length):
            dp[i]=max(nums[i],dp[i-1]+nums[i])

        for i in range(length):
            if dp[i]>self.maxsum:
                self.maxsum=dp[i]
        return self.maxsum
x=Solution()
x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
