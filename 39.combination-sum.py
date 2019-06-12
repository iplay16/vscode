#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrace(candidates: List[int],sum):
            if sum>target:
                return
            if sum==target:
                res.insert(0,li.copy())
                return
            if not candidates:
                return
            backtrace(candidates[1:],sum)
            li.append(candidates[0])
            backtrace(candidates,sum+candidates[0])
            li.pop()
        li=[]
        res=[]
        backtrace(candidates,0)
        return res
x=Solution()
x.combinationSum([2,3,6,7],7)

