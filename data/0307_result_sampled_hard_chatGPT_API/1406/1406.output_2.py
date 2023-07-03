# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-float('inf')] * n

        def maxScore(position):
            if position >= n:
                return 0

            if dp[position] != -float('inf'):
                return dp[position]

            max_val = float('-inf')

            for i in range(1, 4):
                if position + i <= n:
                    score_diff = sum(stoneValue[position:position + i]) - maxScore(position + i)
                    max_val = max(max_val, score_diff)

            dp[position] = max_val
            return dp[position]

        score_diff = maxScore(0)

        if score_diff > 0:
            return "Alice"
        elif score_diff < 0:
            return "Bob"
        else:
            return "Tie"