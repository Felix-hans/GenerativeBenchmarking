# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        memo = {}  # Memoization dictionary
        memo[0] = 0  # Base case

        for count in range(1, n + 1):
            memo[count] = 1 + memo[count - 1]

            if count % 2 == 0:
                memo[count] = min(memo[count], 1 + memo[count // 2])

            if count % 3 == 0:
                memo[count] = min(memo[count], 1 + memo[count // 3])

        return memo[n]