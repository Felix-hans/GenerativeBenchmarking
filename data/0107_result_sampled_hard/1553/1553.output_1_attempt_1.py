# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        memo = {0: 0}  # Memoization dictionary

        for i in range(1, n + 1):
            min_days = memo[i - 1] + 1  # Eat one orange
            if i % 2 == 0:
                min_days = min(min_days, memo[i // 2] + 1)  # Eat n/2 oranges
            if i % 3 == 0:
                min_days = min(min_days, memo[i // 3] + 1)  # Eat 2*(n/3) oranges

            memo[i] = min_days

        return memo[n]