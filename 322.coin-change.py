0#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import List
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        coinnumber=[sys.maxsize]*(amount+1)
        for i in range(1,(amount+1)):
            for coin in coins:
                if i-coin<0:
                    continue
                if i==coin:
                    coinnumber[i]=1
                coinnumber[i]=min(coinnumber[i-coin]+1,coinnumber[i])
        return coinnumber[amount] if coinnumber[amount]!=sys.maxsize else -1

x=Solution()          
x.coinChange([1,2,5],11)

