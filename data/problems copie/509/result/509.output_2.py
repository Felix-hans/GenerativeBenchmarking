# @lc app=leetcode id=509 lang=python3
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        prev1 = 0
        prev2 = 1
        curr = 0
        
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        
        return curr