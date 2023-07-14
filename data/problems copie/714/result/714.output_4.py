# @lc app=leetcode id=714 lang=python3
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = [0] * n  # keep track of the maximum profit when holding the stock
        sell = [0] * n  # keep track of the maximum profit when not holding the stock
        
        buy[0] = -prices[0]  # buy the stock on the first day
        for i in range(1, n):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i] - fee)
        
        return sell[n-1]  # return the maximum profit when not holding the stock on the last day