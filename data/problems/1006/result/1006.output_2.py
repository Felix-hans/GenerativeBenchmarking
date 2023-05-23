# @lc app=leetcode id=1006 lang=python3
class Solution:
    def clumsy(self, n: int) -> int:
        if n <= 2:
            return n
        
        operations = ['*', '/', '+', '-']
        stack = [n]
        operation_idx = 0
        
        for num in range(n-1, 0, -1):
            operation = operations[operation_idx % 4]
            
            if operation == '*':
                stack[-1] *= num
            elif operation == '/':
                stack[-1] = int(stack[-1] / num)  # Floor division
            elif operation == '+':
                stack.append(num)
            else:  # '-'
                stack.append(-num)
            
            operation_idx += 1
        
        return sum(stack)