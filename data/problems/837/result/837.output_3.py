# @lc app=leetcode id=837 lang=python3
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0.0] * (n + k + 1)
        
        for i in range(k, min(n, k + maxPts)):
            dp[i] = 1.0
        
        dp[k-1] = min(n - k + 1, maxPts) / maxPts
        
        for i in range(k - 2, -1, -1):
            dp[i] = dp[i+1] - (dp[i+1+k] - dp[i+1]) / maxPts
        
        result = sum(dp[:k])
        
        return result