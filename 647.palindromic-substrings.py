#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count=0
        for i,_ in enumerate(s):
            self.count+=1
            while(i-1>=0 and i+1<len(s):
                if s[i-1]=s[i+1]

