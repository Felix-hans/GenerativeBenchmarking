# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        memo = {}  # Memoization dictionary to store computed results

        def eatOranges(n: int) -> int:
            if n <= 1:
                return n  # Base case: If n is 0 or 1, return n

            if n not in memo:
                memo[n] = 1 + min(n % 2 + eatOranges(n // 2), n % 3 + eatOranges(n // 3 * 2))

            return memo[n]

        return eatOranges(n)