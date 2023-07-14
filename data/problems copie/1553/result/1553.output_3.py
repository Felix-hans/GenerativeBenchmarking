# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        memo = {}  # Memoization dictionary to store already calculated results
        
        def dp(n):
            if n <= 1:
                return n
            
            if n not in memo:
                memo[n] = 1 + min(n % 2 + dp(n // 2), n % 3 + dp(n // 3))
            
            return memo[n]
        
        return dp(n)