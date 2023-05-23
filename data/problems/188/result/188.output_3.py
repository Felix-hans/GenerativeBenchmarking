# @lc app=leetcode id=188 lang=python3
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        if k >= n // 2:
            return self.maxProfitUnlimited(prices)
        
        dp = [[0] * n for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            maxDiff = -prices[0]  # Max difference between buying and selling on day 0
            
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxDiff)
                
                maxDiff = max(maxDiff, dp[i - 1][j] - prices[j])
        
        return dp[k][n - 1]
    
    def maxProfitUnlimited(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit