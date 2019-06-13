#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        self.lastprice=prices[0]
        self.totalprofit=0
        for price in prices:
            if price>self.lastprice:self.totalprofit+=price-self.lastprice
            self.lastprice=price
        return self.totalprofit
            

