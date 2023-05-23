# @lc app=leetcode id=70 lang=python3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        
        dp[1] = 1  # There's only one way to climb 1 step
        dp[2] = 2  # There are two ways to climb 2 steps (1 step + 1 step or 2 steps)
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]