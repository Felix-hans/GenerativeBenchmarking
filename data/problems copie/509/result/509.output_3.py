# @lc app=leetcode id=509 lang=python3
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_prev = 0
            fib_current = 1
            for _ in range(2, n + 1):
                fib_next = fib_prev + fib_current
                fib_prev = fib_current
                fib_current = fib_next
            return fib_current