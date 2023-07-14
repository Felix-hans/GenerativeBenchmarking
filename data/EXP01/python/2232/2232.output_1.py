# @lc app=leetcode id=2232 lang=python3
class Solution:
    def minimizeResult(self, expression: str) -> str:
        n = len(expression)
        smallest_val = eval(expression)  # evaluate the given expression without parentheses
        smallest_exp = expression

        for i in range(1, n-1):
            num1 = expression[:i]
            num2 = expression[i+1:]
            new_exp = num1 + '(' + num2 + ')'  # add parentheses at position i
            val = eval(new_exp)  # evaluate the new expression

            if val < smallest_val:
                smallest_val = val
                smallest_exp = new_exp

        return smallest_exp