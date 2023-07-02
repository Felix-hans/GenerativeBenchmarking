# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        memo = {}

        def dp(num):
            if num == 0:
                return 0
            if num in memo:
                return memo[num]

            res = dp(num - 1) + 1

            if num % 2 == 0:
                res = min(res, dp(num // 2) + 1)
            if num % 3 == 0:
                res = min(res, dp(num // 3) + 1)

            memo[num] = res
            return res

        return dp(n)