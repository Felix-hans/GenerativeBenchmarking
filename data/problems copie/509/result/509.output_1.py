# @lc app=leetcode id=509 lang=python3
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev1, prev2 = 0, 1
        
        for _ in range(2, n+1):
            curr = prev1 + prev2
            prev1, prev2 = prev2, curr
        
        return prev2