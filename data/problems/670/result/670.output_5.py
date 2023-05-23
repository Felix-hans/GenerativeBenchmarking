# @lc app=leetcode id=670 lang=python3
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)
        
        last_occurrence = {int(digit): i for i, digit in enumerate(digits)}
        
        for i in range(n):
            digit = int(digits[i])
            
            for j in range(9, digit, -1):
                if j in last_occurrence and last_occurrence[j] > i:
                    digits[i], digits[last_occurrence[j]] = digits[last_occurrence[j]], digits[i]
                    
                    return int(''.join(digits))
        
        return num