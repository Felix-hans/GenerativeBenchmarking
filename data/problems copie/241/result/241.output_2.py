# @lc app=leetcode id=241 lang=python3
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():  # Base case: expression is a single number
            return [int(expression)]

        results = []
        for i in range(len(expression)):
            if expression[i] in ['+', '-', '*']:
                left_part = self.diffWaysToCompute(expression[:i])  # Compute results for left part
                right_part = self.diffWaysToCompute(expression[i + 1:])  # Compute results for right part

                for left in left_part:
                    for right in right_part:
                        if expression[i] == '+':
                            results.append(left + right)
                        elif expression[i] == '-':
                            results.append(left - right)
                        elif expression[i] == '*':
                            results.append(left * right)

        return results