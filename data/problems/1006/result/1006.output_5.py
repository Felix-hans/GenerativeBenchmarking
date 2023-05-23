# @lc app=leetcode id=1006 lang=python3
class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        ops = 0
        
        for i in range(n - 1, 0, -1):
            if ops % 4 == 0:
                stack[-1] *= i
            elif ops % 4 == 1:
                stack[-1] //= i
            elif ops % 4 == 2:
                stack.append(i)
            else:
                stack.append(-i)
            
            ops += 1
        
        return sum(stack)