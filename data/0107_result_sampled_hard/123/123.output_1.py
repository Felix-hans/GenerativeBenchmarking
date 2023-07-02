# @lc app=leetcode id=123 lang=python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy = [float('-inf')] * 3
        sell = [0] * 3

        for price in prices:
            for i in range(1, 3):
                buy[i] = max(buy[i], sell[i-1] - price)
                sell[i] = max(sell[i], buy[i] + price)

        return sell[2]