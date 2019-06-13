#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.minprice=sys.maxsize
        self.maxprofit=0
        for price in prices:
            profit=price-self.minprice
            if price<self.minprice:self.minprice=price
            if profit>self.maxprofit:self.maxprofit=profit
        return self.maxprofit
