# @lc app=leetcode id=509 lang=python3
class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def fib_helper(n):
            if n <= 1:
                return n
            elif n in memo:
                return memo[n]
            else:
                memo[n] = fib_helper(n - 1) + fib_helper(n - 2)
                return memo[n]

        return fib_helper(n)