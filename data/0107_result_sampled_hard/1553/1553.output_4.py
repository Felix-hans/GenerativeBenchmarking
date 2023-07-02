# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        memo = {}
        memo[0] = 0

        for num in range(1, n + 1):
            memo[num] = memo[num - 1] + 1

            if num % 2 == 0:
                memo[num] = min(memo[num], memo[num // 2] + 1)
            if num % 3 == 0:
                memo[num] = min(memo[num], memo[num // 3] + 1)

        return memo[n]