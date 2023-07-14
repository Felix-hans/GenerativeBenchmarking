# @lc app=leetcode id=123 lang=python3
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        
        max_profit_1 = [0] * n
        max_profit_2 = [0] * n
        
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            max_profit_1[i] = max(max_profit_1[i-1], prices[i] - min_price)
        
        max_price = prices[n-1]
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i])
            max_profit_2[i] = max(max_profit_2[i+1], max_price - prices[i])
        
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_profit_1[i] + max_profit_2[i])
        
        return max_profit