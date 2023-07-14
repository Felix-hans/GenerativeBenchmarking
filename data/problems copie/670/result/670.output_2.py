# @lc app=leetcode id=670 lang=python3
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        
        max_digit_idx = 0
        for i in range(len(digits)):
            if digits[i] > digits[max_digit_idx]:
                max_digit_idx = i
        
        if max_digit_idx == 0:
            return num
        
        for i in range(len(digits)):
            if digits[i] < digits[max_digit_idx]:
                digits[i], digits[max_digit_idx] = digits[max_digit_idx], digits[i]
                break
        
        return int(''.join(digits))