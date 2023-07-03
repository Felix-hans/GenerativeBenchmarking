# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            take_one = stoneValue[i] - dp[i + 1]
            take_two = sum(stoneValue[i:i + 2]) - dp[i + 2]
            take_three = sum(stoneValue[i:i + 3]) - dp[i + 3]
            
            dp[i] = max(take_one, take_two, take_three)
        
        score_diff = dp[0]
        
        if score_diff > 0:
            return "Alice"
        elif score_diff < 0:
            return "Bob"
        else:
            return "Tie"