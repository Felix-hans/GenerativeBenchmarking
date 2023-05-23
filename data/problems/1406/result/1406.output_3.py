# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            take = 0
            for j in range(i, min(n, i + 3)):
                take += stoneValue[j]
                dp[i] = max(dp[i], take - dp[j + 1])

        score = dp[0]
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"