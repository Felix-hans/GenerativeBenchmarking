# @lc app=leetcode id=837 lang=python3
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + maxPts + 1)
        for i in range(n, min(n + maxPts, k - 1), -1):
            dp[i] = 1.0

        dp[k - 1] = float(min(n - k + 1, maxPts)) / maxPts

        for i in range(k - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + maxPts + 1] - dp[i + 1]) / maxPts

        return sum(dp[:k])