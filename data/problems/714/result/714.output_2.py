# @lc app=leetcode id=714 lang=python3
class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n < 2:
            return 0
        
        cash = 0  # maximum profit if we don't own any stock
        hold = -prices[0]  # maximum profit if we own a stock
        
        for i in range(1, n):
            cash = max(cash, hold + prices[i] - fee)
            
            hold = max(hold, cash - prices[i])
        
        return cash