# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)  # Initialize the dp array with negative infinity
        dp[n] = 0  # Base case: if there are no stones left, the score is 0

        def dfs(idx):
            if dp[idx] != float('-inf'):
                return dp[idx]

            max_score = float('-inf')
            curr_score = 0
            for i in range(idx, min(idx + 3, n)):
                curr_score += stoneValue[i]
                max_score = max(max_score, curr_score - dfs(i + 1))

            dp[idx] = max_score
            return dp[idx]

        score = dfs(0)
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"