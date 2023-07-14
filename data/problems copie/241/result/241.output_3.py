# @lc app=leetcode id=241 lang=python3
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left: List[int], right: List[int], operator: str) -> List[int]:
            results = []
            for l in left:
                for r in right:
                    if operator == '+':
                        results.append(l + r)
                    elif operator == '-':
                        results.append(l - r)
                    elif operator == '*':
                        results.append(l * r)
            return results
        
        def helper(expression: str) -> List[int]:
            results = []
            if expression.isdigit():
                return [int(expression)]
            
            for i, char in enumerate(expression):
                if char in ['+', '-', '*']:
                    left = helper(expression[:i])
                    right = helper(expression[i+1:])
                    
                    results.extend(compute(left, right, char))
            
            return results
        
        return helper(expression)