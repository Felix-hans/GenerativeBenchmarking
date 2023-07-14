# @lc app=leetcode id=837 lang=python3
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + k + 1)
        dp[0] = 1.0
        cumulative_prob = 0.0

        for i in range(1, n + k + 1):
            if i <= k:
                cumulative_prob += dp[i - 1] / maxPts
            else:
                cumulative_prob += dp[i - 1] / maxPts - dp[i - k - 1] / maxPts

            dp[i] = cumulative_prob

            if i > n:
                dp[i] -= dp[i - (n + 1)]

        return dp[n]