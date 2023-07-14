# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        memo = {}  # Memoization dictionary
        
        def eatOranges(n: int, memo: dict) -> int:
            if n <= 1:
                return n  # Base case: no more oranges left
            
            if n in memo:
                return memo[n]  # Return memoized result if available
            
            min_days = 1 + eatOranges(n - 1, memo)
            
            if n % 2 == 0:
                min_days = min(min_days, 1 + eatOranges(n // 2, memo))
            
            if n % 3 == 0:
                min_days = min(min_days, 1 + eatOranges(2 * (n // 3), memo))
            
            memo[n] = min_days  # Memoize the result
            return min_days
        
        return eatOranges(n, memo)