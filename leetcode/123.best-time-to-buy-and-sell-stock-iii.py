#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        self.maxprofit=0
        length=len(prices)
        dp=[[None] *length]*length
        for j in range(length):
            for i in range(j+1,length):
                dp[j][i]=max(dp[j][i-1],self.maxProfitinOne(prices[j:i]))

        for k in range(length-1):
            self.maxprofit=max(self.maxprofit,dp[0][k]+dp[k+1][length-1])
        return self.maxprofit

    def maxProfitinOne(self, prices: List[int]) -> int:
        if not prices:
            return 0
        self.lastprice=prices[0]
        self.totalprofit=0
        for price in prices:
            if price>self.lastprice:self.totalprofit+=price-self.lastprice
            self.lastprice=price
        return self.totalprofit
        #max{dp[i][j]+dp[i+1][k]}

