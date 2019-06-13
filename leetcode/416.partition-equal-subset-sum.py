#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum=0
        for n in nums:
            sum+=n
        if sum%2!=0:
            return False
        sum=sum//2
        dp=[False]*(sum+1)
        dp[0]=True
        val=[0]*(sum+1)
        val[0]=0
        for num in nums:
            #if not reversed,the result is contain duplication nums use
            for i in reversed(range(1,sum+1)):
                if i>=num:
                    dp[i]=dp[i] or dp[i-num]
        return dp[-1]
x=Solution()
x.canPartition([1,2,5])
