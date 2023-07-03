# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)  # Create a DP array to store the optimal scores
        
        for i in range(n-1, -1, -1):
            dp[i] = float('-inf')  # Initialize each score to negative infinity
            
            for k in range(1, 4):
                if i + k <= n:
                    score = sum(stoneValue[i:i+k]) - dp[i+k]
                    dp[i] = max(dp[i], score)
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"