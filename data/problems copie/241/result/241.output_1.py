# @lc app=leetcode id=241 lang=python3
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        results = []
        for i in range(len(expression)):
            if expression[i] in ['+', '-', '*']:
                left_expr = expression[:i]
                right_expr = expression[i+1:]

                left_results = self.diffWaysToCompute(left_expr)
                right_results = self.diffWaysToCompute(right_expr)

                for left in left_results:
                    for right in right_results:
                        if expression[i] == '+':
                            results.append(left + right)
                        elif expression[i] == '-':
                            results.append(left - right)
                        elif expression[i] == '*':
                            results.append(left * right)

        return results