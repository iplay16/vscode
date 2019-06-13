#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return
        if len(cost)==1:
            return 0
        if len(cost)==2:
            return min(cost[0],cost[1])
        cost.append(0)
        dp=[0]*len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            dp[i]=min(dp[i-1]+cost[i],dp[i-2]+cost[i])
        return dp[-1]
x=Solution()
x.minCostClimbingStairs([0,1,1,0])
