# @lc app=leetcode id=1006 lang=python3
class Solution:
    def clumsy(self, n: int) -> int:
        if n <= 2:
            return n
        
        operations = ['*', '/', '+', '-']
        stack = [n]
        operation_index = 0
        
        for num in range(n - 1, 0, -1):
            if operations[operation_index] == '*':
                stack[-1] *= num
            elif operations[operation_index] == '/':
                stack[-1] = int(stack[-1] / float(num))
            elif operations[operation_index] == '+':
                stack.append(num)
            elif operations[operation_index] == '-':
                stack.append(-num)
            
            operation_index = (operation_index + 1) % 4
        
        return sum(stack)