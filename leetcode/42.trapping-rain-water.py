#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        li=[]
        sum=0
        h=0
        while(height):
            li.append(height[0])
            for x in height:
                if x<li[0]:
                    li.append(x)
                    continue
                if x>=li[0]:
                    h=min(x,li[0])
                    while(li):
                        sum+=(h-li.pop())
                    li.append(x)
            li.reverse()
            height=li
            li=[]
        return sum
x=Solution()
x.trap([0,1,0,2,1,0,1,3,2,1,2,1])
