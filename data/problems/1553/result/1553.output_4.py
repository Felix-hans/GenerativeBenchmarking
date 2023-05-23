# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        dp = [0] * (n + 1)  # Initialize dp array
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1  # Eat 1 orange
            
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i // 2] + 1)  # Eat i/2 oranges
            
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i // 3] + 1)  # Eat 2*(i/3) oranges
        
        return dp[n]