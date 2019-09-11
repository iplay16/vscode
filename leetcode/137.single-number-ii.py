#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        d=collections.defaultdict(int)
        for x in nums:
            d[x]+=1
            if d[x]!=2:
                res^=x
        return res

