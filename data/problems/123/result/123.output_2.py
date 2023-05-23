# @lc app=leetcode id=123 lang=python3
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        
        for price in prices:
            buy1 = max(buy1, -price)               # Track the lowest price to buy
            sell1 = max(sell1, buy1 + price)        # Track the maximum profit after the first transaction
            
            buy2 = max(buy2, sell1 - price)         # Track the lowest price to buy after the first sell
            sell2 = max(sell2, buy2 + price)        # Track the maximum profit after the second transaction
            
        return sell2