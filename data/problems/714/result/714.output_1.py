# @lc app=leetcode id=714 lang=python3
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        cash = 0  # maximum profit when not holding any stock
        hold = -prices[0]  # maximum profit when holding a stock
        
        for i in range(1, n):
            cash = max(cash, hold + prices[i] - fee)  # Either continue not holding the stock or sell the stock
            hold = max(hold, cash - prices[i])  # Either continue holding the stock or buy a new stock
        
        return cash