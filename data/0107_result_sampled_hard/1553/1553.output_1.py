# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        memo = {}  # Memoization dictionary

        def eatOranges(remaining):
            if remaining == 0:
                return 0  # No more oranges left to eat
            if remaining in memo:
                return memo[remaining]  # Return memoized result

            min_days = float('inf')
            min_days = min(min_days, eatOranges(remaining - 1) + 1)  # Eat one orange
            if remaining % 2 == 0:
                min_days = min(min_days, eatOranges(remaining // 2) + 1)  # Eat n/2 oranges
            if remaining % 3 == 0:
                min_days = min(min_days, eatOranges(remaining // 3) + 1)  # Eat 2*(n/3) oranges

            memo[remaining] = min_days  # Memoize the result
            return min_days

        return eatOranges(n)