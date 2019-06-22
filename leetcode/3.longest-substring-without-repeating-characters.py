#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        worddict=collections.defaultdict(int)
        s_len=len(s)
        l,r=0,0
        maxlength=0
        for r,c in enumerate(s):
            worddict[c]+=1
            if worddict[c]==2:
                maxlength=r-l if r-l>maxlength else maxlength
                while(True):
                    worddict[s[l]]-=1
                    l+=1
                    if(s[l-1]==s[r]):
                        break
        return maxlength if r-l+1<maxlength else r-l+1   
if __name__=='__main__':
    s=Solution()
    s.lengthOfLongestSubstring(" ")
