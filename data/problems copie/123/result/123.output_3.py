# @lc app=leetcode id=123 lang=python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        buy1 = buy2 = -float('inf')  # Initial buy prices
        sell1 = sell2 = 0  # Initial sell prices
        
        for price in prices:
            buy1 = max(buy1, -price)
            
            sell1 = max(sell1, buy1 + price)
            
            buy2 = max(buy2, sell1 - price)
            
            sell2 = max(sell2, buy2 + price)
        
        return sell2