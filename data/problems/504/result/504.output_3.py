# @lc app=leetcode id=504 lang=python3
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        is_negative = False
        if num < 0:
            is_negative = True
            num = abs(num)
        
        result = ""
        while num > 0:
            result = str(num % 7) + result
            num //= 7
        
        if is_negative:
            result = "-" + result
        
        return result