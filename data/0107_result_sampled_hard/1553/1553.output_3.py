# @lc app=leetcode id=1553 lang=python3
class Solution:
    memo = {}  # Memoization table
    
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n  # Base case: no oranges left or only one orange left
        
        if n in self.memo:
            return self.memo[n]  # Return memoized result if available
        
        result = 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))
        
        self.memo[n] = result  # Memoize the result
        
        return result