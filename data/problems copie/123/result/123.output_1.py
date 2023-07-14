# @lc app=leetcode id=123 lang=python3
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        max_k = 2  # Maximum number of transactions allowed

        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]

        for i in range(n):
            for k in range(max_k, 0, -1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[n - 1][max_k][0]