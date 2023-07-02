# @lc app=leetcode id=123 lang=python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('-inf')  # Initialize the buy variables with negative infinity
        sell1 = sell2 = 0  # Initialize the sell variables with zero
        
        for price in prices:
            buy1 = max(buy1, -price)  # The maximum between the previous buy1 and the negative price
            sell1 = max(sell1, buy1 + price)  # The maximum between the previous sell1 and the sum of buy1 and price
            
            buy2 = max(buy2, sell1 - price)  # The maximum between the previous buy2 and the difference between sell1 and price
            sell2 = max(sell2, buy2 + price)  # The maximum between the previous sell2 and the sum of buy2 and price
        
        return sell2  # Return the maximum profit after two transactions