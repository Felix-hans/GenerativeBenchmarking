# @lc app=leetcode id=121 lang=python3
class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                max_profit = max(max_profit, profit)

        return max_profit