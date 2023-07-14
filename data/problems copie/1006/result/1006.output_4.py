# @lc app=leetcode id=1006 lang=python3
class Solution:
    def clumsy(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 6
        elif n == 4:
            return 7
        
        result = n * (n - 1) // (n - 2) + (n - 3)
        n -= 4

        while n >= 4:
            result += -n * (n - 1) // (n - 2) + (n - 3)
            n -= 4

        if n == 1:
            result -= 1
        elif n == 2:
            result -= 2
        elif n == 3:
            result -= 6

        return result