# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        memo = {}  # Dictionary to store the minimum number of days
        
        def dp(num):
            if num <= 1:
                return num  # Base case: 0 or 1 orange requires 0 or 1 day
            
            if num not in memo:
                if num % 2 == 0 and num % 3 == 0:
                    memo[num] = 1 + min(dp(num - 1), dp(num // 2), dp(num // 3))
                elif num % 2 == 0:
                    memo[num] = 1 + min(dp(num - 1), dp(num // 2))
                elif num % 3 == 0:
                    memo[num] = 1 + min(dp(num - 1), dp(2 * (num // 3)))
                else:
                    memo[num] = 1 + dp(num - 1)
            
            return memo[num]
        
        return dp(n)