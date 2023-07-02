# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)  # Dynamic programming table

        for i in range(n - 1, -1, -1):
            best_score = float('-inf')

            for j in range(1, 4):
                if i + j <= n:
                    score = sum(stoneValue[i:i+j]) - dp[i + j]
                    best_score = max(best_score, score)

            dp[i] = best_score

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"