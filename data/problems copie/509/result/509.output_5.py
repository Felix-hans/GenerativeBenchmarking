# @lc app=leetcode id=509 lang=python3
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        fib_n_minus_2 = 0
        fib_n_minus_1 = 1
        
        for i in range(2, n + 1):
            current_fib = fib_n_minus_1 + fib_n_minus_2
            fib_n_minus_2 = fib_n_minus_1
            fib_n_minus_1 = current_fib
        
        return fib_n_minus_1