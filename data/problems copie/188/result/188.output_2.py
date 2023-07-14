# @lc app=leetcode id=188 lang=python3
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        if k >= n // 2:
            return self.maxProfitUnlimited(prices)
        
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for i in range(1, k + 1):
            maxProfit = -float('inf')
            minPrice = prices[0]
            
            for j in range(1, n):
                maxProfit = max(maxProfit, prices[j] - minPrice)
                
                minPrice = min(minPrice, prices[j] - dp[j - 1][i - 1])
                
                dp[j][i] = max(dp[j - 1][i], maxProfit)
        
        return dp[-1][-1]
    
    def maxProfitUnlimited(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxProfit += prices[i] - prices[i - 1]
        
        return maxProfit