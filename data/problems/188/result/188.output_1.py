# @lc app=leetcode id=188 lang=python3
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        if k >= n // 2:
            return self.maxProfitUnlimitedTransactions(prices)
        
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for i in range(1, k + 1):
            maxProfit = 0
            minPrice = prices[0]
            
            for j in range(1, n):
                minPrice = min(minPrice, prices[j] - dp[j - 1][i - 1])
                
                dp[j][i] = max(dp[j - 1][i], prices[j] - minPrice)
                
                maxProfit = max(maxProfit, dp[j][i])
        
        return maxProfit
    
    def maxProfitUnlimitedTransactions(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxProfit += prices[i] - prices[i - 1]
        
        return maxProfit