# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)  # DP array to store maximum scores
        
        for i in range(n - 1, -1, -1):
            best_score = float('-inf')
            
            for j in range(i, min(i + 3, n)):
                curr_sum = sum(stoneValue[i:j+1])
                next_score = dp[j + 1] if j + 1 <= n else 0
                best_score = max(best_score, curr_sum - next_score)
            
            dp[i] = best_score
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"