# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            dp[i] = min(dp[i], dp[i - 1] + 1)
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i // 2] + 1)
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i // 3] + 1)

        return dp[n]