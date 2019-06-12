#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) +1 )
        dp[0] =True
        for i in range(1,len(dp)):
            for word in wordDict:
                if i - len(word) < 0:
                    continue
                if s[i-len(word):i] ==  word:
                    # dp[i]表示字符串s[:i] 是否可拼接而成
                    #如果对于每一个word,s[:i-len(word)]可以被拼接而成，那么s[:i]可由s[:i-len(word)]和word拼接而成
                    dp[i] = dp[i-len(word)] or dp[i]
        return dp[-1]

x=Solution()
x.wordBreak("cars",["car","ca","rs"])
