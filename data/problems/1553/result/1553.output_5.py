# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        memo = {}  # Memoization dictionary to store already computed results
        
        def eatOranges(n: int) -> int:
            if n <= 1:
                return n
            
            if n in memo:
                return memo[n]
            
            days = 1 + eatOranges(n - 1)
            
            if n % 2 == 0:
                days = min(days, 1 + eatOranges(n // 2))
            
            if n % 3 == 0:
                days = min(days, 1 + eatOranges(n // 3 * 2))
            
            memo[n] = days  # Store the result in the memoization dictionary
            return days
        
        return eatOranges(n)