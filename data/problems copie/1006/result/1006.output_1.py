# @lc app=leetcode id=1006 lang=python3
class Solution:
    def clumsy(self, n: int) -> int:
        if n <= 2:
            return n
        
        if n <= 4:
            return n + 3
        
        if (n - 4) % 4 == 0:
            return n + 1
        
        if (n - 4) % 4 <= 2:
            return n + 2
        
        return n - 1