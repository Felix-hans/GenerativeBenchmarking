# @lc app=leetcode id=122 lang=python3
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = prices[0]  # Initialize the minimum price to the first element
        max_profit = 0  # Initialize the maximum profit to 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price if a lower price is found
            else:
                profit = price - min_price  # Calculate the profit if we sell at the current price
                max_profit = max(max_profit, profit)  # Update the maximum profit if a higher profit is found
        
        return max_profit