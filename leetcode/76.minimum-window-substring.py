#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#https://blog.csdn.net/qq_17550379/article/details/83014880
import sys
from collections import defaultdict
class Solution:
    def minWindow(self, s, t):
        mem = defaultdict(int)
        for c in t:
            mem[c] += 1
        t_len = len(t)
        
        minL, minR = 0, float('inf')
        
        l = 0
        for r, c in enumerate(s):
            if mem[c] > 0:
                t_len -= 1
            mem[c] -= 1
                
            if t_len == 0:
                while mem[s[l]] < 0:
                    mem[s[l]] += 1
                    l += 1
                    
                if r - l < minR - minL:
                    minL, minR = l, r
                
                mem[s[l]] += 1
                t_len += 1
                l += 1
        
        return '' if minR == float('inf') else s[minL:minR+1]

if __name__=='__main__':
    # s="ADOBECODEBANC"
    # t="ABC"
    # BANC
    s="aa"
    t="aa"

    x=Solution()
    r=x.minWindow(s,t)
    print(r)


    