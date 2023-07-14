# @lc app=leetcode id=123 lang=python3
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        max_transactions = 2

        dp = [[0] * (n + 1) for _ in range(max_transactions + 1)]

        for i in range(1, max_transactions + 1):
            min_price = prices[0]
            for j in range(1, n + 1):
                min_price = min(min_price, prices[j - 1] - dp[i - 1][j - 1])
                dp[i][j] = max(dp[i][j - 1], prices[j - 1] - min_price)

        return dp[max_transactions][n]