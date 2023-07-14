# @lc app=leetcode id=2232 lang=python3
class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_index = expression.index("+")
        
        num1 = expression[:plus_index]
        num2 = expression[plus_index+1:]
        
        result = num1 + "(" + num2 + ")"
        
        return result